$(function () {
    $('#fileUpload').on('change', changeAvatar);
    $('#changePasswordForm').submit(passwordChange);
    $('#registrationForm ').submit(profileUpdate);
    $('#followersButton').click(followers);
    $('#followingButton').click(following);
  }
)


function followers(e) {
  let button = $(this)
  console.log(button.data('href'))
   $.ajax({
    type: 'GET',
    url: button.data('href'),
    success: function (data) {
        renderModal(data, button)
        $('#followerModal').modal('show');
    },
    error: function (data) {
      console.log('error', data)
    }
  })
}

function following(e) {
  let button = $(this);
  // $('#followingModal').modal('show');
  console.log('following api');
  $.ajax({
    type: 'GET',
    url: button.data('href'),
    success: function (data) {
        renderModal(data, button)
        $('#followerModal').modal('show');
    },
    error: function (data) {
      console.log('error', data)
    }
  })
}

function renderModal(data, button) {
  $('#followModalTitle').text(button.text())
  followBodyRender(data, button)

}

function followBodyRender(data, button) {
  user_list = data.results
  let body = $('#followModalBody')
  let followUrl = button.data('follow-actions')

  body.empty()
  $.each(user_list, function(i){
   let isShowFollowButton = !!user_list[i].follow
   console.log(isShowFollowButton)
   var templateString = `
      <div class="user">
        <p>
          <img src="${user_list[i].avatar}" class="avatar img-circle img-thumbnail" width=50px>
          <a href='${user_list[i].profile_url}'> ${user_list[i].full_name} </a>
          ${isShowFollowButton ? `
            <button class="btn btn-primary followMe" data-id="${user_list[i].id}" data-href='${followUrl}'> ${user_list[i].follow} </button>
          ` : ''}
        </p>
      </div>
   `
   body.append(templateString);
  })
   $(".followMe").click(followMe);

}

function profileUpdate(e) {
  e.preventDefault();
  console.log('click')
  let form = $(this);
  let path = form.attr('action')
  console.log(path)
  let data = form.serialize()
  console.log(data)


  $.ajax({
    url: path,
    type: 'put',
    data: data,
    success: function (data) {
      console.log('success', data)
//    location.reload()
    },
    error: function (data) {
      console.log('error', data)
      $("#profileGroup").addClass("has-error");
      $("#profileGroup").append(
        '<div class="help-block">' + data.responseJSON.profile + "</div>"
      );
    }
  })


}


function passwordChange(event) {
  event.preventDefault();
  console.log('click')
  let form = $(this);
  let path = form.attr('action')
  console.log(path)
  let data = form.serialize()
  console.log(data)

  $.ajax({
    url: path,
    type: 'post',
    data: data,
    success: function (data) {
//    location.reload()
      $('#passwordChangeSuccess').append(
        '<h3>' + data.detail + '</h3>'
      )

    },
    error: function (data) {
      console.log('error', data)
      let groups = ['#oldPasswordGroup', '#newPassword1Group', '#newPassword2Group']
      for (let group of groups) {
        $(group).removeClass('has-error')
      }
      $('.help-block').remove()
      if (data.responseJSON.old_password) {
        $('#oldPasswordGroup').addClass('has-error')
        $('#oldPasswordGroup').append(
          "<div class='help-block'>" + data.responseJSON.old_password + "</div>"
        )
      }

      if (data.responseJSON.new_password1) {
        $('#newPassword1Group').addClass('has-error')
        $('#newPassword1Group').append(
          "<div class='help-block'>" + data.responseJSON.new_password1 + "</div>"
        )
      }

      if (data.responseJSON.new_password2) {
        $('#newPassword2Group').addClass('has-error')
        $('#newPassword2Group').append(
          "<div class='help-block'>" + data.responseJSON.new_password2 + "</div>"
        )
      }
    }


  })
}


function changeAvatar(e) {
  e.preventDefault();
  console.log('ddd')
  let form = $(this)
  path = form.data('href')
  console.log(path)
  let data = new FormData()
  let file = form[0].files
  console.log(file)
  data.append('image', file[0])

  $.ajax({
    url: path,
    type: 'post',
    data: data,
    contentType: false,
    processData: false,
    success: function (data) {
      $('#user_avatar').attr('src', data.image)
    },
    error: function (data) {
      console.log('error', data)
    }

  })
}
