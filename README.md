# Take A Glance

## Introduce

"Take A Glance" (힐끗 보세요)라는 이름을 가진 이 프로젝트는 숭실대학교 도서관의 출입 과정에서 발생하는 불편함을 줄이기 위해 고안된 **얼굴인식 도서관 출입 간편화 프로젝트** 입니다.

숭실대학교 도서관은 출입 시 학생증 카드를 스캔하여야 입장이 가능합니다. 게다가 출입 카드는 일일이 카드를 휴대하고 다녀야 하고, 분실의 우려가 있어 큰 불편함이 있습니다.

학교 측에서도 이러한 문제를 인식하고, 출입 카드를 대체하기 위해 도서관 모바일 어플리케이션을 이용해 출입이 가능하도록 만들었지만, 이 또한 마찬가지로 일일이 출입 시마다 어플리케이션을 켜서 QR코드 화면을 띄워야 한다는 불편함이 존재합니다.

이러한 문제점을 해소하기 위해, **얼굴 인식을 활용한 도서관 출입 간편화 시스템**을 고안하였습니다. 이 시스템은 기존의 방식에서 웹캠과 프로그램을 실행할 수 있는 컴퓨터만 있으면 실현이 가능하므로, 실효성도 충분할 것으로 보입니다.


## Members

|                                                       asheswook                                                       |                                                       kty1004                                                       |
| :-------------------------------------------------------------------------------------------------------------------: | :-----------------------------------------------------------------------------------------------------------------: |
| <a href="https://github.com/asheswook"><img src="https://avatars.githubusercontent.com/u/25760310?v=4" width=200></a> | <a href="https://github.com/kty1004"><img src="https://avatars.githubusercontent.com/u/95904582?v=4" width=200></a> |
|                                                  얼굴 인식/예측 구현                                                  |                                               GUI, 데이터베이스 구현                                                |

## Implementation

- Sklearn의 LabelPropagation 알고리즘을 이용해 반지도 학습으로 실시간 얼굴 예측을 구현하였으며 [VisageSnap](https://github.com/asheswook/VisageSnap) 라이브러리를 사용하였습니다.
- 얼굴 인식을 위해 [dlib](http://dlib.net/) 라이브러리와 [face_recognition](https://github.com/ageitgey/face_recognition), [OpenCV](https://github.com/opencv/opencv-python) 라이브러리를 사용하였습니다.
- Web으로 전체 GUI를 구성하였으며, [Flask](https://github.com/pallets/flask) 프레임워크를 사용하였습니다.
- 데이터베이스는 빠른 개발을 위해 CSV를 활용하였습니다.

## Result

- 실시간으로 인식된 얼굴에 원이 그려지며, 예측된 이름이 원 왼쪽 아래 출력됩니다.
- 학습된 인물의 이름, 사진의 경로가 나타납니다.

<img src="https://github.com/asheswook/TakeAGlance/blob/main/docs/impl.gif?raw=true" width=827>
<img width="827" alt="image" src="https://github.com/asheswook/TakeAGlance/assets/25760310/5c7f0572-442e-486a-a7b5-744749cac28f">

## P.S.
*이 프로젝트는 숭실대학교 2023년 1학년 교양 필수 '컴퓨팅적사고와활용' 과목의 최종 프로젝트로 제출되었습니다.*
