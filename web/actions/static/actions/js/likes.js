// $(function () {
//   console.log("like-article");
//   $('#like-article').click(addVote);
//   $('#dislike-article').click(addVote);
//   $('.commentLike').click(addCommentVote);
// });

$(function () {
  console.log("like-article");
  $('#likeArticle').click(articleLikeRequest);
  $('#dislikeArticle').click(articleLikeRequest);
  $('.commentLike').click(commentLike);
});

function articleLikeRequest(e) {
  let like = $(this);
  let data = {
    'object_id': like.data('id'),
    'model': like.data('type'),
    'vote': like.data('vote'),
  }
  $.ajax({
    url: like.data('href'),
    type: 'post',
    data: data,
    success: function (data) {
      $('#articleLikeCount').text(' ' + data.count_like)
      $('#articleDislikeCount').text(' ' + data.count_dislike)
      switch (data.status) {
        case 'liked':
          liked_style();
          break
        case 'disliked':
          dislike_status()
          break
        default:
          default_status()
          break
      }
    },
    error: function (data) {
      console.log(data, "Error")
    }
  })
}

function liked_style() {
  $('#articleLikeIcon').removeClass('far', 'fa-thumbs-up')
  $('#articleLikeIcon').addClass('fas', 'fa-thumbs-up')

  $('#articleDislikeIcon').addClass('far', 'fa-thumbs-down')
  $('#articleDislikeIcon').removeClass('fas', 'fa-thumbs-down')
}

function dislike_status() {
  $('#articleLikeIcon').removeClass('fas', 'fa-thumbs-up')
  $('#articleLikeIcon').addClass('far', 'fa-thumbs-up')

  $('#articleDislikeIcon').addClass('fas', 'fa-thumbs-down')
  $('#articleDislikeIcon').removeClass('far', 'fa-thumbs-down')

}

function default_status() {
  $('#articleLikeIcon').removeClass('fas', 'fa-thumbs-up')
  $('#articleLikeIcon').addClass('far', 'fa-thumbs-up')

  $('#articleDislikeIcon').removeClass('fas', 'fa-thumbs-down')
  $('#articleDislikeIcon').addClass('far', 'fa-thumbs-down')
}


function commentLike(e) {
  e.preventDefault()
  console.log('like')
  let like = $(this);
  let data = {
    'object_id': like.data('id'),
    'model': like.data('type'),
    'vote': like.data('vote'),
  }
  console.log(data)
  $.ajax({
    url: like.data('href'),
    type: 'post',
    data: data,
    success: function (data) {
      console.log(data, "success")

    },
    error: function (data) {
      console.log(data, "Error")
    }
  })
}

//
// function addCommentVote() {
//   let button = $(this);
//   console.log(button.data("id"))
//   let data = {
//     model: button.data("type"),
//     object_id: button.data("id"),
//     vote: button.data("vote")
//   }
//
//   $.ajax({
//     url: button.data('href'),
//     type: "post",
//     data: data,
//     success: function (data) {
//       console.log("SUCCESS", data);
//       // $('.commentLike').css('color', 'red');
//
//     },
//     error: function (data) {
//       console.log("ERROR", data);
//     }
//   })
// }
//
// function addVote() {
//
//   let button = $(this);
//   console.log("button", button);
//   let data = {
//     model: button.data("type"),
//     object_id: button.data("id"),
//     vote: button.data("vote")
//   }
//
//   $.ajax({
//     url: button.data('href'),
//     type: "post",
//     data: data,
//     success: function (data) {
//       console.log("SUCCESS", data);
//       $('#like-article').text(`like (${data.count_like})`)
//       $('#dislike-article').text(`dislike (${data.count_dislike})`)
//     },
//     error: function (data) {
//       console.log("ERROR", data);
//     }
//   })
// }
