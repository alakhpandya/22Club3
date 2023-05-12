// getting a random number:
// console.log(Math.random());

// getting a random number >= 5
// console.log(Math.random() + 5);

// getting a random number between 0 to 10
// console.log(Math.random() * 10)

// getting an integer between 0 to 10
// console.log(Math.floor(Math.random() * 10))

// getting an integer between 7 to 20
// console.log(Math.floor(Math.random() * 13) + 7)

let allQuotes = [
    {
        quote: "Any fool can write code that a computer can understand. Good programmers write code that humans can understand.",
        author: "Martin Fowler"
    },
    {
        quote: "If you have built castles in the air, your work need not be lost; that is where they should be. Now put the foundations under them.",
        author: "HENRY DAVID THOREAU"
    },
    {
        quote: "I was never afraid of failure; for I would sooner fail than not be among the greatest.",
        author: "JOHN KEATS "
    },
    {
        quote: "The power of finding beauty in the humblest things makes home happy and lovely" ,
        author: "LOUISA MAY ALCOTT"
    },
    {
        quote: "I do not fear computers. I fear lack of them.",
        author: "Isaac Asimov"
    },
    {
        quote: "The computer was born to solve problems that did not exist before.",
        author: "Bill Gates"
    },
    {
        quote: "Software is a gas; it expands to fill its container.",
        author: "Nathan Myhrvold"
    },
    {
        quote: "Code is like humor. When you have to explain it, it’s bad",
        author: "Cory House"
    },
    {
        quote: "Java is to Javascript what car is to Carpet",
        author: "Chris Heilmann"
    },
    {
        quote: "First, solve the problem. Then, write the code",
        author: "John Johnson"
    }
]

let index
let quote_container = document.querySelector('.quote');
let author_container = document.querySelector('.author');
let btn = document.querySelector('.button');

btn.addEventListener('click', () => {
    index = Math.floor(Math.random() * 10);
    quote_container.innerText = allQuotes[index]["quote"];
    author_container.innerText = allQuotes[index]["author"];
})