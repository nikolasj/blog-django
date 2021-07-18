$(function () {
  console.log("comment");
  $('#commentForm').submit(comment);
});

function comment(e) {
  let form = $(this);
  e.preventDefault();
  console.log("comment", form.serializeArray());
  var formdata = form.serializeArray();
  var data = {};
  $(formdata ).each(function(index, obj){
    data[obj.name] = obj.value;
  });
  let data_ = JSON.stringify(data);
  console.log("data", data_);
  $.ajax({
    url: form.attr('action'),
    type: form.attr('method'),
    contentType: 'application/json; charset=utf-8',
    data: data_,
    dataType: 'json',
    success: function (data) {
      console.log("SUCCESS", data);
      location.reload();

    },
    error: function (data) {
      console.log("ERROR", data);
    }
  })
}

function addParentToComment(email, id) {
  console.log("parent", id);
  $('#commentParent').attr("value", id);
  $('#textComment').text(email + ", ");
}

console.log('blog-detail');
