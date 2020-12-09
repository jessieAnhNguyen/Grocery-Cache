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

    if($('#categoryOptions').length>0){
        $("#categoryOptions option").each(function()
            {
                var toChange = $(this).text();
                var toReplaceWith = toChange.split(":")[1];
                $(this).text(toReplaceWith);
                // Add $(this).val() to your list
            });
    }
});




