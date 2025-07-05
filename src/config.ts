import type { Site, SocialObjects } from "./types";

export const SITE: Site = {
  website: "https://franklinbaldo.github.io/mind-fragments", // replace this with your deployed domain
  author: "Franklin Baldo",
  desc: "A digital chronicle of Franklin Baldo's thoughts, projects, and intellectual journey. An experiment in autobiographical AI.",
  title: "The Chronicle of Franklin Baldo",
  ogImage: "default-og.jpg", // Consider creating a custom one for Franklin
  lightAndDarkMode: true,
  postPerPage: 10, // Adjusted for potentially more frequent, shorter posts
  scheduledPostMargin: 15 * 60 * 1000, // 15 minutes
};

export const LOCALE = {
  lang: "en", // html lang code. Set this empty and default will be "en"
  langTag: ["en-EN"], // BCP 47 Language Tags. Set this empty [] to use the environment default
} as const;

export const LOGO_IMAGE = {
  enable: false, // Can be enabled if Franklin has a logo
  svg: true,
  width: 216,
  height: 46,
};

export const SOCIALS: SocialObjects = [
  {
    name: "Github",
    href: "https://github.com/franklinbaldo",
    linkTitle: `Franklin Baldo on Github`,
    active: true,
  },
  {
    name: "Twitter", // As mentioned in pivot.md (X/Twitter)
    href: "https://twitter.com/franklinbaldo", // Placeholder, Franklin to update if different
    linkTitle: `Franklin Baldo on Twitter`,
    active: true,
  },
  {
    name: "Mail",
    href: "mailto:franklin@franklinbaldo.com", // Placeholder, Franklin to update
    linkTitle: `Send an email to Franklin Baldo`,
    active: true, // Assuming contact is desired
  },
  // { // Example for Manifold Markets if a direct profile link exists and is desired
  //   name: "ManifoldMarkets",
  //   href: "https://manifold.markets/FranklinBaldo", // Placeholder
  //   linkTitle: `Franklin Baldo on Manifold Markets`,
  //   active: true,
  // },
  // Removing other default social links unless Franklin specifies them
];
