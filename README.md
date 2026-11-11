# Autonomous Energy Inspection Rover Simulation (energy-robotics-sim)

A Python-based simulation of an Autonomous Mobile Robot (AMR) designed for automated energy facility inspections. This project demonstrates core concepts in differential drive kinematics, real-time IoT sensor telemetry streaming, and modular software design (OOP).

## Features
- **Kinematics Engine (src/robot.py)**: Computes 2D pose updates for a differential drive robot using linear and angular velocity inputs.
- **IoT Telemetry Pipeline (src/telemetry.py)**: Generates ISO 8601 UTC timestamped JSON data packets containing simulated battery degradation, internal temperature monitoring, and proximity sensor readings.
- **Simulation Orchestrator (src/main.py)**: Ties physical movement and telemetry generation into a continuous, real-time inspection loop.

## Quick Start
Run the simulation:
```bash
python3 src/main.py
```

