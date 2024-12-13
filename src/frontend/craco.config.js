const path = require("path");

module.exports = {
  webpack: {
    alias: {
      src: path.resolve(__dirname, "src"),
    },
    configure: (webpackConfig) => {
      // Personnalisation supplémentaire si nécessaire
      webpackConfig.module.rules.push({
        test: /\.svg$/,
        use: ["@svgr/webpack"],
      });
      return webpackConfig;
    },
  },
  devServer: {
    port: 3001, // Changer le port si nécessaire
  },
};
