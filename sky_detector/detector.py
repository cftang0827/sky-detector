import cv2
from scipy.signal import medfilt
from scipy import ndimage
import numpy as np
from matplotlib import pyplot as plt

def applyfunc(maskw):
    raw = maskw
    after_median = medfilt(raw, 19)
    try:
        first_zero_index = np.where(after_median == 0)[0][0]
        first_one_index = np.where(after_median == 1)[0][0]
        if first_zero_index > 20:
                maskw[first_one_index:first_zero_index] = 1
                maskw[first_zero_index:] = 0
                maskw[:first_one_index] = 0
    except:
        pass
    return maskw
    
def cal_skyline(mask):
    h, w = mask.shape
    np.apply_along_axis(applyfunc,0,mask)
    return mask


def get_sky_region_gradient(img):

    h, w, _ = img.shape

    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    img_gray = cv2.blur(img_gray, (9, 3))
    cv2.medianBlur(img_gray, 5)
    lap = cv2.Laplacian(img_gray, cv2.CV_8U)
    gradient_mask = (lap < 6).astype(np.uint8)

    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (9, 3))

    mask = cv2.morphologyEx(gradient_mask, cv2.MORPH_ERODE, kernel)
    # plt.imshow(mask)
    # plt.show()
    mask = cal_skyline(mask)
    # print("NONzero : ",np.count_nonzero(mask))
    after_img = cv2.bitwise_and(img, img, mask=mask)
    
    return after_img

