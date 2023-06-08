from flask import Flask
from flask_sqlaclhemy import SQLAlchemy
import psycopg2
import psycopg2.extras

app=Flask(__name__)



if __name__=='__main__':
    app.run(debug=True,host='0.0.0.0')