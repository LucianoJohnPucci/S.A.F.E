# S.A.F.E
 (Stalker Analysis &amp; Footprint Extraction)

 Ai Engine= StalkGuard — Detect. Document. Protect.

## ECHO Backend (MVP scaffold)

This repository now includes the initial backend scaffold for the ECHO (Emergency Child Homing Operations) system.

### Stack
- FastAPI (Python 3.11)
- PostgreSQL with PostGIS (via Docker)
- Redis (for queues/caching, via Docker)
- Uvicorn

### Quickstart (Docker)
1. Copy `env.sample` to `.env` and adjust values if needed.
2. Start services:
   - `docker compose up -d --build`
3. Verify health endpoint:
   - `curl http://localhost:8000/health`
   - Expected: `{ "status": "ok" }`

To stop: `docker compose down`

### Local development (without Docker)
1. Create and activate a virtual environment (Python 3.11+).
2. `pip install -r backend/requirements.txt`
3. `cp env.sample .env` (or create a `.env` file) and ensure `DATABASE_URL` and `REDIS_URL` are reachable.
4. Run the API:
   - `uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload` (from `backend/` directory)

### Project structure (initial)
```
backend/
  app/
    main.py
    core/
      settings.py
  Dockerfile
  requirements.txt
docker-compose.yml
env.sample
```

More services (devices, locations, websockets, auth) will be added in upcoming phases.