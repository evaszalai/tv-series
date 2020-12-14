const highlight = {
    init: function () {
        window.onload = function () {
            let oldCards = document.querySelectorAll('[data-older="True"]');
            console.log(oldCards);
            oldCards.forEach((card) => {
                card.classList.add('yellow');
            });
        }
        highlight.addEventListenersToCards();
    },

    addEventListenersToCards: function () {
        let cards = document.querySelectorAll('.card');
        cards.forEach((card) => {
            card.addEventListener('click', function () {
                alert(`${card.dataset.actor}, ${card.dataset.show}`);
            })
        })
    }
}

highlight.init();