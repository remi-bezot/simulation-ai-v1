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
  collectCoverage: true,
  collectCoverageFrom: [
    "src/**/*.{js,jsx,ts,tsx}",
    "!src/index.tsx",
    "!src/**/*.d.ts",
  ],
  coverageReporters: ["text", "lcov", "json", "html"],
  moduleNameMapper: {
    "\\.(css|scss)$": "identity-obj-proxy",
  },
  watchPlugins: [
    "jest-watch-typeahead/filename",
    "jest-watch-typeahead/testname",
  ],
};
