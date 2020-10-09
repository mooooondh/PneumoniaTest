import cv2

def img_cropper(file, load_link, save_link):
    img= cv2.imread(load_link+file, cv2.IMREAD_GRAYSCALE)

    x_mid = int(img.shape[1] / 2)
    x_len = 0

    img_canny = cv2.Canny(img, 10, 40)

    for i in range(4, img.shape[1]):
        if (img_canny[-20][i] != 0):
            x_len = i
            break

    img_crop = img[int(img.shape[0] * 0.1): img.shape[0] - int(img.shape[0] * 0.1), x_len: x_len + 2 * (x_mid - x_len)]
    try:
        img_res = cv2.resize(img_crop, dsize=(224, 224), interpolation=cv2.INTER_AREA)

        cv2.imwrite(save_link + file, img_res)
    except Exception:
        return

    return
