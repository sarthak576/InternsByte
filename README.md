<!-- Banner -->
<p align="center">
  <img src="https://github.com/sarthak576/InternsByte/blob/main/All%20documentation/images/demo.png" alt="Demo Banner" width="80%">
</p>

# 📚 Developer Notes – OpenAI, Whisper AI & More  

> 🚀 **Future-Proof & Clickable** – This doc is structured for quick navigation, visual clarity, and easy updates.

---

## 📑 Table of Contents
1. [🔑 OpenAI API Key Usage](#-1-openai-api-key-usage)
2. [🎙️ Whisper AI – Speech to Text](#-2-whisper-ai--speech-to-text)
3. [📦 Why Install `multipart`](#-3-why-install-multipart)
4. [🆕 Using Latest OpenAI Version](#-4-using-latest-openai-version)
5. [⚡ Quick Reference Table](#-quick-reference-table)

---

## 🔑 1. OpenAI API Key Usage  

![Badge](https://img.shields.io/badge/Status-Important-red)  
### ✅ 5 Key Points – Using `os.getenv("OPEN_AI_API_KEY")` for API Key:

1. **`os.getenv()` Reads Env Vars** – Fetches `OPEN_AI_API_KEY` from environment variables.
2. **Must Export It 🔐** – Before running:
   ```bash
   export OPEN_AI_API_KEY="your_api_key"



   ## 🎙️ 2. Whisper AI – Speech to Text  

![Badge](https://img.shields.io/badge/Model-Whisper_AI-blue)  
### ✅ 5 Key Points – Using Whisper AI with ChatGPT/OpenAI:

1. **What is Whisper? 🎙️** – OpenAI’s automatic speech recognition (ASR) model for converting audio to text.
2. **Usage in Code 💻**:
   ```python
   import openai

   openai.api_key = "your_api_key"

   audio_file = open("your_audio.mp3", "rb")
   transcript = openai.Audio.transcribe("whisper-1", audio_file)

   print(transcript["text"])

## 📦 3. Why Install `multipart`?  

![Badge](https://img.shields.io/badge/Package-python--multipart-green)  
### ✅ 2 Key Points – `pip install multipart`:

1. **Purpose** – Parses `multipart/form-data` for handling file uploads in FastAPI and similar frameworks.
2. **Example**:
   ```python
   from fastapi import FastAPI, File, UploadFile

   app = FastAPI()

   @app.post("/upload/")
   async def upload(file: UploadFile = File(...)):
       return {"filename": file.filename}

   
## 🆕 4. Using Latest OpenAI Version  

![Badge](https://img.shields.io/badge/OpenAI-Version_1+-purple)  
### ✅ 5 Key Points – Updating to Latest OpenAI SDK:

1. **API Key Change 🔑** – Old: `openai.apikey` ❌ → New: `OpenAI(api_key=...)` ✅
2. **File Handling 📂** – Files are temporarily saved before being sent to the API.
3. **Method Update 🛠️** – Old: `transcribe()` ❌ → New: `client.audio.transcriptions.create(...)` ✅
4. **FastAPI Integration ⚡** – `UploadFile = File(...)` ensures proper `multipart/form-data` handling.
5. **Future-Proofing 🚀** – v1+ syntax prevents deprecation issues and keeps code up-to-date.


## ⚡ 5. Quick Reference Table  

![Badge](https://img.shields.io/badge/Reference-Quick_Access-orange)  

| Section | Topic | Key Command / Code | Notes |
|---------|-------|-------------------|-------|
| 1 | OpenAI API Key Usage | `export OPEN_AI_API_KEY="your_api_key"` | Set in terminal before running app |
| 2 | Whisper AI – Speech to Text | `openai.Audio.transcribe("whisper-1", audio_file)` | Works with `.mp3`, `.wav`, `.m4a`, etc. |
| 3 | Install `multipart` | `pip install python-multipart` | Needed for file uploads in FastAPI |
| 4 | Latest OpenAI Version | `OpenAI(api_key=...)` & `client.audio.transcriptions.create(...)` | Updated v1+ SDK syntax |

