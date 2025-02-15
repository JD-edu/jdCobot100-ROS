# jdcobot_ros

ros2 humble 기준으로 만들어진 패키지.

## 시작하기
0. 터미널창에서 기본적으로 워크스페이스 들어가기.

1. 워크스페이스의 src 폴더에 jdcobot100_description 패키지 받기.
2. 워크스페이스에서 colcon bulid
3. 터미널창에서 source install/setup.bash
4. ros2 launch jdcobot100_description display_launch.py 
5. rviz와 joint_state_publisher_gui가 잘 떠있는지 확인.
6. 다른 터미널 창에서 ros2 run jdcobot100_description jdcobot_control.py
7. gui에서 모터 각도를 바꿨을 때 rviz와 실물 로봇이 같이 동작하는지 확인.

8. 만약 내가 원하는 각도로 코드에서 제어하고싶다면 js_5_pub_test.py 파일을 참고해서 작성해보기.  
js_5_pub_test.py 파일은 특정 각도로 서보모터를 5초 주기로 반복해서 작동하는 코드.

## rviz 세팅
TF 축 크기를 변경  
Marker Scale: 1 -> 0.3 으로 조절한 후 rviz_set.rviz에 저장.

## 에러 날 때
5.1. joint_state_publisher_gui 부분에서 에러가 난다면  
sudo apt install ros-<로스버전>-joint-state-publisher-gui    
ex) sudo apt install ros-foxy-joint-state-publisher-gui  
ex) sudo apt install ros-humble-joint-state-publisher-gui  

5.2. urdf가 rviz에 안나왔다면 rviz에서 RobotModel -> Description File 에서 경로부분을 다시 설정.  
urdf 파일 경로는 src/jdcobot_100_description/urdf/jdcobot_100_description.urdf  
다운 받을 때 패키지 경로가 바껴서 urdf 파일을 못불러오는 이유.      

6.1. usb포트 권한이 없을 때 sudo chmod 777 /dev/tty* 하기. 
혹은      
sudo usermod -a -G dialout <username> 해서 사용자를 dialout 그룹에 추가하는 것을 추천. 이후 재부팅해야 반영.  

6.2. USB포트 자체가 인식이 안됬을 때 oracle VM 기준으로 설정 -> USB -> USB필터 만들기 (오른쪽에 USB+ 모양) -> 컴퓨터와 연결된 포트 선택.  
