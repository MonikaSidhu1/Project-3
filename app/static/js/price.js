$("#price").click(() =>{
    var BEDROOMS = $("#BEDROOMS").val();
    var BATHROOMS = $("#BATHROOMS").val();
    var LAND_AREA = $("#LAND_AREA").val();
    var CBD_DIST = $("#CBD_DIST").val();
    var GARAGE = $("#GARAGE").val();
    var NEAREST_SCH_RANK = $("#NEAREST_SCH_RANK").val()
    var NEAREST_STN_DIST = $("#NEAREST_STN_DIST").val()

    console.log(BEDROOMS)
    console.log(BATHROOMS)
    console.log(LAND_AREA)
    console.log(CBD_DIST)
    console.log(GARAGE)
    console.log(NEAREST_SCH_RANK)
    console.log(NEAREST_STN_DIST)


    $.getJSON(`/api/predict/${BEDROOMS}/${BATHROOMS}/${LAND_AREA}/${CBD_DIST}/${GARAGE}/${NEAREST_SCH_RANK}/${NEAREST_STN_DIST}`)(predicted) => { 
        var price =Math.floor(predicted.prediction)
        
        $("#predict").html
    
    }
})