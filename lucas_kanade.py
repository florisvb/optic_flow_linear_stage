import roslib
roslib.load_manifest('optic_flow')
import sys
import rospy
import cv
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError
import numpy as numpy
import cv_numpy


def get_optic_flow(im0, im1):
    
    im0 = (im0*255).astype('uint8')
    im1 = (im1*255).astype('uint8')
    
    im0_cv = cv_numpy.array2cv(im0)
    im1_cv = cv_numpy.array2cv(im1)

    velx = cv.CreateImage((im0_cv.width, im0_cv.height), cv.IPL_DEPTH_32F,1)
    vely = cv.CreateImage((im0_cv.width, im0_cv.height), cv.IPL_DEPTH_32F,1)

    winSize = (5,5)

    cv.CalcOpticalFlowLK(im0_cv, im1_cv, winSize, velx, vely)
    velx_np = cv_numpy.cv2array(velx)

    return velx_np
