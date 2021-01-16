const steps = Array.from(document.querySelectorAll('form .step'));
const nextBtn = document.querySelectorAll('form .next-btn');
const prevBtn = document.querySelectorAll('form .previous-btn');
const submitBtn = document.querySelector('form .submit-btn');
const form = document.querySelector('form');

nextBtn.forEach(button =>{
    button.addEventListener('click', (e) => {
        changeStep('next');
    })
})

prevBtn.forEach(button => {
    button.addEventListener('click', (e) => {
        changeStep('previous');
    })
})

function changeStep(btn) {
    let index = 0;
    const active = document.querySelector('form .step.active');
    index = steps.indexOf(active)
    steps[index].classList.remove('active');
    if (btn === 'next') {
        index++;
    }
    else if (btn === 'previous') {
        index--;
    }
    steps[index].classList.add('active');
    console.log(index);
}