/*
const printHello = () => {
    console.log("Welcome to the party");
    console.log("sponsored by Khush...");
}

let timer = setInterval(printHello, 2000);
play_pause_btn.addEventListener('click', () => {
    clearInterval(timer);
})
*/


let ms = 0, s = 0, min = 0, h = 0;
let play_pause_btn = document.querySelector('.play-icon');
let timer_container = document.getElementById('timer-container');
let reset_btn = document.querySelector('.reset-icon');
const stopWatch = () => {
    ms++;
    if (ms == 100){
        ms = 0;
        s++;
        if (s == 60){
            s = 0;
            min++;
            if(min == 60){
                min = 0;
                h++;
            }
        }
    }
    timer_container.innerHTML = `<span>${h.toString().padStart(2, '0')}</span>:<span>${min.toString().padStart(2, '0')}</span>:<span>${s.toString().padStart(2, '0')}</span>:<span id="milliseconds">${ms.toString().padStart(3, '0')}</span>`;
}

play_pause_btn.addEventListener('click', () => {
    if (play_pause_btn.classList.contains('fa-play')){
        timer = setInterval(stopWatch, 10);
        play_pause_btn.classList.remove('fa-play');
        play_pause_btn.classList.add('fa-pause');
    }
    else{
        clearInterval(timer);
        play_pause_btn.classList.add('fa-play');
        play_pause_btn.classList.remove('fa-pause');
    }
})
reset_btn.addEventListener('click', () => {
    timer_container.innerHTML = `<span>00</span>:<span>00</span>:<span>00</span>:<span id="milliseconds">000</span>`;
    h = 0; min = 0; s = 0; ms = 0;
})