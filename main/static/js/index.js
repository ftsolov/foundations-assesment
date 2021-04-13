let passwordField = document.querySelector("#password");
let passwordRepeatedField = document.querySelector("#password-repeat");

document.getElementById("form").addEventListener("submit", (event) => {
  let password = passwordField.value;
  let passwordRepeated = passwordRepeatedField.value;

  if (!checkPasswordSecurity(password)) {
    // checks if password meets criteria
    event.preventDefault();
    alert("Password does not meet criteria.");
    resetPasswordInputs();
    return;
  }

  if (password !== passwordRepeated) {
    // checks if password is repeated properly
    event.preventDefault();
    alert("Passwords don't match, please try again.");
    resetPasswordInputs();
  }
});

function checkPasswordSecurity(password) {
  return password.length >= 8 && /\d/.test(password);
}

function resetPasswordInputs() {
  // resets input field values
  passwordField.value = "";
  passwordRepeatedField.value = "";
}

function logNewEntryAnimation() {
  let popup = document.getElementById("popup");
  if (popup.style.display === "block") {
    popup.style.opacity = "1";
    popup.style.zIndex = "10";
  } else if (popup.style.display === "none") {
    popup.style.opacity = "1";
    popup.style.zIndex = "10";
  }
}

function closeNewEntryOverlay() {
  let popup = document.getElementById("popup");
  if (popup.style.display === "block") {
    popup.style.opacity = "0";
    popup.style.zIndex = "-10";
  }
}
