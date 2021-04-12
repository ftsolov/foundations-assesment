let passwordField = document.querySelector("#password");
let passwordRepeatedField = document.querySelector("#password-repeat");

document.getElementById("form").addEventListener("submit", (event) => {
  let password = passwordField.value;
  let passwordRepeated = passwordRepeatedField.value;

  if (!checkPasswordSecurity(password)) { // checks if password meets criteria
	event.preventDefault();
	alert("Password does not meet criteria.");
	resetPasswordInputs();
	return;
  }

  if (password !== passwordRepeated) { // checks if password is repeated properly
	event.preventDefault();
	alert("Passwords don't match, please try again.");
	resetPasswordInputs();
  }
});

function checkPasswordSecurity(password) {
  return password.length >= 8 && /\d/.test(password);
}

function resetPasswordInputs() { // resets input field values
  passwordField.value = "";
  passwordRepeatedField.value = "";
}

function logNewEntry() {
    let popup = document.getElementById('new-entry')
    if (popup.style.display === "none") {
    popup.style.display = "block";
  } else {
    popup.style.display = "none";
  }
}
