$(document).ready(()=>{
    $(".nav-menu").click(()=>{
        $(".navbar_side_menu").slideToggle(1000);
        $("body").addClass("modal-open")
    });
    $(".menu_control_btn").click(()=>{
        $(".navbar_side_menu").slideUp(600);
        $("body").removeClass("modal-open")
    })
})

const formU = document.querySelector('#formUpdate');
const editBtn = document.querySelectorAll('.Edit');
const task_input_el = document.querySelectorAll('.form-control');

formU.addEventListener('submit', (e)=>{
    e.preventDefault();
    for (let i = 0; i < editBtn.length; i++) {
        editBtn[i].addEventListener('click', () => {
            if (editBtn[i].innerHTML == "ویرایش") {
                task_input_el[i].removeAttribute("readonly");
                task_input_el[i].focus();//ایجاد امکان تایپ
                editBtn[i].innerText = "زخیره";
            }else{
                task_input_el[i].setAttribute("readonly", "readonly");
                editBtn[i].innerText = "ویرایش";
            }
        });
         
     }
})