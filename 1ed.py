import cv2
import os
import string
img = cv2.imread("mypic.jpg")
if img is None:
    print("Image not found!")
    exit()
msg = input("Enter secret message: ")
password = input("Enter a passcode: ")
d = {}
c = {}
for i in range(255):
    d[chr(i)] = i
    c[i] = chr(i)
m = 0
n = 0
z = 0
for i in range(len(msg)):
    if n >= img.shape[0] or m >= img.shape[1]:
        print("Message is too long for the image dimensions.")
        break
    img[n, m, z] = d[msg[i]]
    n += 1
    m += 1
    z = (z + 1) % 3
cv2.imwrite("encryptedImage.jpg", img)
os.system("start encryptedImage.jpg")  
pas = input("Enter passcode for Decryption: ")
if password == pas:
    message = ""
    n = 0
    m = 0
    z = 0
    for i in range(len(msg)):
        if n >= img.shape[0] or m >= img.shape[1]:
            print("Error: Image does not contain enough pixels to decode the message.")
            break
        message += c[img[n, m, z]]
        n += 1
        m += 1
        z = (z + 1) % 3
    print("Decrypted message:", message)
else:
    print("Incorrect passcode!")
