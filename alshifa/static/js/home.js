function myMenuFunction() {
    var i = document.getElementById("navMenu");
    if (i.className === "navMenu") {
        i.className += " responsive";
    }
    else {
        i.className = "navMenu";
    }
}


// Swiper js

        var swiper = new Swiper(".mySwiperServices", {
            slidesPerView: 1,
            spaceBetween: 10,
            pagination: {
                el: ".swiper-pagination",
                clickable: true,
            },
             navigation: {
                nextEl: ".swiper-button-next",
                prevEl: ".swiper-button-prev",
            },
            breakpoints: {
                640: {
                    slidesPerView: 2,
                    spaceBetween: 20,
                },
                768: {
                    slidesPerView: 2,
                    spaceBetween: 30,
                },
                792:{
                    slidesPerView: 3,
                    spaceBetween: 10,
                },
              
                1024: {
                    slidesPerView: 3,
                    spaceBetween: 10,
                },
            },
        });
    
