
$(document).ready(function() {
    // Let's add the listener to the refresh button
    $("#RefreshButton").click(function(){
        // We need to get the latest info from the server
        $.get("/api/disc/", function( data ) {
            $("#Result").html( data );
            result = $.parseJSON(data)
            for (var r in result) {
                var disc = result[r];
                id = "#Space" + disc.row + disc.column;
                if (disc.color == "r") {
                    $(id).addClass("red").removeClass("yellow");
                }else {
                    $(id).addClass("yellow").removeClass("red");
                }
            }
        });
    });

    // Attach a submit handler to the form
    $( ".gridrow form" ).submit(function( event ) {

        // Stop form from submitting normally
        event.preventDefault();

        // Get some values from elements on the page:
        var $form = $( this ),
        column = $form.find( "input[name='column']" ).val(),
        color = $form.find( "input[name='color']" ).val(),
        csrf = $form.find( "input[name='csrfmiddlewaretoken']" ).val(),
        
        url = $form.attr( "action" );

        // Send the data using post
        var posting = $.post( url, { "column": column, "color": color, "csrfmiddlewaretoken": csrf } );

        // Put the results in a div
        posting.done(function( data ) {
            $("#RefreshButton").click();
        });
    });

    var refreshId = setInterval(function(){
        $("#RefreshButton").click();
    }, 1000);
})