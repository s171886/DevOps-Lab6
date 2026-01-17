import time
import redis
import os

redis_host = os.getenv("REDIS_HOST", "redis")
r = redis.Redis(host=redis_host, port=6379, decode_responses=True)

while True:
    task = r.brpop("tasks")
    print("Wykonano zadanie:", task, flush=True)