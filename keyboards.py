from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from bots import BOTS


def main_menu():
    keyboard = []

    for bot in BOTS:
        keyboard.append([
            InlineKeyboardButton(
                text=bot["name"],
                url=bot["link"]
            )
        ])

    keyboard.append([
        InlineKeyboardButton(
            text="⭐ درباره Astra",
            callback_data="about"
        )
    ])

    return InlineKeyboardMarkup(keyboard)
