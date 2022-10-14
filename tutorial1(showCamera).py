import cv2

cap = cv2.VideoCapture(1)#讀取影片,1=攝像頭

while True:
    ret, frame = cap.read()#cap.read()會產生兩變數,前者(布林,判斷是否取得成功),後者(取得下張影格)
    if ret:
        cv2.imshow('video', frame)#show,‘title'畫面
    else:
        break
    if cv2.waitKey(10) == ord('q'):
        break