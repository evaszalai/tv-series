const characters = {
    init: function () {
        characters.addEventListeners();
    },
    addEventListeners() {
        let submitButton = document.querySelector('#submit');
        submitButton.addEventListener('click', characters.getCharactersList);
    },
    getCharactersList: function () {
        let searchString = document.querySelector('#search').value;
        let characterTable = document.querySelector('#characters');
        characterTable.classList.remove('hidden');
        let searchArray = searchString.split(' ');
        let queryString = `%${searchArray.join('%')}%`;
        fetch(`/search-ajax/${queryString}`,
            {
                method: "GET",
                credentials: "same-origin"
            })
            .then(response => response.json())
            .then(jsonResponse => characters.fillCharacters(jsonResponse))
    },

    fillCharacters: function (characters) {
        let characterList = document.querySelector('#list');
        characterList.innerHTML = '';
        for (let character of characters) {
            let actor = `<li>${character.name} played ${character['character_name']} in ${character.title}.</li>`
            characterList.insertAdjacentHTML('afterbegin', actor);
        }
    }
}

characters.init();