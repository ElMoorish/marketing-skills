# AGENTS.md

This repository is a pack of marketing skills for AI agents.

## For marketing tasks

1. Read `.agents/brand-context.md` first. It is the only source of company facts.
2. Use the matching skill in `.agents/skills/`:
   - `brand-context-builder`: create or update the brand context file
   - `seo-audit`: technical SEO and AI search visibility audits
   - `content-brief`: writer-ready briefs for articles and landing pages
   - `social-posts`: platform-native social posts and scripts
   - `campaign-review`: pre-launch review of campaigns, ads, pages and emails

## Rules for every marketing task

- Never invent statistics, quotes, testimonials, logos, prices or results. Use only the
  approved proof in brand context section 7, or mark the gap `[UNVERIFIED - NEEDS SOURCE]`.
- Draft only. Never publish, post, send, schedule, launch, or change ad budgets or bids
  without explicit approval from a person for that specific action.
- Propose edits to `.agents/brand-context.md` and wait for approval before writing them.

## For changes to this repository

- Skills follow the open Agent Skills spec. Frontmatter keys: `name`, `description`,
  `license`, `compatibility`, `metadata` only. Descriptions stay at or under 200 characters
  with no angle brackets.
- Run `python3 scripts/build.py --check` before committing.
