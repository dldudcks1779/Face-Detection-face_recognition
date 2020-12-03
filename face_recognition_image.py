# 필요한 패키지 import
import numpy as np # 파이썬 행렬 수식 및 수치 계산 처리 모듈
import cv2 # opencv 모듈
import imutils # 파이썬 OpenCV가 제공하는 기능 중 복잡하고 사용성이 떨어지는 부분을 보완(이미지 또는 비디오 스트림 파일 처리 등)
import face_recognition # 얼굴 특성 정보 추출(얼굴 인식) 모듈

# 이미지 파일
image_path = "./face_image.jpg"

# 저장할 이미지 파일
result_path = "result_face_image.jpg"

# 이미지 읽기
face_image = cv2.imread(image_path)

# 이미지 resize
face_image = imutils.resize(face_image, width=500)

# face_recognition.face_locations(이미지(numpy 배열), 모델) : 이미지에서 사람 얼굴의 bounding boxes 반환
face_locations = face_recognition.face_locations(face_image, model='hog') # hog(기본값) : 비교적 덜 정확하지만 cpu에서도 빠름(gpu를 사용 가능한 경우 cnn)

# 얼굴 번호
number = 0

# 얼굴 인식 목록 수 만큼 반복
for face_location in face_locations:
    (y1, x2, y2, x1) = face_location # 인식된 얼굴 좌표

    cv2.putText(face_image, "Face[{}]".format(number + 1), (x1 - 5, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2) # 얼굴 번호 출력
    cv2.rectangle(face_image, (x1, y1), (x2, y2), (0, 255, 0), 2) # bounding box 출력

    number = number + 1 # 얼굴 번호 증가

# 이미지 저장
cv2.imwrite(result_path, face_image) # 파일로 저장, 포맷은 확장자에 따름

# 이미지 show
cv2.imshow("Face Recognition", face_image)
cv2.waitKey(0)
