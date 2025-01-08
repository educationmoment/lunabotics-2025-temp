from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(package='control_pkg', executable='test_control', output='screen'),
        Node(package='control_pkg', executable='drivetrain', output='screen'),
        # etc.
    ])
    
    
    ##To-Do: Update
