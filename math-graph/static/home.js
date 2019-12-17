function handleChange(e) {
  console.log("Change");
  const math = document.getElementById("math").value;
  const coef = document.getElementById("coef").value;
  const img = document.getElementById("graph");

  img.src = '/' + math + '/' + coef;
}
