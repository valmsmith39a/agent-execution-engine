# Agent Execution Engine

Goal: Build a durable, asynchronous job runner for agent/tool tasks, with persistent state and queue-backed execution.

## Architecture (WIP)

- Postgres — durable job storage
- Redis — job queue
- Worker — executes jobs asynchronously
- API — submit jobs and query status

## Local dev

1. Copy `.env.example` to `.env` and adjust if needed.

2. Start dependencies:

```bash
docker compose up -d
```

3. Install app + dev dependencies and run tests:

```bash
pip install -e ".[dev]"
pytest -q
```
