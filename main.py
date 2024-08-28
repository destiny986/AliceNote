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
from pyrogram import Client
from random import randint
from dotenv import dotenv_values


config = dotenv_values(os.path.join(os.getenv('LOCALAPPDATA'), "RTools/.env"))
message_voice_list = [
    "/s Кабан, вставай, <[300]> пора хрюкать",
    "/s Истекаю кровью как свинья на бойне",
    "/s Пора, <[500]> брат",
    "/s Застелил кровать, <[500]> пора убивать",
    "/s Н+оу каб+анас, <[500]> си, <[500]> сеньёре",
]


def send_voice():
    """Звуковое оповещение на колонку Алиса."""
    # app = Client(os.path.join(os.getenv('LOCALAPPDATA'), "RTools/", config["CLIENT_NAME"]), config["ACC_ID"], config["ACC_HASH"])
    app = Client(config["CLIENT_NAME"], config["ACC_ID"], config["ACC_HASH"])
    app.start()
    app.send_message(
        "@alice_speaker_bot",
        message_voice_list[randint(0, len(message_voice_list) - 1)],
    )
    app.stop()


if __name__ == "__main__":
    send_voice()
