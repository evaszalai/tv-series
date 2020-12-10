function init (){
    animation.medalsListener();
}

let animation = {
    medalsListener: function () {
        let medals = document.querySelectorAll('.medal');
        console.log(medals);
        medals.forEach((item) => {
            item.addEventListener('click', animation.grow);
            console.log(item);
        })
    },
    grow: function () {
        let span = this;
        console.log(span.innerHTML);
        let size = 8;
        let timer = setInterval(function () {
            size += 2;
            span.style.fontSize = `${size}pt`;
        }, 100);
        setTimeout(function () {
            clearInterval(timer);
            span.style.fontSize = '12pt';
        }, 2000);

    }
}

init();
