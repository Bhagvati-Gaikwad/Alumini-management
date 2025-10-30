# API Integration Guide

## Authentication

All requests require CodeWords API key:
```
Authorization: Bearer YOUR_API_KEY
```

Get key: https://codewords.agemo.ai/account/keys

## Endpoints

Base URL: `https://runtime.codewords.ai/run/{service_id}`

### 1. Alumni Profile Manager
Service ID: `alumni_profile_manager_ab62a44e`

**Create Profile:**
```json
POST /run/alumni_profile_manager_ab62a44e
{
  "operation": "create",
  "name": "John Doe",
  "email": "john@example.com",
  "graduation_year": 2020,
  "degree": "BS Computer Science"
}
```

**List Profiles:**
```json
{
  "operation": "list",
  "limit": 50,
  "offset": 0
}
```

**Search:**
```json
{
  "operation": "search",
  "search_query": "engineer"
}
```

### 2. Event Manager
Service ID: `event_manager_78a4f98b`

**Create Event:**
```json
{
  "operation": "create",
  "title": "Tech Meetup",
  "description": "Networking event",
  "event_date": "2024-06-01",
  "event_time": "18:00",
  "location": "Campus Center",
  "max_attendees": 100
}
```

**Add RSVP:**
```json
{
  "operation": "add_attendee",
  "event_id": "EVENT_UUID",
  "alumni_id": "ALUMNI_UUID"
}
```

### 3. Analytics Dashboard
Service ID: `analytics_dashboard_9a07f8da`

```json
{ "refresh": true }
```

Returns: totals, breakdowns, statistics

### 4. Newsletter
Service ID: `newsletter_dispatcher_08e3e297`

```json
{
  "subject": "Monthly Update",
  "body": "<h2>Hello!</h2><p>News...</p>",
  "from_name": "Alumni Team"
}
```

**Requires**: Gmail connection

## Response Format

**Success:**
```json
{
  "success": true,
  "message": "Operation successful",
  "profile": {...}
}
```

**Error:**
```json
{
  "detail": "Error message"
}
```

## Status Codes
- 200: Success
- 400: Bad request
- 404: Not found
- 422: Validation error
- 500: Server error

## Examples

See `examples/` folder for:
- Python integration
- TypeScript integration
- cURL commands
