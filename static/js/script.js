// [Read]
$(document).ready(function () {
    listing();
});

function listing() {
    fetch('/movie').then((res) => res.json()).then((data) => {
        // json 형식으로 변환, 반환된 데이터가 res 인자로 들어옴
        // res.json()에 의해 Promise 객체로 변환되어 data에 저장
        // data 내용 테스트
        console.log(data)

        // data의 내용이 OpenAPI로부터 데이터 받는것과 동일
        // 리스트 형태의 data를 rows 변수에 담고
        let rows = data['result']
        console.log(rows)

        // 반복문 전에 하드코딩 부분 비워주기
        $('#cards-box').empty();
        // forEach 반복문을 통해
        rows.forEach((a) => {
            // 한줄씩 콘솔에 출력(브라우저 콘솔)
            console.log(a)

            // 리스트에 있는 key의 value들을 각 변수에 담기
            let image = a['image']
            let title = a['title']
            let desc = a['desc']
            let star = a['star']
            let comment = a['comment']
            console.log(image, title, desc, star, comment)
            
            // 별점은 value가 숫자로 되어있다. 별모양 이미지가 star숫자만큼 .repeat되는것으로 바꾸자.
            let star_image = '⭐'.repeat(star)

            // index.html에 위 변수들이 들어가도록 백틱 내 자리표시자${variable} 작성한 내용을 temp_html에 작성
            let temp_html = `<div class="col">
                                <div class="card h-100">
                                    <img src="${image}"
                                        class="card-img-top">
                                    <div class="card-body">
                                        <h5 class="card-title">${title}</h5>
                                        <p class="card-text">${desc}</p>
                                        <p>${star_image}</p>
                                        <p class="mycomment">${comment}</p>
                                    </div>
                                </div>
                            </div>`
            // 위 temp_html을 index.html의 #cards-box div에 붙여주기.
            $('#cards-box').append(temp_html)
        });
    })
}

// [Create]
function posting() {
    // index.html로부터 값 가져오기
    let url = $('#url').val()
    let comment = $('#comment').val()
    let star = $('#star').val()

    // formData 객체를 생성하고
    let formData = new FormData();
    // formData.append("sample_give", "샘플데이터");
    // append()통해 {key,value}를 객체에 담는다
    formData.append("url_give", url);
    formData.append("comment_give", comment);
    formData.append("star_give", star);

    // POST 요청에 위 formData를 body에 담아 요청한다.
    fetch('/movie', { method: "POST", body: formData }).then((res) => res.json()).then((data) => {
        // console.log(data)
        alert(data['msg'])
        // 브라우저 새로고침 추가
        window.location.reload()
    })
}

// [Page Event]
function open_box() {
    $('#post-box').show()
}
function close_box() {
    $('#post-box').hide()
}