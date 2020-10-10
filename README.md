X-ray사진을 이용한 폐렴 진단 (CNN)
================
본 내용은 요약본입니다.</br>
자세한 내용은 블로그에서 확인하실 수 있습니다.</br>
https://w-storage.tistory.com/31

1 데이터 수집
------------
데이터는 kaggle dataset을 사용했다.</br>
www.kaggle.com/paultimothymooney/chest-xray-pneumonia

2 사전지식 공부
------------
폐 속에 고름, 혈액 등이 차 있으면 X-ray 투과율이 떨어지며, 이로 인해 구름 같은 모양의 음영이 관찰된다면 폐렴이라 진단할 수 있다.</br>
자세한 내용은 블로그 내용 참조

3 데이터 전처리
------------
python과 opencv를 이용하여 필요한 영역만 잘라내고 크기를 조절해주는 프로그램을 만들었다.</br>
이미지를 gray scale로 만들었고 모든 픽셀은 0~255 사이의 값을 가지며 255로 나누어 0과 1사이의 값을 갖도록 했다.</br>
정상인 경우 0, 폐렴의 경우 1을 출력하게끔 정답 데이터를 준비했다.</br>

4 신경망 구축
------------
Keras 라이브러리의 ResNet50을 사용했다.

5 학습결과
------------
val폴더에 있는 총 16개의 데이터를 이용해 검증을 진행했다.</br></br>

epoch 30일 때</br>
마지막 epoch의 loss: 0.0097, accuracy: 0.9973</br>
test set 정확도: 약84.6%</br>
val data 정확도: 87.5%</br>
<img src= "https://user-images.githubusercontent.com/25631105/95660689-786d5b80-0b64-11eb-9b26-5ee427537954.png"></img></br>

epoch 50일 때</br>
마지막 epoch의 loss: 0.0019, accuracy: 0.9992</br>
test set 정확도: 약77.7%</br>
val data 정확도: 62.5%</br>
<img src= "https://user-images.githubusercontent.com/25631105/95660692-7acfb580-0b64-11eb-8ce1-580700532424.png"></img></br>

epoch 80일 때</br>
마지막 epoch의 loss: 0.0051, accuracy: 0.9979</br>
test set 정확도: 약84.3%</br>
val data 정확도: 87.5%</br>
<img src= "https://user-images.githubusercontent.com/25631105/95660694-7b684c00-0b64-11eb-9066-570c433cc442.png"></img></br>

6 결론
------------
개인적인 시간상의 문제로 본 프로젝트는 여기서 종료했다.</br>
epoch가 30일 때와 80일 때 정확도가 가장 높았고 epoch가 50일 때 정확도가 가장 낮았다.</br>
반대로 loss는 epoch가 50일 때 가장 낮았다. 하지만 모두 0.001이하이기에 이 차이에 큰 의미는 없다 생각된다.</br>
overfitting을 의심하려면 epoch가 커질수록 정확도가 떨어져야 할텐데 왜 이런 결과가 나왔는지는 향후 연구가 필요하다 생각된다.</br>

7 아쉬운 점, 더 해봐야 할 것들
------------
* epoch또한 하나의 하이퍼파라미터이기에 다른 파라미터를 변경하면 어떤 변화가 일어나는지 알아보고싶다.
* 검증데이터셋이 몇몇 epoch에서 평탄하지 않은것을 알 수 있다. 이러한 현상이 발생하는 이유를 알아보고 싶다.
* 다양한 신경망을 사용해서 차이점을 비교해보고 싶다.
* 본 프로젝트의 결과물인 신경망을 개선하여 90%이상의 정확도를 갖는 신경망을 만든다면 향후 추가 연구를 통해 전문 의료진의 판단 보조기구로도 사용이 될 수 있다 생각된다. 다만 이를 실제 환경에서 사용하려면 관련 전문가와 함께 프로젝트를 진행해야 할 것이다.
