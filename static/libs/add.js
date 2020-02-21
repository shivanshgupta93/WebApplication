$(document).ready(() => {
    $("#addform").submit(function (e) { 
        var country_id = $("#countryid").val().trim()
        var country_name = $('#countryname').val().trim()
        var institution_data = {
            "institution_id": $("#institutionid").val().trim(),
            "institution_name": $("#institutionname").val().trim(),
            "city_id": $("#cityid").val().trim(),
            "city_name": $("#cityname").val().trim(),
            "country_id": country_id,
            "course_count": $("#coursecount").val().trim(),
            "country_name": country_name
        }

        $.ajax({  
                url: '/api/institutions',  
                type: 'POST',  
                dataType: 'text',  
                data: JSON.stringify(institution_data), 
                contentType: 'application/json', 
                success: function (response) {  
                    alert(response);  
                    document.getElementById("addform").reset();
                },  
                error: function () {  
                    alert("Error please try again");  
                }  
            });
    });
    });