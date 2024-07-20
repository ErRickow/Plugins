# K: Keyboard Buttons

from pyrogram.types import KeyboardButton, ReplyKeyboardMarkup


def gen_keyboard(collection: list, row: int = 2) -> list[list[KeyboardButton]]:
    keyboard = []
    for i in range(0, len(collection), row):
        kyb = []
        for x in collection[i : i + row]:
            kyb.append(KeyboardButton(x))
        keyboard.append(kyb)
    return keyboard


def session_keyboard() -> ReplyKeyboardMarkup:
    return ReplyKeyboardMarkup(
        [
            [
                KeyboardButton("Baru 🔖"),
                KeyboardButton("Hapus ❌"),
            ],
            [
                KeyboardButton("List 📜"),
                KeyboardButton("Beranda🏠"),
            ],
        ],
        resize_keyboard=True,
    )


def start_keyboard() -> ReplyKeyboardMarkup:
    return ReplyKeyboardMarkup(
        [
            [
                KeyboardButton("📟 Session"),
                KeyboardButton("Force Sub ✨"),
            ],
            [
                KeyboardButton("👥 Users"),
                KeyboardButton("Lainnya 📣"),
            ],
        ],
        resize_keyboard=True,
    )
