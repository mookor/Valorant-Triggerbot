import numpy as np
def get_red_pixels_sum(sct_img):
    img = np.array(sct_img)[:,:,:3]
    
    img[img[:,:,2] < 230] = 0
    blue_mask = img[:,:,0] > 230
    green_mask = img[:,:,1] > 230

    img[green_mask] = 0
    img[blue_mask] = 0

    img = img[:,:,2]

    try:
        red_sum = np.sum(img) / img.shape[0] / img.shape[1]
        red_sum = red_sum.astype(np.uint8)
    except:
        red_sum = 0


        
    return red_sum