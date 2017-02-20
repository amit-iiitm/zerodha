"use strict";

function append_to_dom(data) {
    var data = JSON.parse(data)
    if (data.length == 0) {
        return
    }
    var blocks = data.map(function (gainer) {
        var block = "<div class='col-sm-4'><div class='card' style='width: 40rem;border-radius:5px;background-color:#3CB371;text-align:center'><div class='container'><h4 class='card-title' style='font-family: 'Playfair Display', serif;'>" + gainer.symbol;
        block += " " + "</h4><p class='card-text' style='margin-top:-15px'>" + " &nbsp  Ltp: " + gainer.ltp + "<br>";
        block += " &nbsp  Openprice: " + gainer.openPrice + "<br>" +" &nbsp  Highprice: "
        block += gainer.highPrice + "<br> &nbsp Traded quantity: "+ gainer.tradedQuantity + "<br> &nbsp Turnover(in lakhs): "+ gainer.turnoverInLakhs+ "<br> &nbsp Net price(%change): "+ gainer.netPrice +"<br></p></div></div><br></div>";
        return block;
    });
	$("#realtime").empty()
    $("#realtime").prepend(blocks);
    $("#realtime").attr("modified", Date.now());
}

function doPoll() {
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
