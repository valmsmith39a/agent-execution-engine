# Agent Execution Engine — MVP Execution Plan

## Definition of Done

1. `docker compose up --build` starts:
   - postgres
   - redis
   - api
   - worker

2. `POST /jobs`:
   - Persists job in Postgres
   - Enqueues job_id in Redis

3. Worker:
   - Dequeues job
   - Marks RUNNING
   - Executes
   - Marks SUCCEEDED or FAILED
   - Persists result

4. `GET /jobs/{id}`:
   - Returns status
   - attempt_count
   - timestamps
   - result (if completed)

---

## Execution Rules

- Implement **ONE step at a time**
- Small commits only
- No broad refactors
- After each step:
  - Show `git diff --stat`
  - Provide verification commands

---

## Step 1 — Compose Baseline

Create/modify:
- README.md
- .env.example
- docker-compose.yml
- .gitignore

Outcome:
- `docker compose up` starts postgres + redis

Verification:
- `docker compose up -d`
- `docker ps`

---

## Step 2 — FastAPI Skeleton + Health

Create:
- app/main.py
- app/routes/health.py
- app/routes/__init__.py
- app/__init__.py
- app/core/config.py

Outcome:
- `GET /health` returns `{ "ok": true }`

Verification:
- `uv run uvicorn app.main:app --reload`
- `curl localhost:8000/health`

---

## Step 3 — DB Wiring + Jobs Table

Create:
- app/db/session.py
- app/models/job.py
- alembic.ini
- migrations/

Jobs table fields:
- id (UUID, PK)
- status (TEXT)
- type (TEXT)
- payload (JSONB)
- result (JSONB, nullable)
- attempt_count (INT, default 0)
- created_at
- updated_at

Outcome:
- `alembic upgrade head` creates jobs table

Verification:
- Confirm table exists in Postgres

---

## Step 4 — Redis Queue Wrapper

Create:
- app/queue/redis_queue.py
- app/queue/__init__.py

Functions:
- enqueue(job_id)
- dequeue_blocking(timeout)

Outcome:
- Centralized queue logic

---

## Step 5 — POST /jobs

Create/modify:
- app/routes/jobs.py
- app/schemas/job.py
- app/services/job_service.py

Behavior:
- Insert job as PENDING
- Enqueue job_id
- Return job id + status

Verification:
- `curl -X POST localhost:8000/jobs`

---

## Step 6 — GET /jobs/{id}

Modify:
- app/routes/jobs.py
- app/schemas/job.py

Behavior:
- Return status
- attempt_count
- timestamps
- result

Verification:
- `curl localhost:8000/jobs/<id>`

---

## Step 7 — Worker Loop

Create:
- worker/main.py
- worker/executor.py

Behavior:
- Dequeue job_id
- Load job from DB
- Mark RUNNING
- Execute stub
- Mark SUCCEEDED or FAILED
- Persist result

Verification:
- Submit job
- Confirm worker processes it
- Confirm status updates

---

## Step 8 — Dockerize API + Worker

Create:
- Dockerfile.api
- Dockerfile.worker
- Update docker-compose.yml

Outcome:
- Full system runs via `docker compose up --build`

Verification:
- Submit job via curl
- Confirm worker processes it

---

## Step 9 — Reliability Upgrade

Add:
- max_attempts
- Retry on failure
- attempt_count increment
- Optional: lease_expires_at

Outcome:
- Jobs retry until max attempts
- Failed jobs transition correctly

Verification:
- Force executor failure
- Confirm retries then FAILED

---

## Step 10 — Smoke Script + Docs

Create:
- scripts/smoke.sh
- Update README.md

Outcome:
- One-command demo script
