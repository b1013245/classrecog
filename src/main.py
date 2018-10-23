# -*- coding: utf-8 -*- 
# このファイルを呼び出してプログラム実行する

import cv2 as cv
import numpy as np
#import detector as dt
#import statistics as sta
import capture
import os

def read_image(path):
    img = cv.imread(path)
    return img



    

if __name__ == '__main__':
#    path = 'img/liftingL.png'
    capture.capture("4-R-1", "L")
    
    
    '''
    method = ('ORB', 'FFD', 'MSER', 'AKAZE', 'BRISK', 'KAZE', 'SBD')
    
    
    img = read_image(path)
#    for i in range(0,6):
    keypoints, descriptors = dt.feature_detect_compute(img, 5)
        # out = cv.drawKeypoints(img, keypoints, None)
        # dt.image_write(out, 'liftingL_'+ method[i] + '.png')
    print(descriptors[1])
    '''