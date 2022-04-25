$(document).ready(function(){
    $(".main-slider").owlCarousel({
        items:1,
        loop:true,
        rtl: true,
        autoplay: false,
        autoplayTimeout: 4000,
        autoplaySpeed: 1000,
        autoplayHoverPause: true,
        responsive:{
            0:{
                items:1,
            },
            600:{
                items:1,
            },
            1200:{
                items:1,
            },
        },
        dots:true,
        nav:true,
    });  
});