let rform=document.querySelector("#register_form")
rform.onsubmit=function(){
//$("#register_form").onsubmit(function(){
    // pass the current username into check as the username value
    $.get("/check", {username:$("#uname").value}, function(data){
        // if data that is returned is true, submit form. Function will deal with what happens when we get a response from check
        if(data){
            $("#register-form").submit();
        }
        alert("username already exists!")
        return false;

    });
}
// prints data back, useful but not needed
// console.log("");