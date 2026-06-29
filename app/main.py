from app.models.machine import Machine
from app.services.machine_service import MachineService


def main():
    machine = Machine(
        machine_id="g352",
        manufacturer="GROB",
        controller="TNC7",
    )

    service = MachineService()

    print(machine)

    service.update_state(machine, "AUTOMATIC")

    print(machine)


if __name__ == "__main__":
    main()
