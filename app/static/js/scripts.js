import Swiper from "swiper";

document.addEventListener("DOMContentLoaded", () => {
  const swiperEl = document.querySelector("swiper-container");

  const params = {
    autoplay: {
      enabled: true,
      delay: 1000,
    },
    centeredSlides: false,
    slidesPerView: 1,
    keyboard: {
      enabled: true,
    },
    breakpoints: {
      768: {
        slidesPerView: 3,
        slidesPerGroup: 3,
      },
      1024: {
        slidesPerView: 5,
        slidesPerGroup: 5,
      },
    },
    pagination: {
      clickable: true,
    },
  };

  new Swiper(swiperEl, params);
});
