$('#menu-toggler').click(function (e) {
    console.log('clicked');
    e.preventDefault();

    $('#wrapper').toggleClass('menuDisplayed');
});

console.log('wtf')

