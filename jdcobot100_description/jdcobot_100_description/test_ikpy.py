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