d3.select("#startDate").on("change", update_start);
d3.select("#endDate").on("change", update_end);

function update_start() {
    document.getElementById("endDate").min = date;
}
function update_end() {
    var date = endDate.value;// startDate.value;
    document.getElementById("startDate").max = date;

}
