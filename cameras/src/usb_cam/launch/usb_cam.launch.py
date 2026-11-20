from launch import LaunchDescription
from launch_ros.actions import Node, PushRosNamespace


def generate_launch_description():
    return LaunchDescription([
        PushRosNamespace('NAME_OF_T3'),
        Node(
            package='v4l2_camera',
            executable='v4l2_camera_node',
            name='usb_camera',
            parameters=[{'video_device': '/dev/video0'}],
            output='screen',
        ),
    ])
