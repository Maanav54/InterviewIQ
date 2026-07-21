# InterviewIQ

InterviewIQ is an AI interview intelligence platform for placement candidates. It pairs a premium React dashboard with a modular FastAPI API for authentication, personalized questions, answer evaluation, and readiness analytics.

## Product highlights

- Responsive dark SaaS dashboard with performance trend, radar skills matrix, focus plan, and interview launcher
- JWT authentication and password hashing
- Resume-ready data model (skills and ATS score storage)
- Structured question generation and answer evaluation endpoints ready to be backed by OpenAI/Gemini
- PostgreSQL-ready SQLAlchemy architecture with a SQLite local-development fallback
- Docker-ready backend and Vercel-compatible Vite frontend

## Architecture

```text
React + Vite dashboard → FastAPI routers → services/ai → OpenAI or Gemini
                              ↓
                       SQLAlchemy → PostgreSQL
```

## Run locally

```bash
# frontend
cd client
npm install
npm run dev

# backend (in another terminal)
cd server
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
copy .env.example .env
uvicorn app.main:app --reload
```

Visit `http://localhost:5173`; API documentation is at `http://localhost:8000/docs`.

## API surface

| Method | Path | Purpose |
| --- | --- | --- |
| POST | `/auth/register` | Create user and return JWT |
| POST | `/auth/login` | Authenticate user |
| POST | `/interviews/questions` | Generate personalized questions |
| POST | `/interviews/evaluate` | Return structured answer feedback |
| GET | `/dashboard/summary` | Fetch readiness analytics |

## Deployment

Deploy `client/` to Vercel with `npm run build`. Deploy `server/` to Render with the included Dockerfile, configure `DATABASE_URL`, `JWT_SECRET`, `FRONTEND_ORIGIN`, and optionally `OPENAI_API_KEY`. Use a managed PostgreSQL URL in production.
