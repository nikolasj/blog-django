console.log('feedback');
$(function () {
  $('#commentForm').submit(comment);
});

function comment(e) {
  let form = $(this);
  e.preventDefault();
  $.ajax({
    url: form.attr('action'),
    type: form.attr('method'),
    data: form.serialize(),
    contentType: false,
    processData: false,
    success: function (data) {
      console.log("SUCCESS", data);
      // let url = form.data('success');
      // window.location.href = url;
    },
    error: function (data) {
      console.log("ERROR", data);
    }
  })
}


console.log('blog-detail')
