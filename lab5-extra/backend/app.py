from flask import Flask
import redis
import os

app = Flask(__name__)
redis_host = os.getenv("REDIS_HOST", "redis")
r = redis.Redis(host=redis_host, port=6379, decode_responses=True)

@app.route("/task")
def send_task():
    r.lpush("tasks", "nowe zadanie")
    return "Zadanie wysłane do kolejki"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)