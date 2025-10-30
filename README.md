# Alumni Platform - CodeWords Backend

## 🎓 SIH25017: Digital Platform for Alumni Data Management

**Built with**: CodeWords Automation Platform

### 🚀 Live Services

1. [Alumni Profile Manager](https://codewords.agemo.ai/run/alumni_profile_manager_ab62a44e)
2. [Event Manager](https://codewords.agemo.ai/run/event_manager_78a4f98b)
3. [Analytics Dashboard](https://codewords.agemo.ai/run/analytics_dashboard_9a07f8da)
4. [Newsletter Dispatcher](https://codewords.agemo.ai/run/newsletter_dispatcher_08e3e297)

### 📦 Service IDs
```
alumni_profile_manager_ab62a44e
event_manager_78a4f98b
analytics_dashboard_9a07f8da
newsletter_dispatcher_08e3e297
```

### 🔑 API Access
**Base URL**: `https://runtime.codewords.ai/run/{service_id}`
**Auth**: `Authorization: Bearer YOUR_API_KEY`
**Get Key**: https://codewords.agemo.ai/account/keys

### 📚 Documentation
- `docs/ARCHITECTURE.md` - System architecture
- `docs/API_GUIDE.md` - API integration guide
- `docs/DEPLOYMENT.md` - Deployment info
- `team-guides/` - Role-specific guides

### 💡 Quick Test
```bash
curl -X POST https://runtime.codewords.ai/run/alumni_profile_manager_ab62a44e \
  -H "Authorization: Bearer YOUR_KEY" \
  -H "Content-Type: application/json" \
  -d '{"operation": "list", "limit": 10, "offset": 0}'
```

### 👥 Team Roles
- **Frontend Dev**: Build custom UI (see team-guides/)
- **Backend Dev**: Maintain services (see team-guides/)  
- **Engagement Lead**: Use analytics & newsletters (see team-guides/)

---
**Questions?** Contact via https://codewords.agemo.ai support
