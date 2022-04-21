
import cv2
import pytesseract

pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files (x86)/Tesseract-OCR/tesseract.exe'
image = cv2.imread('download4.jpg')

image = cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
height,width,_ =image.shape
print(height,width)
text = pytesseract.image_to_string('download4.jpg',lang = 'eng',)
print(text)

cv2.imshow('Output', image)
cv2.waitKey(0)



#https://stackabuse.com/pytesseract-simple-python-optical-character-recognition