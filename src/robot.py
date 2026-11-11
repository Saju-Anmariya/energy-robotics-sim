import math

class EnergyInspectionRobot:
    def __init__(self, x: float = 0.0, y: float = 0.0, theta: float = 0.0):
        """
        Initializes the inspection robot position and orientation.
        :param x: Initial X coordinate (meters)
        :param y: Initial Y coordinate (meters)
        :param theta: Initial heading angle (radians)
        """
        self.x = x
        self.y = y
        self.theta = theta

    def update_pose(self, linear_velocity: float, angular_velocity: float, dt: float):
        """
        Updates the robot's position (x, y, theta) using differential drive kinematics over time step dt.
        """
        # Update orientation
        self.theta += angular_velocity * dt
        
        # Normalize theta between -pi and pi
        self.theta = math.atan2(math.sin(self.theta), math.cos(self.theta))

        # Update position based on heading
        self.x += linear_velocity * math.cos(self.theta) * dt
        self.y += linear_velocity * math.sin(self.theta) * dt

        return {"x": round(self.x, 3), "y": round(self.y, 3), "theta": round(self.theta, 3)}

# Quick local test if run directly
if __name__ == "__main__":
    robot = EnergyInspectionRobot()
    print("Initial Pose:", (robot.x, robot.y, robot.theta))
    
    # Simulate moving forward with a slight turn for 1 second (dt = 1.0)
    new_pose = robot.update_pose(linear_velocity=1.5, angular_velocity=0.1, dt=1.0)
    print("Updated Pose after 1s:", new_pose)