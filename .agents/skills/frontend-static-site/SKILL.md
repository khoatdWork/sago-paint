---
name: frontend-static-site
description: Build, edit, and review this repository's Sago Paint static frontend pages. Use when working on HTML, CSS, Bootstrap layout, responsive behavior, Vietnamese marketing content presentation, SEO metadata, visual polish, accessibility, or browser verification for this static site.
---

# Frontend Static Site

## Sago Paint working agreements

- Read `AGENTS.md`, `DESIGN.md` and the relevant `docs/pages/<route>/CONTEXT.md`.
- Record every task's phases and skill usage using `docs/tasks/TEMPLATE.md`.
- Be Vietnam Pro is the only UI typeface; shared overrides live in `assets/css/site-base.css`.
- Fix generated output and its source together. Never classify a page as a product by filename alone.
- Run the checks listed in `AGENTS.md`. Deploy only the public `dist` output.
- Audit with `ponytail-audit` and review the final diff with `ponytail-review`.

## Source Basis

Use the relevant guidance categories from `finfin/awesome-frontend-skills`: general frontend UI engineering, frontend design, web design review, web quality, and browser testing. Do not apply framework-specific guidance unless the repo actually adopts that framework.

## Project Shape

- Treat this as a static HTML/CSS site: root `*.html` pages, shared `styles.css`, `category-pages.css`, assets under `assets/`, generated SEO files such as `sitemap.xml` and `robots.txt`.
- Prefer existing Bootstrap 5 patterns and project CSS variables before adding new CSS.
- Keep Vietnamese copy and SEO metadata intact unless the task is explicitly about copy changes.
- Keep changes scoped to the smallest page/CSS surface that solves the request.

## Frontend Workflow

1. Inspect the target page plus shared CSS before editing.
2. Reuse existing sections, classes, spacing, button styles, color tokens, and image patterns.
3. Make semantic HTML changes first; use CSS only for layout or presentation that HTML cannot express.
4. Preserve responsive behavior for mobile, tablet, and desktop.
5. Avoid new dependencies, build tools, JavaScript frameworks, or component systems unless the user asks for them.

## Quality Bar

- Keep navigation, calls to action, cards, images, forms, and footer consistent across pages.
- Check accessibility basics: meaningful headings, alt text, visible focus, sufficient contrast, labels for inputs, no keyboard traps.
- Check web quality basics: valid links for touched navigation, image dimensions or responsive constraints, no layout overflow, no text hidden behind fixed headers, no oversized decorative effects.
- For SEO pages, keep one canonical URL, one descriptive `title`, one meta description, Open Graph/Twitter metadata when already present, and internal links that match existing site structure.

## Verification

- For small text or metadata edits, inspect the changed HTML/CSS and run a quick search for broken duplicated snippets.
- For layout or visual edits, serve the site locally with the simplest static server available and inspect at mobile and desktop widths.
- If touching SEO generation files or automation, run the existing documented command from `SEO_AUTOMATION.md` when available.
