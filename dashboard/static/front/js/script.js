
$("#amit2").owlCarousel({
    items: 4,
    margin: 15,
    ltr: true,
    nav: true,
    dots: false,
    slideTransition: "linear",
    autoplay: true,
    loop: true,
    center: false,
    autoplayTimeout: 3000,
    autoplaySpeed: 8000,
    autoplayHoverPause: false,
    autoHeight: true,
    smartSpeed: 2000,
    responsive: {
        0: {
            items: 1
        },
        520: {
            items: 2
        },
        768: {
            items: 2
        },
        1200: {
            items: 3
        },
        1400: {
            items: 3
        },
        1600: {
            items: 3
        },
    },
});
