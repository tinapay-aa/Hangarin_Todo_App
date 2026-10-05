const date_radio_btns = document.querySelectorAll(
    'input[type="radio"][name="date-sort"]'
);

const status_checkboxes = document.querySelectorAll('.status-filter-checkbox')
const status_toggler = document.getElementById('status-toggler')

const cat_checkboxes = document.querySelectorAll('.cat-filter-checkbox')
const cat_toggler = document.getElementById('cat-toggler')

const priority_checkboxes = document.querySelectorAll('.priority-filter-checkbox')
const priority_toggler = document.getElementById('priority-toggler')

const filter_modal = document.getElementById('filter-modal-container')

function toggle_filter_modal() {
    filter_modal.classList.toggle('close')
}

date_radio_btns.forEach(radio => {
    radio.addEventListener('change', function() {
        date_radio_btns.forEach(r => {
            r.parentElement.classList.toggle(
                'active',
                r.checked
            )
        })
    })
})

function toggle_checkboxes(toggler, checkboxes) {
    checkboxes.forEach(checkbox => {
        checkbox.checked = toggler.checked;
    });
};

function toggle_checkbox_toggler(toggler, checkboxes) {
    toggler.checked = [...checkboxes].every(checkbox => checkbox.checked)
}