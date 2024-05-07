document.addEventListener("DOMContentLoaded", function() {
    const form = document.querySelector("form");

    form.addEventListener("submit", function(event) {
        event.preventDefault();

        const username = document.getElementById("username").value;
        const password = document.getElementById("password").value;

        fetch('/login', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ username, password })
        })
        .then(response => {
            if (response.status === 200) {
                // Se il login è riuscito, segui il reindirizzamento
                window.location.href = response.url;
            } else {
                // Se c'è un errore, mostra un messaggio
                response.text().then(message => alert(message));
            }
        })
        .catch(error => {
            console.error("Error:", error);
        });
    });
});