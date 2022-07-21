$(document).ready(function () {
    $("#datosformulario").validate({
        rules: {
            name: {
                required: true,

            },
            apellido: {
                required: true,
            },
            edad: {
                number: true,
                min: 18
            },
            emial: {
                required: true,
                email: true
            }

        }
    });
});