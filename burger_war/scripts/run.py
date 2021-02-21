#!/usr/bin/env python
# -*- coding: utf-8 -*-

#===================================================================
#Project Name	: burger_war
#File Name		: run.py
#
#© 2021 Curereaper. All rights reserved.
#===================================================================

import rospy
import random

from geometry_msgs.msg import Twist
import tf

#navi
import actionlib
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal
import actionlib_msgs

class RunBot():
    def __init__(self):

        self.vel_pub = rospy.Publisher('cmd_vel', Twist,queue_size=1)
        self.client = actionlib.SimpleActionClient('move_base',MoveBaseAction)

    def setGoal(self,x,y,yaw):
        self.client.wait_for_server()

        goal = MoveBaseGoal()
        goal.target_pose.header.frame_id = "/map"
        goal.target_pose.header.stamp = rospy.Time.now()
        goal.target_pose.pose.position.x = x
        goal.target_pose.pose.position.y = y

        q=tf.transformations.quaternion_from_euler(0,0,yaw)        
        goal.target_pose.pose.orientation.x = q[0]
        goal.target_pose.pose.orientation.y = q[1]
        goal.target_pose.pose.orientation.z = q[2]
        goal.target_pose.pose.orientation.w = q[3]

        self.client.send_goal(goal)
        wait = self.client.wait_for_result()
        if not wait:
            rospy.logerr("Action server not available!")
            rospy.signal_shutdown("Action server not available!")
        else:
            return self.client.get_result()        


    def strategy(self):
        r = rospy.Rate(5) # change speed 5fps

        while not rospy.is_shutdown():

            self.setGoal(-0.8,-0.5,0)
            self.setGoal(-0.8,-0.5,3.1415/2)

            self.setGoal(-0.4,0,0)
            self.setGoal(-0.4,0,-3.1415/2)

            self.setGoal(-0.2,-0.5,0)
            self.setGoal(-0.2,-0.5,3.1415)

            self.setGoal(0,-0.5,0)
            self.setGoal(0,-0.5,3.1415/2)
            self.setGoal(0,-0.5,-3.1415/2)

            self.setGoal(0.2,-0.5,0)
            self.setGoal(0.2,-0.5,3.1415/2)

            self.setGoal(0.4,0,0)
            self.setGoal(0.4,0,3.1415)

            self.setGoal(0.8,-0.5,0)
            self.setGoal(0.8,-0.5,3.1415)
            self.setGoal(0.8,-0.5,-3.1415/2)

            self.setGoal(0.8,0.5,0)
            self.setGoal(0.8,0.5,3.1415)

            self.setGoal(0.8,0.5,3.1415/2)
            self.setGoal(0.8,0,0)

            self.setGoal(0.2,0.5,0)

            self.setGoal(0.0,0.5,0)
            self.setGoal(0.0,0.5,3.1415/2)

            self.setGoal(-0.8,0.5,0)
            self.setGoal(-0.8,0.5,3.1415)

            self.setGoal(-0.4,0,0)

            self.setGoal(-0.8,-0.5,0)
               


if __name__ == '__main__':
    rospy.init_node('test')
    bot = RunBot()
    bot.strategy()
