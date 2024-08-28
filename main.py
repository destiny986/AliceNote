## Nuitka 2.3
# nuitka-project: --mingw64
# nuitka-project: --onefile
# nuitka-project: --windows-console-mode=disable
#
# nuitka-project: --enable-plugin=pyside6
# nuitka-project: --include-qt-plugins=qml
#
# nuitka-project: --file-version=1.0
# nuitka-project: --company-name=KabanTechnologies
# nuitka-project: --product-name=AliceNote
# nuitka-project: --output-filename=AliceNote

import os
from random import randint

from dotenv import dotenv_values
from pyrogram import Client


def send_voice():
    """Звуковое оповещение на колонку Алиса."""
    config = dotenv_values(
        os.path.join(os.getenv("LOCALAPPDATA"), "RTools/.env")
    )
    with open(
        os.path.join(os.getenv("LOCALAPPDATA"), "RTools/AlicePhrases.txt"),
        "r",
        encoding="UTF-8",
    ) as file:
        message_voice_list = [line.rstrip() for line in file]

    app = Client(
        os.path.join(
            os.getenv("LOCALAPPDATA"), "RTools/", config["CLIENT_NAME"]
        ),
        config["ACC_ID"],
        config["ACC_HASH"],
    )
    app.start()
    app.send_message(
        "@alice_speaker_bot",
        message_voice_list[randint(0, len(message_voice_list) - 1)],
    )
    app.stop()


if __name__ == "__main__":
    send_voice()
