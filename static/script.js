document.getElementById('relativity-btn').addEventListener('click', function() {
    fetch('/relativity')
        .then(response => response.json())
        .then(data => {
            const container = document.getElementById('answer-container');
            container.innerHTML = `<h2>${data.question}</h2><p>${data.answer}</p>`;
        })
        .catch(error => console.error('Error:', error));
});
