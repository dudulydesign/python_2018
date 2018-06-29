<script>
  function cutStr(len){
    var obj=document.getElementById("table").getElementsByTagName("td");
    for(i=0; i < obj.length; i++){
      obj[i].innerHTML=obj[i].innerHTML.substring(0,len)+"...";
    }
  }
</script>
