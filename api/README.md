# Utilizando API Telegram Telethon

Classe utilizando o Telethon para adicionar usuários de um determinado grupo em outro grupo.

*Algumas mudanças:
- Utilizando funções async/await conforme exigência da biblioteca Telethon recente (1.34.0).
- Para efeito de testes utilizei grupo pequeno, o que altera na forma de manipulação e tratativas de chats/supergroup/users. (Manipulação em caso de supergroup comentadas)
- Utilizando o decouple para não expor config da API no repositório.

#### Procedimento
Renomeie o arquivo env-sample para .env.
Preencha os dados da sua API Telegram.


#### Requisitos
```
pip install -r requirements.txt
python run.py
