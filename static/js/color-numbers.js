const colors = {
    init: function () {
        colors.addEventListenersToCards();
    },
    addEventListenersToCards: function () {
        let cards = document.querySelectorAll('.card');
        for (let card of cards) {
            if (parseInt(card.children[0].innerHTML) % 2 === 1) {
                card.addEventListener('dblclick', function (e) {
                    e.currentTarget.classList.add('green');
                })
            }
            else {
                card.addEventListener('dblclick', function (e) {
                    e.currentTarget.classList.add('blue');
                })
            }
        }
    }
}

colors.init();