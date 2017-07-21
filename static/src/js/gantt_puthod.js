$(function() {	
	"use strict";
	
	var rrr = 3;//$('#ganttx').text();
	$('#ganttx').toggleClass('hidden');
	console.log(rrr);
	$.ajax({
		type: "POST",
		url: "/getgantt/" + rrr,
		async: false,
		data: JSON.stringify({'fiche' : rrr}),
		contentType: "application/json",
		complete: function (data) {
			console.log("chart rendering");
			$(".gantt").gantt({
				source: data,
				navigate: "scroll",
				scale: "hours",
				maxScale: "hours",
				minScale: "hours",
				itemsPerPage: 10,
				onRender: function() {
					if (window.console && typeof console.log === "function") {
						console.log(data);
					}
				

					//prettyPrint();
				}
				
		});
		console.log(data);
			
		}
	});
	
	$(".gantt").popover({
		selector: ".bar",
		title: "I'm a popover",
		content: "And I'm the content of said popover.",
		trigger: "hover"
	});

	prettyPrint();
});