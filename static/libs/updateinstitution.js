$(document).ready(() => {
    $("#updateinstitutionform").submit(function (e) { 
        var country_id = $("#inscountryid").val().trim()
        var institution_id = $("#institutionid").val().trim()
        var institution_data = {
            "institution_id": institution_id,
            "institution_name": $("#institutionname").val().trim(),
            "city_id": $("#cityid").val().trim(),
            "city_name": $("#cityname").val().trim(),
            "country_id": country_id,
            "course_count": $("#coursecount").val().trim()
        }

        $.ajax({  
                url: '/api/institutions/'+ institution_id,  
                type: 'PUT',  
                dataType: 'text',  
                data: JSON.stringify(institution_data), 
                contentType: 'application/json', 
                complete: function (response, textStatus) {  
                alert(textStatus);  
                document.getElementById("updateinstitutionform").reset();  
                },  
                error: function () {  
                alert("Error please try again");  
                }  
            });
    });
    });