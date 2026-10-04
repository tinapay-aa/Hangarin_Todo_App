const date_radio_btns = document.querySelectorAll(
    'input[type="radio"][name="date-sort"]'
);

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