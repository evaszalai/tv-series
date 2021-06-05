const colors = {
    init: function () {
        colors.addEventListenersToCards();
    },
    addEventListenersToCards: function () {
        let cards = document.querySelectorAll('.show');
        for (let card of cards) {
            if (parseInt(card.children[2].innerHTML) % 2 === 1) {
                card.addEventListener('dblclick', function (e) {
                    e.currentTarget.classList.toggle('green');
                })
            }
            else {
                card.addEventListener('dblclick', function (e) {
                    e.currentTarget.classList.toggle('blue');
                })
            }
        }
    }
}

colors.init();