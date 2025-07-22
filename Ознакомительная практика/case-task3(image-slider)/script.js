const imagesURI = {
    0:'./public/images/cat-1.jpg',
    1:'./public/images/cat-2.jpg',
    2:'./public/images/turtle.jpg'
}

const slider = document.querySelector('#image-container');

function defaultImageLoader(){
    for(key in imagesURI)
    {
        const image = document.createElement('img');
        image.src=imagesURI[key];
        slider.append(image) 
    }
}
defaultImageLoader();

const prevButton = document.querySelector('#control-left');
const nextButton = document.querySelector('#control-right');
let slideIndex = 0;
const slides = Array.from(slider.querySelectorAll('img'));
const slideCount = slides.length;

prevButton.addEventListener('click', showPreviousSlide);
nextButton.addEventListener('click', showNextSlide);

function showPreviousSlide() {
  slideIndex = (slideIndex - 1 + slideCount) % slideCount;
  updateSlider();
}

function showNextSlide() {
  slideIndex = (slideIndex + 1) % slideCount;
  updateSlider();
}

function updateSlider() {
  slides.forEach((slide, index) => {
    if (index === slideIndex) {
      slide.style.display = 'block';
    } else {
      slide.style.display = 'none';
    }
  });
}
updateSlider();