function filterFunction() {
    var input, filter, ul, li, a, i;
    input = document.getElementById("dropdownMenuButton1");
    let inputText = document.getElementById("dropdownMenuButton1").value;

    // const done_btn = document.createElement("button");
    // done_btn.classList.add("filter_close");
    // const done_i = document.createElement("i");
    // done_i.classList.add("material-icons");
    // done_btn.appendChild(done_i);
    // inputText.appendChild(done_btn);

    filter = input.value.toUpperCase();
    div = document.getElementById("myDropdown");
    a = div.getElementsByTagName("a");
    for (i = 0; i < a.length; i++) {
        txtValue = a[i].textContent || a[i].innerText;
        if (txtValue.toUpperCase().indexOf(filter) > -1) {
            a[i].style.display = "";
        } else {
            a[i].style.display = "none";
        }
    }
}
function createSpan() {
    let inputText = document.getElementById("dropdownMenuButton1").value;
    // create dic value
    let dicBox_span = document.createElement("section");
    dicBox_span.classList.add("dis_box_span");
    let dicBox_btn = document.createElement("button");
    dicBox_btn.classList.add("dis_box_btn");
    let dicBox_i = document.createElement("i");
    dicBox_i.classList.add("material-icons");
    dicBox_btn.appendChild(dicBox_i);
    dicBox_span.appendChild(dicBox_btn);
    
}