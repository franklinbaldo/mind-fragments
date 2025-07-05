# Mind Fragments 📄

![Typescript](https://img.shields.io/badge/TypeScript-007ACC?style=for-the-badge&logo=typescript&logoColor=white)
![GitHub](https://img.shields.io/github/license/satnaing/astro-paper?color=%232F3741&style=for-the-badge)
[![Conventional Commits](https://img.shields.io/badge/Conventional%20Commits-1.0.0-%23FE5196?logo=conventionalcommits&logoColor=white&style=for-the-badge)](https://conventionalcommits.org)
[![Commitizen friendly](https://img.shields.io/badge/commitizen-friendly-brightgreen.svg?style=for-the-badge)](http://commitizen.github.io/cz-cli/)

Mind Fragments is a minimal, responsive, accessible and SEO-friendly Astro blog theme. This theme is designed and crafted based on [my personal blog](https://satnaing.dev/blog).

This theme follows best practices and provides accessibility out of the box. Light and dark mode are supported by default. Moreover, additional color schemes can also be configured.

This theme is self-documented \_ which means articles/posts in this theme can also be considered as documentations. Read [the blog posts](https://astro-paper.pages.dev/posts/) or check [the README Documentation Section](#-documentation) for more info.

## 🔥 Features

- [x] type-safe markdown
- [x] super fast performance
- [x] accessible (Keyboard/VoiceOver)
- [x] responsive (mobile ~ desktops)
- [x] SEO-friendly
- [x] light & dark mode
- [x] fuzzy search
- [x] draft posts & pagination
- [x] sitemap & rss feed
- [x] followed best practices
- [x] highly customizable
- [x] dynamic OG image generation for blog posts [#15](https://github.com/satnaing/astro-paper/pull/15) ([Blog Post](https://astro-paper.pages.dev/posts/dynamic-og-image-generation-in-astropaper-blog-posts/))

_Note: I've tested screen-reader accessibility of Mind Fragments using **VoiceOver** on Mac and **TalkBack** on Android. I couldn't test all other screen-readers out there. However, accessibility enhancements in Mind Fragments should be working fine on others as well._

## ✅ Lighthouse Score

<p align="center">
  <a href="https://pagespeed.web.dev/report?url=https%3A%2F%2Fastro-paper.pages.dev%2F&form_factor=desktop">
    <!-- Removed broken image link to AstroPaper-lighthouse-score.svg -->
  <a>
</p>

## 🚀 Project Structure

Inside of Mind Fragments, you'll see the following folders and files:

```bash
/
├── public/
│   ├── assets/
│   │   └── logo.svg
│   │   └── logo.png
│   └── favicon.svg
│   └── astropaper-og.jpg
│   └── robots.txt
│   └── toggle-theme.js
├── src/
│   ├── assets/
│   │   └── socialIcons.ts
│   ├── components/
│   ├── content/
│   │   |  blog/
│   │   |    └── some-blog-posts.md
│   │   └── config.ts
│   ├── layouts/
│   └── pages/
│   └── styles/
│   └── utils/
│   └── config.ts
│   └── types.ts
├── .github/
├── .husky/
├── .vscode/
├── docs/
├── puppeteer_scripts/
├── AGENTS.md
├── bootstrap_infra.sh
├── CHANGELOG.md
├── docker-compose.yml
├── LICENSE
├── mkdocs.yml
├── n8n_starter_flow.json
├── package.json
└── requirements.txt
```

Astro looks for `.astro` or `.md` files in the `src/pages/` directory. Each page is exposed as a route based on its file name.

Any static assets, like images, can be placed in the `public/` directory.

All blog posts are stored in `src/content/blog` directory.

## 📖 Documentation

This theme is self-documented, meaning that the articles and posts within this theme also serve as its documentation. You can find more information by reading the [blog posts](https://astro-paper.pages.dev/posts/) or by exploring the `docs/` directory.

Key documentation files include:

- [Adding a New Post](docs/blog/posts/adding-new-post.md)
- [Dynamic OG Images](docs/blog/posts/dynamic-og-images.md)
- [How to Add a New Social Icon](docs/blog/posts/how-to-add-a-new-social-icon.md)
- [How to Update Dependencies](docs/blog/posts/how-to-update-dependencies.md)
- [Portfolio Website Development](docs/blog/posts/portfolio-website-development.md)
- [Predefined Color Schemes](docs/blog/posts/predefined-color-schemes.md)
- [Tailwind Typography](docs/blog/posts/tailwind-typography.md)
- [Terminal Development](docs/blog/posts/terminal-development.md)

> For Mind Fragments v1, check out [this branch](https://github.com/satnaing/astro-paper/tree/astro-paper-v1) and this [live URL](https://astro-paper-v1.astro-paper.pages.dev/)

## 💻 Tech Stack

**Main Framework** - [Astro](https://astro.build/) (v4.x)
**Type Checking** - [TypeScript](https://www.typescriptlang.org/)
**Component Framework** - [ReactJS](https://reactjs.org/) (v18.x)
**Styling** - [TailwindCSS](https://tailwindcss.com/) (v3.x)
**UI/UX** - [Figma](https://figma.com)
**Fuzzy Search** - [FuseJS](https://fusejs.io/)
**Icons** - [Boxicons](https://boxicons.com/) | [Tablers](https://tabler-icons.io/)
**Code Formatting** - [Prettier](https://prettier.io/)
**Deployment** - [Cloudflare Pages](https://pages.cloudflare.com/)
**Illustration in About Page** - [https://freesvgillustration.com](https://freesvgillustration.com/)
**Linting** - [ESLint](https://eslint.org/)
**Package Management** - [npm](https://www.npmjs.com/) / [Yarn](https://yarnpkg.com/) / [pnpm](https://pnpm.io/)
**Containerization** - [Docker](https://www.docker.com/)

## 👨🏻‍💻 Running Locally

The easiest way to run this project locally is to use the `create-astro` CLI. Open your terminal, `cd` into your desired directory, and run one of the following commands:

```bash
# npm 6.x
npm create astro@latest --template satnaing/astro-paper

# npm 7+, extra double-dash is needed:
npm create astro@latest -- --template satnaing/astro-paper

# yarn
yarn create astro --template satnaing/astro-paper

# pnpm
pnpm create astro --template satnaing/astro-paper
```

Alternatively, you can clone the repository and install dependencies manually:

```bash
git clone https://github.com/satnaing/astro-paper.git
cd astro-paper
npm install # or yarn install or pnpm install
npm run dev
```

### Running with Docker

If you prefer to use Docker, you can run the project with the following commands:

```bash
# Build and run the Docker container in detached mode
docker compose up -d --build

# To stop the container
docker compose down
```
The application will be accessible at `http://localhost:4321`.

## Google Site Verification (Optional)

If you wish to verify your site with Google, you can add your [Google Site Verification HTML tag](https://support.google.com/webmasters/answer/9008080#meta_tag_verification&zippy=%2Chtml-tag) to Mind Fragments using an environment variable. This step is entirely optional. If you do not add the following environment variable, the `google-site-verification` tag will not be included in the HTML `<head>` section.

Create a `.env` file in the root of your project (if it doesn't already exist) and add the following line:

```bash
# .env
PUBLIC_GOOGLE_SITE_VERIFICATION=your-google-site-verification-value
```
Replace `your-google-site-verification-value` with the actual content attribute from your Google meta tag.

## 🧞 Commands

All commands are run from the root of the project in a terminal:

> **_Note!_** For `Docker` commands, you must have Docker [installed](https://docs.docker.com/engine/install/) on your machine.

| Command                              | Action                                                                                                                               |
| :----------------------------------- | :----------------------------------------------------------------------------------------------------------------------------------- |
| `npm install`                        | Installs project dependencies.                                                                                                       |
| `npm run dev`                        | Starts the local development server at `http://localhost:4321`.                                                                      |
| `npm run build`                      | Builds your production site into the `./dist/` directory.                                                                            |
| `npm run preview`                    | Starts a local server to preview your production build from `./dist/`.                                                               |
| `npm run format:check`               | Checks code formatting with Prettier without making changes.                                                                         |
| `npm run format`                     | Formats all code with Prettier.                                                                                                      |
| `npm run lint`                       | Lints code with ESLint to find and fix problems.                                                                                     |
| `npm run lint:fix`                   | Lints code with ESLint and automatically fixes fixable issues.                                                                       |
| `npm run cz`                         | Starts the Commitizen CLI for creating conventional commit messages.                                                                 |
| `npm run sync`                       | Generates TypeScript types for all Astro modules. [Learn more](https://docs.astro.build/en/reference/cli-reference/#astro-sync).     |
| `npm run new-post <title>`           | Creates a new blog post markdown file with the given title in `src/content/blog/`. (e.g., `npm run new-post "My Awesome Post"`)    |
| `docker compose up -d --build`       | Builds and starts the Docker containers in detached mode. The application will be available at `http://localhost:4321`.             |
| `docker compose down`                | Stops and removes the Docker containers defined in `docker-compose.yml`.                                                             |
| `docker compose logs -f`             | Follows the logs of the running Docker containers.                                                                                   |
| `docker compose exec app <command>`  | Executes a command inside the running `app` service container (e.g., `docker compose exec app npm install`).                       |

> **_Warning!_** Windows PowerShell users may need to install the [concurrently package](https://www.npmjs.com/package/concurrently) globally (`npm install -g concurrently`) if they encounter issues [running diagnostics](https://docs.astro.build/en/reference/cli-reference/#astro-check) during development (e.g., `astro check --watch & astro dev`). For more information, see [this issue](https://github.com/satnaing/astro-paper/issues/113).

## ✨ Feedback & Suggestions

If you have any suggestions/feedback, you can contact me via [my email](mailto:contact@satnaing.dev). Alternatively, feel free to open an issue if you find bugs or want to request new features.

## 📜 License

Licensed under the MIT License, Copyright © 2023

---

Made with 🤍 by [Sat Naing](https://satnaing.dev) 👨🏻‍💻 and [contributors](https://github.com/satnaing/astro-paper/graphs/contributors).
