// https://observablehq.com/@d3/parallel-coordinates@152
export default function define(runtime, observer) {
  const main = runtime.module();
  // const fileAttachments = new Map([["cars.csv",new URL("./files/4cb40b94ee98c9296d28913c84e041a1bba5e6821131116b506dcbbfa383592985d94310ad25deb564b61d14ed20fd17c014ed38ab465d0a717dd81e4ea5759e",import.meta.url)]]);
  const fileAttachments = new Map([["cars.csv",new URL("/../CovidTrackingProject/Daily/State/ak/20200306.csv",import.meta.url)]]);
  main.builtin("FileAttachment", runtime.fileAttachments(name => fileAttachments.get(name)));
  main.variable(observer()).define(["md"], function(md){return(
md`# COVID 19 Data By State`
)});
  main.variable(observer("viewof keyz")).define("viewof keyz", ["html","keys"], function(html,keys)
{
  const form = html`<form>${Object.assign(html`<select name=select>${keys.map(key => Object.assign(html`<option>`, {value: key, textContent: key}))}</select>`, {value: "weight (lb)"})} <i style="font-size:smaller;">color encoding</i>`;
  form.select.onchange = () => (form.value = form.select.value, form.dispatchEvent(new CustomEvent("input")));
  form.select.onchange();
  return form;
}
);
  main.variable(observer("keyz")).define("keyz", ["Generators", "viewof keyz"], (G, _) => G.input(_));
  main.variable(observer("chart")).define("chart", ["d3","DOM","width","height","data","keyz","z","x","y","keys","margin"], function(d3,DOM,width,height,data,keyz,z,x,y,keys,margin)
{
  const svg = d3.select(DOM.svg(width, height));

  svg.append("g")
      .attr("fill", "none")
      .attr("stroke-width", 1.5)
    .selectAll("path")
    .data(data.slice().sort((a, b) => d3.ascending(a[keyz], b[keyz])))
    .join("path")
      .attr("stroke", d => z(d[keyz]))
      .attr("stroke-opacity", 0.4)
      .attr("d", d => d3.line()
          .defined(([, value]) => value != null)
          .x(([key, value]) => x.get(key)(value))
          .y(([key]) => y(key))
        (d3.cross(keys, [d], (key, d) => [key, d[key]])))
    .append("title")
      .text(d => d.name);

  svg.append("g")
    .selectAll("g")
    .data(keys)
    .join("g")
      .attr("transform", d => `translate(0,${y(d)})`)
      .each(function(d) { d3.select(this).call(d3.axisBottom(x.get(d))); })
      .call(g => g.append("text")
        .attr("x", margin.left)
        .attr("y", -6)
        .attr("text-anchor", "start")
        .attr("fill", "currentColor")
        .text(d => d))
      .call(g => g.selectAll("text")
        .clone(true).lower()
        .attr("fill", "none")
        .attr("stroke-width", 5)
        .attr("stroke-linejoin", "round")
        .attr("stroke", "white"));

  return svg.node();
}
);
  main.variable(observer("data")).define("data", ["d3","FileAttachment"], async function(d3,FileAttachment){return(
d3.csvParse(await FileAttachment("cars.csv").text(), d3.autoType)
)});
  main.variable(observer("keys")).define("keys", ["data"], function(data){return(
data.columns.slice(1)
)});
  main.variable(observer("x")).define("x", ["keys","d3","data","margin","width"], function(keys,d3,data,margin,width){return(
new Map(
  Array.from(
    keys,
    key => [key, d3.scaleLinear(d3.extent(data, d => d[key]), [margin.left, width - margin.right])]
  )
)
)});
  main.variable(observer("y")).define("y", ["d3","keys","margin","height"], function(d3,keys,margin,height){return(
d3.scalePoint(keys, [margin.top, height - margin.bottom])
)});
  main.variable(observer("z")).define("z", ["d3","x","keyz"], function(d3,x,keyz){return(
d3.scaleSequential(x.get(keyz).domain().reverse(), d3.interpolateBrBG)
)});
  main.variable(observer("margin")).define("margin", function(){return(
{top: 20, right: 10, bottom: 20, left: 10}
)});
  main.variable(observer("height")).define("height", ["keys"], function(keys){return(
keys.length * 120
)});
  main.variable(observer("d3")).define("d3", ["require"], function(require){return(
require("d3@5")
)});
  return main;
}
