$(function () {
  // $(document).on("click", "a.login", login);
  $('#loginForm').submit(login);
  $('#forgotPasswordForm').submit(passwordReset);
});

function login(e) {
  let form = $(this);
  e.preventDefault();
  // let d_ = form.ser*ialize();
  // var data = form.serialize().split("&");
  // console.log(data);
  // var obj={};
  // for(var key in data)
  // {
  //       console.log(data[key]);
  //       obj[data[key].split("=")[0]] = data[key].split("=")[1];
  // }
  // console.log(obj);
  var formdata = form.serializeArray();
  var data = {};
  $(formdata ).each(function(index, obj){
    data[obj.name] = obj.value;
  });
  // console.log(data);
  let d_ = JSON.stringify(data);
  // console.log("login", d_);
  $.ajax({
    url: form.attr("action"),
    type: "POST",
    contentType: 'application/json; charset=utf-8',
    dataType: 'json',
    data: d_,
    success: function (data) {
      location.reload();
    },
    error: function (data) {
      console.log("ERROR", data);
      $("#emailGroup").addClass("has-error");
      $("#passwordGroup").addClass("has-error");
      $(".help-block").remove();
      $("#passwordGroup").append(
        '<div class="help-block">' + data.responseJSON.email + "</div>"
      );

    }
  })
}

function passwordReset(e) {
  let form = $(this);
  e.preventDefault();
  $.ajax({
    url: form.attr("action"),
    type: "POST",
    dataType: 'json',
    data: form.serialize(),
    success: function (data) {
      let url_ = $("#successPassReset").data('href');
      window.location.href = url_;
    },
    error: function (data) {
      $("#emailGroup").addClass("has-error");
      $("#passwordGroup").addClass("has-error");
      $(".help-block").remove();
      $("#passwordGroup").append(
        '<div class="help-block">' + data.responseJSON.email + "</div>"
      );

    }
  })
}
