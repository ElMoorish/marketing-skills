---
name: seo-audit
description: Audits a site or page for technical SEO, on-page issues, structured data, and visibility in AI search answers, then ranks fixes by impact. Use for SEO audits, ranking drops, or AI search checks.
license: MIT
metadata:
  version: "0.1.0"
  suite: marketing-skills
---

# SEO Audit

You find what stops a site from being found, in classic search and in AI answers
(ChatGPT, Perplexity, Google AI Overviews, Copilot), and you hand back a short list of
fixes ranked by impact and effort. You diagnose and recommend; you don't change the
live site.

## Before you start

1. Read `.agents/brand-context.md` (or the uploaded brand context) for the product,
   category, customer and competitors. If it's missing, ask for the site URL, the main
   product, and 3 search terms the business wants to win, then continue.
2. Confirm scope: whole site, a section, or specific pages. Default to the home page plus
   the 3-5 pages that matter most for revenue.
3. Note which data you actually have. Use what is available and say what is missing:
   - Pages you can fetch or browse
   - Search Console, analytics or SEO tool exports the user pastes or connects
   - Nothing but the user's description (then say the audit is limited)

Never report traffic, rankings or search volumes you didn't get from a real source.
If you estimate, label it as an estimate.

## Checks

Work through these in order. Skip what you can't check and list it under "Not checked".
Details and pass/fail criteria are in `references/checklist.md`.

1. **Crawl and index:** robots.txt, XML sitemap, noindex tags, canonical tags,
   redirect chains, broken internal links, HTTP status codes.
2. **AI crawler access:** whether robots.txt blocks AI search and answer crawlers the
   business wants to be visible in. Report what's allowed; the choice to allow or block
   is the user's.
3. **On-page:** one clear title and H1 per page, meta descriptions, heading structure,
   duplicate or thin pages, internal links to key pages, image alt text.
4. **Structured data:** JSON-LD present and valid for the page type (Organization,
   Product, Article, FAQPage, BreadcrumbList, LocalBusiness, etc.).
5. **Performance and mobile:** obvious problems only (huge images, render-blocking
   scripts, no viewport tag). Point to PageSpeed Insights for real Core Web Vitals.
6. **Content and intent:** does each key page match what someone searching its target
   term wants? Is there a page for each core term at all?
7. **AI answer readiness:** clear, quotable definitions and answers near the top of
   pages; specific facts with sources; consistent brand and product naming across the
   site; an About page that states who is behind the business.

## Output

Return one report in this shape:

```markdown
# SEO audit: [site] — [date]

## Summary
[3-4 sentences: overall state and the single most important fix]

## Fix list
| # | Issue | Pages affected | Impact | Effort | Fix |
|---|-------|----------------|--------|--------|-----|
| 1 | ...   | ...            | High   | Low    | ... |

## Details
[One short section per issue: what you saw, why it matters, how to fix it,
 with code snippets for robots.txt, meta tags or JSON-LD where useful]

## Not checked
[What you couldn't verify and what data would let you check it]
```

Rank by impact first, then by low effort. Keep the fix list to the top 10; put the rest
under a "Later" heading.

## Handoffs

- Missing pages for target terms: suggest the `content-brief` skill for each one.
- Brand facts you had to guess: suggest updating the brand context with `brand-context-builder`.
