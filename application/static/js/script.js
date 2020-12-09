$('#menu-toggler').click(function (e) {
    console.log('clicked');
    e.preventDefault();

    $('#wrapper').toggleClass('menuDisplayed');
});

$(window).on('load',function(){
   
    $('#registerModal').modal('show');
    $('#loginModal').modal('show');

    if($('#invalidForm').length>0){
        $('#staticBackdrop').modal('show');
    }else{
        $('#staticBackdrop').modal('hide');
    }
});




