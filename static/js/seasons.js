const seasons = {
    init: function () {
        seasons.addEventListeners();
    },
    addEventListeners() {
        let range = document.querySelector('#season-numbers');
        range.addEventListener('input', function () {
            let number = parseInt(range.value);
            let shows = document.querySelectorAll('.show');
            for (let show of shows) {
                if (parseInt(show.dataset.seasons) < number) {
                    show.classList.add('hidden');
                } else {
                    if (show.classList.contains('hidden')) {
                        show.classList.remove('hidden');
                    }
                }
                }
        })
    }
}

seasons.init();