import json
import random
from datetime import datetime

class TelemetryLogger:
    def __init__(self, robot_id: str = "ROVER-EON-01"):
        self.robot_id = robot_id
        self.battery_level = 100.0  
        self.internal_temp = 25.0   

    def generate_telemetry_packet(self, x: float, y: float, theta: float) -> str:
        self.battery_level = max(0.0, self.battery_level - random.uniform(0.05, 0.2))
        self.internal_temp += random.uniform(-0.1, 0.2)
        obstacle_distance = round(random.uniform(1.5, 10.0), 2)

        telemetry_data = {
            "timestamp": datetime.utcnow().isoformat() + "Z",
            "robot_id": self.robot_id,
            "pose": {"x": x, "y": y, "heading": theta},
            "sensors": {
                "battery_percent": round(self.battery_level, 2),
                "internal_temp_c": round(self.internal_temp, 2),
                "obstacle_distance_m": obstacle_distance
            },
            "status": "NORMAL" if self.battery_level > 20.0 else "LOW_BATTERY"
        }
        return json.dumps(telemetry_data, indent=4)

if __name__ == "__main__":
    logger = TelemetryLogger()
    packet = logger.generate_telemetry_packet(x=1.493, y=0.15, theta=0.1)
    print("Generated IoT Telemetry Packet:")
    print(packet)