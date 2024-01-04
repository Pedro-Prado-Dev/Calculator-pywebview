function toggleDarkMode() {
    const body = document.body;
    const isDarkMode = body.classList.toggle("dark-mode");
    localStorage.setItem('darkMode', isDarkMode);
}

window.onload = function () {
    const darkMode = localStorage.getItem('darkMode');
    const body = document.body;
    if (darkMode === 'true') {
        body.classList.add('dark-mode');
    }
};