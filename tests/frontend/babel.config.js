module.exports = {
  presets: [
    [
      "@babel/preset-env",
      {
        targets: {
          browsers: [">0.2%", "not dead", "not op_mini all"],
        },
        useBuiltIns: "usage",
        corejs: "3.30",
      },
    ],
    [
      "@babel/preset-react",
      {
        runtime: "automatic", // Automatisation du JSX pour React 17+
      },
    ],
    "@babel/preset-typescript",
  ],
  plugins: [
    "@babel/plugin-proposal-class-properties",
    "@babel/plugin-transform-runtime",
  ],
};
