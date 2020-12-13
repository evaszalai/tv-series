const rating = {
    init: function () {
        this.addEventListenersToRating();
    },
    addEventListenersToRating: function () {
        let ratingFields = document.querySelectorAll('.rating');
        ratingFields.forEach((field) => rating.increaseRating(field));
        ratingFields.forEach((field) => rating.decreaseRating(field));
    },
    increaseRating: function (field) {
        field.addEventListener('click', function(e) {
            e.currentTarget.innerHTML = parseFloat(e.currentTarget.innerHTML) + 0.1;
        })
    },
    decreaseRating: function (field) {
        field.addEventListener('contextmenu', function (e) {
            e.preventDefault();
            e.currentTarget.innerHTML = parseFloat(e.currentTarget.innerHTML) - 0.1;
        })
    }
}

rating.init();