import time

from decouple import config
from telethon.errors.rpcerrorlist import (
    PeerFloodError,
    TakeoutRequiredError,
    UserPrivacyRestrictedError,
)
from telethon.sync import TelegramClient
from telethon.tl.functions.channels import InviteToChannelRequest
from telethon.tl.functions.messages import AddChatUserRequest, GetDialogsRequest
from telethon.tl.types import (
    InputPeerChannel,
    InputPeerEmpty,
    InputPeerUser,
    InputPeerChat,
)


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
                if chat.participants_count <= 2:
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

    async def add_member_to_group(self, user, target_group):
        """
        target_group_entity = InputPeerChannel(
            target_group.id, target_group.access_hash
        )
        """

        target_group_entity = InputPeerChat(target_group.id)

        try:
            print("Adicionando usuário %s" % user.id)

            user_to_add = InputPeerUser(user.id, user.access_hash)

            await self.client(
                # InviteToChannelRequest(target_group_entity, [user_to_add])
                AddChatUserRequest(
                    target_group_entity.chat_id, user_to_add.user_id, fwd_limit=0
                )
            )

            time.sleep(2)
            return True

        except PeerFloodError:
            print("Erro de flood. Dormindo por 1 hora.")
            time.sleep(3600)
            return False

        except UserPrivacyRestrictedError:
            print("Usuário não permite ser adicionado no grupo.")
            return False

        except Exception as e:
            print(str(e))
            return False

    async def initialize(self):
        await self.connect()
        print("Conectado ao Telegram!")
