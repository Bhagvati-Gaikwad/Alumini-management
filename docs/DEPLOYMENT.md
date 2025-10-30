# Deployment Guide

## ✅ Services Already Deployed

All services are live and ready to use!

### Service URLs

1. Alumni: https://codewords.agemo.ai/run/alumni_profile_manager_ab62a44e
2. Events: https://codewords.agemo.ai/run/event_manager_78a4f98b  
3. Analytics: https://codewords.agemo.ai/run/analytics_dashboard_9a07f8da
4. Newsletter: https://codewords.agemo.ai/run/newsletter_dispatcher_08e3e297

### API Endpoints

```
https://runtime.codewords.ai/run/{service_id}
```

## Setup

### 1. Get API Key
https://codewords.agemo.ai/account/keys

### 2. Connect Gmail (Newsletter only)
https://codewords.agemo.ai/account/integrations

## No Deployment Needed

Services are already deployed. Just:
1. Get your API key
2. Start integrating
3. Build frontend UI

## Updating Services

If you need to modify services:
1. Edit service code
2. Use CodeWords platform to deploy
3. Version control available (can rollback)

## Monitoring

View requests and logs:
- Go to service URL
- Click "Requests" tab
- See execution history

## Data

- Stored in Redis
- Persists across deployments
- Sample data already created
