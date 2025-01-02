# lunabotics_nodes/vision_data_node.py
import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image  # or CompressedImage, etc.
# from custom_interfaces.msg import ???  # if you have custom outputs

class VisionDataNode(Node):
    def __init__(self):
        super().__init__('vision_data_node')
        
        # Subscriber(s) to camera topics
        self.subscription_cam1 = self.create_subscription(
            Image,
            '/camera1',
            self.camera1_callback,
            10)
        
        self.subscription_cam2 = self.create_subscription(
            Image,
            '/camera2',
            self.camera2_callback,
            10)
        
        # setup a publisher for processed vision data (tbd?)
        # self.publisher_vision_data = self.create_publisher(...)

    def camera1_callback(self, msg: Image):
        # Process camera1 data...
        self.get_logger().info('Camera1 frame received')
        # Possibly publish some processed result
        # self.publisher_vision_data.publish(...)

    def camera2_callback(self, msg: Image):
        
        self.get_logger().info('Camera2 frame received')

def main(args=None):
    rclpy.init(args=args)
    node = VisionDataNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()
