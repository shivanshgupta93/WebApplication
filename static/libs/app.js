$(document).ready(() => {
    console.log(document.URL+"/api/countries")
    $.get("/api/countries", (countries, err) => {
    $.get("/api/institutions", (institutions, err) => {
        if (err !== "success") console.error(err);
        if (institutions && Array.isArray(institutions.data)) {
            for(var i=0; i<institutions.data.length; i++)
            {
                for(var j=0; j<countries.data.length; j++)
                {
                    if (institutions.data[i]["country_id"] == countries.data[j]["country_id"])
                    {
                    $('#detailstable').append('<tr><td>'+institutions.data[i]["institution_id"]+
                    '<td>'+institutions.data[i]["institution_name"]+'</td>'+
                    '<td>'+institutions.data[i]["city_id"]+'</td>'+
                    '<td>'+institutions.data[i]["city_name"]+'</td>'+
                    '<td>'+institutions.data[i]["country_id"]+'</td>'+
                    '<td>'+countries.data[j]["country_name"]+'</td>'+
                    '<td>'+institutions.data[i]["course_count"]+'</td>'+
                    '</td></tr>')        
                    }
                }
            }
        }
    })
})
});