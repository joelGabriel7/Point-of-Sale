$(function () {
    $('#date_birthday').datetimepicker({
        format: 'DD/MM/YYYY',
        date: moment().format('DD/MM/YYYY'),
        locale: 'es',
    });
});