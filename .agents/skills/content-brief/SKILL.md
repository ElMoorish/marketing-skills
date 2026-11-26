---
name: content-brief
description: Creates writer-ready content briefs for blog posts, landing pages and guides, covering search intent, angle, outline, proof points, and SEO details. Use before writing any long-form marketing content.
license: MIT
metadata:
  version: "0.1.0"
  suite: marketing-skills
---

# Content Brief

You turn a topic or target search term into a brief that a writer (human or AI) can
follow to produce a page that ranks, gets quoted, and sounds like the brand. You write
the brief, not the article, unless the user asks for both.

## Before you start

1. Read `.agents/brand-context.md` (or the uploaded brand context). You need the
   customer (section 2), positioning (3), customer language (5), approved proof (7)
   and voice (8). If it's missing, ask for: who the reader is, what the product does,
   and what the reader should do after reading.
2. Get the input: a topic, a target search term, or an existing page to rewrite.
3. Ask for the goal if it isn't obvious: traffic, signups, demo requests, or supporting sales.

## Workflow

### 1. Pin down intent

- Who searches this, at what stage (problem-aware, comparing solutions, ready to buy)?
- What format would satisfy them (how-to guide, comparison, list, template, landing page)?
- If you can search the web, look at what currently ranks and note the common format,
  depth and gaps. If you can't, say so and reason from the term.

### 2. Choose an angle

Pick one angle that is true for this brand and hard for competitors to copy:
first-hand data, a strong opinion, a specific customer segment, a worked example, or a
contrarian take backed by proof. State it in one sentence. If two angles compete, pick
one and list the other as an alternative.

### 3. Build the outline

- H1 and 5-10 H2s, each with 1-2 lines on what the section must cover.
- Put the direct answer to the main question in the first 100 words.
- Mark where to use a table, checklist, example, screenshot or quote.
- Map proof points from brand context section 7 to the sections that need them by ID
  (e.g. `P-01`). If a section needs proof that doesn't exist, write
  `[PROOF NEEDED: what kind]` instead of inventing it.

### 4. Add the SEO and AI answer details

- Primary term and 3-8 related terms or questions to cover naturally
- Title tag (about 50-60 characters) and meta description (about 120-160) — 2 options each
- Suggested URL slug
- Internal links: 3-5 existing pages to link to and from (ask, or list as placeholders)
- Schema type to add (Article, FAQPage, HowTo, Product)
- One quotable, self-contained definition or answer sentence for AI answer engines

### 5. Voice and guardrails

- Copy the relevant voice traits and one writing sample reference from brand context.
- List customer phrases from section 5 the writer should use.
- List banned words and forbidden claims from sections 5 and 7.

## Output

Use the template in `references/brief-template.md`. Keep the brief to what a writer
needs: aim for one to two pages.

## Handoffs

- Social promotion of the finished piece: `social-posts`.
- Review before publishing: `campaign-review`.
