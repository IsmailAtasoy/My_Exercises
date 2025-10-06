import rclpy
from rclpy.node import Node
from example_interfaces.msg import Float64


class node_3(Node):

    def __init__(self):
        super().__init__("node_3")
        self.number_sub_ = self.create_subscription(Float64, "data_2", self.number_callback, 10)

    def number_callback(self, msg: Float64):
         self.get_logger().info("Received: " + str(msg.data))


def main(args=None):
    rclpy.init(args=args)
    node = node_3()
    rclpy.spin(node)
    rclpy.shutdown()

    