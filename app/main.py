from app.handlers.console_event_handler import ConsoleEventHandler
from app.models.machine import Machine
from app.services.machine_service import MachineService


def main():
    machine = Machine(
        machine_id="g352",
        manufacturer="GROB",
        controller="TNC7",
    )

    service = MachineService()
    handler = ConsoleEventHandler()

    event = service.update_state(machine, "AUTOMATIC", source="SIMULATOR")

    if event:
        handler.handle_machine_state_changed(event)


if __name__ == "__main__":
    main()
