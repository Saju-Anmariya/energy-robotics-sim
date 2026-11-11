import time
from robot import EnergyInspectionRobot
from telemetry import TelemetryLogger

def run_inspection_simulation():
    print("=== E.ON Autonomous Energy Inspection Rover Simulation ===")
    
    # Initialize robot and telemetry modules
    rover = EnergyInspectionRobot(x=0.0, y=0.0, theta=0.0)
    logger = TelemetryLogger(robot_id="ROVER-EON-01")
    
    # Simulate an inspection run over 5 time steps
    simulation_steps = 5
    dt = 1.0  # 1 second per step
    
    print(f"Starting inspection route with {simulation_steps} waypoints...\n")
    
    for step in range(1, simulation_steps + 1):
        # Drive forward with a slight curve (linear velocity = 1.2 m/s, angular velocity = 0.05 rad/s)
        pose = rover.update_pose(linear_velocity=1.2, angular_velocity=0.05, dt=dt)
        
        # Generate telemetry packet for the current pose
        telemetry_packet = logger.generate_telemetry_packet(
            x=pose["x"], 
            y=pose["y"], 
            theta=pose["theta"]
        )
        
        print(f"--- Telemetry Stream [Step {step}/{simulation_steps}] ---")
        print(telemetry_packet)
        print("-" * 40)
        
        # Brief pause to simulate real-time sensor polling
        time.sleep(0.5)

    print("Simulation complete! All inspection logs successfully processed.")

if __name__ == "__main__":
    run_inspection_simulation()
