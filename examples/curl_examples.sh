#!/bin/bash
# Set your API key: export CODEWORDS_API_KEY=your_key

API_KEY="${CODEWORDS_API_KEY}"
BASE="https://runtime.codewords.ai/run"

# List alumni
curl -X POST "$BASE/alumni_profile_manager_ab62a44e" \
  -H "Authorization: Bearer $API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"operation": "list", "limit": 10, "offset": 0}'

# Get analytics
curl -X POST "$BASE/analytics_dashboard_9a07f8da" \
  -H "Authorization: Bearer $API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"refresh": true}'
