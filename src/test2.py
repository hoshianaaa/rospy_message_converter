from rospy_message_converter import json_message_converter
from std_msgs.msg import String
from std_msgs.msg import Float32MultiArray
from geometry_msgs.msg import Twist

message = String()
message.data = "hello"
json_str = json_message_converter.convert_ros_message_to_json(message)
print(json_str)

message = Twist()
json_str = json_message_converter.convert_ros_message_to_json(message)
print(json_str)

message = Float32MultiArray()
message.data = [1,2,3,4]
json_str = json_message_converter.convert_ros_message_to_json(message)
print(json_str)
