import React from "react";
import { render, screen } from "@testing-library/react";
import SimulationControls from "../../../src/frontend/components/simulation/simulation_controls";

test("renders simulation controls", () => {
  render(<SimulationControls />);
  const buttonElement = screen.getByRole("button", {
    name: /Start Simulation/i,
  });
  expect(buttonElement).toBeInTheDocument();
});
