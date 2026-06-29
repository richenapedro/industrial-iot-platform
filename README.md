# Industrial IoT Platform

Industrial IoT learning project focused on CNC/PLC data acquisition, OPC UA, MQTT, Python backend, PostgreSQL, Grafana and Docker.

## Architecture

```text
CNC / PLC
↓
OPC UA Server
↓
Python OPC UA Connector
↓
MQTT Broker
↓
Backend / Database
↓
Grafana / REST API
