from app.models.machine import Machine
from app.services.machine_service import MachineService


def main():
    machine = Machine(
        machine_id="g352",
        manufacturer="GROB",
        controller="TNC7",
    )

    service = MachineService()

    event = service.update_state(machine, "AUTOMATIC", source="SIMULATOR")
    if event:
        print(event.to_dict())
    else:
        print("No state change detected")

    event = service.update_state(machine, "AUTOMATIC", source="SIMULATOR")
    if event:
        print(event.to_dict())
    else:
        print("No state change detected")

    event = service.update_state(machine, "ALARM", source="SIMULATOR")
    if event:
        print(event.to_dict())
    else:
        print("No state change detected")


if __name__ == "__main__":
    main()
