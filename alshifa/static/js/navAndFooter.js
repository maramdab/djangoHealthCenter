function myMenuFunction() {
    var i = document.getElementById("navMenu");
    if (i.className === "navMenu") {
        i.className += " responsive";
    }
    else {
        i.className = "navMenu";
    }
}



