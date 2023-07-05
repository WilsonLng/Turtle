#!/usr/bin/env/ python3
import rclpy
from rclpy.node import Node

from example_interfaces.msg import Int64


class NumberCounter(Node):
    def __init__(self):
        super().__init__("number_counter")

        # Subscriber
        self.subscriber_ = self.create_subscription(
            Int64, "number", self.callback_number, 1)

        # Publisher
        self.counter_ = 0
        self.publisher_ = self.create_publisher(Int64, "number_count", 2)
        self.timer_ = self.create_timer(0.5, self.publish_counter)

        self.get_logger().info("number_counter has started")

    def callback_number(self, msg):
        self.counter_ += msg.data
        self.get_logger().info(str(msg.data))

    def publish_counter(self):
        msg = Int64()
        msg.data = self.counter_
        self.counter_ += 2
        self.publisher_.publish(msg)

def main(args=None):
    rclpy.init(args=args)
    node = NumberCounter()
    rclpy.spin(node)
    rclpy.shutdown()


if __name__ == "__main__":
    main()
