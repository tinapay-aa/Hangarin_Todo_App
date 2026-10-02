const sidebar_toggleButton = document.getElementById('toggle-btn')
const sidebar = document.getElementById('sidebar')
const date_filter = document.getElementById('date-filter-state')
const date_filter_container = document.getElementById('date-filter-container')

document.addEventListener('DOMContentLoaded', function() {
    if (date_filter.value == 'asc') {
        date_filter_container.classList.add('rotate')
    }
    else {
        date_filter_container.classList.remove('rotate')
    }
});

function toggleSidebar() {
    if (sidebar.classList.contains('close')) {
        sidebar.classList.remove('close')
        sidebar_toggleButton.classList.add('rotate')
    }
    else {
        sidebar.classList.add('close')
        sidebar_toggleButton.classList.remove('rotate')
    }
}

function toggle_date_filter() {
    date_filter.value = date_filter.value == 'asc' ? 'desc' : 'asc'
    date_filter_container.classList.toggle('rotate')
}
