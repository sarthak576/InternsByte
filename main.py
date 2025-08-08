from fastapi import FastAPI, UploadFile
from dotenv import load_dotenv
import openai
import os
load_dotenv()

client = openai.Client(
api_key = os.getenv("OPEN_AI_KEY"),
organization = os.getenv("OPEN_AI_ORG")
)


app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}



@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile):
    return {"filename": file.filename}

@app.post("/talk")
async def post_audio(file:UploadFile):
    audio_file = open(file.filename, "rb")
    transcript = openai.Audio.transcribe("whisper-1", audio_file)
    print(transcript)



# 1. Send in audio and Have it transcribed  (All most Done - 80% now facing Errors)
# 2. We want to send it to chat GPT and get the response (Not Started Yet - 0%)
# 3. We want to save the cht history to send back and forth the context. (Not begin yet - 0%)