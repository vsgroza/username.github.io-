document.addEventListener("DOMContentLoaded", function () {
    const questionsLink = document.getElementById("questionsLink");
    const contactPopup = document.getElementById("contactPopup");
    const closePopup = document.getElementById("closePopup");
  
    questionsLink.addEventListener("click", function (e) {
      e.preventDefault();
      contactPopup.style.display = "flex";
    });
  
    closePopup.addEventListener("click", function () {
      contactPopup.style.display = "none";
    });
  });
  