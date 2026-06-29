# Industrial IoT Platform

Industrial IoT platform for CNC/PLC data acquisition using **OPC UA**, **MQTT**, **Python**, **FastAPI**, **PostgreSQL**, **Grafana** and **Docker**.

---

## Overview

This project simulates a modern Industrial IoT architecture used to collect, process, store and visualize data from CNC machines and PLCs.

The objective is to build a **portfolio-grade Industrial IoT platform**, following software engineering best practices commonly used in industrial environments.

---

## Architecture

```text
CNC / PLC / Industrial Controller
              │
              ▼
        OPC UA Server
              │
              ▼
     Python OPC UA Connector
              │
              ▼
          MQTT Broker
              │
              ▼
      FastAPI Backend Service
              │
              ▼
          PostgreSQL
              │
              ▼
           Grafana
```

---

## Industrial Use Case

The platform is designed to monitor industrial machines and collect information such as:

- Machine State
- Current Program
- Active Tool
- Spindle Speed
- Feed Rate
- Active Alarms
- Part Counter
- Connection Status

---

## Tech Stack

| Layer | Technology |
|-------|------------|
| Machine Communication | OPC UA |
| Messaging | MQTT |
| Backend | Python, FastAPI |
| Database | PostgreSQL |
| Visualization | Grafana |
| Deployment | Docker & Docker Compose |
| CI/CD | GitHub Actions |

---

## Current Status

### ✅ Implemented

- Initial repository structure
- Professional GitHub repository setup
- Basic CI workflow
- Project documentation

### 🚧 Planned

- OPC UA Connector
- MQTT Publisher
- Machine Data Models
- FastAPI REST API
- PostgreSQL Integration
- Grafana Dashboard
- Docker Compose Environment

---

## Development Workflow

This repository follows **Semantic Commit Messages**.

```text
feat: new feature
fix: bug fix
docs: documentation
refactor: code improvements
test: tests
chore: maintenance
```

---

## Getting Started

Clone the repository

```bash
git clone https://github.com/richenapedro/industrial-iot-platform.git
cd industrial-iot-platform
```

Create a virtual environment

```bash
python -m venv .venv
```

Activate (PowerShell)

```powershell
.\.venv\Scripts\Activate.ps1
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the application

```bash
python -m app.main
```

---

## Roadmap

```text
PLC / CNC
      │
      ▼
   OPC UA
      │
      ▼
 Python Connector
      │
      ▼
    MQTT
      │
      ▼
  FastAPI API
      │
      ▼
 PostgreSQL
      │
      ▼
   Grafana
      │
      ▼
Docker Compose
      │
      ▼
 Cloud-ready Architecture
```

---

## Author

**Pedro Calefo Richena**

Automation Software Engineer (Industrial Software)

Germany 🇩🇪
