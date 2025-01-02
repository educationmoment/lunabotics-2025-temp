from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(package='lunabotics_nodes', executable='vision_data_node', output='screen'),
        Node(package='lunabotics_nodes', executable='brain_node', output='screen'),
        Node(package='lunabotics_nodes', executable='drivetrain_control_node', output='screen'),
        Node(package='lunabotics_nodes', executable='scoop_control_node', output='screen'),
        Node(package='lunabotics_nodes', executable='status_tracking_node', output='screen'),
        # etc.
    ])
