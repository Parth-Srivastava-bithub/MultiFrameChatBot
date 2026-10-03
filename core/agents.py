from langchain_groq import ChatGroq
from dotenv import load_dotenv
import pydantic
import typing
import os

load_dotenv()


class Agents(pydantic.BaseModel):
    agent: typing.Literal['sam', 'yono']



 