# 📝 FastAPI Notes API WITH SQLite DATABASE

A simple REST API for managing notes built using **FastAPI**, **SQLAlchemy**, and **SQLite**.  
This API allows users to create, retrieve, and delete notes stored in a database.

---



---

## 🛠 Tech Stack

- Python
- FastAPI
- SQLAlchemy
- SQLite
- Pydantic
- Uvicorn

---

## 📂 Project Structure

```
.
├── main.py
├── notes.db
└── README.md
```

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/Arik-code98/notes-db.git
cd notes-db
```

### 2. Create a virtual environment (optional but recommended)

```bash
python -m venv venv
```

Activate it:

**Windows**

```bash
venv\Scripts\activate
```

**Mac/Linux**

```bash
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Running the API

Start the server with:

```bash
uvicorn main:app --reload
```

The API will run at:

```
http://127.0.0.1:8000
```

---

## 📘 API Documentation

FastAPI automatically generates interactive documentation.

**Swagger UI**

```
http://127.0.0.1:8000/docs
```

**ReDoc**

```
http://127.0.0.1:8000/redoc
```

---

## 📡 API Endpoints

### Check API Status

**GET /**

Response

```json
{
  "Message": "api is running"
}
```

---

### Create a Note

**POST /notes**

Request Body

```json
{
  "title": "My Note",
  "content": "This is a note"
}
```

---

### Get All Notes

**GET /notes**

Example Response

```json
[
  {
    "id": 1,
    "title": "My Note",
    "content": "This is a note"
  }
]
```

---

### Get Note by ID

**GET /notes/{note_id}**

Example

```
/notes/1
```

Response

```json
{
  "id": 1,
  "title": "My Note",
  "content": "This is a note"
}
```

---

### Delete a Note

**DELETE /notes/{note_id}**

Response

```json
{
  "Message": "Note deleted",
  "Note": {
    "id": 1,
    "title": "My Note",
    "content": "This is a note"
  }
}
```

---

## 🗄 Database

This project uses **SQLite** as the database.

Database file:

```
notes.db
```

Tables are automatically created using:

```python
Base.metadata.create_all(bind=engine)
```

---


## 👨‍💻 Author

Developed as a backend practice project using FastAPI.
