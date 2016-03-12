$(document).ready({

});

$("#url-form").on('submit', function(e) {
  e.preventDefault();
  console.log($("#input-url").val());
  $.post('/app/decomposed/', {
    url: $("#input-url").val(),
    csrfmiddlewaretoken: $("input[name='csrfmiddlewaretoken']").val()
  }, function(data){
    console.log(data);
    $("#original").text(data.text);
    $("#translated").text(data.transtxt);
  }).fail( function() {
    console.log("An error occured");
  });
});