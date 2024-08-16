# BlindSQLInjection
Python을 이용한 Blind SQL Injection 자동화 공격 스크립트
<br>

## 개요
웹사이트의 데이터베이스를 탈취하기 위해 공격 대상에 SQL Injection 취약점이 있는지 파악한 후, <br>
Injection 공격을 자동으로 수행하기 위한 Python 스크립트를 개발함

<br>

## 주요 기능
1. SQL Injection 구문을 반복적으로 웹사이트에 보내는 기능<br>
2. 로그인 할 때마다 바뀌는 세션 ID 값을 새롭게 GET Request Header에 넣는 기능<br>
3. 테이블명과 컬럼명을 공격자가 선택하여 선택한 부분에 해당하는 데이터만 추출하여 보여주는 기능<br>

<br>

## 프로젝트 수행 일정
- 06.18 ~ 06.19	공격 타겟 분석, 취약점 파악<br>
- 06.20	개발 환경 구성<br>
- 06.21 ~ 06.24	자동화 기능 개발<br>
- 06.25 ~ 06.27	프로그램 GUI 개발<br>
- 06.27 ~ 06.30	프로젝트 수행 보고서 작성<br>

<br>

## 개발 환경
<div>
  <img src="https://img.shields.io/badge/burpsuite-FF6633.svg?style=for-the-badge&logo=burpsuite&fontColor=white" />
  <img src="https://img.shields.io/badge/python-3776AB.svg?style=for-the-badge&logo=python&fontColor=white" />
  <img src="https://img.shields.io/badge/visualstudio-0854C1.svg?style=for-the-badge&logo=googlechrome&fontColor=white" />
  <img src="https://img.shields.io/badge/chromium-4285F4.svg?style=for-the-badge&logo=googlechrome&fontColor=white" />
  <img src="https://img.shields.io/badge/windows-000000.svg?style=for-the-badge&logo=gnometerminal&fontColor=white" />
</div>
<br>

## 공격 과정
- 공격 흐름도
<img width="441" alt="image" src="https://github.com/user-attachments/assets/269ba74c-5eda-428e-afeb-2933b8b08a07">
<br><br>
① 웹사이트의 세션 ID값 확인<br><br>
② 프로그램 실행 후 세션 ID 입력하여 공격<br>
<img width="434" alt="image" src="https://github.com/user-attachments/assets/ded2889c-7b3b-4a15-b53a-a4d9f8c4add7">
<br>
  - 만약 세션 ID가 비어있다면 경고창 실행<br>
<img width="434" alt="image" src="https://github.com/user-attachments/assets/1804e550-c278-4c5a-867e-28b3ee1f9fc4">
<br>
  - 명령 프롬프트에서 테이블 탈취 중임을 확인<br>
<img width="432" alt="image" src="https://github.com/user-attachments/assets/442ffbbd-1cf0-47f9-a3e0-dac220738e6c">
<br><br>
③ 컬럼명 탈취<br>
  - 테이블 리스트에서 컬럼을 구하고자 하는 테이블을 하나 선택하면 해당 테이블의 모든 컬럼을 구하는 SQL Injection이 실행됨<br>
<img width="432" alt="image" src="https://github.com/user-attachments/assets/dc5ed307-7a5d-48f4-ada9-5bd86f8f1064"><br>
<br><br>
④ 데이터 탈취<br>
  - 위에서 구한 컬럼 리스트에서 데이터를 구하고자 하는 컬럼을 하나 선택하면 해당 컬럼의 모든 데이터를 추출하는 SQL Injection이 실행되고 이를 출력함<br>
<img width="398" alt="image" src="https://github.com/user-attachments/assets/04ee9a7f-663f-4d85-9944-21aaf7dec3e2">
<br>

## 공격 순서에 따른 함수 호출 과정
<img width="412" alt="image" src="https://github.com/user-attachments/assets/1327616f-69a8-424c-ba46-178ccbf1595f">
<br>

## 파일 및 함수 명세
<h3>파일 명세</h3>
- moduletwo_shopping.py: Blind SQL Injection 자동 수행 스크립트 <br>
- moduletwo_gui.py: GUI 화면 구현 <br>
<br>
<h3>함수 명세</h3>
① moduletwo_gui.py <br>
- exploit():	쿠키값 입력 후 공격 버튼 눌러 테이블 탈취 실행<br>
- updateColumns():	선택한 테이블의 전체 컬럼명을 리스트에 업데이트<br>
- updateData():	선택한 테이블, 선택한 컬럼의 데이터를 리스트에 업데이트<br>
- reset():	리스트로 보여지는 값 초기화<br>
- listboxView():	테이블, 컬럼, 데이터 리스트 박스를 정의<br>
<br>
② moduletwo_shopping.py<br>
- main():	데이터베이스에서 전체 테이블 탈취 실행<br>
- mainColumn():	테이블 하나의 전체 컬럼 탈취 실행<br>
- mainData():	테이블 하나, 컬럼 하나의 전체 데이터 탈취 실행<br>
- bnSearch():	Blind SQL Injection 구문을 웹사이트에 공격하고, Binary Search를 통해 문자 범위를 비교하여 문자 추출<br>
- dataSearch():	단계별 SQL구문을 설정하고, 이진 탐색을 실행시켜 추출된 문자를 하나의 문자열로 조합하여 리스트로 반환<br>
- hangulDecode():	ASCII값인 한글 데이터 디코딩 <br>

<br>
