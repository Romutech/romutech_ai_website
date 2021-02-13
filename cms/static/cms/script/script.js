$(document).ready(function() {
  $(window).scroll(function() {
    if ($(this).scrollTop() > 1) {
      $('body').addClass("sticky");
    } else {
      $('body').removeClass("sticky");
    }
  });
  // smooth scroll
  $(".smooth-scroll").click(function() {
    var target = $(this).attr("href"),
      scrollTo = $(target).offset().top,
      headerHeight = $('#Header').outerHeight();
    console.log(headerHeight);
    $('html, body').animate({ scrollTop: scrollTo - headerHeight });
    $('#nav-icon1').trigger("click");
    $("body").removeClass("menu-active");
  });
  //menu icon animation
  $('#nav-icon1').click(function() {
    $(this).toggleClass('open');
    $("body").toggleClass("menu-active");
  });
  //menu link click
});

// modal
$(document).ready(function() {
    $("#modal_open").click(function() {
        $(".modal").fadeIn();
        $(".message").slideDown();
    });

    $("#modal_close").click(function() {
        $(".message").slideUp();
        $(".modal").fadeOut();
    });
});
