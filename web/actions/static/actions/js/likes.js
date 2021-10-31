$(function () {
  console.log("like-article");
  $('#like-article').click(addVote);
  $('#dislike-article').click(addVote);
  $('.commentLike').click(addCommentVote);
});

function addCommentVote() {
  let button = $(this);
  console.log(button.data("id"))
  let data = {
    model: button.data("type"),
    object_id: button.data("id"),
    vote: button.data("vote")
  }

  $.ajax({
    url: button.data('href'),
    type: "post",
    data: data,
    success: function (data) {
      console.log("SUCCESS", data);

    },
    error: function (data) {
      console.log("ERROR", data);
    }
  })
}

function addVote() {

  let button = $(this);
  console.log("button", button);
  let data = {
    model: button.data("type"),
    object_id: button.data("id"),
    vote: button.data("vote")
  }

  $.ajax({
    url: button.data('href'),
    type: "post",
    data: data,
    success: function (data) {
      console.log("SUCCESS", data);
      $('#like-article').text(`like (${data.count_like})`)
      $('#dislike-article').text(`dislike (${data.count_dislike})`)
    },
    error: function (data) {
      console.log("ERROR", data);
    }
  })
}
