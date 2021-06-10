console.log('sing-up');
$(function () {
  $('#signUpForm').submit(singUp);
});

function singUp(e) {
  let form = $(this);
  e.preventDefault();
  $.ajax({
    url: form.attr('action'),
    type: form.attr('method'),
    data: form.serialize(),
    success: function (data) {
      console.log("SUCCESS", data);
      let url = form.data('success');
      window.location.href = url;
    },
    error: function (data) {
      errorProcess(data)
    }
  })
  console.log('here')
}

const class_name_for_error = 'has-error';

function errorProcess(data) {
  $(".help-block").remove();
  let list = ['#emailGroup', '#password1Group', '#password2Group', '#firstNameGroup', '#lastNameGroup'];
  for (let group of list) {
    $(group).removeClass(class_name_for_error);
  }

  if (data.responseJSON.email) {
    set_block_error("#emailGroup", data.responseJSON.email);
  }
  if (data.responseJSON.password1) {
    set_block_error("#password1Group", data.responseJSON.password1);
  }
  if (data.responseJSON.password2) {
    set_block_error("#password2Group", data.responseJSON.password2);
  }
  if (data.responseJSON.first_name) {
    set_block_error("#firstNameGroup", data.responseJSON.first_name);
  }
  if (data.responseJSON.last_name) {
    set_block_error("#lastNameGroup", data.responseJSON.last_name);
  }
}

function set_block_error(group, data) {
  $(group).addClass(class_name_for_error);
  $(group).append('<div class="help-block">' + data + '</div>');
}
