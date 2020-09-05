# Obstacle-Avoidance-Using-Ros-Gazebo
_Obstacle avoiding Differential drive bot using ROS and Gazebo.  The robot design and other requirements can be found in this [PDF](https://github.com/Git-Saurabh5/Obstacle-Avoidance-Using-Ros-Gazebo/blob/master/ProblemStatement.pdf)._ 
Reference taken for this project was [this](https://www.theconstructsim.com/ros-projects-exploring-ros-using-2-wheeled-robot-part-1).

## Prerequisites  

* [ROS](http://wiki.ros.org/kinetic)  
* [Gazebo](http://wiki.ros.org/gazebo_ros_pkgs)

## Getting Started
1. Clone this respository.
2. Launch your terminal and run the command `roslaunch my_worlds <world_name>.launch`. 
   This will launch the gazebo enviroment.
3. In another terminal, run the command `roslaunch my_robot_urdf robot.launch`. 
This will load the dd robot in the gazebo environment at origin.  
4. In another terminal run `rosrun motion_plan OA.py`. This will start the robot and obstacle avoidance algorithm.




## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details
