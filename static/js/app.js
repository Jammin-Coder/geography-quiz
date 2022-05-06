let lastUrl = window.location;



pageFadeOut = () => {
    document.body.classList.remove('fade-in');
    document.body.classList.add('fade-out');
    document.body.onanimationend = function () {
        document.body.style.opacity = '0';
    }
};

pageFadeIn = () => {
    document.body.classList.remove('fade-out');
    document.body.classList.add('fade-in');
    document.body.onanimationend = function () {
        document.body.style.opacity = '1';
    }
}


goToRegion = region => {
    pageFadeOut();

    setTimeout(() => {
        window.location.href = region + '/quiz';
        pageFadeIn();
    }, 500);
    
}

getSelectedAnswer = (answers, submittedAnswer) => {
    let selectedAnswer;
    answers.forEach(answer => {
        if (answer.innerText == submittedAnswer) {
            selectedAnswer = answer;
            return;
        }
    });
    return selectedAnswer;
}

handleQuizAnswer = (submittedAnswer, correctAnswer) => {
    const answers = document.querySelectorAll('.answer');
    const messageElement = document.querySelector('.message');
    const nextButton = document.querySelector('.quiz-next');
    let selectedAnswerButton = getSelectedAnswer(answers, submittedAnswer);

    answers.forEach(answer => {answer.style.backgroundColor = 'inherit'});
    if (submittedAnswer === correctAnswer) {
        selectedAnswerButton.style.backgroundColor = 'green';
        selectedAnswerButton.style.color = 'white';
        messageElement.innerText = 'CORRECT';
    } else {
        selectedAnswerButton.style.backgroundColor = 'red';
        selectedAnswerButton.style.color = 'white';
        messageElement.innerHTML = 'FALSE<br>The correct answer is ' + correctAnswer;
    }



    nextButton.style.display = 'block';
    nextButton.classList.add('fade-in');
    nextButton.style.opacity = '1';
    nextButton.onclick = () => {
        pageFadeOut();
        window.location.href = window.location;
    }

}