# Agent Execution Engine

Goal: Build a durable, asynchronous job runner for agent/tool tasks, with persistent state and queue-backed execution.

## Architecture (WIP)

- Postgres — durable job storage
- Redis — job queue
- Worker — executes jobs asynchronously
- API — submit jobs and query status

## Local dev

1. Copy `.env.example` to `.env` and adjust if needed.

2. Start the local stack (FastAPI + Redis + Postgres):

```bash
docker compose up --build app redis postgres
```

3. Confirm services in another shell (app listens on `127.0.0.1:8000`, Redis on `127.0.0.1:6379`):

```bash
curl -i http://127.0.0.1:8000/health
curl -i -X POST http://127.0.0.1:8000/jobs \
  -H "Content-Type: application/json" \
  -d '{"task_type":"example","payload":{"message":"hello"}}'
docker compose exec redis redis-cli LRANGE jobs 0 -1
```

4. Run the test suite inside the dedicated dev/test image:

```bash
docker compose run --rm test
```

5. If you want to run tests on host instead of Docker:

```bash
pip install -e ".[dev]"
pytest -q
```
