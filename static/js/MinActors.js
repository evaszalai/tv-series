const minActors = {
    init: function () {
        minActors.addEventListeners();
    },
    addEventListeners: function () {
        let titles = document.querySelectorAll('.show-title');
        titles.forEach((title) =>
        title.addEventListener('mouseover', minActors.showActors));
    },
    showActors(e) {
        let showTitle = e.currentTarget.id;
        let modal = document.querySelector('#modal');
        let span = document.getElementsByClassName("close")[0];
        span.onclick = function() {
            modal.classList.add('hidden');
        }
        modal.classList.remove('hidden');
        fetch(`/min-actors/${showTitle}`, {
            method: 'GET',
            credentials: 'same-origin'
        })
            .then(response => response.json())  // parse the response as JSON
            .then(json_response => minActors.fillTable(json_response));  // Call the `callback` with the returned object
    },
    fillTable(actors) {
        let tableBody = document.querySelector('#modal-table');
        tableBody.innerHTML = '';
        for (let actor of actors) {
            let tableRow = `
        <tr>
            <td>${actor['name']}</td>
            <td>${actor['birthday']}</td>
            <td>${actor['death']}</td>
            <td>${actor['biography']}</td>`;
            tableBody.insertAdjacentHTML('afterbegin', tableRow);
        }
    }
}

minActors.init();