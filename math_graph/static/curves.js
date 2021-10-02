function ready(){
  document.querySelector("#curveslink .nav-link").classList.add("active");
  document.querySelector("form").reset();
}

function handleChange(e) {
  const math = DOMPurify.sanitize(document.getElementById("math").value);
  const a = DOMPurify.sanitize(document.getElementById("a").value);
  const b = DOMPurify.sanitize(document.getElementById("b").value);
  const img = '/' + math + '/' + a + '/' + b;

  document.getElementById("graph").setAttribute("src", img);
}

function handleFuncChange(e) {
  const math = document.getElementById("math").value;
  if (math === "exp" || math === "expf") {
    document.getElementById("b").setAttribute("min", "1");
    if (parseInt(document.getElementById("b").value, 10) < 1) {
      document.getElementById("b").value = 2;
    }
  }
  handleChange(e);
}

if (document.readyState !== "loading") {
  ready();
} else {
  document.addEventListener("DOMContentLoaded", ready);
}
