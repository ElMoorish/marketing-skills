---
name: brand-context-builder
description: Builds or updates the shared brand-context.md file (customer, positioning, proof, voice) through a short interview and site review. Use when onboarding a business or refreshing its marketing facts.
license: MIT
metadata:
  version: "0.1.0"
  suite: marketing-skills
---

# Brand Context Builder

You create and maintain `.agents/brand-context.md`, the one file every other marketing skill
in this pack reads before it writes. Your job is accuracy, not polish: a short file of
verified facts beats a long file of guesses.

## Where the file lives

1. Look for `.agents/brand-context.md` in the project.
2. If you can't access a file system (for example in a chat app), look for an uploaded
   brand context file in the conversation or project knowledge.
3. If none exists, start from the template in `references/template.md`.

## Workflow

### Step 1: Gather what already exists

Ask the user for whatever they can share quickly, and read anything they point to:

- Website URL (read the home, pricing, about and one product page if you can browse)
- Pitch deck, sales one-pager, or existing positioning doc
- 2-3 pieces of writing they're proud of (for voice samples)
- Customer reviews, testimonials, or support tickets (for real customer language)

Don't block on any of these. Work with what you have.

### Step 2: Interview to fill gaps

Ask in small batches of 3-5 questions, most important first. Prioritize these sections,
because the other skills depend on them most:

1. **Company and product** (section 1)
2. **Ideal customer** (section 2)
3. **Approved proof and claims** (section 7)
4. **Brand voice** (section 8)

Then positioning, objections, competitors and channels. Stop when the user wants to stop;
unanswered fields stay `[UNKNOWN]`.

Good questions are concrete. Ask "What happened the week before your last three customers
signed up?" rather than "What is your customer's trigger event?".

### Step 3: Write or update the file

- Keep the template's headings so other skills can find sections.
- Use the user's words. Put customer quotes in section 5 exactly as written, with source and date.
- Only put a claim in section 7 if the user confirms it and names a source. Otherwise leave it out.
- Never invent numbers, quotes, logos, competitor prices or results.
- Mark anything inferred from the website (not confirmed by the user) with `(from site, unconfirmed)`.

### Step 4: Version it

When updating an existing file:

- Show the user a short summary of what you'll change before writing.
- Bump the version (patch for small fixes, minor for new sections or a positioning change).
- Add a changelog row with the date and the reason.
- Never silently delete a claim or learning. Move outdated items to the changelog note.

## Audit mode

If the user asks to review or audit the file, check and report:

- Fields still `[UNKNOWN]` or blank, ranked by how much they block other skills
- Claims in section 7 past their re-check date
- Competitor prices older than 90 days
- Voice section with no real writing samples
- Contradictions between sections (e.g. the target customer in section 2 vs. the positioning statement)

## Output

- In a project with files: write `.agents/brand-context.md` and summarize changes in chat.
- In a chat app: output the full file in one Markdown block the user can save and upload,
  then list the top 3 gaps to fill next.
