#!/usr/bin/env python
from gpiozero import  CPUTemperature
import rospy
from std_msgs.msg import  Float32


if __name__ == "__main__":

  rospy.init_node("temp_sensor")
  pub = rospy.Publisher('rov/temp_sensor', Float32, queue_size=10)
  rate = rospy.Rate(10)

  while not rospy.is_shutdown():
	try:
	  temp = CPUTemperature(min_temp=0, max_temp=100).temperature
	  pub.publish(temp)
	except IOError:
	  pass
	rate.sleep()
