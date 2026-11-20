from setuptools import setup


package_name = 'usb_cam'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages', ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        ('share/' + package_name + '/launch', ['launch/usb_cam.launch.py']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='[Turtlebot_Name]',
    maintainer_email='esg@eecs.berkeley.edu',
    description='Launching USB Camera',
    license='Apache License 2.0',
    entry_points={'console_scripts': []},
)
