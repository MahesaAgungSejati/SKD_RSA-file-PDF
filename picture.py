import cv2
import numpy as np

# Ganti mode baca menjadi cv2.IMREAD_GRAYSCALE
demo = cv2.imread("C:\\Users\\Mahesa Agung Sejati\\Pictures\\SKD\\4.jpg", cv2.IMREAD_GRAYSCALE)

# Periksa apakah gambar berhasil dimuat
if demo is None:
    print("Error: Unable to load the image")
    exit()

r, c = demo.shape
key = np.random.randint(0, 256, size=(r, c), dtype=np.uint8)
cv2.imwrite("C:\\Users\\Mahesa Agung Sejati\\Pictures\\SKD\\KEY-4.jpg", key)

cv2.imshow("demo", demo)
cv2.imshow("key", key)

encryption = cv2.bitwise_xor(demo, key)
cv2.imwrite("C:\\Users\\Mahesa Agung Sejati\\Pictures\\SKD\\ENC-4.jpg", encryption)
decryption = cv2.bitwise_xor(encryption, key)
cv2.imwrite("C:\\Users\\Mahesa Agung Sejati\\Pictures\\SKD\\DES-4.jpg", decryption)

cv2.imshow("encryption", encryption)
cv2.imshow("decryption", decryption)

cv2.waitKey(-1)
cv2.destroyAllWindows()
