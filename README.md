# Lunabotics 2025 at University of Illinois Chicago

How to Launch:
# clone repo
git clone https://github.com/educationmoment/lunabotics-2025-temp.git

cd lunabotics_ros2_ws

# source ros 2 environemnt


source /opt/ros/humble/setup.bash

# build ros2


cd lunabotics_ros2_ws


colcon build 

# source nodes


source install/setup.bash

# launch file!


ros2 launch lunabotics_nodes lunabotics.launch.py


to install web gui dependencies:

cd lunabotics_ros2_ws/src/lunabotics_webgui

# install rosbridge:

sudo apt-get update

sudo apt-get install ros-humble-rosbridge-server

# start her up


ros2 launch rosbridge_server rosbridge_websocket_launch.xml


python3 web_gui.py


http://localhost:5000 <- this will be changed later :3
