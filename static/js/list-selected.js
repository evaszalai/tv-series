const listSelected = {
    init: function () {
        listSelected.addEventListeners();
    },
    addEventListeners: function () {
        let cards = document.querySelectorAll('.item');
        cards.forEach((card) => function (card) {
        card.addEventListener('mouseover', listSelected.displayOverview);
        card.addEventListener('mouseout', listSelected.hideOverview);})
    },
    displayOverview(e) {
        let overview = e.currentTarget.children[0];
        overview.classList.remove('hidden');
    },
    hideOverview(e) {
        let overview = e.currentTarget.children[0];
        overview.classList.add('hidden');
    }
}

listSelected.init();