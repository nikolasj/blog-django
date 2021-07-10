console.log('feedback');
$(function () {
  $('#feedbackForm').submit(feedback);
});

$('input:file').change(
  function (e) {
    var files = e.originalEvent.target.files;

    var n = files[0].name, s = files[0].size, t = files[0].type;

    if (s > 400000) {
      console.log('Please deselect this file: "' + n + '," it\'s larger than the maximum filesize allowed. Sorry!');
      alert('Please deselect this file: "' + n + '," it\'s larger than the maximum filesize allowed. Sorry!');
      // submitEvent.preventDefault();
      $("#file").val("");
    }
    var fileExtension = ['jpeg', 'jpg', 'png', 'gif', 'bmp'];
    if ($.inArray($(this).val().split('.').pop().toLowerCase(), fileExtension) == -1) {
      alert("Only formats are allowed : " + fileExtension.join(', '));
      $("#file").val("");
    }

  });

function feedback(e) {
  let form = $(this);
  e.preventDefault();
  let formData = new FormData(form[0]);
  $.ajax({
    url: form.attr('action'),
    type: form.attr('method'),
    data: formData,
    contentType: false,
    processData: false,
    success: function (data) {
      console.log("SUCCESS", data);
      // let url = form.data('success');
      // window.location.href = url;
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
  let list = ['#emailGroup', '#nameGroup', '#contentGroup', '#fileGroup'];
  for (let group of list) {
    $(group).removeClass(class_name_for_error);
  }
  if (data.responseJSON.email) {
    set_block_error("#emailGroup", data.responseJSON.email);
  }
  if (data.responseJSON.name) {
    set_block_error("#nameGroup", data.responseJSON.name);
  }
  if (data.responseJSON.content) {
    set_block_error("#contentGroup", data.responseJSON.content);
  }
  if (data.responseJSON.file) {
    set_block_error("#fileGroup", data.responseJSON.file);
  }
}

function set_block_error(group, data) {
  $(group).addClass(class_name_for_error);
  $(group).append('<div class="help-block">' + data + '</div>');
}
