window.addEventListener("load", () => {
	const content = document.querySelector(".container");
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
	}, 50); // 2500 milliseconds = 2.5 seconds
});

window.addEventListener("load", function () {
	document.body.classList.add("zoomIn");
});


var modal = document.getElementById("feedback-modal");
var span = document.getElementsByClassName("close")[0];
var refererBeforeSubmit = document.getElementById('referer-before-submit').value;

if (modal) {
	modal.style.opacity = '1';
	modal.style.visibility = 'visible';

	span.onclick = function () {
    modal.style.opacity = '0';
    modal.style.visibility = 'hidden';
	};

	window.onclick = function (event) {
		if (event.target === modal) {
			modal.style.opacity = '0';
			modal.style.visibility = 'hidden';
		}
	};
};
