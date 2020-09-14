#! /usr/bin/env python
import rospy
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist, Point
from nav_msgs.msg import Odometry
from tf import transformations
import math

# robot state variables
position = Point()
yaw = 0
# robot state
state = 0   # while going straight it is 1 , when reaches goal it is 2 
# goal
goal_pos = Point()
goal_pos.x = -5
goal_pos.y = 5
goal_pos.z = 0
# parameters
yaw_diff = math.pi / 90
min_dist = 0.1

# publishers
pub = None


# callback
def callback_odom(msg):
    global position
    global yaw
    # position
    position = msg.pose.pose.position 
    # yaw
    quaternion = (msg.pose.pose.orientation.x,
                  msg.pose.pose.orientation.y,
                  msg.pose.pose.orientation.z,
                  msg.pose.pose.orientation.w)
    euler = transformations.euler_from_quaternion(quaternion)
    yaw = euler[2]
    # roll = euler[0]
    # pitch = euler[1]

               
# Orienting towards Obstacle function 
def head_towards_goal(goal_pos):
    global yaw, pub, yaw_diff, state
    goal_yaw = math.atan2( goal_pos.y - position.y, goal_pos.x - position.x)
    error_yaw = goal_yaw - yaw

    twist_msg = Twist()
    if math.fabs(error_yaw) > yaw_diff:
        twist_msg.angular.z = 0.7 if error_yaw > 0 else -0.7
    pub.publish(twist_msg)
    if math.fabs(error_yaw) <= yaw_diff:
        rospy.loginfo("Orientation Difference : %s ", error_yaw)
        state = 1         

# Go Straight function
def go_striaght(goal_pos):
    global yaw, pub, yaw_diff, state
    goal_yaw = math.atan2( goal_pos.y - position.y, goal_pos.x - position.x)
    error_yaw = goal_yaw - yaw
    dist_to_goal = math.sqrt(pow(goal_pos.y - position.y, 2) + pow(goal_pos.x - position.x, 2))
    if dist_to_goal > min_dist : 
        twist_msg = Twist()
        twist_msg.linear.x = 0.6
        pub.publish(twist_msg)
    else:
        rospy.loginfo("Goal Reached : %s ", dist_to_goal)
        state = 2
    
    if math.fabs(error_yaw) > yaw_diff :
        rospy.loginfo("Orientation Difference: %s ", error_yaw)
        state = 0

# Stop after reaching at Goal
def goal_reached():
    twist_msg = Twist()
    twist_msg.linear.x = 0.0
    twist_msg.angular.z = 0.0
    pub.publish(twist_msg)

def main():
    rospy.loginfo("hello")
    global pub
    rospy.init_node('go_to_point', anonymous=True)
    pub = rospy.Publisher('/cmd_vel', Twist, queue_size=1)
    sub = rospy.Subscriber('/odom', Odometry, callback_odom)

    while not rospy.is_shutdown():
        if state == 0:
            head_towards_goal(goal_pos)
        elif state == 1:
            go_striaght(goal_pos)
        elif state == 2:
            goal_reached()
            pass
        else:
            rospy.logerr('Unknown State')
            pass
        rospy.sleep(0.1)
if __name__ == "__main__":
    main()



