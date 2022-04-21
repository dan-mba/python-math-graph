function ready(){
  document.querySelector("#curveslink .nav-link").classList.add("active");
  document.querySelector(`li[data-value='${math}'] a`).classList.add("active");
  if (math === "exp" || math === "expf") {
    document.getElementById("b").setAttribute("min", "1");
  }
}

function handleChange(e) {
  const func = DOMPurify.sanitize(math);
  const a = DOMPurify.sanitize(document.getElementById("a").value);
  const b = DOMPurify.sanitize(document.getElementById("b").value);
  const img = `/${math}/${a}/${b}`;

  document.getElementById("graph").setAttribute("src", img);
}

if (document.readyState !== "loading") {
  ready();
} else {
  document.addEventListener("DOMContentLoaded", ready);
}
