document.addEventListener("DOMContentLoaded", () => {
    var elems = document.getElementsByClassName('confirmation');
    var confirmIt = function (e) {
        if (!confirm('Esta seguro de esta accion?')) e.preventDefault();
    };
    for (var i = 0, l = elems.length; i < l; i++) {
        elems[i].addEventListener('click', confirmIt, false);
    }

    // const addToCartButton = document.getElementById("addCartBtn")
    // addToCartButton.addEventListener('click', (e)=> {
    //     e.preventDefault()
    //     alert('adding item to cart...')

    // })
})