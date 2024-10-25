import os
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.actions import Node

def generate_launch_description():
    gazebo_empty_world_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(
                'gazebo_ros', 'share', 'gazebo_ros', 'launch', 'empty_world.launch.py'
            )
        )
    )
    tf_footprint_base = Node(
        package='tf2_ros',
        executable='static_transform_publisher',
        name='tf_footprint_base',
        arguments=['0', '0', '0', '0', '0', '0', 'base_link', 'base_footprint']
    )
    spawn_model = Node(
        package='gazebo_ros',
        executable='spawn_entity.py',
        name='spawn_model',
        output='screen',
        remappings=[
            ('gazebo', 'gazebo_ros'),
            ('model', 'jdcobot_100_description/urdf/jdcobot_100_description.urdf'),  # 상대 경로로 수정
            ('name', 'jdcobot_100_description')
        ]
    )
    fake_joint_calibration = Node(
        package='ros2topic',
        executable='ros2topic',
        name='fake_joint_calibration',
        arguments=['pub', '/calibrated', 'std_msgs/Bool', "{'data': true}"]
    )
    return LaunchDescription([
        gazebo_empty_world_launch,
        tf_footprint_base,
        spawn_model,
        fake_joint_calibration
    ])

if __name__ == '__main__':
    generate_launch_description()
