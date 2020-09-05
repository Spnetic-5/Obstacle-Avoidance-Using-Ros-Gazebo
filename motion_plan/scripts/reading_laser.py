#! /usr/bin/env python

import rospy
from sensor_msgs.msg import LaserScan

def callback_laser(msg):
    # 10/5 = 2
	regions = [ 
      min(msg.ranges[0:1], 10),
      min(msg.ranges[2:3], 10),
      min(msg.ranges[4:5], 10),
      min(msg.ranges[6:7], 10),
      min(msg.ranges[8:9], 10),
     ]
	rospy.loginfo(regions)

def main():
    rospy.init_node('Laser_readings')
    sub= rospy.Subscriber("/dd_urdf/laser_scan", LaserScan, callback_laser)

    rospy.spin()

if __name__ == '__main__':
    main()
