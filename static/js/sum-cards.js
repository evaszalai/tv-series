const cards = {
    init: function() {
        cards.addEventListenersToCards();
    },
    addEventListenersToCards: function () {
        let cards = document.querySelectorAll('.small-card');
        cards.forEach( (card) =>
            card.addEventListener('click', function() {
                let container = document.querySelector('#container');
                let section = document.querySelector('section');
                let calculation = document.querySelector('#calculation');
                if (section.contains(calculation)) {
                    calculation.remove();
                }
                card.classList.add('selected');
                let selected = document.querySelectorAll('.selected')
                let sum = 0;
                for (let item of selected) {
                    sum += parseFloat(item.children[1].innerHTML);
                }
                let average = sum / selected.length;
                calculation = `<p id="calculation">The average rating of shows in selected years is ${average}.</p>`;
                container.insertAdjacentHTML('beforebegin', calculation);
            })
        )
    },
}

cards.init()