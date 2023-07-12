# 라이브러리 임포트
# Flask Framework
# view페이지 렌더링을 위한 render_template 메서드
# 요청 데이터에 접근 할 수 있는 flask.request 모듈
# dictionary를 json형식의 응답 데이터를 내보낼 수 있는 jsonify 메서드
from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

# "localhost:5001/" URL요청에 메인 뷰 페이지 반환 응답
@app.route('/')
def home():
    return render_template('index.html')

# fetch('URL')부분, 반환값은 res로 전달.
# "localhost:5001/movie" URL POST방식 요청에 응답
@app.route("/movie", methods=["POST"])
def movie_post():
    sample_receive = request.form['sample_give']
    print(sample_receive)
    return jsonify({'msg':'POST 연결 완료!'})

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