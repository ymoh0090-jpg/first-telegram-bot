# 🤖 Basic Telegram Bot

A simple Telegram bot built with Python and the `python-telegram-bot` library.

## Features

* `/start` - Start the bot
* `/help` - Show available commands
* `/about` - About the bot
* `/id` - Show your Telegram ID
* `/ping` - Check if the bot is online
* `/echo <text>` - Repeat a message
* Interactive reply keyboard
* Text message handling

## Technologies

* Python
* python-telegram-bot

## Project Structure

```text
project-1/
├── main.py
├── handlers.py
├── config.py
├── requirements.txt
├── README.md
└── .gitignore
```

## Setup

Install dependencies:

```bash
pip install -r requirements.txt
```

Set your bot token in `config.py`, then run:

```bash
python main.py
```

## Note

`config.py` contains the bot token and is excluded from Git using `.gitignore`.
