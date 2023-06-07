function ready(){
  document.querySelector("#curveslink a").classList.add("active");
  document.querySelector(`li[data-value='${math}'] a`).classList.add("active");
  if (math === "exp" || math === "expf") {
    document.getElementById("b").setAttribute("min", "1");
  }
  handleChange();
}

async function handleChange(e) {
  const func = DOMPurify.sanitize(math);
  const a = DOMPurify.sanitize(document.getElementById("a").value);
  const b = DOMPurify.sanitize(document.getElementById("b").value);
  const route = `/${math}/${a}/${b}`;

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
