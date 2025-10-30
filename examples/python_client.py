#!/usr/bin/env python3
# Alumni Platform - Python Client
# pip install codewords-client

import asyncio
from codewords_client import AsyncCodewordsClient

ALUMNI_SVC = "alumni_profile_manager_ab62a44e"
EVENT_SVC = "event_manager_78a4f98b"
ANALYTICS_SVC = "analytics_dashboard_9a07f8da"

async def main():
    async with AsyncCodewordsClient() as client:
        # List alumni
        resp = await client.run(
            service_id=ALUMNI_SVC,
            inputs={"operation": "list", "limit": 10, "offset": 0}
        )
        data = resp.json()
        print(f"Found {data['total_count']} alumni")
        
        # Get analytics
        resp = await client.run(
            service_id=ANALYTICS_SVC,
            inputs={"refresh": True}
        )
        analytics = resp.json()['dashboard']
        print(f"Total Events: {analytics['total_events']}")

asyncio.run(main())
