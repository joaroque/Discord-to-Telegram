import re

"""
    Feel free to improve this code. 
    I do something basic that suits my needs.
"""


important_keywords = [
    "EURGBP",
    "AUDJPY",
    "EURAUD",
    "EURCHF",
    "AUDNZD",
    "NZDJPY",
    "GBPAUD",
    "GBPCAD",
    "EURNZD",
    "AUDCAD",
    "GBPCHF",
    "AUDCHF",
    "EURCAD",
    "CADJPY",
    "GBPNZD",
    "CADCHF",
    "CHFJPY",
    "NZDCAD",
    "NZDCHF",
    "XAUUSD",
    "EURUSD",
    "USDJPY",
    "GBPUSD",
    "AUDUSD",
    "USDCAD",
    "USDCHF",
    "NZDUSD",
    "EURJPY",
    "GBPJPY"
]


def should_send(message):
    cleaned_message = re.sub(r'\s+AT\s+\d+\.\d+\s+\(.*\)', '', message)

    if any(keyword in cleaned_message.upper() for keyword in important_keywords):
        return cleaned_message.strip()
    