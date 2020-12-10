const stars = {
    init: function () {
        stars.addEventListenersToStars();
    },
    addEventListenersToStars: function () {
        let starList = document.getElementsByClassName("fa-star");
        for (let star of starList) {
            console.log(star.id);
            star.addEventListener('mouseover', stars.fillStars);
        }
    },
    fillStars: function(e) {
        e.currentTarget.classList.remove('gold');
        console.log(e.currentTarget.left);
        e.currentTarget.left.classList.add('icon-star');
        e.currentTarget.right.classList.add('icon-star-empty');
    }
}

stars.init();