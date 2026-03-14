import os

from redis import Redis

QUEUE_NAME = "jobs"


def _redis_client() -> Redis:
    host = os.getenv("REDIS_HOST", "redis")
    port = int(os.getenv("REDIS_PORT", "6379"))
    password = os.getenv("REDIS_PASSWORD") or None
    return Redis(host=host, port=port, password=password, decode_responses=True)


def enqueue(job_id: str) -> None:
    client = _redis_client()
    client.rpush(QUEUE_NAME, job_id)
