from flask import Flask 
import psycopg2 
import os 

app = Flask(__name__) 

db_config = { 
    "host": "db", 
    "user": os.getenv("POSTGRES_USER"), 
    "password": os.getenv("POSTGRES_PASSWORD"), 
    "dbname": os.getenv("POSTGRES_DB"), 
} 

@app.route("/") 
def index(): 
    conn = psycopg2.connect(**db_config) 
    cur = conn.cursor() 
    cur.execute("SELECT content FROM messages LIMIT 1;") 
    result = cur.fetchone() 
    cur.close() 
    conn.close() 

    return result[0] 

 

if __name__ == "__main__": 
    app.run(host="0.0.0.0", port=int(os.getenv("BACKEND_PORT"))) 