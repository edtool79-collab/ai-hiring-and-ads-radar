# AI hiring & ads radar

A dated, evidence-backed snapshot of **10 companies**: public hiring activity, website technology and Google Ads Transparency results. All 10 Google Ads lookups completed successfully.

[API catalog](https://gethirepulse.xyz/v1/catalog) · [MCP server](https://github.com/edtool79-collab/hirepulse-mcp) · [Apify task directory](https://edtool79-collab.github.io/hirepulse-tools/tasks-directory.md)

## Company snapshot

| Company / evidence | Open roles | Hiring score | Hiring signal | Google Ads sample | Google total estimate | Checked (UTC) |
|---|---:|---:|---|---:|---|---|
| [ramp.com](data/ramp.com.json) | 169 | 100 / 100 | hypergrowth | 40 | 3,000–4,000 | 2026-10-21 14:41:30 |
| [stripe.com](data/stripe.com.json) | 730 | 100 / 100 | hypergrowth | 40 | 8,000–9,000 | 2026-10-21 14:41:37 |
| [cloudflare.com](data/cloudflare.com.json) | 439 | 100 / 100 | hypergrowth | 40 | 3,000–4,000 | 2026-10-21 14:41:54 |
| [notion.so](data/notion.so.json) | 135 | 100 / 100 | hypergrowth | 13 | 13 | 2026-10-21 14:41:57 |
| [anthropic.com](data/anthropic.com.json) | 674 | 100 / 100 | hypergrowth | 5 | 5 | 2026-10-21 14:42:05 |
| [figma.com](data/figma.com.json) | 140 | 100 / 100 | hypergrowth | 40 | 1,000–2,000 | 2026-10-21 14:42:09 |
| [datadoghq.com](data/datadoghq.com.json) | 438 | 100 / 100 | hypergrowth | 40 | 9,000–10,000 | 2026-10-21 15:05:09 |
| [vercel.com](data/vercel.com.json) | 94 | 96 / 100 | hypergrowth | 40 | 100–200 | 2026-10-21 14:41:40 |
| [linear.app](data/linear.app.json) | 29 | 67 / 100 | active hiring | 26 | 26 | 2026-10-21 14:41:25 |
| [monday.com](data/monday.com.json) | 113 | 63 / 100 | active hiring | 40 | 30,000–40,000 | 2026-10-21 15:05:09 |

## Evidence and interpretation

- The JSON linked in every row contains the completed profile, section statuses, ad creatives and source timestamps. Google Ads sample size is capped at 40; the total estimate is Google’s range, not a count of every active ad or an estimate of advertising spend.
- Hiring score is a documented heuristic based on open roles, known posting dates and hiring functions. It is not a purchase prediction. Some job-board responses are truncated; the JSON states this, and breakdowns describe the returned sample.
- Monday.com hiring was supplemented from its [official careers page](https://monday.com/careers), which exposes 113 positions. Posting dates are unavailable there, so recency points are not awarded.
- Datadog hiring was supplemented from its [public company Greenhouse feed](https://boards-api.greenhouse.io/v1/boards/datadog/jobs?content=true), which returned 438 positions. These two supplements correct automatic board discovery misses; they are identified in each JSON file.
- The maintainer collected this snapshot through authenticated access to the independent Modal engine using the production TypeScript adapters. No Apify Actors were run, no public IP quota was bypassed, and no x402 payments were signed. The public API still has a shared allowance of five successful calls per IP per UTC day.

## Refresh

```bash
python refresh.py --render-only
python refresh.py linear.app ramp.com
```

The first command rebuilds this README from saved evidence without network calls. The second refreshes only the named companies through the public gateway, then rebuilds the table. A 402, timeout or incomplete section preserves the previous verified snapshot. The script never pays automatically. Fresh timestamps are stored per company; running the renderer does not make older data fresh.

To import a verified maintainer snapshot: `python refresh.py --import-dir /path/to/verified-json`. This requires one valid JSON file per imported company; no engine credentials belong in this repository.

## Use responsibly

Public job postings, website tags and advertising activity are operating signals. They do not establish revenue, financial health, employment headcount, merchant safety or ownership. A HirePulse badge is a link to public signals, not a security certification.

Maintained by [HirePulse](https://gethirepulse.xyz). Data is a snapshot of public sources and can change after collection. Code: MIT. Public-source content remains subject to its original terms.
