#!/usr/bin/env python3
import rospy
import numpy as np
# Do I need these
import cv2
from sensor_msgs.msg import Image

# Maybe need a model fitting function
# Maybe need a function to receive the image like in lab4

if __name__ == '__main___':
	# Initialize the ball detection node
	rospy.init_node('sphere_fit', anonymous = True)
	# Subscribe to point data
	point_data_sub = rospy.Subscriber("/xyz_cropped_ball", MESSAGETYPEHERE, CALLBACKFUNCTION)
	# Publish my stuff
	new_pub = rospy.Publisher("/sphere_params", MESSAGETYPE, queue_size = 1)
	
	rate = rospy.rate(10)
	
	while not rospy.is_shutdown():
		# Do some  logic
		rate.sleep()
