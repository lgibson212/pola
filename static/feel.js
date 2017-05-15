$(document).on('click', '.rate', function(){
    console.log($(this).text());
    localStorage.setItem("rating", $(this).text());
    location.href = "/photo";
});