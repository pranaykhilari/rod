$(document).ready(function () {
    var table = $('#example').DataTable({
        "pageLength": 5,
        "pagingType": "full_numbers"
        // 'scrollX': true
    });
    $('#example').removeClass('display').addClass('table table-striped table-bordered');
});