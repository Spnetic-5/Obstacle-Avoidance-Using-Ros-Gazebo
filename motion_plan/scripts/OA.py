#! /usr/bin/env python
import rospy
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist
pub = None

def main():
    global pub
    rospy.init_node('Laser_readings', anonymous=True)
    pub = rospy.Publisher('/cmd_vel', Twist, queue_size=1)
    sub = rospy.Subscriber('/dd_urdf/laser_scan', LaserScan, callback_laser)
    rospy.spin()

def callback_laser(msg):
    # 145 degrees sensor divided into 3 sensors
	sensors = {
      'RIGHT' : min(min(msg.ranges[0:2]), 10),
      'FRONT' : min(min(msg.ranges[3:5]), 10),
      'LEFT' : min(min(msg.ranges[6:9]), 10),
      
    }
	motion(sensors)

def motion(sensors):
    msg = Twist()
    linear_x = 0
    angular_z = 0
    current_state = ''
    # 0 0 0
    if sensors['FRONT'] > 1 and sensors['LEFT'] > 1 and sensors['RIGHT'] > 1 :
        current_state = '--- NO OBSTACLES ---'
        linear_x = 0.6
        angular_z = 0
    # 0 1 0
    elif sensors['FRONT'] < 1 and sensors['LEFT'] > 1 and sensors['RIGHT'] > 1:
        current_state = '--- OBSTACLE AT FRONT ---'
        linear_x = 0
        angular_z = 0.3
    # 0 0 1
    elif sensors['FRONT'] > 1 and sensors['LEFT'] > 1 and sensors['RIGHT'] < 1:
        current_state = '--- OBSTACLE AT RIGHT ---'
        linear_x = 0
        angular_z = 0.3
    # 1 0 0
    elif sensors['FRONT'] > 1 and sensors['LEFT'] < 1 and sensors['RIGHT'] > 1:
        current_state = '--- OBSTACLE AT LEFT ---'
        linear_x = 0
        angular_z = -0.3
    # 0 1 1
    elif sensors['FRONT'] < 1 and sensors['LEFT'] > 1 and sensors['RIGHT'] < 1:
        current_state = '--- OBSTACLE AT FRONT AND RIGHT ---'
        linear_x = 0
        angular_z = 0.3
    # 1 1 0
    elif sensors['FRONT'] < 1 and sensors['LEFT'] < 1 and sensors['RIGHT'] > 1:
        current_state = '--- OBSTACLE AT FRONT AND LEFT ---'
        linear_x = 0
        angular_z = -0.3
    # 1 1 1
    elif sensors['FRONT'] < 1 and sensors['LEFT'] < 1 and sensors['RIGHT'] < 1:
        current_state = '--- OBSTACLE AT FRONT, LEFT AND RIGHT ---'
        linear_x = 0
        angular_z = 0.3
    # 1 0 1
    elif sensors['FRONT'] > 1 and sensors['LEFT'] < 1 and sensors['RIGHT'] < 1:
        current_state = '--- OBSTACLE AT LEFT AND RIGHT ---'
        linear_x = 0.3
        angular_z = 0
    else:
        current_state = 'UNKNOWN CASE'
        rospy.loginfo(sensors)
    
    rospy.loginfo(current_state)
    msg.linear.x = linear_x
    msg.angular.z = angular_z
    pub.publish(msg)

if __name__ == '__main__':
    main()


#! /usr/bin/env python
import rospy
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist
pub = None

def main():
    global pub
    rospy.init_node('Laser_readings', anonymous=True)
    pub = rospy.Publisher('/cmd_vel', Twist, queue_size=1)
    sub = rospy.Subscriber('/dd_urdf/laser_scan', LaserScan, callback_laser)
    rospy.spin()

def callback_laser(msg):
    # 145 degrees sensor divided into 3 sensors
	sensors = {
      'RIGHT' : min(min(msg.ranges[0:2]), 10),
      'FRONT' : min(min(msg.ranges[3:5]), 10),
      'LEFT' : min(min(msg.ranges[6:9]), 10),
      
    }
	motion(sensors)

def motion(sensors):
    msg = Twist()
    linear_x = 0
    angular_z = 0
    current_state = ''
    # 0 0 0
    if sensors['FRONT'] > 1 and sensors['LEFT'] > 1 and sensors['RIGHT'] > 1 :
        current_state = '--- NO OBSTACLES ---'
        linear_x = 0.6
        angular_z = 0
    # 0 1 0
    elif sensors['FRONT'] < 1 and sensors['LEFT'] > 1 and sensors['RIGHT'] > 1:
        current_state = '--- OBSTACLE AT FRONT ---'
        linear_x = 0
        angular_z = 0.3
    # 0 0 1
    elif sensors['FRONT'] > 1 and sensors['LEFT'] > 1 and sensors['RIGHT'] < 1:
        current_state = '--- OBSTACLE AT RIGHT ---'
        linear_x = 0
        angular_z = 0.3
    # 1 0 0
    elif sensors['FRONT'] > 1 and sensors['LEFT'] < 1 and sensors['RIGHT'] > 1:
        current_state = '--- OBSTACLE AT LEFT ---'
        linear_x = 0
        angular_z = -0.3
    # 0 1 1
    elif sensors['FRONT'] < 1 and sensors['LEFT'] > 1 and sensors['RIGHT'] < 1:
        current_state = '--- OBSTACLE AT FRONT AND RIGHT ---'
        linear_x = 0
        angular_z = 0.3
    # 1 1 0
    elif sensors['FRONT'] < 1 and sensors['LEFT'] < 1 and sensors['RIGHT'] > 1:
        current_state = '--- OBSTACLE AT FRONT AND LEFT ---'
        linear_x = 0
        angular_z = -0.3
    # 1 1 1
    elif sensors['FRONT'] < 1 and sensors['LEFT'] < 1 and sensors['RIGHT'] < 1:
        current_state = '--- OBSTACLE AT FRONT, LEFT AND RIGHT ---'
        linear_x = 0
        angular_z = 0.3
    # 1 0 1
    elif sensors['FRONT'] > 1 and sensors['LEFT'] < 1 and sensors['RIGHT'] < 1:
        current_state = '--- OBSTACLE AT LEFT AND RIGHT ---'
        linear_x = 0.3
        angular_z = 0
    else:
        current_state = 'UNKNOWN CASE'
        rospy.loginfo(sensors)
    
    rospy.loginfo(current_state)
    msg.linear.x = linear_x
    msg.angular.z = angular_z
    pub.publish(msg)

if __name__ == '__main__':
    main()


