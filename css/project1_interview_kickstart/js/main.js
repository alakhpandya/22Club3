$('.owl-carousel').owlCarousel({
    loop:true,
    margin:10,
    nav:true,
    dots:false,
    // navText: ['<i class="fa-solid fa-chevron-left"></i>','<i class="fa-solid fa-chevron-right"></i>'],
    navText: [$('.owl-nav-prev'), $('.owl-nav-next')],
    responsive:{
        0:{
            items:1
        },
        600:{
            items:3
        }
        // 1000:{
        //     items:5
        // }
    }
})