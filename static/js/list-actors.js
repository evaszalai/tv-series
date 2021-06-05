const life = {
    init: function () {
        life.addEventListenersToLiveCards();
        life.addEventListenersToDeadCards();
    },
    addEventListenersToLiveCards: function () {
        let live_cards = document.querySelectorAll("[data-alive='alive']")
        console.log(live_cards);
        live_cards.forEach((card) => {
            card.addEventListener('mouseover', life.turnGreen);
            card.addEventListener('mouseout', life.removeGreen);
        })
    },
    addEventListenersToDeadCards: function () {
        let dead_cards = document.querySelectorAll('[data-alive="dead"]')
        dead_cards.forEach((card) => {
            card.addEventListener('mouseover', life.turnDark);
            card.addEventListener('mouseout', life.removeDark);
        })
    },
    turnGreen: function (e) {
        e.currentTarget.classList.add('green');
    },
    removeGreen: function (e) {
        e.currentTarget.classList.remove('green');
    },
    turnDark: function (e) {
        e.currentTarget.classList.add('dead-card');
    },
    removeDark: function (e) {
        e.currentTarget.classList.remove('dead-card');
    }
}

life.init();