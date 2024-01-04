window.addEventListener("load", () => {
	// const content = document.querySelector(".main-content");
	// content.style.opacity = 0;
	// Add a delay of 3 seconds before showing the content
	setTimeout(() => {
		const preloader = document.querySelector(".preloader");
		preloader.classList.add("hidden");

		// Show content with a fade-in transition
		setTimeout(() => {
			preloader.style.display = "none";
		}, 500); // 500 milliseconds = 0.5 seconds (match the transition duration)
		setTimeout(() => {
			// content.style.opacity = 1;
		}, 250);
	}, 50); // 2500 milliseconds = 1.5 seconds
});

window.addEventListener("load", function () {
	document.body.classList.add("zoomIn");
});

const observer = new IntersectionObserver((entries) => {
	entries.forEach((entry) => {
		if (entry.isIntersecting) {
			entry.target.classList.add("show");
		}
		// else {
		// 	entry.target.classList.remove("show");
		// }
	});
});

const hiddenElements = document.querySelectorAll(".hidden");
hiddenElements.forEach((el) => observer.observe(el));


const imageWrapper = document.querySelector(".image-wrapper");
const imageItems = document.querySelectorAll(".image-wrapper > *");
const imageLength = imageItems.length;
const perView = 3;
let totalScroll = 0;
const delay = 2000;

imageWrapper.style.setProperty("--per-view", perView);
for (let i = 0; i < perView; i++) {
	imageWrapper.insertAdjacentHTML("beforeend", imageItems[i].outerHTML);
}

let autoScroll = setInterval(scrolling, delay);

function scrolling() {
	totalScroll++;
	if (totalScroll == imageLength + 1) {
		clearInterval(autoScroll);
		totalScroll = 1;
		imageWrapper.style.transition = "0s";
		imageWrapper.style.left = "0";
		autoScroll = setInterval(scrolling, delay);
	}
	const widthEl =
		document.querySelector(".image-wrapper > :first-child").offsetWidth + 24;
	imageWrapper.style.left = `-${totalScroll * widthEl}px`;
	imageWrapper.style.transition = ".3s";
}
