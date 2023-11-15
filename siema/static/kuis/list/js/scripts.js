var currentQuestionIndex = 0;
var score = 0;

function showQuestion() {
  var question = questions[currentQuestionIndex];
  document.getElementById('quiz-image').src = question.image;
  document.getElementById('quiz-question').innerText = question.question;

  var choicesContainer = document.getElementById('choices-container');
  choicesContainer.innerHTML = ""; // Clear previous choices

  question.choices.forEach(function (choice, index) {
      var choiceElement = document.createElement('button');
      choiceElement.onclick = function () {
          checkAnswer(choice.isAnswer);
      };

      if (choice.imageURL) {
          var imageElement = document.createElement('img');
          imageElement.src = choice.imageURL;
          imageElement.alt = "Option " + (index + 1);
          choiceElement.appendChild(imageElement);
          choiceElement.classList.add('button-img');
      } else {
          choiceElement.innerHTML = choice.text;
          choiceElement.classList.add('button-text');
      }

      choicesContainer.appendChild(choiceElement);
  });

  var feedbackContainer = document.getElementById('feedback-container');
  feedbackContainer.style.padding = 0;
  feedbackContainer.style.minHeight = 0;
  feedbackContainer.style.opacity = 0;
  feedbackContainer.style.visibility = 'hidden';
  feedbackContainer.style.height = 0;

  var questionContainer = document.getElementById('question-container');
  questionContainer.style.padding = '1rem';
  questionContainer.style.opacity = 1;
  questionContainer.style.visibility = 'visible';
  questionContainer.style.height = 'auto';
}


function checkAnswer(userAnswer) {
  var question = questions[currentQuestionIndex];
  var feedbackContainer = document.getElementById('feedback-container');
  var feedbackElement = document.getElementById('feedback');

  if (userAnswer === question.choices.find(choice => choice.isAnswer).isAnswer) {
      score++;
      feedbackContainer.className = 'correct';
      if (question.imageCorrectFeedback) {
          feedbackElement.innerHTML = `<img src="${question.imageCorrectFeedback}" alt="Correct"><p>${question.textCorrectFeedback}</p>`;
      } else {
          feedbackElement.innerText = question.textCorrectFeedback;
      }
  } else {
      feedbackContainer.className = 'incorrect';
      if (question.imageIncorrectFeedback) {
          feedbackElement.innerHTML = `<img src="${question.imageIncorrectFeedback}" alt="Incorrect"><p>${question.textIncorrectFeedback}</p>`;
      } else {
          feedbackElement.innerText = question.textIncorrectFeedback;
      }
  }

  var questionContainer = document.getElementById('question-container');
  questionContainer.style.opacity = 0;
  questionContainer.style.visibility = 'hidden';
  questionContainer.style.height = 0;
  questionContainer.style.padding = 0;
  feedbackContainer.style.minHeight = '10rem';
  feedbackContainer.style.padding = '1rem';
  feedbackContainer.style.opacity = 1;
  feedbackContainer.style.visibility = 'visible';
  feedbackContainer.style.height = 'auto';
}


function nextQuestion() {
  currentQuestionIndex++;
  if (currentQuestionIndex < questions.length) {
      showQuestion();
  } else {
      showResult();
  }
}

function showResult() {
  // document.getElementById('result-text').innerHTML = `<p>Kamu menjawab ${score} dari ${questions.length} pertanyaan dengan benar</p>`;const percentageScore = (score / questions.length) * 100;
  const percentageScore = (score / questions.length) * 100;
  let message = '';
  if (score === questions.length) {
    message = `Hebat! Kamu berhasil menjawab ${questions.length} pertanyaan dengan benar. Pertahankan!`;
  } else if (percentageScore > 50) {
    message = `Keren! Kamu menjawab ${score} dari ${questions.length} pertanyaan dengan benar. Tingkatkan lagi!`;
  } else if (percentageScore > 0) {
    message = `Sayang sekali, kamu hanya menjawab ${score} dari ${questions.length} pertanyaan dengan benar. Tapi jangan sedih, kamu bisa belajar lebih giat lagi.`;
  } else {
    message = `Sayang sekali, kamu belum menjawab ${questions.length} pertanyaan dengan benar. Tapi jangan sedih, kamu bisa belajar lebih giat lagi.`;
  }
  document.getElementById('result-text').innerHTML = `<p>${message}</p>`;

  var feedbackContainer = document.getElementById('feedback-container');
  feedbackContainer.style.opacity = 0;
  feedbackContainer.style.visibility = 'hidden';
  feedbackContainer.style.height = 0;
  feedbackContainer.style.minHeight = 0;
  feedbackContainer.style.padding = 0;

  var resultContainer = document.getElementById('result');
  resultContainer.style.opacity = 1;
  resultContainer.style.padding = '3rem';
  resultContainer.style.visibility = 'visible';
  resultContainer.style.height = 'auto';

  var botnav = document.getElementById('botnav');
  botnav.style.opacity = 1;
  botnav.style.visibility = 'visible';
  botnav.style.height = 'auto';
}

// Start the quiz
showQuestion();


window.addEventListener("load", () => {
  const content = document.querySelector(".main-content");
  content.style.opacity = "0";
  // Add a delay of 3 seconds before showing the content
  setTimeout(() => {
    const preloader = document.querySelector(".preloader");
    preloader.classList.add("hidden");

    // Show content with a fade-in transition
    setTimeout(() => {
      preloader.style.display = "none";
    }, 500); // 500 milliseconds = 0.5 seconds (match the transition duration)
    setTimeout(() => {
      content.style.opacity = "1";
    }, 250);
  }, 50); // 2500 milliseconds = 1.5 seconds
});

window.addEventListener("load", function () {
  document.body.classList.add("zoomIn");
});
