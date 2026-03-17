from fastapi import FastAPI
from pydantic import BaseModel
from fastapi import HTTPException
from sqlalchemy import create_engine, Column, Integer, String, select
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL="sqlite:///./notes.db"
engine=create_engine(DATABASE_URL, connect_args={"check_same_thread":False})
SessionLocal=sessionmaker(bind=engine)
Base=declarative_base()



class Notedb(Base):
    __tablename__="notes"
    id=Column(Integer,primary_key=True,index=True)
    title=Column(String)
    content=Column(String)

Base.metadata.create_all(bind=engine)

class Note(BaseModel):
    title:str
    content:str


app=FastAPI()

@app.get("/")
def root():
    return{"Message":"api is running"}

@app.post("/notes")
def create_note(note:Note):
    db=SessionLocal()
    note_store=Notedb(title=note.title,content=note.content)
    db.add(note_store)
    db.commit()
    db.refresh(note_store)
    db.close()
    return {
        "id":note_store.id,
        "title":note_store.title,
        "content":note_store.content
    }

@app.get("/notes")
def show_notes():
    db=SessionLocal()
    stmt=select(Notedb)
    result=db.execute(stmt)
    all_note=result.scalars().all()
    db.close()
    response=[]
    for note in all_note:
        response.append({
            "id":note.id,
            "title":note.title,
            "content":note.content
        })
    return response

@app.get("/notes/{note_id}")
def find_note(note_id:int):
    db=SessionLocal()
    note = db.query(Notedb).filter(Notedb.id == note_id).first()
    if note is None:
        db.close()
        raise HTTPException(status_code=404, detail="Note not found")
    result={"id":note.id,
            "title":note.title,
            "content":note.content}
    db.close()
    return result

@app.put("/notes/{note_id}")
def update_note(note_id:int,note_data:Note):
    db=SessionLocal()
    note=db.query(Notedb).filter(Notedb.id==note_id).first()
    if note is None:
        db.close()
        raise HTTPException(status_code=404, detail="Note not found")
    note.title=note_data.title
    note.content=note_data.content
    db.commit()
    result={"id":note.id,
            "title":note.title,
            "content":note.content}
    db.close()
    return result

@app.delete("/notes/{note_id}")
def delete_note(note_id:int):
    db=SessionLocal()
    note = db.query(Notedb).filter(Notedb.id == note_id).first()
    if note is None:
        db.close()
        raise HTTPException(status_code=404, detail="Note not found")
    deleted_note={"id":note.id,
                  "title":note.title,
                  "content":note.content}
    db.delete(note)
    db.commit()
    db.close()
    return{"Message":"Note deleted","Note":deleted_note}