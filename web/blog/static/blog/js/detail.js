$(function () {
  console.log("comment");
  $('#formReview').submit(comment);
});

function comment(e) {
  e.preventDefault();
  let form = $(this);
  // console.log("comment2", form.serializeArray());
  // var formdata = form.serializeArray();
  // var data = {};
  // $(formdata ).each(function(index, obj){
  //   data[obj.name] = obj.value;
  // });
  // let data_ = JSON.stringify(data);
  let data_ = form.serialize();
  console.log("data", data_);
  $.ajax({
    url: form.attr('action'),
    type: form.attr('method'),
    data: data_,
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
