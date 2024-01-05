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

function updatePerView() {
	const windowWidth = window.innerWidth;

	if (windowWidth < 600) {
		// Adjust this threshold based on your design
		perView = 1;
	} else if (windowWidth < 1200) {
		// Adjust this threshold based on your design
		perView = 2;
	} else {
		perView = 3;
	}
	console.log("perView change to ", perView);

	imageWrapper.style.setProperty("--per-view", perView);
	for (let i = 0; i < perView; i++) {
		imageWrapper.insertAdjacentHTML("beforeend", imageItems[i].outerHTML);
	}
}

const imageWrapper = document.querySelector(".image-wrapper");
const imageItems = document.querySelectorAll(".image-wrapper > *");
const imageLength = imageItems.length;
let perView;
let totalScroll = 0;
const delay = 2000;

// Initial call to set perView based on the current window size
updatePerView();

// Listen for window resize events
window.addEventListener("resize", updatePerView);

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
	const widthEl = document.querySelector(".image-wrapper > :first-child").offsetWidth + 24;
	imageWrapper.style.left = `-${totalScroll * widthEl}px`;
	imageWrapper.style.transition = ".3s";

	// Update the image indicator
	updateImageIndicator();
}

const imageIndicator = document.querySelector(".image-indicator");

// Function to update the image indicator
function updateImageIndicator() {
	// Remove existing indicator circles
	imageIndicator.innerHTML = "";

	// Add a circle for each image
	for (let i = 0; i < imageLength; i++) {
		const circle = document.createElement("div");
		circle.classList.add("indicator-circle");
		circle.addEventListener("click", () => goToImage(i));
		imageIndicator.appendChild(circle);
	}

	// Highlight the current image circle
	const currentCircle = imageIndicator.children[totalScroll - 1];
	if (currentCircle) {
		currentCircle.classList.add("active");
	}
}

// Initial call to set up the image indicator
updateImageIndicator();

// Function to handle manual navigation by clicking on the indicator circles
function goToImage(index) {
	clearInterval(autoScroll);
	totalScroll = index + 1;
	imageWrapper.style.transition = ".3s";
	const widthEl =
		document.querySelector(".image-wrapper > :first-child").offsetWidth + 24;
	imageWrapper.style.left = `-${totalScroll * widthEl}px`;
	updateImageIndicator();
	autoScroll = setInterval(scrolling, delay);
}
