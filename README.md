# Flask_project_pedia
[Flask] Flask framework 미니프로젝트(project pedia) 

## 🖥️ 프로젝트 소개 
웹 크롤링을 활용한 간단 리뷰 게시판 형태의 "영화" 리뷰를 등록하는 웹 페이지 서비스

## 🕰️ 개발 기간
* 23.07.12일 - 23.07.13일

### 🧑‍🤝‍🧑 맴버구성 
 - 김인용 - 싱글 프로젝트

### ⚙️ 개발 환경 
- **MainLanguage** : `PYTHON`
- **IDE** : VisualStudio Code 1.79.2 (Universal)
- **Framework** : Flask Framework(2.3.2)
- **Database** : MongoDB(5.0.11)
- **SERVER** : Flask

## 📌 주요 기능
#### View 구성
- top부분에 웹 페이지 정보 : 타이틀(title), 영화 기록하기(button)
- button을 누르면 content부분에 리뷰를 기록하는 양식(form) 이 나타남
   : 영화 URL(input type=text), 별점(select>1~5option), 영화 리뷰 코멘트(input type=text area)
- bottom(사실상 content 하단 division)에는 DB에 저장된(영화가 기록 된) 영화 리스트 : 영화 이미지, 영화 제목, 영화 설명, 별점, 리뷰 코멘트

#### 웹 크롤링
- URL로부터 영화 이미지, 영화 제목, 영화 설명 항목 메타태그 크롤링(soup.select_one)

#### 영화 리뷰 기록 진행
- 대상 영화 URL, 별점, 리뷰 코멘트 입력
- '기록하기' 버튼으로 입력값+크롤링 데이터 DB로 전송 및 저장 (insert)

#### 리뷰목록확인
- DB에 저장된 기록된 리뷰 데이터 받기(find(==read))
- 받은 데이터를 footer 부분에 4열 카드 형태로 출력
