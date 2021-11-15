import cv2
import numpy as np
import os

frameWidth = 640
frameHeight = 480

capture = cv2.VideoCapture(0)
capture.set(3, frameWidth)
capture.set(4, frameHeight)



def noop(_):
    pass

def getImageFromPath(fileName): 
    absolute_path = os.path.join(os.getcwd(), 'imgs', fileName)
    return scaleImage(cv2.imread(absolute_path), 30)

def processImage(source):
    imgBlur = cv2.GaussianBlur(source, (7,7),1)
    imgGrayBlur = cv2.cvtColor(imgBlur, cv2.COLOR_BGR2GRAY)
    threshold1 = cv2.getTrackbarPos("Threshold1", "Thresholds")
    threshold2 =  cv2.getTrackbarPos("Threshold2", "Thresholds")
    return dilateImage(cv2.Canny(imgGrayBlur,threshold1, threshold2))

def resizeImage(img, width, height): 
    dim = (width, height)
    return cv2.resize(img, dim, interpolation= cv2.INTER_AREA)

def scaleImage(img, scalePercentFactor): 
    width = int(img.shape[1] * scalePercentFactor /100)
    height = int(img.shape[0] * scalePercentFactor /100)
    dim = (width,height)
    return cv2.resize(img, dim, interpolation= cv2.INTER_AREA)

def dilateImage(img):
    kernel = np.ones((5,5))
    return cv2.dilate(img, kernel, iterations=1)
    
def drawContours():
    img = processImage(getImageFromPath('free connection with arrow.jpg'))
    imgContour = getImageFromPath('free connection with arrow.jpg').copy();
    contours, hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    cv2.drawContours(imgContour, contours, -1, (255,0,255), 7)
    cv2.imshow("stick test", imgContour)
    for cnt in contours:
        cv2.drawContours(imgContour, cnt, -1, (255,0,255), 7)
        peri = cv2.arcLength(cnt, True)
        area = cv2.contourArea(cnt);
        approx = cv2.approxPolyDP(cnt, 0.02 * peri, True)
        print(len(approx))


cv2.namedWindow("Thresholds")
cv2.resizeWindow("Thresholds",600,400)
cv2.createTrackbar("Threshold1","Thresholds", 80,255,noop)
cv2.createTrackbar("Threshold2","Thresholds", 80,255,noop)

while True:
    success, img = capture.read()
    # cv2.imshow("Video", processImage(img))
    # cv2.imshow("Circles", processImage(getImageFromPath('circles.jpg')))
    # cv2.imshow("free connection with arrow", processImage(getImageFromPath('free connection with arrow.jpg')))
    # cv2.imshow("free connection with line", processImage(getImageFromPath('free connection with line.jpg')))
    # cv2.imshow("stick connections", processImage(getImageFromPath('stick connections.jpg')))
    drawContours()
    if(cv2.waitKey(1) & 0xFF == ord('q')):
        break
