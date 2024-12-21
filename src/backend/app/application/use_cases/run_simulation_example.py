from run_simulation import SimulationInterface, SimulationRunner


class DummySimulation(SimulationInterface):
    def execute(self):
        print("Simulation exécutée.")


if __name__ == "__main__":
    simulation = DummySimulation()
    runner = SimulationRunner(simulation)
    runner.run()
