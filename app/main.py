from app.models.machine_state import MachineState


def main():
    machine_state = MachineState.create(
        machine_id="g352",
        state="AUTOMATIC",
        source="SIMULATOR",
    )

    print(machine_state.to_dict())


if __name__ == "__main__":
    main()
