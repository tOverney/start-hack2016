$body = $("body");

$(document).on({
  ajaxStart: function() { $body.addClass("loading");    },
  ajaxStop: function() { $body.removeClass("loading"); }
});

var mouseX = 0;
var mouseY = 0;

$("#url-form").on('submit', function(e) {
  e.preventDefault();
  $.post('/app/decomposed/', {
    url: $("#input-url").val(),
    csrfmiddlewaretoken: $("input[name='csrfmiddlewaretoken']").val(),
    dest_lang: $("select[name='dest_lang']").val()
  }, function(data){
    $("#article_template").html(data);
    $("#input-url").text("");
    //SetFunctionTagCallbacks();
  }).fail( function() {
    console.log("An error occured");
  });
});

$('body').on('click', '.fill-div', function(e) {
  e.preventDefault();e.stopPropagation();
  $("#article_text").text($(this).attr('data-text'));
  $("#article_title").text($(this).attr('data-title'));
  $("#article_image").attr('src', $(this).attr('data-image'));
});

/*
function CalculateOffset(e, isHorizontal)
{
  var tresholdHor = 0.55;
  var tresholdVer = 0.45;
  var moveLeft = 20;
  var moveDown = 10;
  // Do horizontal offset calculations
  if(isHorizontal)
  {
    var windowWidth = window.innerWidth;
    var horPos = e.pageX / windowWidth;
    if(horPos > tresholdHor)
    {
      var hoverWidth = $('div#hover').width() + 20;
      moveLeft = -hoverWidth;
      return moveLeft;
    }
    else
      return moveLeft;
  }
  // Do vertical offset calculations
  if(!isHorizontal)
  {
    var windowHeight = window.innerHeight;
    // Offset the actual scrolling position from the pageY variable (gets actual window location instead of page location)
    var mouseY = e.pageY - $(window).scrollTop();
    var vertPos = mouseY / windowHeight;
    // $('div#hover').html(windowHeight + ' ' + mouseY); // Debug
    if(vertPos > tresholdVer)
    {
      var hoverHeight = $('div#hover').height() + 40;
      moveDown = -hoverHeight;
      return moveDown;
    }
    else
      return moveDown;
  }
}
// Sets callback pointers for mousehover and mousemove, for function references on function tag.
function SetFunctionTagCallbacks()
{
  // Callback that ensures that the div will show when the user hoves over the reference
  $('#translated').hoverIntent({
    over: function(e)
    {
      $('div#hover').fadeIn(250)
        .css('top', mouseY + CalculateOffset(e, false))
        .css('left', mouseX + CalculateOffset(e, true))
        .appendTo('body');
    },
    out: function()
    {
      $('div#hover').hide();
    },
    selector: '.word-help'});

  // Callback to make sure the div stays close to the mouse
  $('body').on('onmousemove', '.word-help', function(e) {
    mouseX = e.pageX;
    mouseY = e.pageY;
    var posX = e.pageX + CalculateOffset(e, true);
    var posY = e.pageY + CalculateOffset(e, false);
    $("div#hover").css('top', posY).css('left', posX);
  });

  // Callback that loads the content via ajax in the div
  $('body').on('mouseenter', '.word-help', function(e) {
    $('div#hover').hide();
    $('div#hover').html('');
    var postData = {'concept': $(e.target).text()};
    $.post('/app/concepts/', postData, function(data){
      console.log(data);
    }).fail( function() {
      console.log("An error occured");
    });
  });
  // Ensures that if the user accidentilly enters the hover div, it's still able to hide it by removing the mouse from this div
  $('body').on('mouseleave', 'div#hover', function(e) {
    $(this).hide();
  });
}
*/