$(function () {
    $('.select2').select2({
        theme: "bootstrap4",
        language: 'es'
    });
    $('#date_joined').datetimepicker({
        format: 'DD-MM-YYYY',
        date: moment().format('YYYY-MM-DD'),
        locale: 'es',

        minDate: moment().format('YYYY-MM-DD'),

    });



    $("input[name='iva']").TouchSpin({
        min: 0,
        max: 100,
        step: 0.1,
        decimals: 2,
        boostat: 5,
        maxboostedstep: 10,
        postfix: '$',
        buttondown_class: 'btn btn-secondary',
         buttonup_class: 'btn btn-secondary',

    })
});