$(document).ready(function () {
    $('.select2').select2();
    $('#id_empleado').on('change', function () {
        //console.log("Something change");
        const empleadoId = $(this).val();
        //console.log(empleadoId);
        $.ajax({
            url: '/pyturnos/turnosProgramados/' + (empleadoId),
            data: { empleado_id: empleadoId },
            dataType: 'json',
            success: function (data) {
                //console.log(data)
                var select = $('#id_turno_programado');
                select.empty();
                $.each(data, function (key, value) {
                    select.append($('<option>', {
                        value: key,
                        text : value,
                    }
                    ));
                });
            }
        });
    });
});

/*$(document).ready(function() {
    $("#id_empleado").select2();
    $("#id_turno_programado").select2();
});*/