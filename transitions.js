function waitBeforeNavigate(ev) {
    ev.preventDefualt();
    const goTo = this.getAttribute("href");

    transition();

    setTimeout(function(){
        window.location = goTo;
    } , 2000);
};

document.querySelectorAll("a")
.forEach(EL => EL.addEventListener ("click", waitBeforeNavigate));

function transition() {
    document.getElementById('blue').style.animation = "righttransition 1s ease forwards";
    document.getElementById('yellow').style.animation = "righttransition 1.5s ease forwards";
    document.getElementById('green').style.animation = "righttransition 2s ease forwards";
}