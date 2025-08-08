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
