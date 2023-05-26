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
