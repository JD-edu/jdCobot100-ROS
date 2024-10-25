<<<<<<< HEAD
=======
'''
/*MIT License

Copyright (c) 2024 JD edu. http://jdedu.kr author: conner.jeong@gmail.com
     
Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:
     
The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.
     
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN TH
SOFTWARE.*/
'''
>>>>>>> 8b854a925ac64fde88564efda5b755bd5a590752
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
<<<<<<< HEAD
            joint_state.position = [ 1.5708, 1.5708, 1.5708, 1.5708, 0.0 ]
            self.joint_angle = 1
        else:
            joint_state.position = [ 0.0, 0.0, 3.1416, 0.0, 0.03]
=======
            joint_state.position = [ 0.0, 0.0, 0.0, 0.0, 0.0 ]
            self.joint_angle = 1
        else:
            joint_state.position = [ 1.8, -0.8, 0.4, -1.4, -2.4 ]
>>>>>>> 8b854a925ac64fde88564efda5b755bd5a590752
            self.joint_angle = 0

        self.publisher_.publish(joint_state)
        self.get_logger().info(f"joint state: {joint_state.position}")

def main(args=None):
    rclpy.init(args=args)
    joint_state_publisher = joint_state_publisher_test()
    rclpy.spin(joint_state_publisher)

if __name__ == '__main__':
    main()

