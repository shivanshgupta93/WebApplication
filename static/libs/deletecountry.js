$(document).ready(() => {
    $("#deletecountryform").submit(function (e) { 
        var country_id = $("#countryid").val().trim()
        var country_data = {}

        $.ajax({  
                url: '/api/countries/' + country_id,  
                type: 'DELETE',  
                dataType: 'text',  
                data: JSON.stringify(country_data), 
                contentType: 'application/json', 
                complete: function (response, textStatus) {  
                alert(textStatus);  
                document.getElementById("deletecountryform").reset();  
                },  
                error: function () {  
                alert("Error please try again");  
                }  
            });
    });
    });