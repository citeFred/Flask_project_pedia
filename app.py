# 라이브러리 임포트
# Flask Framework
# view페이지 렌더링을 위한 render_template 메서드
# 요청 데이터에 접근 할 수 있는 flask.request 모듈
# dictionary를 json형식의 응답 데이터를 내보낼 수 있는 jsonify 메서드
from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

# [POST-4] 웹 크롤링을 위해서 임포트를 시작하자.
# 웹 크롤링을 위한 requests 임포트
# 크롤링한 HTML을 text로 변환 parsing할 BeautifulSoup 임포트
import requests
from bs4 import BeautifulSoup

# [POST-8] MongoDB사용을 위한 pymongo와 certifi 임포트
from pymongo import MongoClient
import certifi
# [POST-9] DB 커넥션 구성
ca = certifi.where()
client = MongoClient('mongodb+srv://ohnyong:test@cluster0.lu7mz8j.mongodb.net/?retryWrites=true&w=majority',tlsCAFile=ca)
db = client.dbsparta

# "localhost:5001/" URL요청에 메인 뷰 페이지 반환 응답
@app.route('/')
def home():
    return render_template('index.html')

# [POST-0] CREATE 부분부터 코드를 작성하는 것(==POST)이 확인이 가능(READ부터하면 데이터가없어서 테스트 어려움)
# fetch('URL')부분, 반환값은 res로 전달.
# "localhost:5001/movie" URL POST방식 요청에 응답
@app.route("/movie", methods=["POST"])
def movie_post():
    # [POST-1] 프론트로부터 무엇을 받아야 하는가? -> 프론트 input으로부터 url, star, comment를 받을 것이다.
    url_receive = request.form['url_give']
    star_receive = request.form['star_give']
    comment_receive = request.form['comment_give']
    # [POST-2] url로부터는 무엇을 할 것인가? -> 웹크롤링으로 image, title, description을 받을 것이다.
    # [POST-3] 그럼 웹 크롤링을 하기 위해서는? -> 상단에 임포트부터 시작하자. 테스트한것을 이용하자.

    # [POST-5] 웹 크롤링에서 URL은 어디서오는가? -> 위 url_receive를 이용
    # [POST-6] 웹 크롤링에서는 무엇을 가져오는가? -> ogtitle, ogimage, ogdesc
    # ----start----- meta_prac.py 테스트 샘플에서 가져온 코드 ----start-----
    headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
    data = requests.get(url_receive,headers=headers)
    soup = BeautifulSoup(data.text, 'html.parser')

    # meta태그의 프로퍼티가 og:title인 것을 가져온다.
    # image, description도 가져온다.
    ogtitle = soup.select_one('meta[property="og:title"]')['content']
    ogimage = soup.select_one('meta[property="og:image"]')['content']
    ogdesc = soup.select_one('meta[property="og:description"]')['content']
    print(
        "INPUT URL : "+url_receive+" / ",
        "INPUT STAR : "+star_receive+" / ",
        "INPUT COMMENT : "+comment_receive+" / ",
        "CRAWLED INPUT TITLE : "+ogtitle+" / ",
        "CRAWLED INPUT IMAGE URL : "+ogimage+" / ",
        "CRAWLED INPUT DESCRIPTION : "+ogdesc+" / "
    )
    # ----end----- meta_prac.py 테스트 샘플에서 가져온 코드 ----end-----


    # [POST-7] BS로 추출한 텍스트를 DB에 넣자 MongoDB연결을 위한 임포트부터 시작
    # [POST-10] DB연결이 완료되었으니 document처럼 담는다.
    # INSERT_ONE
    # 저장 - 예시
    # doc = {'name':'bobby','age':21}
    # db.users.insert_one(doc)
    doc = {
        'title' : ogtitle,
        'desc' : ogdesc,
        'image' : ogimage,
        # url은 현재 View에서 필요하지 않지만 추후 Update 기능을 위해서 DB에 저장까지만 진행하도록 했다.
        'url' : url_receive,
        'comment' : comment_receive,
        'star':star_receive
    }
    # [POST-11] doc에 담았으니 DB에 insert 한다.
    db.moviespedia.insert_one(doc)
    # [POST-12] insert가 완료되었으니 완료 메시지를 반환한다.
    return jsonify({'msg':'POST 연결 완료!'+'DB 저장 완료!'})

# fetch('URL')부분, 반환값은 res로 전달.
# "localhost:5001/movie" URL GET방식 요청에 응답
@app.route("/movie", methods=["GET"])
def movie_get():
    return jsonify({'msg':'GET 연결 완료!'})

# app이라는 메인 함수 
# if __name__ == "__main__" 의 의미는 메인 함수의 선언, 시작을 의미
# 이 파이썬 스크립트가 직접 실행될 때에는 main() 함수를 실행하라
if __name__ == '__main__':
    app.run('0.0.0.0', port=5001, debug=True)