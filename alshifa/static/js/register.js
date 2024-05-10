
var inputForm = document.getElementById("inputForm");

var usersData = JSON.parse(localStorage.getItem('users')) || [];

inputForm.addEventListener('submit', function (e) {
    e.preventDefault();

    var nameForm = document.getElementById('userName').value;
    var emailForm = document.getElementById("regEmial").value;
    var passwordForm = document.getElementById("regPass").value;
    var confirmPasswordForm = document.getElementById("confirmPass").value;
    
      if (!isStrongPassword(passwordForm)) {
        Swal.fire({
            position: 'center',
            icon: 'error',
            title: 'Password should be at least 8 characters long and include at least one uppercase letter, one lowercase letter, one digit, and one special character.',
            showConfirmButton: false,
            timer: 8000
        });
        return; // Exit the function if the password is not strong
    }

    if (passwordForm != confirmPasswordForm) {
        Swal.fire({
            position: 'center',
            icon: 'error',
            title: 'Password and Confirm Password are not the same',
            showConfirmButton: false,
            timer: 6000
        });
    } else {
        let user = {
            name: nameForm,
            email: emailForm,
            password: passwordForm
        };

        if (usersData != null) {
            let isExist = false;
            for (let i = 0; i < usersData.length; i++) {
                if (usersData[i]['email'] == emailForm) {
                    Swal.fire({
                        position: 'center',
                        icon: 'error',
                        title: 'Email already exists',
                        showConfirmButton: false,
                        timer: 6000
                    });
                    isExist = true; // Update to true if the email already exists
                    break; // Exit the loop once a match is found
                } else if (usersData[i]['name'] == nameForm) {
                    Swal.fire({
                        position: 'center',
                        icon: 'error',
                        title: 'Name already exists',
                        showConfirmButton: false,
                        timer: 6000
                    });
                    isExist = true; // Update to true if the name already exists
                    break; // Exit the loop once a match is found
                }
            }
            
            if (!isExist) {
                usersData.push(user);
                localStorage.setItem('users', JSON.stringify(usersData));
                console.log(localStorage.getItem('users'));
                Swal.fire({
                    position: 'center',
                    icon: 'success',
                    title: 'Your account was created successfully',
                    showConfirmButton: false,
                    timer: 1500
                }).then(function () {
                    window.location = "../index.html";
                });
            }
        } else {
            usersData.push(user);
            localStorage.setItem('users', JSON.stringify(usersData));
            console.log(localStorage.getItem('users'));
            Swal.fire({
                position: 'top-end',
                icon: 'success',
                title: 'Your account was created successfully',
                showConfirmButton: false,
                timer: 1500
            }).then(function () {
                    window.location = "../index.html";
                });
        }
    }
});
function isStrongPassword(password) {
    // Password should be at least 8 characters long and include at least one uppercase letter, one lowercase letter, one digit, and one special character.
    var strongPasswordRegex = /^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$/;
    return strongPasswordRegex.test(password);
}


function updateNavigationButtons() {
    var isLoggedIn = localStorage.getItem('email') !== null;
    var loginLink = document.getElementById('loginLink');
    var registerLink = document.getElementById('registerLink');

    if (isLoggedIn) {
        // User is logged in, update buttons to show logout
        loginLink.innerHTML = '<button class="btn white-button" id="loginBtn" onclick="handleLoginClick()">Logout</button>';
        registerLink.style.display = 'none'; // Hide the register button when logged in
    } else {
        // User is not logged in, show login and register buttons
        loginLink.innerHTML = '<button class="btn white-button" id="loginBtn" onclick="handleLoginClick()">Sign In</button>';
        registerLink.innerHTML = '<button class="btn" id="registerBtn">Sign Up</button>';
        registerLink.style.display = 'inline-block'; // Show the register button when not logged in
    }
}
