# AI Hiring & Ads Radar

Live, evidence-based hiring signals and advertising activity for leading tech companies — measured, not guessed.

**Built on [HirePulse](https://gethirepulse.xyz).** MCP server: `https://gethirepulse.xyz/mcp` · 5 free calls/day · x402 USDC on Base · [API catalog](https://gethirepulse.xyz/v1/catalog)

| Badge | Company | Open roles | Hiring intent | Status | ATS | Detected tech | Google Ads | Checked (UTC) |
|---|---|---|---|---|---|---|---|---|
| ![badge](https://gethirepulse.xyz/badge/ramp.com.svg) **ramp.com** | 169 | 100/100 | hypergrowth | ashby | Google Workspace | no data | 2026-10-21 13:59:33 |
| ![badge](https://gethirepulse.xyz/badge/stripe.com.svg) **stripe.com** | 730 | 100/100 | hypergrowth | greenhouse | Google Workspace | no data | 2026-10-21 13:59:40 |
| ![badge](https://gethirepulse.xyz/badge/vercel.com.svg) **vercel.com** | 94 | 96/100 | hypergrowth | greenhouse | Google Workspace | no data | 2026-10-21 13:59:42 |
| ![badge](https://gethirepulse.xyz/badge/linear.app.svg) **linear.app** | 29 | 67/100 | active_hiring | ashby | Google Workspace | no data | 2026-10-21 13:59:28 |

> Rows are produced from public sources only (company job boards, website HTML/DNS, Google Ads Transparency Center). `intent_score` is a hiring-based heuristic, not a purchase prediction. `no data` means the section returned nothing free of charge — never a paid estimate. Each row costs one of the 5 free daily calls.

### Queued — free quota resets 2026-10-22 00:00 UTC

`monday.com`, `cloudflare.com`, `notion.so`, `anthropic.com`, `figma.com`, `datadoghq.com` — not fetched yet: the 5 free calls per IP per day were spent on the rows above (verified `402` responses, no payment made).

## Refresh

```bash
python refresh.py linear.app ramp.com stripe.com vercel.com   # add domains as free quota allows
```

`refresh.py` calls `POST https://gethirepulse.xyz/v1/company-profile` (one free call per domain per day), writes the raw JSON into `data/<domain>.json` and rebuilds this table. No API key, no account.

## Why this matters for agents

- Hiring velocity is one of the few public, forward-looking buying signals for B2B.
- Ads + tech stack show what a company is actively investing in right now.
- Everything here is reproducible: same input, same public evidence, no proprietary data.

Related: [HirePulse Apify tasks directory](https://github.com/edtool79-collab/hirepulse-tools/blob/main/tasks-directory.md) · [HirePulse MCP](https://github.com/edtool79-collab/hirepulse-mcp)

_Generated 2026-10-21 14:00 UTC from live API responses stored under `data/`._
