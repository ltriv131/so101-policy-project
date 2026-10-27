from lerobot.teleoperators.so_leader import SO101Leader, SO101LeaderConfig
from lerobot.robots.so_follower import SO101Follower, SO101FollowerConfig
import sys
robot_config = SO101FollowerConfig(
    port="/dev/ttyACM1",
    id="my_follower_arm",
)

teleop_config = SO101LeaderConfig(
    port="/dev/ttyACM0",
    id="my_leader_arm",
)

robot = SO101Follower(robot_config)
teleop_device = SO101Leader(teleop_config)
robot.connect()
teleop_device.connect()

while True:
    action = teleop_device.get_action()
    print(action)
    robot.send_action(action)