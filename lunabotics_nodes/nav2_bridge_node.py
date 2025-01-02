import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist

class Nav2BridgeNode(Node):
    def __init__(self):
        super().__init__('nav2_bridge_node')

        self.subscription_cmd_vel = self.create_subscription(
            Twist,
            '/cmd_vel',
            self.cmd_vel_callback,
            10)
        
        self.brain_cmd_vel_pub = self.create_publisher(
            Twist,
            '/cmd_vel_nav2_brain',
            10)

    def cmd_vel_callback(self, twist_msg: Twist):
        # Possibly do some extra logic
        self.brain_cmd_vel_pub.publish(twist_msg)

def main(args=None):
    rclpy.init(args=args)
    node = Nav2BridgeNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()
