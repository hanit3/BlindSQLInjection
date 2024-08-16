# BlindSQLInjection
Python을 이용한 Blind SQL Injection 자동화 공격 스크립트


## 개요
웹사이트의 데이터베이스를 탈취하기 위해 공격 대상에 SQL Injection 취약점이 있는지 파악한 후, Injection 공격을 자동으로 수행하기 위한 Python 스크립트를 개발함

<br>
<h3>주요 기능</h3>
1. SQL Injection 구문을 반복적으로 웹사이트에 보내는 기능
2. 로그인 할 때마다 바뀌는 세션 ID 값을 새롭게 GET Request Header에 넣는 기능
3. 테이블명과 컬럼명을 공격자가 선택하여 선택한 부분에 해당하는 데이터만 추출하여 보여주는 기능

<br><br>
<h3>프로젝트 수행 일정</h3>
일정	수행 내용
06.18 ~ 06.19	공격 타겟 분석, 취약점 파악
06.20	개발 환경 구성
06.21 ~ 06.24	자동화 기능 개발
06.25 ~ 06.27	프로그램 GUI 개발
06.27 ~ 06.30	프로젝트 수행 보고서 작성
![image](https://github.com/user-attachments/assets/64cb3393-8dad-4e3f-8197-67ea4ac3e204)


## 개발 도구
<img src="https://img.shields.io/badge/burpsuite-20232a.svg?style=for-the-badge&logo=burpsuite&fontColor=FF6633" />
