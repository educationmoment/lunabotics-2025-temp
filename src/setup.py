from setuptools import setup
import os
from glob import glob

package_name = 'lunabotics_nodes'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
         ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        # (os.path.join('share', package_name, 'launch'), glob('launch/*.launch.py')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer="Fat Loser",  
    maintainer_email='example@example.com',
    description='Lunabotics nodes',
    license='Apache License 2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            # e.g. 'vision_data_node = lunabotics_nodes.vision_data_node:main',
        ],
    },
)
