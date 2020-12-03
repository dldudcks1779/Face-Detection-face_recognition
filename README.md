<div>
  <p align="center">
    <img width="500" src="result_face_video.gif"> 
  </p>
</div>

## face_recognition
* #### 파이썬 얼굴 인식 라이브러리
---
### 실행 환경
* #### Ubuntu
* #### OpenCV Version : 3.x.x
  * ##### 설치 : https://blog.naver.com/dldudcks1779/222020005648
* #### imutils
  * ##### 설치 : sudo pip3 install imutils
* #### face_recognition
  * ##### 설치 : sudo pip3 install face_recognition
---
## 이미지 얼굴 인식
* #### 이미지를 저장하지 않을 경우
  * sudo python3 object_detection_image.py --input 이미지 경로
    * 예) sudo python3 object_detection_image.py --input ./test_image/test_image_1.jpg
* #### 이미지를 저장할 경우
  * sudo python3 object_detection_image.py --input 이미지 경로 --output 저장할 이미지 경로
    * 예) sudo python3 object_detection_image.py --input ./test_image/test_image_1.jpg --output ./result_image/result_image_1.jpg

<div>
  <p align="center">
    <img width="300" src="face_image.jpg"> 
    <img width="300" src="result_face_image.jpg">
  </p>
</div>
---
