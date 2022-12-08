const show_btn = document.getElementById('show-btn');
    const show_text = document.getElementById('show-text');

    show_btn.addEventListener('click', ()=>{
        show_text.innerText = 'I am the hidden text!';
    })