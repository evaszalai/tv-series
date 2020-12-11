const highlight = {
    init: function() {
        let lines = document.querySelectorAll('tr');
        lines.forEach((line) => {
            line.addEventListener('mouseover', function() {
                let dataId = this.dataset.id;
                if (this.classList.contains('actor')) {
                    let siblings = document.querySelectorAll(`[data-id = '${dataId}']`);
                    for (let sibling of siblings) {
                        if (sibling.classList.contains('show')) {
                        sibling.classList.add('highlighted');}
                    }
                }
                else {
                    let siblings = document.querySelectorAll(`[data-id = '${dataId}']`);
                    for (let sibling of siblings) {
                        if (sibling.classList.contains('actor')) {
                        sibling.classList.add('highlighted');}
                    }
                }
            })
            line.addEventListener('mouseout', function () {
                let highlightedAreas = document.querySelectorAll('.highlighted');
                highlightedAreas.forEach((area) => area.classList.remove('highlighted'));
            })
        })
    }
}

highlight.init();