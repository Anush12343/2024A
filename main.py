
from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import sessionmaker, declarative_base, Session
from pydantic import BaseModel, Field
from typing import List
import os 

DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://Cloud24AAnusharan:Slayer1234@anusharan-bhattarai-db.postgres.database.azure.com:5432/cloude24a")
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()

class QueryModel(Base):
    __tablename__ = "queries"
    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    phone_number = Column(String, nullable=False)
    query = Column(String, nullable=False)

Base.metadata.create_all(bind=engine)

class Query(BaseModel):
    first_name: str
    last_name: str
    phone_number: str
    query: str
    
    class Config:
        orm_mode = True
        from_attributes = True

app = FastAPI()

# Enable CORS for frontend integration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Health check endpoints
@app.get("/")
def health_check():
    return {"status": "ok"}

@app.get("/health")
def health_check_alt():
    return {"status": "ok"}

@app.get("/api/health")
def health_check_api():
    return {"status": "ok"}

@app.post("/queries", response_model=Query)
def create_query(query: Query, db: Session = Depends(get_db)):
    db_query = QueryModel(**query.model_dump() if hasattr(query, "model_dump") else query.dict())
    db.add(db_query)
    db.commit()
    db.refresh(db_query)
    return db_query

@app.get("/queries", response_model=List[Query])
def get_queries(db: Session = Depends(get_db)):
    queries = db.query(QueryModel).all()
    # Return empty list instead of 404 so frontend shows the empty state correctly
    return queries

