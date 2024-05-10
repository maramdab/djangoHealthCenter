var loginForm = document.getElementById("loginForm");


loginForm.addEventListener('submit', function (e) {
    e.preventDefault();
    var emailForm = document.getElementById("emailForm");
    var passwordForm = document.getElementById("passwordForm");
    let isLogin=false;
    let usersData =  JSON.parse(localStorage.getItem('users')) || [];
    if (usersData!=null){
        for(let  i = 0 ;i< usersData.length;i++){
        if(emailForm.value == usersData[i]['email'] && passwordForm.value == usersData[i]['password']){
            localStorage.setItem('email',usersData[i]['email']);
            localStorage.setItem('password',usersData[i]['password']);
            localStorage.setItem('name',usersData[i]['name']);
         Swal.fire({
                    position: 'center',
                    icon: 'success',
                    title: 'You have logged in successfully.',
                    showConfirmButton: false,
                    timer: 1500
                }).then(function () {
                    window.location = "../index.html";
                });
                isLogin = false;
            return;
        }
        else {
            isLogin = true;
        }
    }
    if(isLogin){
        Swal.fire({
            position: 'center',
            icon: 'error',
            title: 'Your email or password is wrong',
            showConfirmButton: false,
            timer: 6000
        });
    }
    } 
    else{
         Swal.fire({
            position: 'center',
            icon: 'error',
            title: 'You must sign up first',
            showConfirmButton: false,
            timer: 6000
        }).then(function () {
                    window.location = "../pages/register.html";
                });
        
    }
    
});

function handleLoginClick() {
    var isLoggedIn = localStorage.getItem('email') !== null;

    if (isLoggedIn) {
        // User is logged in, perform logout actions
        logout();
    } else {
        // User is not logged in, redirect to the login page
        window.location.href = '../pages/login.html';
    }
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

// Initial call to set the correct buttons when the page loads
updateNavigationButtons();

function logout() {
    // Clear user data from localStorage or perform other logout actions
    localStorage.removeItem('email');
    localStorage.removeItem('password');
    localStorage.removeItem('name');

    // Redirect to the home page or any other desired location after logout
    window.location.href = '../index.html';
}

// Call updateNavigationButtons after logout to update the button state
updateNavigationButtons();

