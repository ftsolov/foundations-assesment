let passwordField = document.querySelector('#password');
let passwordRepeatedField = document.querySelector('#password-repeat');

document.getElementById('form').addEventListener('submit', event => {
    let password = passwordField.value;
    let passwordRepeated = passwordRepeatedField.value;

    if (!checkPasswordSecurity(password)) {
        event.preventDefault();
        alert("Password not valid.")
        return
    }

    if (password !== passwordRepeated) {
        event.preventDefault();
        alert("Passwords don't match.")
    }
})

function checkPasswordSecurity(password) {
    return password.length >= 8 && /\d/.test(password)
}

