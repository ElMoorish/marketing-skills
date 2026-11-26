# SEO audit checklist

Pass/fail criteria for each check in `SKILL.md`. Read only the section you need.

## 1. Crawl and index

| Check | Pass | Flag when |
|---|---|---|
| robots.txt | Exists at `/robots.txt`, doesn't block key pages or CSS/JS | `Disallow: /` on production, or key folders blocked |
| XML sitemap | Listed in robots.txt or at `/sitemap.xml`; only indexable 200-status URLs | Missing, lists redirects/404s/noindex pages |
| noindex | Only on pages meant to be hidden (thank-you, internal search) | On money pages, blog, or the home page |
| Canonical | Each page has a self-referencing canonical or points to the true original | Missing on duplicates, points to a 404 or redirect, conflicts with sitemap |
| Redirects | Single hop, 301 for permanent moves | Chains of 2+ hops, 302 for permanent moves, loops |
| Status codes | Key pages return 200 | 4xx/5xx on linked pages |
| Internal links | Every key page reachable within 3 clicks of home | Orphan pages, broken links |
| HTTPS | One version (https, www or non-www) with others redirecting | Mixed versions both indexable |

## 2. AI crawler access

Look for user-agent groups in robots.txt that apply to AI crawlers. Common ones include
`GPTBot`, `OAI-SearchBot`, `ChatGPT-User`, `ClaudeBot`, `Claude-SearchBot`, `PerplexityBot`,
`Google-Extended` and `Applebot-Extended`. Crawler names change; check each vendor's
current documentation before giving advice.

Report a table of which are allowed or blocked. Distinguish crawlers used for **search
and live answers** (blocking them removes you from those answers) from crawlers used for
**model training** (blocking them usually doesn't affect search visibility). The decision
is the business's; your job is to make the trade-off visible.

Also check that the CDN or firewall isn't blocking these bots even when robots.txt allows them
(ask the user if you can't test it).

## 3. On-page

| Check | Pass | Flag when |
|---|---|---|
| Title tag | Unique, leads with the main term, roughly 50-60 characters | Missing, duplicated, or truncated mid-word |
| Meta description | Unique, states the benefit, roughly 120-160 characters | Missing or duplicated across many pages |
| H1 | Exactly one, matches the page's intent | Missing, multiple, or just the logo |
| Headings | Logical H2/H3 outline | Skipped levels used for styling only |
| Thin / duplicate content | Each page has a distinct purpose | Near-identical pages competing for the same term |
| Images | Descriptive alt text on meaningful images, modern formats | Missing alt, multi-MB images |
| URLs | Short, readable, lowercase, hyphenated | Session IDs, long parameter strings |

## 4. Structured data

Use JSON-LD. Validate with Google's Rich Results Test or the Schema.org validator.

| Page type | Expected schema |
|---|---|
| Home / About | `Organization` (name, url, logo, sameAs links to official profiles) |
| Product / pricing | `Product` or `SoftwareApplication` with `Offer` |
| Blog post | `Article` or `BlogPosting` with author and dates |
| FAQ section | `FAQPage` (only for real visible Q&A) |
| Any deep page | `BreadcrumbList` |
| Local business | `LocalBusiness` with address, hours, phone |

Flag schema that describes content not visible on the page; search engines treat that as spam.

## 5. Performance and mobile

Only flag what you can see. Recommend PageSpeed Insights (field data) for real
Core Web Vitals numbers rather than guessing them.

- Viewport meta tag present
- Hero images sized and compressed; lazy-load below the fold
- No large render-blocking scripts in `<head>`
- Text readable without zoom; tap targets not crowded

## 6. Content and intent

For each target term the business cares about:

1. What does the current top result type look like (guide, product page, list, tool)?
2. Which page on this site targets the term? Is there one?
3. Does that page match the intent and go deeper than what ranks now?

No page for a core term = recommend a new page and hand off to `content-brief`.

## 7. AI answer readiness

AI answer engines quote pages that state things plainly and can be trusted. Check:

- **Answer first:** key pages define the product and answer the main question in the
  first paragraph, in a sentence that makes sense quoted on its own.
- **Specific facts:** numbers, dates, prices and comparisons that are sourced and current.
- **Entity consistency:** the same brand name, product names and description across the
  site, social profiles and directory listings.
- **Authorship and trust:** named authors with bios on articles, a real About page,
  contact details, and dates on content.
- **Original material:** first-hand data, examples or research that other sites can't copy.

These are good practice for readers and search alike; don't promise they guarantee AI citations.
