## 1. Open ai api key usages...

### ✅ 5 Key Points – Using `os.getenv("OPEN_AI_API_KEY")` for API Key:

1. **`os.getenv()` Reads Env Vars**:
   It fetches the `OPEN_AI_API_KEY` from environment variables.

2. **You **Must** Export It 🔐**:
   Before running your app, run:

   ```bash
   export OPEN_AI_API_KEY="your_api_key"
   ```

3. **Correct Syntax – No Spaces 🚫**:
   ✅ Correct: `export OPEN_AI_API_KEY="key"`
   ❌ Wrong: `export OPEN_AI_API_KEY = "key"`

4. **One-Time Per Terminal Session 🧠**:
   You need to run `export` again if you open a new terminal.

5. **Permanent Option (Optional) 📁**:
   Add `export` line to `~/.bashrc` or `~/.zshrc` to set it permanently.

---

### 🔟 Word Crisp Version:

Yes, but you **must** export the key properly first.


--- 


## 2. Wishper AI - Speech to Text (ASR) Model  

### ✅ 5 Key Points – Using Whisper AI with ChatGPT/OpenAI:

1. **What is Whisper? 🎙️**
   Whisper is OpenAI’s automatic speech recognition (ASR) model for transcribing audio to text.

2. **How to Use in Code 💻**
   Upload audio and send to OpenAI like this:

   ```python
   import openai

   openai.api_key = "your_api_key"

   audio_file = open("your_audio.mp3", "rb")
   transcript = openai.Audio.transcribe("whisper-1", audio_file)

   print(transcript["text"])
   ```

3. **Supported Formats 🎧**
   Works with `.mp3`, `.mp4`, `.mpeg`, `.mpga`, `.m4a`, `.wav`, `.webm`.

4. **No Fine-Tuning Needed ⚙️**
   It’s pre-trained — just plug and use!

5. **In ChatGPT (Plus Only) 💬**
   ChatGPT (Plus) can transcribe voice messages sent in the chat using Whisper internally.

---

### 🔟 Word Crisp Version:

Use `openai.Audio.transcribe("whisper-1", audio_file)` with API key.


---

## 3. Why to install `multipart` ?

### ✅ 2 High-Quality Points – `pip install multipart`

1. **What it is**:
   `python-multipart` parses `multipart/form-data` (used in file uploads, forms) in FastAPI and similar frameworks.

2. **Example Usage**:

   ```python
   from fastapi import FastAPI, File, UploadFile

   app = FastAPI()

   @app.post("/upload/")
   async def upload(file: UploadFile = File(...)):
       return {"filename": file.filename}
   ```

   ⚠️ Without `multipart`, file upload parsing fails.


## 4. Using latest openai version 



### 🔧 Notes:

* ✅ `openai.apikey` is incorrect in v1+ → replaced with `OpenAI(api_key=...)`
* ✅ File is **saved temporarily** to disk before sending to API
* ✅ `transcribe()` → now `client.audio.transcriptions.create(...)`
* ✅ `UploadFile = File(...)` ensures FastAPI handles `multipart/form-data`

---

### 🔟 Word Crisp Version:

Updated to latest SDK with `OpenAI()` and proper file handling.
