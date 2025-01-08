import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Joy
from geometry_msgs.msg import Twist
# from std_msgs.msg import Bool, etc. if needed 

class BrainNode(Node):
    def __init__(self):
        super().__init__('brain_node')
        
        self.auto_mode = True  # optional to be false (start manually)

        self.joy_sub = self.create_subscription(
            Joy,
            '/joy',
            self.joy_callback,
            10)
        
        self.nav_cmd_vel_sub = self.create_subscription(
            Twist,
            '/cmd_vel',  # or '/cmd_vel_nav2_brain' if bridging
            self.nav_cmd_vel_callback,
            10)
        
        # push to drivtrain node
        self.drivetrain_pub = self.create_publisher(
            Twist,
            '/drivetrain',
            10)
        
        # publish to /scoop for scoop_control node, again tbd
        # self.scoop_pub = self.create_publisher(...)

    def joy_callback(self, msg: Joy):
        if len(msg.buttons) > 0 and msg.buttons[0] == 1:
            self.auto_mode = not self.auto_mode
            self.get_logger().info(f'Switched auto_mode to {self.auto_mode}')
        
        if not self.auto_mode:
            manual_twist = Twist()
            # switch joystick mapping later, tbd
            manual_twist.linear.x = msg.axes[1]
            manual_twist.angular.z = msg.axes[0]
            self.drivetrain_pub.publish(manual_twist)
            self.get_logger().info('herrow drive train :3')

    def nav_cmd_vel_callback(self, twist_msg: Twist):
        # If in auto mode, pass it through:
        if self.auto_mode:
            self.drivetrain_pub.publish(twist_msg)

def main(args=None):
    rclpy.init(args=args)
    node = BrainNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()
