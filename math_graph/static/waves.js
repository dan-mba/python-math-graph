function ready(){
  document.querySelector("#waveslink .nav-link").classList.add("active");
  document.querySelector(`li[data-value='${math}'] a`).classList.add("active");
  handleChange();
}

async function handleChange() {
  const func = DOMPurify.sanitize(math);
  const coef = DOMPurify.sanitize(document.getElementById("coef").value);
  const route = `/${math}/${coef}`;

  const response = await fetch(route);
  const item = await response.json();
  document.getElementById("graph").textContent = '';
  Bokeh.embed.embed_item(item, "graph");
}

if (document.readyState !== "loading") {
  ready();
} else {
  document.addEventListener("DOMContentLoaded", ready);
}
