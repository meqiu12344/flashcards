document.addEventListener('DOMContentLoaded', function() {
    let searchBox = document.getElementById('search-box');

    searchBox.addEventListener('input', () => {
        let titles = document.querySelectorAll('.title');

        titles.forEach((e) => {

            let parent_node = e.parentNode
            let mather = parent_node.parentNode

            if (searchBox.value === '') {
                mather.style.display = 'flex';
            } else {
                mather.style.display = e.innerHTML.toLowerCase().includes(searchBox.value.toLowerCase()) ? '' : 'none';
            }
        });
    });
});
