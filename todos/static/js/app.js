const toggleButton = document.getElementById('toggle-btn')
const sidebar = document.getElementById('sidebar')

function toggleSidebar() {
    if (sidebar.classList.contains('close')) {
        sidebar.classList.remove('close')
        toggleButton.classList.remove('rotate')
    }
    else {
        sidebar.classList.add('close')
        toggleButton.classList.add('rotate')
    }
}