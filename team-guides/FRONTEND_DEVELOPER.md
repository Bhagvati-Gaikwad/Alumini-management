# Frontend Developer Guide

## Your Mission
Build custom UI consuming CodeWords REST APIs

## Services to Integrate
- Alumni Profile Manager (CRUD)
- Event Manager (Events + RSVP)
- Analytics Dashboard (Stats)
- Newsletter Dispatcher (Email)

## Tech Stack Recommendation
- React + TypeScript
- @codewords/client
- TailwindCSS
- shadcn/ui

## Quick Start
```typescript
import { createServiceClient } from "@codewords/client";
const client = createServiceClient(process.env.CODEWORDS_API_KEY!);

const alumni = await client.runService(
  "alumni_profile_manager_ab62a44e",
  "",
  { operation: "list", limit: 50, offset: 0 }
);
```

## Pages to Build
1. Dashboard (Analytics overview)
2. Alumni Directory (List + Search)
3. Events (List + RSVP)
4. Newsletter Composer

## Resources
- API Examples: `../examples/typescript_client.ts`
- API Guide: `../docs/API_GUIDE.md`

**Get UI Generated**: Ask Cody for v0.dev/Lovable.dev prompt!
