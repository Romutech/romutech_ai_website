// modale
$(document).ready(function() {
    $("#modale_open").click(function() {
        $(".modale").fadeIn();
        $(".message").slideDown();
    });

    $("#modale_close").click(function() {
        $(".message").slideUp();
        $(".modale").fadeOut();
    });
});

