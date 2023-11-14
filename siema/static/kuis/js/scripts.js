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

function updateLayout() {
  var information = document.querySelector(".information");
  var isOverflowing = information.scrollWidth > information.clientWidth;

  if (isOverflowing) {
    information.style.justifyContent = "flex-start";
  } else {
    information.style.justifyContent = "center";
  }
}

// Call the function on load and when the window is resized
window.addEventListener("resize", updateLayout);
window.addEventListener("load", updateLayout);
