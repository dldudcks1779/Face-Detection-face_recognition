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
* #### 비디오를 저장하지 않을 경우
  * webcam : sudo python3 yolo_object_counting.py
    * 예) sudo python3 yolo_object_counting.py
  * video : sudo python3 yolo_object_counting.py --input 비디오 경로
    * 예) sudo python3 yolo_object_counting.py --input test_video.mp4
* #### 비디오를 저장할 경우
  * webcam : sudo python3 yolo_object_counting.py --output 저장할 비디오 경로
    * 예) sudo python3 yolo_object_counting.py --output result_video.avi
  * video : sudo python3yolo_object_counting.py --input 비디오 경로 --output 저장할 비디오 경로
    * 예) sudo python3 yolo_object_counting.py --input test_video.mp4 --output result_video.avi
---
