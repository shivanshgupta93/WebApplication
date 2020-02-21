$(document).ready(() => {
    $("#updatecountryform").submit(function (e) { 
        var country_id = $("#countryid").val().trim()
        var country_name = $('#countryname').val().trim()
        var country_data = {
            "country_id": country_id,
            "country_name": country_name
        }

        $.ajax({  
                url: '/api/countries/' + country_id,  
                type: 'PUT',  
                dataType: 'text',  
                data: JSON.stringify(country_data), 
                contentType: 'application/json', 
                complete: function (response, textStatus) {  
                alert(textStatus);  
                document.getElementById("updatecountryform").reset();  
                },  
                error: function () {  
                alert("Error please try again");  
                }  
            });
    });
    });