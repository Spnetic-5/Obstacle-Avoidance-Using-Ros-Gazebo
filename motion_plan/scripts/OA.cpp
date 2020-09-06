#include "ros/ros.h"
#include "std_msgs/String.h"
#include "sensor_msgs/LaserScan.h"
#include "geometry_msgs/Twist.h"
#include <iostream>
using namespace std; 

float sensors;
float sensor_angle;


void callback_laser(const sensor_msgs::LaserScan laser)
{
 
	sensors = laser.ranges[0];
	
	for(int j=0;j<=10;j++){
             if(laser.ranges[j]<sensors)
			{
				sensors = laser.ranges[j];
				sensor_angle = j/2;
			}
           }

}

void motion(sensors, sensor_angle)
{
	
        
	if(sensors <= 1.0)  // min_range<=0.5 gave box pushing like behaviour, min_range<=1.2 gave obstacle avoidance
	{
		if(sensor_angle <= 1)
		{
			 cmdvel.angular.z=1.0;
			 cmdvel.linear.x=0;
			 cout<<"OBSTACLE AT RIGHT\n";
		}
        else if(sensor_angle > 1 && sensor_angle <= 2.5)
		{
			 cmdvel.angular.z=0.3;
			 cmdvel.linear.x=0;
			 cout<<("OBSTACLE AT FRONT\n");
		}
		else if
		{
			 cmdvel.angular.z=-0.3;
			 cmdvel.linear.x=0;
			 cout<<("OBSTACLE AT LEFT\n");
		}
	
	    else
	    {
			cmdvel.linear.x=0.6;
			cmdvel.angular.z=0;
			cout<<("NO OBSTACLE\n");
		}
	 
	}

}
int main(int argc, char **argv)
{
    // Initialising a Node 
    ros::init(argc, argv, "Laser_readings");

    // NodeHandle is the main access point to communications with the ROS system 
    ros::NodeHandle nh;

    // advertise() function tells ROS to publish on a given topic name 
    ros::Publisher pub = nh.advertise<geometry_msgs::Twist>("/cmd_vel", 1);

	// The subscribe() tells ROS  to receive messages on a given topic.  
    ros::Subscriber sub = nh.subscribe("/dd_urdf/laser_scan", 1, callback_laser);

	// cmdvel parameters
	 while (ros::ok()) {
	geometry_msgs::Twist cmdvel;
  	cmdvel.linear.x=0;
  	cmdvel.linear.y=0;
  	cmdvel.linear.z=0;
  	cmdvel.angular.x=0;
  	cmdvel.angular.y=0;
  	cmdvel.angular.z=0; 
	pub.publish(cmdvel);
	 }
    

    // ros::spin() will enter a loop, pumping callbacks 
    ros::spin();
    
return 0;

}

