$(function () {
    $('#date_birthday').datetimepicker({
        format: 'YYYY-MM-DD',
        date: moment().format('YYYY-MM-DD'),
        locale: 'es',
    });
});