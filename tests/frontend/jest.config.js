module.exports = {
  roots: [
    "<rootDir>/tests/frontend/unit",
    "<rootDir>/tests/frontend/integration",
  ],
  testMatch: ["**/?(*.)+(spec|test).[jt]s?(x)"],
  transform: {
    "^.+\\.(js|jsx|ts|tsx)$": "babel-jest",
  },
  verbose: true,
  testEnvironment: "jsdom",
  setupFilesAfterEnv: ["<rootDir>/tests/frontend/setupTests.ts"],
};
