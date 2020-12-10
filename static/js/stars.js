const stars = {
    init: function () {
        stars.addEventListenersToStars();
    },
    _goldStars: 0,
    addEventListenersToStars: function () {
        let starList = document.querySelectorAll('.fa-star');
        console.log(starList);
        for (let star of starList) {
            console.log(star);
            star.addEventListener('mouseover', stars.fillStars);
            star.addEventListener('mouseleave', stars.restoreStars);
        }
    },
    fillStars: function(e) {
        stars._goldStars = e.currentTarget.parentNode.querySelectorAll('.gold').length;
        let starRow = e.currentTarget.parentNode.children
        for (let star of starRow) {
            star.classList.remove('gold');
        }
        for (let star of starRow) {
            star.classList.add('gold');
            if (star === e.currentTarget) {
                break;
            }
        }
    },
    restoreStars: function(e) {
        let starRow = e.currentTarget.parentNode.children
        for (let star of starRow) {
            star.classList.remove('gold');
        }
        for (let i=0; i<stars._goldStars; i++) {
            starRow[i].classList.add('gold');
        }

    }
}

stars.init();