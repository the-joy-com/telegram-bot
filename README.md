# telegram-bot

bot hosted for the natural language entry point of The Joy's agentic system

## pre requisites

- we assume you run Ubuntu 24
- we assume you have set up https://github.com/the-joy-com/agentic-entry-point on your server

## setup

### step 1: get your bot token (to run only once)

1. open Telegram and search for `@BotFather`
2. send the command `/newbot`
3. follow the prompts to give your bot a name and a unique username (the username must end in `bot`)
4. botFather will provide an HTTP API Token (e.g., `123456789:ABCdefGhIJKlmNo...`). Keep this secure

## step 2: install deps

`python3 -m venv venv && source venv/bin/activate && pip install -r requirements.txt`

## step 3: env setting

`cp .env.example .env` + fill in sensible values

## step 4: run it locally

`python3 bot.py`

## step 4: set as a service

<!-- TODO -->