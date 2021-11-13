$(function(){
$('#fileUpload').on('change', changeAvatar);
$('#changePasswordForm').submit(passwordChange);
$('#registrationForm ').submit(profileUpdate)
}
)


function profileUpdate(e){
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
    success: function(data){
    console.log('success', data)
//    location.reload()
    },
    error: function(data){
    console.log('error', data)
    $("#profileGroup").addClass("has-error");
      $("#profileGroup").append(
        '<div class="help-block">' + data.responseJSON.profile + "</div>"
      );
    }
    })


}


function passwordChange(event){
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
    success: function(data){
//    location.reload()
    $('#passwordChangeSuccess').append(
    '<h3>' + data.detail + '</h3>'
    )

    },
    error: function(data){
    console.log('error', data)
    let groups = ['#oldPasswordGroup', '#newPassword1Group', '#newPassword2Group']
    for (let group of groups){
    $(group).removeClass('has-error')
    }
    $('.help-block').remove()
      if ( data.responseJSON.old_password ){
         $('#oldPasswordGroup').addClass('has-error')
         $('#oldPasswordGroup').append(
         "<div class='help-block'>"+ data.responseJSON.old_password +"</div>"
      )}

      if ( data.responseJSON.new_password1 ){
         $('#newPassword1Group').addClass('has-error')
         $('#newPassword1Group').append(
         "<div class='help-block'>"+ data.responseJSON.new_password1 +"</div>"
      )}

      if ( data.responseJSON.new_password2 ){
         $('#newPassword2Group').addClass('has-error')
         $('#newPassword2Group').append(
         "<div class='help-block'>"+ data.responseJSON.new_password2 +"</div>"
      )}
    }


    })
}



function changeAvatar(e){
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
   success: function(data){
   $('#user_avatar').attr('src', data.image)
   },
   error: function(data){
   console.log('error', data)
   }

   })
}
