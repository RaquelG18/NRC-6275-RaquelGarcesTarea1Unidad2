/*
    Creamos la función para la validación de 
    los campos de nuestro formulario
*/
$(document).ready(function () {
    /* como parámetro añadimos el id de nuestro formulario
        #datosformulario 
         Llamamos al método validate() y agregamos 
         como parámetro los campos del formulario 
         con la restricción de tipo required
        */
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