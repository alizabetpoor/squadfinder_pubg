$(document).ready(function(){
    $("#menu-toggle").click(function(){
        if ($(".menu").css("display") == "none"){
            $(".menu").removeClass("d-none")
            $(".menu").removeClass("d-sm-flex")
            $(".menu").css("display","none")
            $(".menu").slideDown(300);
        }
        else{
            $(".menu").slideUp(300);
            setTimeout(function(){
                $(".menu").addClass("d-none")
                $(".menu").addClass("d-sm-flex")
            },300)
           
        }

    })
    $("#close-notif").click(function(){
        setTimeout(function(){
            $(".main-notification").removeClass("d-flex")
        },300)
        $(".main-notification").slideUp(300);
    })
})