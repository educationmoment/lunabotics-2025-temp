from setuptools import setup

package_name = 'lunabotics_nodes'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Aakash Bajaj',
    maintainer_email='abaja5@uic.edu',
    description='Lunabotics nodes for controlling the robot',
    license='Apache License 2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'vision_data_node = lunabotics_nodes.vision_data_node:main',
            'brain_node = lunabotics_nodes.brain_node:main',
            'drivetrain_control_node = lunabotics_nodes.drivetrain_control_node:main',
            'scoop_control_node = lunabotics_nodes.scoop_control_node:main',
            'status_tracking_node = lunabotics_nodes.status_tracking_node:main',
            'web_gui_node = lunabotics_nodes.web_gui_node:main',
            # etc.
        ],
    },
)
