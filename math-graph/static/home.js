function handleChange(e) {
  const math = $("#math").val();
  const coef = $("#coef").val();
  const img = '/' + math + '/' + coef;

  $("#graph").attr("src", img);
}
