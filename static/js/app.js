function update() {
    console.log("update now")
}

$(document).ready(function(){

    $("form").submit(function(event) {
        inp = $(this).serializeArray();
        $.post('/update', 
        {
            name: inp[0]['value'],
            age: inp[1]['value']
        }, 
        function(data, status){
            displayList();
            document.getElementById("myform").reset(); 
        })
        event.preventDefault();
    });
    function displayList() {
        $.get("/getall", function(data, status) {
            displayHtml = "";
            for (i in data) {
                displayHtml += data[i][0] + " was born in " + data[i][1] + "<br>";
            }
            $("#namelist").html(displayHtml);
        })
    }
    displayList();
});