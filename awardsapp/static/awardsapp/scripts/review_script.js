window.addEventListener('load', function () {
//    var design_slider = document.getElementById("design");
//    var design_output = document.getElementById("design_txt");
//    design_output.innerHTML = design_slider.value;

//    var usability_slider = document.getElementById("usability");
//    var usability_output = document.getElementById("usability_txt");
//    usability_output.innerHTML = design_slider.value;

    initial_seek_val("design")
    initial_seek_val("usability")
    initial_seek_val("content")

})

function initial_seek_val (seek_id){
    var slider = document.getElementById(seek_id.toString());
    var output = document.getElementById(seek_id.toString() + "_txt");
    output.innerHTML = slider.value;
    console.log("The initial value is " + slider.value.toString());
}

function update_design_seek(updated_val){
    var output = document.getElementById("design_txt");
    console.log("The updated value is " + updated_val.toString());
    output.innerHTML = updated_val;
}

function update_usability_seek(updated_val){
    var output = document.getElementById("usability_txt");
    console.log("The updated value is " + updated_val.toString());
    output.innerHTML = updated_val;
}

function update_content_seek(updated_val){
    var output = document.getElementById("content_txt");
    console.log("The updated value is " + updated_val.toString());
    output.innerHTML = updated_val;
}