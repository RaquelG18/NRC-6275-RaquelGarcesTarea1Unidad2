//Tambien valida los datos del formulario
/*
    Se crea una funcion que permita validar los datos del formulario,
     añadiendo en los campos la restricción "required" y confirmando el valor con "true"

*/
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
