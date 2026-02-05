# Sienna's Personal Website & Blog

A personal website built with Astro, featuring a blog for documenting learning, thoughts, and growth.

## 🎨 Design Philosophy

- **Apple-inspired** - Clean, minimalist design with gray tones
- **Content-focused** - Typography and readability prioritized
- **Simple** - No clutter, just what matters

## 🛠️ Tech Stack

| Technology | Purpose |
|------------|---------|
| **Astro** | Static site generator |
| **Tailwind CSS** | Styling with custom Apple-inspired config |
| **Markdown** | Writing blog posts |
| **TypeScript** | Type safety |
| **Vercel** | Deployment platform |

## 📁 Project Structure

```
sienna-blog-clone/
├── src/
│   ├── content/
│   │   └── blog/              # Blog posts (Markdown)
│   ├── layouts/
│   │   └── Layout.astro       # Main layout
│   ├── pages/
│   │   ├── index.astro        # Home page
│   │   └── blog/
│   │       ├── index.astro    # Blog listing
│   │       └── [slug].astro  # Post template
│   └── styles/
├── public/                    # Static assets (images)
├── astro.config.mjs
├── tailwind.config.mjs
├── package.json
└── vercel.json
```

## 🚀 Quick Start

```bash
npm install
npm run dev      # Development
npm run build    # Production build
npm run preview  # Preview build
```

## 📝 Writing Posts

Create in `src/content/blog/`:

```markdown
---
title: "Your Title"
description: "Brief description"
pubDate: 2026-02-05  # IMPORTANT: use pubDate NOT date
author: "Sienna"
tags: ["Tag1", "Tag2"]
image: "/your-image.png"
---

Your content...
```

## 🖼️ Adding Images

1. Put images in `public/` directory
2. Reference with absolute path: `/image.png`
3. DO NOT use external image hosts

## 🚀 Deployment

### Automatic
Push to GitHub → Vercel auto-deploys

### Manual
```bash
npm run build
npx vercel --prod --yes
```

**URL**: https://sienna-blog-clone.vercel.app

## 🐛 Troubleshooting

| Problem | Solution |
|---------|----------|
| Build fails | Use `pubDate` NOT `date` in frontmatter |
| Post not showing | Put in `src/content/blog/` |
| Images 404 | Use `public/` directory, path `/image.png` |
| Git push fails | Use HTTPS URL: `git remote set-url origin https://...` |

## 📄 License

MIT

**Updated**: 2026-02-05
