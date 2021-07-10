$(function () {
  // $(document).on("click", "a.login", login);
  $('#loginForm').submit(login);
  $('#forgotPasswordForm').submit(passwordReset);
});

function login(e) {
  let form = $(this);
  e.preventDefault();
  $.ajax({
    url: form.attr("action"),
    type: "POST",
    dataType: 'json',
    data: form.serialize(),
    contentType: false,
    processData: false,
    success: function (data) {
      location.reload();
    },
    error: function (data) {
      $("#emailGroup").addClass("has-error");
      $("#passwordGroup").addClass("has-error");
      $(".help-block").remove()
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
      $(".help-block").remove()
      $("#passwordGroup").append(
        '<div class="help-block">' + data.responseJSON.email + "</div>"
      );

    }
  })
}
