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
  return password.length >= 6 && /\d/.test(password);
}

function resetPasswordInputs() {
  // resets input field values
  passwordField.value = "";
  passwordRepeatedField.value = "";
}

function logNewEntryAnimation() {
  let popup = document.getElementById("popup");
  if (popup.style.display === "none") {
    popup.style.display = "block";
    setTimeout(function(){popup.style.opacity = "1";
    console.log("hey")}, 100)
  } else if (popup.style.display === "block") {
    popup.style.opacity = "0";
    setTimeout(function(){popup.style.display = "none"}, 200)
    document.getElementById("title-entry").value = "";
  }
}

