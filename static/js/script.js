// [Read]
$(document).ready(function () {
    listing();
});

function listing() {
    fetch('/movie').then((res) => res.json()).then((data) => {
        console.log(data)
        alert(data['msg'])
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