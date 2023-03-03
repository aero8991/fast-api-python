from fastapi import FastAPI, Response, status, HTTPException, Depends
from app import models
from app.database import engine, SessionLocal
from sqlalchemy.orm import Session
from typing import Optional
import pandas as pd
from app.schemas import Data, Bundle
from app.crud import sql
from fastapi.middleware.cors import CORSMiddleware


models.Base.metadata.create_all(bind=engine)

app = FastAPI()

origins = [

    "http://localhost:3000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Dependency


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get('/')
def root():
    return {"message": "Hello world!"}


@app.get("/sqlalchemy")
def test_post(db: Session = Depends(get_db)):
    posts = db.query(models.NewReportRule).all()
    return {"data": posts}


@app.post("/add_data", status_code=status.HTTP_201_CREATED)
def create_item(post: Data, db: Session = Depends(get_db)):
    print(post.dict())
    new_post = models.BackupRulesReport(**post.dict())
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return {"data": new_post}


@app.get("/search")
def search_items(query: str, address: Optional[str] = "", name: Optional[str] = "", db: Session = Depends(get_db)):
    items = db.query(models.NewReportRule).filter(models.NewReportRule.Pharmacy_Report_Name.contains(query))\
        .filter(models.NewReportRule.RoutingAddress1.contains(address))\
        .filter(models.NewReportRule.RoutingName.contains(name)).all()

    return {"data": items}


@app.get("/search_pharmacies")
def read_db():
    stored_proc = engine.execute(sql)
    results_as_dic = stored_proc.mappings().all()

    data = pd.DataFrame.from_dict(results_as_dic)
    return {"data": data['ProdigyReportName']}


@app.put("/search{id}")
def update_item(id: int, updated_post: Data, db: Session = Depends(get_db)):

    # change to payeeid for non-demo
    post_query = db.query(models.NewReportRule).filter(
        models.NewReportRule.id == id)

    post = post_query.first()

    if post == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"post with id: {id} does not exist")
    # testing id = 10834  ################################################################
    post_query.update(updated_post.dict(), synchronize_session=False)
    db.commit()
    return {"message": post_query.first()}


@app.delete("/search{id}", status_code=status.HTTP_204_NO_CONTENT)
def remove_item(id: int, db: Session = Depends(get_db)):

    # change to payeeid for non-demo
    post_query = db.query(models.NewReportRule).filter(
        models.NewReportRule.id == id)

    if post_query.first() == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"post with id: {id} does not exist")

    post_query.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)


@app.patch('/search/modify')
def update_part_of_item(id: str,  address: Optional[str] = "", name: Optional[str] = "", db: Session = Depends(get_db)):
    items = db.query(models.BackupRulesReport).filter(models.BackupRulesReport.RoutingAddress1.contains(id))\
        .filter(models.BackupRulesReport.RoutingAddress1.contains(address))\
        .filter(models.BackupRulesReport.Pharmacy_Report_Name.contains(name)).all()

    return items


@app.get("/api")
async def api_test():
    return {"message": "This is working correctly!"}
