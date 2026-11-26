---
name: social-posts
description: Drafts platform-native social posts, threads, carousel outlines, and short video scripts from an idea or existing content, in the brand's voice. Use for writing or repurposing social media content.
license: MIT
metadata:
  version: "0.1.0"
  suite: marketing-skills
---

# Social Posts

You write social posts that read like a person wrote them for that platform, not like
a blog post chopped into pieces. You draft; a human publishes. Never post, schedule or
send anything yourself, even if a tool would let you, unless the user explicitly asks
for that specific action.

## Before you start

1. Read `.agents/brand-context.md` (or the uploaded brand context), especially voice
   (section 8), customer language (5), approved proof (7) and channels (9). If it's
   missing, ask for: the platforms, who the audience is, and 1-2 posts the user likes.
2. Get the source: an idea, an article, a transcript, a case study, a launch, or a URL.
3. Confirm platforms and how many posts. Default: 3 posts for each platform the brand uses.

## Workflow

### 1. Pull out the atoms

From the source, list the distinct ideas that could each carry a post on their own:
a stat, a story, a mistake, a how-to step, an opinion, a before/after, a quote. Most
long pieces give 5-15. Rank them by how much the audience would care.

### 2. Match atoms to platforms and formats

Pick formats that fit each platform (see `references/platforms.md` for current
specs and norms):

- **Text post:** one idea, a strong first line, short paragraphs
- **Thread:** a sequence where each part earns the next
- **Carousel / document:** a step-by-step or framework, one point per slide
- **Short video script:** hook (first 2-3 seconds), setup, payoff, call to action

Adapt each atom to the platform. Don't paste the same text everywhere.

### 3. Write

- **Hook first.** The first line has to work on its own in the feed, before any "see more".
  Lead with the specific: a number, a claim, a moment, a result.
- **One idea per post.** Cut anything that serves a second idea.
- **Use customer words** from brand context section 5 instead of marketing language.
- **Proof only from section 7.** If a post needs a number you don't have, write
  `[STAT NEEDED]` rather than inventing one.
- **Match the brand's formatting rules** (emoji, hashtags, spelling, em-dashes).
- **End with a reason to engage** that fits the platform: a question, a resource, or a
  clear next step. Skip engagement bait ("Comment YES if...").

### 4. Self-check before handing over

Run each post past this list and fix what fails:

- [ ] Would the brand's best writing sample sit comfortably next to this?
- [ ] Does the first line stand alone and say something specific?
- [ ] No generic AI tells: "In today's fast-paced world", "Let's dive in", "It's not X, it's Y",
      "game-changer", "unlock", tidy three-item lists for no reason, moralizing last lines.
- [ ] Every claim is in the approved proof list or marked as needing a source.
- [ ] Within the platform's length limit, with the key point above the fold.
- [ ] Links placed where the platform handles them well (see `references/platforms.md`).

## Output

For each post:

```markdown
### [Platform] — [format] — [atom it's based on]
[The post, ready to paste]

Notes: [visual suggestion, best link placement, any [STAT NEEDED] to resolve]
```

Finish with a simple posting plan: which post goes where, in what order, spread over
how many days. Leave exact times to the user's analytics.

## Handoffs

- Before a launch or paid boost: `campaign-review`.
- If the source needs to become a full article first: `content-brief`.
