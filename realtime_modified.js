

function append_to_dom(data) {
    var data = JSON.parse(data)
    if (data.length == 0) {
        return
    }
	console.log(data.length);
    var blocks = data.map(function (top_gainers) {
        var block = "<div class='card' style='width: 20rem;background-color:lavender;'><div class='card-block'><h4 class='card-title'>" + 		                top_gainers.symbol;
        block += ", " + top_gainers.ltp + "</h4>";
        block += "<div class=card-text>" + top_gainers.openPrice + " "
        block += top_gainers.highPrice + "</div></div></div>";
		console.log(block)
        return block;
    });
    $("#realtime").prepend(blocks).hide().fadeIn();
    $("#realtime").attr("modified", Date.now());
}

function doPoll() {
	console.log("before ajax")
    $.ajax({
        url: "update",
        data: {
            "timestamp": parseInt($('#realtime').attr("modified") / 1000) || 0
        }
    }).done(function (data) {
        append_to_dom(data);
    }).always(function () {
        setTimeout(doPoll, 5000);
    })
}


$(document).ready(function () {
    doPoll();
})
