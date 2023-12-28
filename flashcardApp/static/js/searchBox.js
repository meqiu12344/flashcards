document.addEventListener('DOMContentLoaded', function() {
    let searchBox = document.getElementById('search-box');

    searchBox.addEventListener('input', () => {
        let titles = document.querySelectorAll('.title');

        titles.forEach((e) => {
            if (searchBox.value === '') {
                e.parentNode.style.display = 'flex';
            } else {
                e.parentNode.style.display = e.innerHTML.toLowerCase().includes(searchBox.value.toLowerCase()) ? '' : 'none';
            }
        });
    });
});
