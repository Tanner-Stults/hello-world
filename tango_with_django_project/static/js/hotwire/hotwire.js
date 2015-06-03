$(document).ready(function(){
    $("#test").click(function(){
        console.log("clicked!");
        searchHotels("Boston","06/20/2015","06/22/2015");
    });
});


function searchHotels(dest, startdate, enddate){
    var apikey = "fj25bnus8zedsk6fjd9bha3q";
    formatVar = "JSONP";
    rooms = 1;
    adults = 1;
    children = 0;
    var url = "http://api.hotwire.com/v1/search/hotel"
    var values = {
        "apikey":       apikey,
        "format":       formatVar,
        "dest":         dest, //To be hooked into?
        "rooms":        rooms,
        "adults":       adults, 
        "children":     children,
        "startdate":    startdate,
        "enddate":      enddate
    }
    var data = $.param(values)
    url = url + "?" + data
    console.log("url: " + url)
    ajaxCall(url)
};
function ajaxCall(apiUrl){
    console.log("in ajaxCall")
    var call = $.get({
        url:   apiUrl,
        success: function(data){response(data)},
        dataType: "JSONP"
    }).fail(function() {
        console.log('whoops'); // or whatever
    });
}
function response(returnedData){
        console.log(returnedData);
}

function Hotel (type) {
    this.hotelDict = hotelDict
    this.amenitiesDict = amenitiesDict
    this.neighborhoodsDict = neighborhoodsDict
    this.amenities = []
    this.city = ""
    this.starRating = 0
    this.deepLink = ""
    this.averagePricePerNight = 0
    this.savingsPrecentage = 0
    this.recommendationPercentage = 0
    this.resultId = 0
};
 
Hotel.prototype.cleanHotel = function() {
    /* --- Get Amenities --- */
    codes = this.hotelDict["AmenityCodes"]
    translatedCodes = []
    for (code in codes){
        trans = this.amenCodeToName(this.amenitiesDict, code)
        if (trans){
            translatedCodes.append(trans)
        }
    }
    this.amenities = translatedCodes
    
    /* --- Get City --- */
    neighborId = this.hotelDict["NeighborhoodId"]
    this.city = this.neighboorIdToCity(neighborId)
    
    /* --- Get StarRating --- */
    this.starRating = this.hotelDict["StarRating"]
    
    /* --- Get deepUrl --- */
    this.deepLink = this.hotelDict["DeepLink"]
 
    /* --- Get averagePricePerNight --- */
    this.averagePricePerNight = this.hotelDict["AveragePricePerNight"]
  
    /* --- Get savingsPrecent --- */
    if ("SavingsPercentage" in this.hotelDict){ //This field not returned if below 0
        this.savingsPrecentage = this.hotelDict["SavingsPercentage"]
    }
    else{
        this.savingsPrecentage = 0
    }
    
    /* --- Get savingsPrecent --- */
    if ("RecommendationPercentage" in this.hotelDict){ //This field not returned if below 0
        this.recommendationPercentage = this.hotelDict["RecommendationPercentage"]
    }
    else{
        this.recommendationPercentage = 0
    }
    
     /* --- Get ResultId --- */
    this.resultId = this.hotelDict["ResultId"]
};

Hotel.prototype.amenCodeToName = function(code) {
    return this.color + ' ' + this.type + ' apple';
};

Hotel.prototype.neighboorIdToCity = function(neighborId) {
    return this.color + ' ' + this.type + ' apple';
};