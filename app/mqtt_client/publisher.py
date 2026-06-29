import json

import paho.mqtt.client as mqtt

from app.models.machine_state import MachineState


class MqttPublisher:
    def __init__(
        self,
        broker_host: str = "localhost",
        broker_port: int = 1883,
        client_id: str = "industrial-iot-platform",
        base_topic: str = "machines",
    ):
        self.broker_host = broker_host
        self.broker_port = broker_port
        self.client_id = client_id
        self.base_topic = base_topic

        self.client = mqtt.Client(client_id=self.client_id)

    def connect(self) -> None:
        self.client.connect(self.broker_host, self.broker_port)
        self.client.loop_start()

    def disconnect(self) -> None:
        self.client.loop_stop()
        self.client.disconnect()

    def publish_machine_state(self, machine_state: MachineState) -> None:
        topic = f"{self.base_topic}/{machine_state.machine_id}/state"
        payload = json.dumps(machine_state.to_dict())

        self.client.publish(
            topic=topic,
            payload=payload,
            qos=1,
            retain=True,
        )
