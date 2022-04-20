function ready(){
  document.querySelector("#waveslink .nav-link").classList.add("active");
  document.querySelector(`li[data-value='${math}'] a`).classList.add("active");
}

function handleChange() {
  const func = DOMPurify.sanitize(math);
  const coef = DOMPurify.sanitize(document.getElementById("coef").value);
  const img = `/${math}/${coef}`;

  document.getElementById("graph").setAttribute("src", img);
}

if (document.readyState !== "loading") {
  ready();
} else {
  document.addEventListener("DOMContentLoaded", ready);
}
