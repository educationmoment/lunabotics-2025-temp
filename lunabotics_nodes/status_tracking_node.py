import rclpy
from rclpy.node import Node
# from std_msgs.msg import String # optinal

class StatusTrackingNode(Node):
    def __init__(self):
        super().__init__('status_tracking_node')
        
        #  subscribe to /drivetrain_status and /scoop_status
        # self.drivetrain_status_sub = self.create_subscription(String, '/drivetrain_status', self.drivetrain_status_cb, 10)
        # self.scoop_status_sub = self.create_subscription(String, '/scoop_status', self.scoop_status_cb, 10)

        # single “system_status” publisher
        # self.system_status_pub = self.create_publisher(String, '/system_status', 10)

    def drivetrain_status_cb(self, msg):
        # log status
        pass

    def scoop_status_cb(self, msg):
        pass

def main(args=None):
    rclpy.init(args=args)
    node = StatusTrackingNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()
