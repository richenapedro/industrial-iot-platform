import time
from app.simulator import MachineSimulator


def main():
    simulator = MachineSimulator(machine_id="g352")

    while True:
        machine_state = simulator.get_current_state()
        print(machine_state.to_dict())
        time.sleep(2)


if __name__ == "__main__":
    main()
