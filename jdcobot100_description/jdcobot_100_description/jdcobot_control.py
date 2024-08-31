import rclpy
from rclpy.node import Node
from sensor_msgs.msg import JointState
import serial 

class JointStateSubscriber(Node):
    def __init__(self):
        super().__init__('joint_state_subscriber')
        self.subscriber = self.create_subscription(
            JointState,
            '/joint_states',
            self.joint_state_callback,
            10
        )
        self.pub_count = 0
        self.ser = serial.Serial("/dev/ttyUSB0", baudrate = 115200, parity=serial.PARITY_NONE, 
                               stopbits=serial.STOPBITS_ONE, bytesize=serial.EIGHTBITS, 
                               timeout=0.3)
   

    def joint_state_callback(self, msg):
        # Process the received joint state message
        base = msg.position[0]*(180/3.14)
        shoulder = msg.position[1]*(180/3.14)
        forearm = msg.position[2]*(180/3.14)
        upperarm = msg.position[3]*(180/3.14)
        self.pub_count +=1
        if self.pub_count > 3: 
            #print(msg.position[0], msg.position[1], msg.position[2], msg.position[3])
            cmd = "a"+str(int(base))+"b"+str(int(shoulder))+"c"+str(int(forearm))+"d"+str(int(upperarm))+ "e92f\n"
            print(cmd)
            self.ser.write(cmd.encode())
            self.pub_count = 0

def main(args=None):
    rclpy.init(args=args)

    joint_state_subscriber = JointStateSubscriber()

    rclpy.spin(joint_state_subscriber)

    rclpy.shutdown()

if __name__ == '__main__':
    main()