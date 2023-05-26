let target;

window.addEventListener('click', (e) => {
    target = e.target;
    console.log(target);
    if (target.classList.contains('close-btn')){
        if (target.parentElement.parentElement.classList.contains('show')){
            target.parentElement.parentElement.classList.remove('show');
            target.innerText = "+";
        }
        else{
            target.parentElement.parentElement.classList.add('show');
            target.innerText = "-";
        }
    }
})