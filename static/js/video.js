var url =  window.location.href ;

$(document).ready(function(){

   var reg = /id=\d/;
   url=(reg.exec(url));
   var list=new Array();
   var name=new Array();
   name[1] = "常见实验室事故及处理预案";
   name[2] = "生物实验室基础知识";
   name[3] = "实验室摇床安全操作";
   name[4] = "通风橱的安全操作";
   name[5] = "DNA污染保护";
   var list2=new Array();
   if (url == "id=1"){
     list[0]="done2";
     list2[0]=2;
   } else if (url == "id=2") {
     list[0]="done3";
     list2[0]=3;
     list[1]="done4";
     list2[1]=4;
   } else if (url == "id=3") {

   } else if (url == "id=4") {
     list2[0]=5;
     list[0]="done5";
   } else if (url == "id=5") {
     list2[0]=1;
     list[0]="done1";
   }
   if (list.length == 0) {
     document.write('<div>此种视频可能暂未更新</div>');
   }
   for (var i = 0 ; i < list.length ; i ++) {
     document.write('<font color= "#316B93">' + name[list2[i]] + '</font>');
     document.write('<div>');
     document.write('<video src="'+list[i]+'"controls="controls" height="349px" width="724px webkit-playsinline="true"">你的设备可能不太支持h5哦 (´・ω・`)</video>');
     document.write('</div>');
    }


});
