import  cv2 as cv

print("hello")
img=cv.imread("Photos/twocats.jpeg")
img=cv.resize(img,(500,400))
cv.imshow("img",img)
cv.waitKey(0)
cv.destroyAllWindows()
