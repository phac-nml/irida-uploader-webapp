/*jslint browser: true*/
/*global $*/

/*
https://stackoverflow.com/questions/19491336/how-to-get-url-parameter-using-jquery-or-plain-javascript
*/
var getUrlParameter = function getUrlParameter(sParam) {
    var sPageURL = window.location.search.substring(1),
        sURLVariables = sPageURL.split('&'),
        sParameterName,
        i;

    for (i = 0; i < sURLVariables.length; i++) {
        sParameterName = sURLVariables[i].split('=');

        if (sParameterName[0] === sParam) {
            return sParameterName[1] === undefined ? true : decodeURIComponent(sParameterName[1]);
        }
    }
};

$(document).ready(function () {
  var run = getUrlParameter('run');
  var run_status = $.get('/tables/run_table?run='+run, function (data) {
    $('#run_table').DataTable({
      data: data.data,
      paging: true,
      dom: 'frtipB',
      columns: [
        {"data": "directory", "title": "Directory"},
        {"data": "status", "title": "Status"},
        {"data": "message", "title": "Message"},
      ]
    });
    // Check if we should show the continue run button, only partial runs can be continued
    console.log("run status: " + data.data[0].status);
    if (data.data[0].status !== "partial") {
        document.getElementById("continue_run").style.display = "none";
    }
  });



  $.get('/tables/run_sample_sheet?run='+run, function(data){
    $('#sample_sheet').text(data.data);
  });

  document.getElementById("save_sample_sheet").onclick = function(){
    text_to_send = $('#sample_sheet').val();
    console.log("save button clicked");
    console.log("text to send:");
    console.log(text_to_send);
    $.post('/tables/run_sample_sheet?run='+run, text_to_send);
  }

  document.getElementById("upload_run").onclick = function(){
    console.log("upload button clicked");
    $.post('/tables/upload_run?run='+run);
    location.reload();
  }

  document.getElementById("continue_run").onclick = function(){
    console.log("continue run button clicked")
    $.post('/tables/continue_run?run='+run)
    location.reload();
  }

  document.getElementById("refresh").onclick = function(){
    location.reload();
  }

});
