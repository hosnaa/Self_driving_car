# Self_driving_car
This repo contain the files needed to make a self driving car, This is the software part of this project.
## Description for the process:
* [IPwebCam.py](https://github.com/hosnaa/Self_driving_car/blob/master/IPwebCam.py) This is an initial file for connecting the IPwebcam mobile app to your laptop (you'll see on your pc what your mobile camera sees)
* [Self_driving_car.py](https://github.com/hosnaa/Self_driving_car/blob/master/Self_driving_car.py) This is the main python file for self driving that detects the lane lines, then its heading line and then sends an order for the arduino that it needs to move forward or steer to the right or left depending on what lane it detects (right or left)
* []() This is the arduino file that takes the orders from the python file and moves the motors

##### Note: for the hardware, you'll mainly need an ESP, bluetooth module, motors, adapter, H-bridge, blue lane line(any blue adhesive material will do well)
