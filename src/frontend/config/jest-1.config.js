module.exports = {
  roots: ["<rootDir>/tests"],
  testMatch: ["**/*.(spec|test).[jt]s?(x)"],
  transform: {
    "^.+\\.(js|jsx|ts|tsx)$": "babel-jest",
  },
  moduleDirectories: ["node_modules", "src"],
};
