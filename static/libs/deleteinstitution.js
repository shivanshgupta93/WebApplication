$(document).ready(() => {
    $("#deleteinstitutionform").submit(function (e) { 
        var institution_id = $("#institutionid").val().trim()
        var institution_data = {}

        $.ajax({  
            url: '/api/institutions/' + institution_id,  
            type: 'DELETE',  
            dataType: 'text',  
            data: JSON.stringify(institution_data), 
            contentType: 'application/json', 
            complete: function (response, textStatus) {  
            alert(textStatus);  
            document.getElementById("deleteinstitutionform").reset();  
            },  
            error: function () {  
            alert("Error please try again");  
            }  
        });
    });
    });