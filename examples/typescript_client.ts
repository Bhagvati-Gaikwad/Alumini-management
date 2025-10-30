// npm install @codewords/client
import { createServiceClient } from "@codewords/client";

const client = createServiceClient(process.env.CODEWORDS_API_KEY!);

const ALUMNI_SVC = "alumni_profile_manager_ab62a44e";
const ANALYTICS_SVC = "analytics_dashboard_9a07f8da";

async function main() {
  // List alumni
  const alumni = await client.runService(ALUMNI_SVC, "", {
    operation: "list",
    limit: 10,
    offset: 0
  });
  console.log(`Found ${alumni.total_count} alumni`);
  
  // Get analytics
  const analytics = await client.runService(ANALYTICS_SVC, "", {
    refresh: true
  });
  console.log(`Total Events: ${analytics.dashboard.total_events}`);
}

main();
