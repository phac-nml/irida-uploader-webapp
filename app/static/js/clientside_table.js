/*jslint browser: true*/
/*global $*/


$(document).ready(function () {
  $.get('/tables/clientside_table', function (data) {
    $('#clientside_table').DataTable({
      data: data.data,
      paging: true,
      dom: 'frtipB',
      columns: [
        {"data": "directory", "title": "Directory"},
        {"data": "status", "title": "Status"},
        {"data": "message", "title": "Message"},
        {
            "className":      'details',
            "data":           null,
            "render": function(data){
               return '<button class="btn btn-mini btn-primary pull-right" onclick="location.href=\'../run_table?run=' + data.directory + '\';">Details</button>';
            }
        },
      ]
    });
  });
});
