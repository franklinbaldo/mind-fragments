# Mind Fragments 📄

![Typescript](https://img.shields.io/badge/TypeScript-007ACC?style=for-the-badge&logo=typescript&logoColor=white)
![GitHub](https://img.shields.io/github/license/satnaing/astro-paper?color=%232F3741&style=for-the-badge)
[![Conventional Commits](https://img.shields.io/badge/Conventional%20Commits-1.0.0-%23FE5196?logo=conventionalcommits&logoColor=white&style=for-the-badge)](https://conventionalcommits.org)
[![Commitizen friendly](https://img.shields.io/badge/commitizen-friendly-brightgreen.svg?style=for-the-badge)](http://commitizen.github.io/cz-cli/)

Mind Fragments is a minimal, responsive, accessible and SEO-friendly Astro blog theme. This theme is designed and crafted based on [my personal blog](https://satnaing.dev/blog).

This theme follows best practices and provides accessibility out of the box. Light and dark mode are supported by default. Moreover, additional color schemes can also be configured.

This theme is self-documented \_ which means articles/posts in this theme can also be considered as documentations. Read [the blog posts](https://astro-paper.pages.dev/posts/) or check [the README Documentation Section](#-documentation) for more info.

## 🔥 Features

- [x] Markdown-based content
- [x] Responsive design (mobile ~ desktops)
- [x] SEO-friendly
- [x] Light & dark mode (via MkDocs Material theme)
- [x] Categories
- [x] RSS feed generation
- [x] Search functionality
- [x] Highly customizable (via MkDocs configuration)

## ✅ Lighthouse Score

(Lighthouse score will depend on your deployment and content, but MkDocs Material is generally performant.)

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

To run this project locally, you'll need Python and `pip` installed. Then, install the required Python packages:

```bash
pip install -r requirements.txt
```

Once dependencies are installed, you can serve the site:

```bash
mkdocs serve
```

The application will be accessible at `http://localhost:8000`.

### Running with Docker

If you prefer to use Docker, you can run the project with the following commands:

```bash
# Build and run the Docker container in detached mode
docker compose up -d --build

# To stop the container
docker compose down
```

## 🧞 Commands

All commands are run from the root of the project in a terminal:

> **_Note!_** For `Docker` commands, you must have Docker [installed](https://docs.docker.com/engine/install/) on your machine.

| Command                              | Action                                                                                                                               |
| :----------------------------------- | :----------------------------------------------------------------------------------------------------------------------------------- |
| `pip install -r requirements.txt`    | Installs project dependencies.                                                                                                       |
| `mkdocs serve`                       | Starts the local development server at `http://localhost:8000`.                                                                      |
| `mkdocs build`                       | Builds your production site into the `./site/` directory.                                                                            |
| `mkdocs gh-deploy`                   | Deploys your site to GitHub Pages.                                                                                                   |
| `docker compose up -d --build`       | Builds and starts the Docker containers in detached mode.                                                                            |
| `docker compose down`                | Stops and removes the Docker containers defined in `docker-compose.yml`.                                                             |
| `docker compose logs -f`             | Follows the logs of the running Docker containers.                                                                                   |
| `docker compose exec app <command>`  | Executes a command inside the running `app` service container (e.g., `docker compose exec app pip install`).                       |

## ✨ Feedback & Suggestions

If you have any suggestions/feedback, you can contact me via [my email](mailto:contact@satnaing.dev). Alternatively, feel free to open an issue if you find bugs or want to request new features.

## 📜 License

Licensed under the MIT License, Copyright © 2023

---

Made with 🤍 by [Sat Naing](https://satnaing.dev) 👨🏻‍💻 and [contributors](https://github.com/satnaing/astro-paper/graphs/contributors).
