$(document).ready(function(){
  $("#img1").hover(function(){
    $(".m-img").css("background-image","url(./img/img.jpg)");
  });
  $("#img2").hover(function(){
    $(".m-img").css("background-image","url(./img/img2.jpg)");
  });
  $("#img3").hover(function(){
    $(".m-img").css("background-image","url(./img/img3.jpg)");
  });
});

$(document).ready(function(){

  $(".login-btn").hover(function(){
    var name = $("#user").val();

    var judge = name.substring(0, 3);

    if (judge == "U20") {
      console.log(judge);
      $("#login").attr("href", "choose");
    } else {

      $("#login").attr("href", "#");
    }
  });
  $(".login-btn").click(function(){
    var name = $("#user").val();
    var judge = name.substring(0, 3);
    console.log(judge);

    if (judge == "U20") {
    } else {

      alert("Username error");
    }

  });


});
