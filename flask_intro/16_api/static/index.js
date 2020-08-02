document.addEventListener('DOMContentLoaded', function() {
    document.querySelector('form').onsubmit = function() {

        // 1. Inicjalizacja zapytania asycnchronicznego (XMLHTTP request)
        const request = new XMLHttpRequest();
        request.open('POST', '/convert');
        // Przygotowanie danych do wysyłki
        const amount = document.querySelector('#amount').value;
        const symbols = document.querySelector("#symbols").value;
        const data = new FormData();
        //data.append('amount', amount);
        data.append('symbols', symbols);

        // 2. Co ma się stać po otrzymaniu odpowiedzi
        request.onload = function() {
            const response_data = request.responseText;
            const response = JSON.parse(response_data);

            if (response.success) {
                const result = Number(amount) / Number(response.rates);
                document.querySelector('#result').innerHTML = `Zostanie wypłacone ${result} euro.`;
            }
            else {
                document.querySelector('#result').innerHTML = 'Wystąpił błąd. Skontaktuj się ze wspaciem.';
            }
        }

        request.send(data);
        return false;
    }
});
