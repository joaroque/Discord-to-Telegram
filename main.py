import asyncio
import configparser
import json
import logging
import ssl

import websockets
import websockets.exceptions
from telethon import TelegramClient

from utils.middleware import should_send

# Configuring the logging
logging.basicConfig(level=logging.INFO)

config = configparser.ConfigParser()
config.read("config.ini")

# Telegram settings
api_id = config.getint("TELEGRAM", "API_ID")
api_hash = config.get("TELEGRAM", "API_HASH")
client_name = config.get("TELEGRAM", "CLIENT_NAME")
destination_channel = config.getint("TELEGRAM", "DEST_CHANNEL")

# Discord settings
channel_id_to_monitor = config.get("DISCORD", "SOURCE_CHANNEL")
token = config.get("DISCORD", "AUTH_TOKEN")

discord_ws_url = "wss://gateway.discord.gg/?v=6&encoding=json"

client = TelegramClient(client_name, api_id, api_hash)


async def send_to_telegram(message):
    await client.send_message(destination_channel, message)
    logging.info(f"Message sent to Telegram: {message}")


async def heartbeat(ws, interval, last_sequence):
    while True:
        await asyncio.sleep(interval)
        payload = {
            "op": 1,
            "d": last_sequence
        }
        await ws.send(json.dumps(payload))
        logging.info("Heartbeat packet sent.")


async def identify(ws):
    identify_payload = {
        "op": 2,
        "d": {
            "token": token,
            "properties": {
                "$os": "windows",
                "$browser": "chrome",
                "$device": "pc"
            }
        }
    }
    await ws.send(json.dumps(identify_payload))
    logging.info("Identification sent.")


async def on_message(ws):
    last_sequence = None
    while True:
        event = json.loads(await ws.recv())
        logging.info(f"Event received: {event}")
        op_code = event.get('op', None)

        if op_code == 10:
            interval = event['d']['heartbeat_interval'] / 1000
            asyncio.create_task(heartbeat(ws, interval, last_sequence))

        elif op_code == 0:
            last_sequence = event.get('s', None)
            event_type = event.get('t')
            if event_type == 'MESSAGE_CREATE':
                channel_id = event['d']['channel_id']
                message = event['d']['content']
                if channel_id == channel_id_to_monitor and message != '':
                    logging.info(f"Message received from Discord: {message}")
                    
                    # comment this line if you dont want to use middlware
                    cleaned_message = should_send(message)
                    if cleaned_message:
                        await send_to_telegram(f"{cleaned_message}")

                    # await send_to_telegram(f"{message}")
                    

        elif op_code == 9:
            logging.info("Invalid session. Starting a new session...")
            await identify(ws)


async def main():
    ssl_context = ssl.create_default_context()
    ssl_context.check_hostname = False
    ssl_context.verify_mode = ssl.CERT_NONE

    while True:
        try:
            async with websockets.connect(discord_ws_url, ssl=ssl_context) as ws:
                await identify(ws)
                await on_message(ws)
        except websockets.exceptions.ConnectionClosed as e:
            logging.error(
                f"WebSocket connection closed unexpectedly: {e}. Reconnecting...")
            await asyncio.sleep(5)
            continue

with client:
    client.loop.run_until_complete(main())
