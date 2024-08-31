import rclpy
from rclpy.node import Node
from sensor_msgs.msg import JointState

class joint_state_publisher_test(Node):
    def __init__(self):
        super().__init__('joint_state_publisher')
        self.publisher_ = self.create_publisher(JointState, 'joint_states', 20)
        self.timer = self.create_timer(5.0, self.publish_joint_state)  # 5초 주기로 발행
        self.joint_angle = 0
        self.get_logger().info("start")

    def publish_joint_state(self):
        joint_state = JointState()
        joint_state.header.stamp = self.get_clock().now().to_msg()
        joint_state.name = ['joint_1', 'joint_2', 'joint_3', 'joint_4','joint_5']

        if self.joint_angle == 0:
            joint_state.position = [ 0.0, 0.0, 0.0, 0.0, 0.0 ]
            self.joint_angle = 1
        else:
            joint_state.position = [ 1.8, -0.8, 0.4, -1.4, -2.4 ]
            self.joint_angle = 0

        self.publisher_.publish(joint_state)
        self.get_logger().info(f"joint state: {joint_state.position}")

def main(args=None):
    rclpy.init(args=args)
    joint_state_publisher = joint_state_publisher_test()
    rclpy.spin(joint_state_publisher)

if __name__ == '__main__':
    main()

