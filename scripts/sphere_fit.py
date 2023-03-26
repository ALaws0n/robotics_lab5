#!/usr/bin/env python3
import rospy
import numpy as np
from robot_vision_lectures.msg import XYZarray
from robot_vision_lectures.msg import SphereParams

matrix_a = []
matrix_b = []

# Maybe need a model fitting function
# Maybe need a function to receive the image like in lab4
def receive_point_data(point_data):
	global matrix_a
	global matrix_b
	
	# Point Data is an array of points
	for point in point_data.points:
		try:
			matrix_a.append([2*point.x, 2*point.y, 2*point.z, 1])
			matrix_b.append([point.x**2 + point.y**2 + point.z**2])
		except:
			print("Data is not being appended")
		


if __name__ == '__main__':
	# Initialize the ball detection node
	rospy.init_node('sphere_fit', anonymous = True)
	# Subscribe to point data
	point_data_sub = rospy.Subscriber("/xyz_cropped_ball", XYZarray, receive_point_data)
	# Publish my stuff -- Rename publisher later
	new_pub = rospy.Publisher("/sphere_params", SphereParams, queue_size = 1)
	
	rate = rospy.Rate(10)
	
	while not rospy.is_shutdown():
		# If our initial matrices are constructed and not empty
		if len(matrix_a) > 0 and len(matrix_b) > 0:
			print(matrix_b)
		
		# Do some  logic
		rate.sleep()
