import axios from "axios";

document.addEventListener('DOMContentLoaded', (e) => {
    console.log(e)


    axios.get('https://localhost:8000/hello_world')
        .then(function (response) {
            // handle success
            console.log(response);
        })
        .catch(function (error) {
            // handle error
            console.log(error);
        })
        .then(function () {
            // always executed
        });

})