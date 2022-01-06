from src.bot import Bot

import logging


def main() -> None:
    logging.basicConfig(level=logging.DEBUG)
    
    bot = Bot()
    bot.run()

if __name__ == '__main__':
    main()