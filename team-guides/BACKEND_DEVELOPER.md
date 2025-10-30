# Backend Developer Guide

## Your Mission
Maintain and extend CodeWords services

## Services
1. Alumni Profile Manager - CRUD operations
2. Event Manager - Events + RSVP
3. Analytics Dashboard - Statistics
4. Newsletter Dispatcher - Email campaigns

## Tech Stack
- Python 3.11
- FastAPI
- Pydantic
- Redis (CodeWords)

## Service Pattern
```python
from codewords_client import logger, run_service, redis_client
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

app = FastAPI(title="Service Name")

@app.post("/")
async def endpoint(request: Request):
    async with redis_client() as (redis, ns):
        # Use Redis with namespace
        result = await process(request, redis, ns)
        return Response(success=True, data=result)

if __name__ == "__main__":
    run_service(app)
```

## Resources
- Service Code: `../services/`
- Architecture: `../docs/ARCHITECTURE.md`
- CodeWords Docs: https://codewords.agemo.ai
