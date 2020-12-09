// This function is to initialize the application
function init() {
    // init data
    showEpisodes.init();
}

let showEpisodes = {
    init: function () {
        let tableData = document.querySelectorAll('td');
        for (let item of tableData) {
            if (item.innerHTML % 2 === 0) {
                let tableRow = item.closest('tr');
                tableRow.classList.add('lightgreen');
            }
            else if (item.innerHTML % 2 === 1) {
                let tableRow = item.closest('tr');
                tableRow.classList.add('lightblue');
            }
        }
    }
}

init();
