import rclpy
from rclpy.node import Node
# from custom_interfaces.msg import ScoopCommand # optional

class ScoopControlNode(Node):
    def __init__(self):
        super().__init__('scoop_control_node')

        self.scoop_sub = self.create_subscription(
            # ScoopCommand or std_msgs/Float32
            # e.g. std_msgs.msg.Float32
            # or geometry_msgs/msg/Twist if controlling a motor
            # We'll assume Float32 = speed
            # for example:
            # from std_msgs.msg import Float32
            # Float32,
            # '/scoop',
            # self.scoop_callback,
            # 10
        )
        # self.status_pub = self.create_publisher(...)

    def scoop_callback(self, msg):
        self.get_logger().info(f'Received scoop cmd: {msg.data}')
        # self.send_to_motor_controller(msg.data)
        # publish heartbeat system again
    def send_to_motor_controller(self, speed):
        # tbd
        pass

def main(args=None):
    rclpy.init(args=args)
    node = ScoopControlNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()
