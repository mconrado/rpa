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

    async def get_groups(self):
        groups = []
        chats = await self.client(
            GetDialogsRequest(
                offset_date=None,
                offset_id=0,
                offset_peer=InputPeerEmpty(),
                limit=200,
                hash=0,
            )
        )

        for chat in chats.chats:
            try:
                # if chat.megagroup == True:
                if chat.participants_count == 2:
                    groups.append(chat)
            except:
                continue

        print("Escolha um grupo")
        i = 0
        for group in groups:
            print(str(i) + " - " + group.title)
            i += 1

        escolha = input("Escolha um número: ")
        grupo_alvo = groups[int(escolha)]
        return grupo_alvo

    async def get_members_of_group(self, target_group):
        all_participants = await self.client.get_participants(
            target_group, aggressive=True
        )

        return all_participants

    async def initialize(self):
        await self.connect()
        print("Conectado ao Telegram!")
