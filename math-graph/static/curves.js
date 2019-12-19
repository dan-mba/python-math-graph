$(function(){
  $("#waveslink").addClass("active");
})

function handleChange(e) {
  const math = $("#math").val();
  const a = $("#a").val();
  const b = $("#b").val();
  const img = '/' + math + '/' + a + '/' + b;

  $("#graph").attr("src", img);
}
