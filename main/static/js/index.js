function is_numeric(str){
    return /^\d+$/.test(str);
}

function password_check() {
    let password = document.getElementById("#password").value;
    console.log(password)
    if (password.length > 6) {
        let i;
        for (i=0; i < password.length; i++) {
            let bool = is_numeric(letter);
            if (bool === true) {
                return true;
            }
        }
    }
}

function password_repeat_check() {
    let password = document.querySelector('#password').value;
    let password_repeated = document.querySelector('#password-repeat').value;
    if (password === password_repeated) {
        console.log("true")
    } else {
        console.log("false")
    }
}