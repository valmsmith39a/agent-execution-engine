# Agent Execution Engine

Goal: Build a durable job runner for agent/tool tasks.

Stack:
- FastAPI control plane
- Redis queue
- Postgres durable job state
- Worker process executes jobs

MVP Definition of Done:
1) docker compose up starts postgres, redis, api, worker
2) POST /jobs creates a job and enqueues it
3) Worker picks job, marks RUNNING then SUCCEEDED/FAILED
4) GET /jobs/{id} returns status + timestamps
5) Result stored durably in Postgres

Constraints:
- Keep it simple. No auth. No UI. No fancy frameworks.
- Keep diffs small, avoid broad refactors.

## Modes

### Writer Mode (Terminal A)
- May create/modify files.
- Must keep diffs small and scoped.
- Must run verification commands after each slice.

### Reviewer Mode (Terminal B)
- DO NOT edit files.
- DO NOT run commands that modify files (formatters, generators, migrations, etc.).
- Only read, analyze, explain, and suggest.
- Provide risks + test checklist for each diff.
