import time

from decouple import config
from telethon.errors.rpcerrorlist import PeerFloodError, UserPrivacyRestrictedError
from telethon.sync import TelegramClient
from telethon.tl.functions.channels import InviteToChannelRequest
from telethon.tl.functions.messages import GetDialogsRequest
from telethon.tl.types import InputPeerChannel, InputPeerEmpty, InputPeerUser


class TelegramBot:
    def __init__(self) -> None:
        self.api_id = config("API_ID")
        self.api_hash = config("API_HASH")
        self.phone = config("PHONE")
        self.client = TelegramClient(self.phone, self.api_id, self.api_hash)

    async def connect(self):
        await self.client.start()
        if not await self.client.is_user_authorized():
            await self.client.send_code_request(self.phone)
            await self.client.sign_in(self.phone, input("Digite o código: "))
            return True

    async def initialize(self):
        await self.connect()
        print("Conectado ao Telegram!")
