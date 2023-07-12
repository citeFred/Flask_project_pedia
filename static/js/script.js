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
    let formData = new FormData();
    formData.append("sample_give", "샘플데이터");

    fetch('/movie', { method: "POST", body: formData }).then((res) => res.json()).then((data) => {
        console.log(data)
        alert(data['msg'])
    })
}

// [Page Event]
function open_box() {
    $('#post-box').show()
}
function close_box() {
    $('#post-box').hide()
}