
# Envio de e-mail automático

Script simples de envio de e-mail

*Pequenas mudanças:
- Isolando as variáveis de ambientes evitando expor senhas e dados pessoais.
- Correção de envio para mais de um e-mail, fazendo .split(',') no toaddr.

#### Procedimento
Renomeie o arquivo .env-sample para .env.
Edite o arquivo .env e configure seu email, senha, smtp, porta e os emails a enviar.

#### Dica para quem usa GMAIL
O Google não permite usar a senha do Gmail diretamente, é necessário usar uma senha de app configurada na sua conta Google, para isso acesse [Senhas do App](https://myaccount.google.com/apppasswords). 


#### Requisitos
```
pip install -r requirements.txt
python script.py

