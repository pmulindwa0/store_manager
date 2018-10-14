let modal = document.getElementById('myModal');
const productList = document.querySelector('#product-list');
let addToCart = document.getElementById('addToCart');
let closeBtn = document.getElementsByClassName("close")[0];

productList.addEventListener('click', saleProduct);

function saleProduct(e) { 
    if (e.target.classList.contains('add-to-cart')) {
        e.preventDefault();
        modal.style.display = "block";
    }
    
}

closeBtn.onclick = function() {
    modal.style.display = "none";
}