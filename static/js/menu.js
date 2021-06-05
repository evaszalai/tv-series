const menu = {
    init: function () {
        menu.addEventListenerToOptionsMenu();
    },
    addEventListenerToOptionsMenu: function () {
        let optionsButton = document.querySelector('#bt-options');
        optionsButton.addEventListener('click', menu.showOptions);
    },
    showOptions: function() {
                let options = document.querySelector('#options');
                options.classList.toggle('hidden');
    }
}

menu.init();