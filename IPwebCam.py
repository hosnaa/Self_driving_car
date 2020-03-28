# -*- coding: utf-8 -*-
"""
Created on Wed Nov  6 23:51:43 2019

@author: hosna
"""

1) videoCapture
"""Access IP Camera in Python OpenCV"""

import cv2

stream = cv2.VideoCapture('protocol://IP:port/1')

# Use the next line if your camera has a username and password
# stream = cv2.VideoCapture('protocol://username:password@IP:port/1')  

while True:

    r, f = stream.read()
    cv2.imshow('IP Camera stream',f)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
-----------------------------------------------
------------------------------------------------
2) bluetooth.close()
---------------------------------------------
--------------------------------------------
3) delete break/waitkey 
------------------------------------------------------           
    if(!vcap.read(image)) {
            std::cout << "No frame" << std::endl;
            cv::waitKey();
        }
        cv::imshow("Output Window", image);
        if(cv::waitKey(1) >= 0) break;
    }   
}
------------------------------------------------
------------------------------------------------
4) Threading
    

    
    