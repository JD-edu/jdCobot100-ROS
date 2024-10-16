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


import time
import numpy as np
import matplotlib.pyplot as plt
from ikpy.chain import Chain
from ikpy.utils import plot
from scipy.spatial.transform import Rotation as R
import os
from ament_index_python.packages import get_package_share_directory

urdf_file = os.path.join(get_package_share_directory('jdcobot_100_description'),'urdf','jdcobot_100_description.urdf')

def ikpy_test(urdf_file_path=None, position=None, angles_degrees=None, return_val='deg', graph_print=False, info_print=True):
    arm_chain = Chain.from_urdf_file(urdf_file_path)
    
    target_position = position
    euler_angles_degrees = angles_degrees

    euler_angles_radians = np.radians(euler_angles_degrees)

    rotation_matrix = R.from_euler('xyz', euler_angles_radians).as_matrix()
    target_orientation = rotation_matrix

    ik = arm_chain.inverse_kinematics(
        target_position=target_position,
        target_orientation=target_orientation,
        orientation_mode="all")

    ik_deg = np.degrees(ik).tolist()
    ik_rad = ik

    if return_val == 'deg':
        return ik_deg[1:]
    elif return_val == 'rad':
        return ik_rad[1:]
    
    if info_print == True:
        print("IK (Degrees):")
        print(ik_deg)

    if graph_print == True:
        fig, ax = plot.init_3d_figure()
        arm_chain.plot(ik, ax)
        ax.legend()
        plt.show()

target_1 = [0.2, 0.3, 0.2]
ang_1 = [0,90,0]

print(ikpy_test(urdf_file,target_1,ang_1,return_val='rad'))