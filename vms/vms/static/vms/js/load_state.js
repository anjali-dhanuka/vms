/** Fetches states belonging to selected  country */
$(document).ready(function() {
    $("#select_country").change(function() {
        var countryId = $(this).val();
        $.ajax({
            url: CheckState,
            data: {
                "country": countryId
            },
            success: function(statecheck) {
                if (statecheck === 0) {
                    $("#div_id_state").hide();
                    $.ajax({
                        url: CityUrl,
                        data: {
                            "country": countryId,
                            "state": 0
                        },
                        success: function(cities) {
                            $("#select_city").html(cities);
                        }
                    });
                } else if (statecheck === 1) {
                    $.ajax({
                        url: StateUrl,
                        data: {
                            "country": countryId
                        },
                        success: function(states) {
                            $("#select_state").html(states);
                            $("#select_city").empty();
                        }
                    });
                }
            }
        });
    });
});