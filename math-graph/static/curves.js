$(function(){
  $("#curveslink").addClass("active");
  $("form").trigger("reset");
})

function handleChange(e) {
  const math = $("#math").val();
  const a = $("#a").val();
  const b = $("#b").val();
  const img = '/' + math + '/' + a + '/' + b;

  $("#graph").attr("src", img);
}

function handleFuncChange(e) {
  const math = $("#math").val();
  if (math === "exp" || math === "expf") {
    $("#b").attr("min", "1");
    if (parseInt($("#b").val(), 10) < 1) {
      $("#b").val("1");
    }
  }
  handleChange(e);
}
