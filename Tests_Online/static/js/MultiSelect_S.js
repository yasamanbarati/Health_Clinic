const downBtn = document.querySelector(".filter_close1");
const inputText = document.getElementById("dis_input1");
const disBox = document.querySelector("#dis_box1");
const formBox = document.querySelector('#wizard');
function filterFunc() {
    var  filter, a, i;
    filter = inputText.value.toUpperCase();
    div = document.getElementById("myDropdown1");
    a = div.getElementsByTagName("a");
    console.log(a);
    for (i = 0; i < a.length; i++) {
        txtValue = a[i].textContent || a[i].innerText;
        if (txtValue.toUpperCase().indexOf(filter) > -1) {
            a[i].style.display = "";
        } else {
            a[i].style.display = "none";
        }
    }
} 
function showDownBtn1() {
    downBtn.classList.add("showIcon");
}
// ایجاد بیماری ها
formBox.addEventListener('submit', (e) => {
    e.preventDefault();
})
function dropdwnValue1(dropdwnValueT) {
    console.log(dropdwnValueT.innerHTML);
    if (!inputText.value){

    }else{
        inputText.value = dropdwnValueT.innerHTML;
        showDownBtn1();
    }
}
function createDic1() {
    const text = inputText.value;

    // create dic value
    let dicBox_span = document.createElement("span");
    dicBox_span.classList.add("dis_box_span");
    dicBox_span.innerHTML = text;
    disBox.appendChild(dicBox_span);

    let dicBox_btn = document.createElement("button");
    dicBox_btn.classList.add("dis_box_btn");
    dicBox_span.appendChild(dicBox_btn);

    let dicBox_i = document.createElement("i");
    dicBox_i.classList.add("material-icons");
    dicBox_i.innerHTML = "close";
    dicBox_btn.appendChild(dicBox_i);


    inputText.value = " ";
    console.log(text);

}