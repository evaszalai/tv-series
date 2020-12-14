const longest = {
    init: function(){
        longest.addEventListeners();
    },
    addEventListeners: function() {
        let submitButton = document.querySelector('#submit');
        submitButton.addEventListener('click', longest.getLongestByGenre);
    },

    getLongestByGenre: function () {
        let selectedOption = document.querySelector('#genres').value
        fetch(`/longest/${selectedOption}`, {
            method: 'GET',
            credentials: "same-origin"
        })
            .then(response => response.json())
            .then(jsonResponse => longest.listShows(jsonResponse))
    },
    listShows(shows) {
        let table = document.querySelector('#shows');
        table.classList.remove('hidden');
        let tableBody = document.querySelector('tbody');
        tableBody.innerHTML=''
        for (let show of shows) {
            let row = `
                <tr>
                <td>${show['title']}</td>
                <td>${show['number_of_seasons']}</td>
                <td>${show['number_of_episodes']}</td>
                </tr>`
            tableBody.insertAdjacentHTML('afterbegin', row);
        }
    }
}

longest.init();