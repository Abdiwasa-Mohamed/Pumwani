from main import from db
import psycopg2
import os

class Admin():
    __tablename__='administartors'
    try:
            create table(
        id=db.column(db.integer primary_key=True)
        admin_name=db.column(db.string(250), nullable=False, unquie=True)
        email=db.column(db.string(100),nullable=False unique=True)
        password=db.column(db.string(100),nullable=False, format=(hash)))
    except Exception as e:
        print(e)
    
    