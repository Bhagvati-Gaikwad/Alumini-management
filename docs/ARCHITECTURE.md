# Alumni Platform Architecture

## System Overview

```
Frontend (Custom UI)
    ↓ REST API calls
CodeWords Backend Services
    ├─ Alumni Profile Manager
    ├─ Event Manager  
    ├─ Analytics Dashboard
    └─ Newsletter Dispatcher
    ↓
Redis Storage (Persistent)
Pipedream Integrations (Gmail)
```

## Components

### 1. Backend Services (Python/FastAPI)
- **Stateless**: Each request is independent
- **Auto-scaling**: CodeWords handles scaling
- **Serverless**: No server management needed

### 2. Storage (Redis)
- **Persistent**: Data survives restarts
- **Namespaced**: User-isolated data
- **Fast**: In-memory performance

### 3. Integrations (Pipedream)
- **Gmail**: Newsletter sending
- **2000+ platforms**: Available for future

## Data Models

### Alumni Profile
```python
{
    "profile_id": "uuid",
    "name": str,
    "email": str,
    "graduation_year": int,
    "degree": str,
    "current_job": str | None,
    "company": str | None,
    "skills": [str],
    "achievements": [str],
    "created_at": "ISO timestamp",
    "updated_at": "ISO timestamp"
}
```

### Event
```python
{
    "event_id": "uuid",
    "title": str,
    "description": str,
    "event_date": "YYYY-MM-DD",
    "event_time": "HH:MM",
    "location": str,
    "max_attendees": int,
    "attendee_ids": [str],  # Alumni profile IDs
    "created_at": "ISO timestamp",
    "updated_at": "ISO timestamp"
}
```

## API Design

All services expose:
- **POST /** endpoint (main operations)
- **Pydantic models** for validation
- **HTTP status codes** for errors
- **JSON responses**

## Security

- **Authentication**: Bearer tokens
- **Data isolation**: User namespaces
- **Input validation**: Pydantic strict mode
- **Error handling**: HTTP exceptions

## Scalability

- Horizontal scaling (automatic)
- Redis for persistent state
- Async operations for performance
- Rate limiting (built-in)
