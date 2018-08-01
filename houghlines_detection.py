import cv2
import numpy as np

def get_image(img):
    cv2.imshow('image1', img)
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)#灰度图像 
    #open to see how to use: cv2.Canny
    #http://blog.csdn.net/on2way/article/details/46851451 
    edges = cv2.Canny(gray,20,80)
    cv2.imshow('image2', edges )
    #hough transform
    return edges , gray
def get_line(lines1):
    num_list = []
    x = 1
    max_rho = 0
    max_theta = 0
    for rho,theta in lines1: 
        if -0.5 < (theta - np.pi/2) < 0.5:
            num_list.append(rho)
    num_list = sorted(num_list)
    max_rho = num_list[1]
    max_theta = np.pi/2
    print(num_list)

    a = np.cos(max_theta)
    b = np.sin(max_theta)
    x0 = a*max_rho
    y0 = b*max_rho
    x1 = int(x0 + 1000*(-b))
    y1 = int(y0 + 1000*(a))
    x2 = int(x0 - 1000*(-b))
    y2 = int(y0 - 1000*(a)) 
    cv2.line(img,(x1,y1),(x2,y2),(255,0,0),2)


    i = 2
    while i < 10:
        if (max_rho - num_list[i]) < -20:
            max_rho = num_list[i]
            break
        else:
            i = i+1
    a = np.cos(max_theta)
    b = np.sin(max_theta)
    x0 = a*max_rho
    y0 = b*max_rho
    x3 = int(x0 + 1000*(-b))
    y3 = int(y0 + 1000*(a))
    x4 = int(x0 - 1000*(-b))
    y4 = int(y0 - 1000*(a)) 
    cv2.line(img,(x3,y3),(x4,y4),(255,0,0),2)
    cv2.imshow('image4', img )
    return x1,x2,y1,y3
if __name__ == '__main__':
    img = cv2.imread(r'H:\desktop\no\71136650639607.jpg')
    edges , gray = get_image(img)
    lines = cv2.HoughLines(edges,1,np.pi/180,160)
    lines1 = lines[:,0,:]  #提取为二维
    
    x1,x2,y1,y3 = get_line(lines1)
    img = img[y1:y3,x1:x2]
    print(x1,x2,y1,y3)
 
    if img.shape[0]>0:
        if(img.shape[1]>0):
             cv2.imshow('image3', img )
    
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    