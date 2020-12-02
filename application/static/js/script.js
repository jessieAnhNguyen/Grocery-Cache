$('#menu-toggler').click(function (e) {
    console.log('clicked');
    e.preventDefault();

    $('#wrapper').toggleClass('menuDisplayed');
});

$(window).on('load',function(){
   
    $('#registerModal').modal('show');
    $('#loginModal').modal('show');
});



console.log('wtf')

