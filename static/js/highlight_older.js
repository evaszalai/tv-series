const highlight = {
    init: function () {
        window.onload = function () {
            let oldCards = document.querySelectorAll('[data-older="True"]');
            console.log(oldCards);
            oldCards.forEach((card) => {
                card.classList.add('yellow');
            })
            //highlight.addEventListenersToCards();
        }
    }
}

highlight.init();