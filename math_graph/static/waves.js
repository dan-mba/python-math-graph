function ready(){
  document.querySelector("#waveslink .nav-link").classList.add("active");
}

function handleChange(e) {
  const math = DOMPurify.sanitize(document.getElementById("math").value);
  const coef = DOMPurify.sanitize(document.getElementById("coef").value);
  const img = '/' + math + '/' + coef;

  document.getElementById("graph").setAttribute("src", img);
}

if (document.readyState !== "loading") {
  ready();
} else {
  document.addEventListener("DOMContentLoaded", ready);
}
