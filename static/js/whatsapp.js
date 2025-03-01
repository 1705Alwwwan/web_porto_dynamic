function sendToWhatsapp(){
    let number = "+6289678194404";
    let name = document.getElementById('cf-name').value;
    let email = document.getElementById('cf-email').value;
    let message = document.getElementById('cf-message').value;

    var url = "https://wa.me/" + number + "?text=" 
    + "name =" + name +  "%0a"
    + "email = " + email + "%0a"
    + "message =" + message + "%0a%0a";

    window.open(url, '_blank').focus(); 
}