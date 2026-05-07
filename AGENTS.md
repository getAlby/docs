# AGENTS.md

Guidance for AI coding agents (Claude Code, Cursor, Copilot, Codex, Aider) working on this repository.

## What this repo is

The public Alby documentation. Pages are written as Markdown files and synced to [GitBook](https://docs.getalby.com), which is the live site. The repo is the source of truth — changes merged here update the published docs.

Each top-level folder (currently just `hub/`) is a separate GitBook space with its own `SUMMARY.md` and `.gitbook.yaml`.

## Working rules

1. **`SUMMARY.md` is the navigation source of truth.** Every page that should appear in the sidebar must be listed there. When adding, removing, or renaming pages, update `SUMMARY.md` in the same change.
2. **Use relative Markdown links between pages** (e.g. `[link](../node/on-chain-balance.md)`). GitBook resolves these to the published URL.
3. **Renaming or moving a page?** Add a redirect in `hub/.gitbook.yaml` under `redirects:` so existing inbound links keep working. Format: `old/path: new/path.md` (the key has no `.md`, the value does).
4. **Don't reference the same Markdown file twice in `SUMMARY.md`** — each page has exactly one URL.
5. **Don't edit files inside `hub/.gitbook/includes/` or `hub/.gitbook/assets/` directly** unless you know what you're doing. Reusable content blocks and uploaded images are typically managed through the GitBook UI.
6. **Match terminology to the product.** The product is Alby Hub (the wallet). Use the same nouns the UI uses (e.g. "Lightning Balance", not "Spending Balance"; "App Connections", not "NWC apps").
7. **Don't introduce raw HTML tables for layout.** Use GitBook's custom blocks (`{% tabs %}`, `{% columns %}`, `{% hint %}`) — see the skill below for syntax.

## Writing style and tone

The current docs are written in a friendly, conversational, second-person voice. Match it. New copy you write should sound like a confident peer walking the user through something, not a technical spec.

**Do**

- **Address the reader directly.** "You'll see a heart icon", "your Hub", "click Save". Avoid third-person constructions.
- **Use contractions** (you'll, don't, it's). They're consistent with existing copy.
- **Lead with the user's goal**, then the mechanics. "To open a channel, click X. This connects your Hub to the network." — not the other way around.
- **Use the product's own vocabulary.** Alby Hub *is* the wallet. The user is *inside* it. Don't write "connect to a lightning wallet" or explain what a lightning wallet is — they're already using one.
- **Match noun casing to the UI.** "Lightning Balance", "On-chain Balance", "App Connections", "Sub-wallets" — these are product surfaces and should be capitalized as the UI shows them.
- **Be concrete.** Concrete UI labels in quotes (`click "Swap"`), concrete numbers (`1,000,000 sats`), concrete examples beat hand-wavy descriptions.

**Avoid**

- **Excessive cheerleading.** One "Congrats!" or "🎉" at the end of a multi-step tutorial is fine. Adding "Awesome!", "Great!", "Amazing!", "💪" between every step makes the docs feel infantile and dilutes real success moments. Default to none; add one only when the user has actually accomplished something meaningful.
- **Decorative emoji on every heading.** Existing pages already use emoji heavily (🚀 💪 🎉 ❤️ 🚰). Don't add more unless they serve as wayfinding (e.g. matching a sidebar icon).
- **Intensifiers** like "super exciting", "extremely powerful", "highly recommended", "truly empowering". Cut them — the facts speak louder.
- **Marketing copy in reference docs.** FAQ entries, glossary definitions, and step-by-step guides should be informative first. Save enthusiasm for landing-page-style intros.
- **Defining terms the reader already knows.** If they're reading the swaps page, they know what bitcoin and the lightning network are. Skip the primer.
- **Inconsistent terminology in the same page.** Pick "on-chain" or "onchain" and stick with it. (The repo uses both today; existing pages should be migrated only as part of a deliberate cleanup, not casually.)

**Conventions to follow**

- `bitcoin` (lowercase) for the asset, `Bitcoin` only when referring to the network/protocol as a proper noun. Existing docs are inconsistent — match the dominant choice in nearby paragraphs.
- `lightning network` lowercase; `Lightning Network` is acceptable when referring to it as a proper noun in formal contexts. Stay consistent within a page.
- `Alby Hub` always capitalized (it's the product name).
- `sats` lowercase, plural. Never "Sats" or "SATs".
- Use `&#x20;` at end of lines only if GitBook generated it — don't add it manually, don't strip it from existing files.

## GitBook syntax cheat sheet

The most commonly used blocks in this repo:

```markdown
{% hint style="info" %}…{% endhint %}            # info / warning / danger / success
{% tabs %}{% tab title="…" %}…{% endtab %}{% endtabs %}
{% stepper %}{% step %}…{% endstep %}{% endstepper %}
{% content-ref url="…md" %}[label](…md){% endcontent-ref %}
{% embed url="https://…" %}
{% file src="…" %}caption{% endfile %}
<details><summary>…</summary>…</details>
```

Page frontmatter:

```yaml
---
description: SEO description (also shown as page subtitle)
hidden: true   # hide from sidebar without removing the file
icon: book-open
---
```

## Full GitBook reference

For full GitBook authoring guidance — every custom block, frontmatter field, redirect format, monorepo setup, variables/expressions, and pitfalls — install the upstream **`gitbook` skill**:

> https://1050631731-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNkEGS7hzeqa35sMXQZ4X%2Fuploads%2F98DviOHe8vonzDstAxFA%2Fskill.md?alt=media&token=0a2d5fa2-ee75-4096-8309-22d66f337388

For Claude Code, save it under `~/.claude/skills/gitbook/SKILL.md` with YAML frontmatter (`name: gitbook`, a one-line `description`, `user-invocable: false`). Other agents: follow your tool's skill / rules-file convention.

## Verifying your changes

- After renaming files: `grep -rn "<old-slug>" hub/` should return nothing except the entry in `hub/.gitbook.yaml`.
- After editing copy: re-grep for the old wording across all of `hub/` to catch sibling files.
- Preview the rendered page in GitBook before merging when in doubt — Markdown extensions like `{% content-ref %}` and frontmatter `layout:` blocks don't render correctly in plain Markdown previewers.

## Commits and PRs

- Conventional Commits format (`feat:`, `fix:`, `chore:`, `docs:`).
- Branch off `main`. PR target is `main`.
- One logical change per PR — large copy renames and structural changes (renames, redirects, new sections) should not be mixed.
