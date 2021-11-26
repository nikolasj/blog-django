$(function () {
  $(".followMe").click(followMe);
});

function followMe() {
  let button = $(this)
  let data = {
    'user_id': button.data('id')
  }

  $.ajax({
    url: button.data('href'),
    type: 'post',
    data: data,
    success: function (data) {
      console.log(data, "success");
      // $('button#followUnfollow').text(data.status_icon);
      button.text(data.status_icon);
    }
  })
}
