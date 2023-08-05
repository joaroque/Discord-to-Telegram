<p align="center">
  <a href="https://github.com/joaroque/Discord-to-Telegram">
    <img alt="Slickr" src="screenshot/banner.png" width="630" />
  </a>
</p>
<h2 align="center">Messages forwarder in real time by Websockets</h2>
<p align="center">
    <a href="https://github.com/joaroque/Discord-to-Telegram/issues">Report Bug</a>
    ·
    <a href="https://github.com/joaroque/Discord-to-Telegram/issues">Request Feature</a>
</p>
<p align="center">
<a href="https://github.com/joaroque/Discord-to-Telegram/fork" target="blank">
<img src="https://img.shields.io/github/forks/joaroque/Discord-to-Telegram?style=flat-square" alt="Discord-To-Teleram forks"/>
</a>
<a href="https://github.com/joaroque/Discord-to-Telegram/stargazers" target="blank">
<img src="https://img.shields.io/github/stars/joaroque/Discord-to-Telegram?style=flat-square" alt="Discord-to-Telegram stars"/>
</a>
<a href="https://github.com/joaroque/Discord-to-Telegram/issues" target="blank">
<img src="https://img.shields.io/github/issues/joaroque/Discord-to-Telegram?style=flat-square" alt="Discord-to-Telegramissues"/>
</a>
<a href="https://github.com/joaroque/Discord-to-Telegram/pulls" target="blank">
<img src="https://img.shields.io/github/issues-pr/joaroque/Discord-to-Telegram?style=flat-square" alt="Discord-to-Telegram pull-requests"/>
</a>
</p>

## :arrow_down: Installation
To get a local copy installed and working, follow these steps:

 - Clone this repository

    ```console
    git clone https://github.com/joaroque/Discord-to-Telegram.git
    ```
    
 - Enter the project folder

    ```sh
    cd Discord-to-Telegram
    ```

### 📦 Install dependencies

Note: use `pip install -r requirements .txt` to install all dependencies.


### 🚀 Setup the bot

 1. Get telegram client (credentials)[https://my.telegram.org/auth]
 
 2. Get discord token on Chrome Devtools request monitoring 

 3. Insert your token in the `.ini` file

    ```ini
      [TELEGRAM]
      API_ID = 
      API_HASH = 
      CLIENT_NAME = 
      DEST_CHANNEL = -100123456789
      
      [DISCORD]
      SOURCE_CHANNEL = 
      AUTH_TOKEN = 
      HEARTBEAT_INTERVAL = 100

    ```

 4. Start the bot

    ```shell
    python main.py
    ```
   

## Meta

I made this banner using saviomartin's [Slickr](https://slickr.vercel.app/) tool.
