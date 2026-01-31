import os
from typing import Dict, List
from fastapi_mail import FastMail, MessageSchema, ConnectionConfig, MessageType
from dotenv import load_dotenv

load_dotenv()

class Envs:
    MAIL_USERNAME=os.getenv("MAIL_USERNAME")
    MAIL_PASSWORD=os.getenv("MAIL_PASSWORD")
    MAIL_FROM=os.getenv("MAIL_FROM")
    MAIL_PORT=int(os.getenv("MAIL_PORT", 587))
    MAIL_SERVER=os.getenv("MAIL_SERVER")
    MAIL_FROM_NAME=os.getenv("MAIL_FROM_NAME")


conf = ConnectionConfig(
    MAIL_USERNAME=Envs.MAIL_USERNAME,
    MAIL_PASSWORD=Envs.MAIL_PASSWORD,
    MAIL_FROM=Envs.MAIL_FROM,
    MAIL_PORT=Envs.MAIL_PORT,
    MAIL_SERVER=Envs.MAIL_SERVER,
    MAIL_FROM_NAME=Envs.MAIL_FROM_NAME,
    MAIL_STARTTLS=True,
    MAIL_SSL_TLS=False,
    USE_CREDENTIALS=True,
    TEMPLATE_FOLDER="templates"
)


async def send_email(subject:str, email_to: list , data:Dict | List, file: str):
    message = MessageSchema(
        subject=subject,
        recipients=email_to,
        template_body=data,
        subtype=MessageType.html,
        attachments=[file] if file else []
    )

    fmail = FastMail(conf)
    await fmail.send_message(message, template_name="email.html")


