const trailer = {
    init: function () {
        trailer.addEventListenerToTrailerButton();
    },
    addEventListenerToTrailerButton: function () {
        let trailerButtons = document.querySelectorAll('.trailer');
        trailerButtons.forEach((button) => {
            button.addEventListener('click', trailer.showModal)
        })
    },
    showModal: function(e) {
                let videoId = e.currentTarget.id;
                let modal = `<div class='modal'> 
                    <div class="modal-content">
                        <span class="close">&times;</span>                   
                        <iframe width="560" height="315" src="${videoId}" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
                    </div>
                </div>`
                let section = document.querySelector('section');
                section.insertAdjacentHTML('afterbegin', modal);
                let span = document.getElementsByClassName("close")[0];
                span.onclick = function() {
                    let modal = document.getElementsByClassName('modal')[0]
                    modal.style.display = 'none';
                }
            }
    }


trailer.init();