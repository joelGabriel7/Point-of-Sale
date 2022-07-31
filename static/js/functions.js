function message_error(obj) {
    let html = '<ul style="text-align: left;">';
    $.each(obj, function (key, value) {
        html += '<li>' + key + value + '</li>'
    });
    html += '</ul>';
    Swal.fire({
        title: 'Error!',
        html: html,
        icon: 'error',
    });
}