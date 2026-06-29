from app.models.machine import Machine


def main():
    machine = Machine(
        machine_id="g352",
        manufacturer="GROB",
        controller="TNC7",
    )

    print(machine)


if __name__ == "__main__":
    main()
