import React from "react";
import { render, screen } from "@testing-library/react";
import Header from "../../../src/frontend/components/shared/header";
test("renders header component", () => {
  render(<Header />);
  const linkElement = screen.getByText(/Simulation AI v3/i);
  expect(linkElement).toBeInTheDocument();
});
