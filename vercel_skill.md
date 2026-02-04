# Vercel Skill

Use the `vercel` CLI to interact with Vercel platform for deployments and project management.

## Installation

```bash
npm install -g vercel
# or use npx to run without installing globally
npx vercel --version
```

## Authentication

```bash
vercel login
```

## Common Commands

Deploy a project:
```bash
vercel                    # Deploy current directory
vercel --prod             # Deploy to production
vercel --env NODE_ENV=production  # Set environment variables
```

Link to an existing project:
```bash
vercel link               # Link current directory to existing Vercel project
```

Project management:
```bash
vercel ls                 # List projects
vercel env ls             # List environment variables
vercel env add            # Add environment variable
vercel domains            # Manage domains
```

Logs and monitoring:
```bash
vercel logs example.vercel.app  # View deployment logs
```

Aliases:
```bash
vercel alias              # Manage domain aliases
```