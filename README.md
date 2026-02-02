# Sienna's Personal Website & Blog

A personal website built with Astro, featuring a blog for documenting learning, thoughts, and growth.

## Design Philosophy

- **Apple-inspired** - Clean, minimalist design with gray tones
- **Content-focused** - Typography and readability prioritized
- **Simple** - No clutter, just what matters

## Tech Stack

- **Astro** - Static site generator
- **Tailwind CSS** - Styling with custom Apple-inspired config
- **Markdown** - Writing content
- **TypeScript** - Type safety

## Project Structure

```
src/
├── content/
│   └── blog/          # Blog posts (Markdown)
├── layouts/
│   └── Layout.astro   # Main layout component
├── pages/
│   ├── index.astro    # Home page
│   └── blog/
│       ├── index.astro    # Blog listing
│       └── [slug].astro   # Blog post template
├── styles/
│   └── global.css     # Global styles
└── content.config.ts  # Content collections config
```

## Getting Started

```bash
# Install dependencies
npm install

# Start development server
npm run dev

# Build for production
npm run build

# Preview production build
npm run preview
```

## Writing Blog Posts

Create new Markdown files in `src/content/blog/`:

```markdown
---
title: "Your Post Title"
description: "Brief description for SEO and previews"
pubDate: 2026-02-02
tags: ["Tag1", "Tag2"]
---

Your content here...
```

## Deployment

Automatically deploys to Vercel on push to main branch.

## License

MIT - Feel free to use as a template.
