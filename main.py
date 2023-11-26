from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel


chats = []

app = FastAPI()


class Chat(BaseModel):
    id: int
    content: str
    


@app.post("/chat")
def create_chat(chat:Chat):
    chats.append(chat)
    return "채팅 추가 성공"

@app.get("/chats")
def read_chat():
    return chats

app.mount("/", StaticFiles(directory="static", html=True),name= "static")