//Реализую через обьект потому что на практике ссылки на картинки получаем с сервера.
const imagesURI = {
    0:'./public/images/cat-1.jpg',
    1:'./public/images/cat-2.jpg',
    2:'./public/images/turtle.jpg'
}

let activeImage = 0;

const controls = [document.getElementById('control-left'),document.getElementById('control-right')];

controls.forEach(control=>{
    control.addEventListener("click",(event)=>{
        event.target.id === 'control-left' ? changeActiveImage(-1) : changeActiveImage(1);
    })
})

function changeActiveImage(value)
{
    if(value === -1)
    {
        if(activeImage > 0)
        {
            activeImage--;
        }
        else
        {
            activeImage = Object.keys(imagesURI).length - 1
        }
    }

    if(value === 1)
    {
        if(activeImage < Object.keys(imagesURI).length - 1)
        {
            activeImage++;
        }
        else{
            activeImage = 0;
        }
        
    }
    drawActiveImage();
}

function drawActiveImage()
{
    console.log(activeImage)
    if(document.getElementById('current-image'))
    {
        const currentImage = document.getElementById('current-image')
        currentImage.src= imagesURI[activeImage];
    }
    if(!document.getElementById('current-image')){
        let image = document.createElement('img');
        image.src=imagesURI[activeImage];
        image.id='current-image';
        document.getElementById('image-container').appendChild(image);
    }
    document.getElementById('image-counter').innerText = `${activeImage + 1} из ${Object.keys(imagesURI).length}`
}

drawActiveImage();