import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
# from custom_interfaces.msg import DriveCommand  # for custom message logging, optional

class DrivetrainControlNode(Node):
    def __init__(self):
        super().__init__('drivetrain_control_node')

        # brain's commands
        self.subscription = self.create_subscription(
            Twist,            # twist in plce of custom driving command, tbd(?)
            '/drivetrain',
            self.drivetrain_callback,
            10)

        # success status logger, tbd
        # self.status_pub = self.create_publisher(std_msgs.msg.String, '/drivetrain_status', 10)

    def drivetrain_callback(self, twist_msg: Twist):
        linear_x = twist_msg.linear.x
        angular_z = twist_msg.angular.z
        
        left_speed = linear_x - angular_z
        right_speed = linear_x + angular_z

        # duty cycle vs velocity, tbd
        # self.send_to_sparkmax(left_speed, right_speed)

        self.get_logger().info(f'Drivetrain command: left={left_speed}, right={right_speed}')
        # publish success/ fail tbd
        # self.status_pub.publish(...)

    def send_to_sparkmax(self, left, right):
        # talk over CAN, tbd!
        pass

def main(args=None):
    rclpy.init(args=args)
    node = DrivetrainControlNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()
