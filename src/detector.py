# 特徴検出器
# 参考：https://qiita.com/hitomatagi/items/62989573a30ec1d8180b


import cv2 as cv





def feature_detect_compute(img, num):
    print('feature_detect')
    # TODO:検出器&記述子考える！！！
    if num == 1:
        detector = cv.ORB_create()
    elif num == 2:
        detector = cv.FastFeatureDetector_create()
    elif num == 3:
        detector = cv.MSER_create()
    elif num == 4:
        detector = cv.AKAZE_create()
    elif num == 5:
        detector = cv.BRISK_create()
    elif num == 6:
        detector = cv.KAZE_create()
    elif num == 7:
        detector = cv.SimpleBlobDetector_create()
    
    keypoints = detector.detect(img)
    descriptors = detector.compute(img, keypoints)
    return keypoints, descriptors


# 表示してキー入力でウィンドウ閉じる or 画像保存
def image_write(keypoints, name):
    cv.imwrite('img/'+name, keypoints)
    '''
    cv.imshow("keypoints", keypoints)
    cv.waitKey(0)
    cv.destroyAllWindows()
    '''









