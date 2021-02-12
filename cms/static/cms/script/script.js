// Pop up
$(function(){
    $(".popup-light").click(function() {
        var obj = $(this),
            popupClass = obj.data("popupClass"),
            popupWidth = obj.data("popupWidth"),
            objPopup =  $('.' + popupClass);

        objPopup
            .css("width", popupWidth)
            .prepend('<img src="static/cms/images/close.png" class="popup-btn-close" title="Close Window" alt="Close" />')
            .css({
                "margin-top":  -objPopup.outerHeight(true)/2,
                "margin-left": -objPopup.outerWidth(true)/2
            })
            .fadeIn();

        return false;
    });

    $("body").delegate(".popup-btn-close", "click", function(){
        $('.popup-block').fadeOut(function(){
            $(".popup-btn-close").remove();
        });

        return false;
    });
});
