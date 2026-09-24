🤖 Telegram Bot

Bot para Telegram desenvolvido em Python 3.14, utilizando a biblioteca python-telegram-bot.

O projeto possui comandos e botões de ação rápida para facilitar a interação com o usuário.

🛠️ Tecnologias

Python 3.14

python-telegram-bot

python-dotenv

HTTPX

Docker



📁 Estrutura
meu-bot/
├── handlers/
│   ├── __init__.py
│   ├── talk.py
│   └── botoes.py
├── main.py
├── requirements.txt
├── Dockerfile
├── .dockerignore
├── .env
└── README.md




⚙️ Configuração

Clone o projeto e entre na pasta:

git clone SEU_REPOSITORIO
cd meu-bot


Crie um ambiente virtual:

python -m venv .venv


Ative o ambiente virtual.

Windows
.venv\Scripts\activate

Linux/macOS
source .venv/bin/activate


Instale as dependências:

pip install -r requirements.txt

🔐 Variáveis de ambiente

Crie um arquivo .env na raiz do projeto:

TELEGRAM_TOKEN_API=SEU_TOKEN_AQUI


O token deve ser obtido através do BotFather no Telegram.

⚠️ Nunca compartilhe ou publique seu token do Telegram.

▶️ Executando

Com o ambiente virtual ativado:

python main.py


Se tudo estiver configurado corretamente, o bot começará a receber atualizações do Telegram.

🐳 Docker

Para construir a imagem:

docker build -t meu-bot .


Para executar:

docker run --env-file .env meu-bot


Se estiver utilizando Docker Compose:

docker compose up -d


Para visualizar os logs:

docker compose logs -f


Para parar o container:

docker compose down

📌 Comandos

O bot possui atualmente comandos como:

/start
/help
/report
/hours
/net
/bolsa


Também possui um teclado com ações rápidas para facilitar o acesso às funções do bot.

🚧 Status

Projeto em desenvolvimento.

Novas funcionalidades e melhorias serão adicionadas conforme o desenvolvimento do bot.

👨‍💻 Desenvolvimento

Desenvolvido em Python 3.14.

Este projeto foi criado com objetivo de estudo e desenvolvimento de aplicações para Telegram.
