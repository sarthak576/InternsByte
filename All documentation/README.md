## 1.Setup Python Virtual Environment 
--- 
### 🔑 5 Key Points on `python -m venv venv`:

1. ✅ **Creates virtual environment** named `venv` in your project folder.
2. 🐍 **`python -m venv`** is a built-in module for making isolated Python environments.
3. 📦 Keeps project dependencies **separate from global Python** installation.
4. 🛠️ Helps manage **different packages for different projects** easily.
5. ▶️ After running it, **activate using**:

   * Windows: `venv\Scripts\activate`
   * macOS/Linux: `source venv/bin/activate`

---

### 🔟 Crisp Summary (10 words):

`python -m venv venv` creates a virtual environment named "venv."

---

## 2. Why error while putting source in Fish Shell ? 
### 🔥 Error Cause (in simple words):
You're likely using fish shell 🐟 instead of bash, and the `venv/bin/activate` script is written for bash, not fish.

---

## 3. How to install Fast API 
### ✅ 5 Key Points on `pip install "fastapi[standard]"`:

1. **Installs FastAPI**:
   It installs the core `FastAPI` library.

2. **`[standard]` Extras**:
   Adds recommended dependencies for full functionality.

3. **Includes `uvicorn`**:
   Installs `uvicorn`, the suggested ASGI server for running FastAPI.

4. **Adds `pydantic`, `httpx`, etc.**:
   Brings in tools for validation, testing, and performance.

5. **Best for Development**:
   Ensures you're ready for production/development without manual setup.

---

### 🔟 Word Crisp Version:

Installs FastAPI with recommended tools like `uvicorn`, `httpx`, etc.

 ---

## 4.Reloading main python file

### ✅ 5 Key Points on `uvicorn main:app --reload`:

1. **`main:app` Reference**:
   `main` = Python file (`main.py`), `app` = FastAPI instance inside.

2. **`app` Must Be Defined**:
   You must have `app = FastAPI()` in `main.py`.

3. **Colon (`:`) Means "Import"**:
   Tells Uvicorn to import `app` from `main.py`.

4. **`--reload` Flag**:
   Enables auto-reloading on file changes—great for development.

5. **Not Reloading File, Reloading Server**:
   It restarts the server *when* your code changes, not the file directly.

---

### 🔟 Word Crisp Version:

Runs `app` from `main.py`, auto-reloads server on code change.

---

## 5. Spelling mistake 

### ✅ 5 Key Points – Fixing `bash: uvicorn: command not found` Error:

1. **Typo Check 🔍**:
   You typed `uvicron`, not `uvicorn`. Fix the spelling!

2. **Install Uvicorn 🧩**:
   Run:

   ```bash
   pip install "fastapi[standard]"
   # or separately
   pip install uvicorn
   ```

3. **Verify Installation ✅**:
   Check if Uvicorn is installed:

   ```bash
   uvicorn --version
   ```

4. **Add to PATH (if needed) 🛠️**:
   If installed but still not found, add Python’s Scripts folder to your system `PATH`.

5. **Use `python -m` (Safe way) 🧪**:
   Instead of relying on `PATH`, run:

   ```bash
   python -m uvicorn main:app --reload
   ```

---

### 🔟 Word Crisp Version:

Fix typo, install `uvicorn`, check PATH, or use `python -m`.
