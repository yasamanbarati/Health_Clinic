$(document).ready(function(){
    $(".main-slider").owlCarousel({
        items:1,
        loop:true,
        rtl: true,
        autoplay: true,
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
    })  
    $(".our-team-slder").owlCarousel({
        dots:true,
        loop:true,
        rtl: true,
        margin: 50,
        autoplay: false,
        autoplayTimeout: 4000,
        autoplaySpeed: 1000,
        autoplayHoverPause: true,
        responsive:{
            0:{
                items:1,
            },
            400:{
                items:2,
            },
            600:{
                items:3,
            },
            1200:{
                items:4,
            },
        },
    }); 
});