import cv2 as cv
cap = cv.VideoCapture("vidmp4.mp4")
image1 = cv.imread("image1.png")
image2 = cv.imread("image2.png")
image3 = cv.imread("image3.png")
image4 = cv.imread("image4.png")
#option = int(input("enter the filter option"))
while True:
    flag, frame = cap.read()
    if not flag:
        print("Could not access the video")
        break
    #if option == 1:
    image1 = cv.resize(image1, (frame.shape[1], frame.shape[0]))
    blended_frame1 = cv.addWeighted(frame, 0.8, image1, 0.2, gamma=0.5)
    cv.imshow("Blended frame1", blended_frame1)
    #else:
    image2 = cv.resize(image2, (frame.shape[1], frame.shape[0]))
    blended_frame2 = cv.addWeighted(frame, 0.8, image2, 0.2, gamma=0.5)
    cv.imshow("Blended frame2", blended_frame2)

    if cv.waitKey(10) & 0xff == ord('q'):
        break
cap.release()
cv.destroyAllWindows()