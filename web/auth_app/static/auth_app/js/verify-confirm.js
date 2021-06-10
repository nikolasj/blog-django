function verifyConfirm() {
  console.log('click verify');
  let url = window.location.pathname;
  let key_ = url.split('/')[3];
  let data = {'key': key_};
  console.log(data);
  let api_url = $('#verifyConfirm').data('href');
  console.log(api_url);
  $.ajax({
    url: api_url,
    type: "post",
    data: data,
    success: function (data) {
      console.log("SUCCESS", data);
      url = $('#singIn').data('href');
      window.location.href = url;
    },
    error: function (data) {
      console.log("ERROR", data);
      $('#ifErrors').append('<h2>Your url is not valid</h2>');
    }
  })
}
