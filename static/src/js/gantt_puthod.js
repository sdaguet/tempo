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
			var list = []
			$.each(data['responseJSON']["result"], function( key, value ) {
				var today = moment();
				var andTwoHours = moment().add("hours",key);
				list.push({
					name: value.name,
					desc: value.desc,
					values: [{
						from: "/Date(" + today.valueOf() + ")/",
						to: "/Date(" + andTwoHours.valueOf() + ")/",
						label: value.values[0].label, 
						customClass: value.values[0].customClass
						}]
					});
				console.log("1111111111111");
				console.log("/Date(" + andTwoHours.valueOf() + ")/");
				console.log(value.values[0].to);
				console.log(andTwoHours.valueOf());
				console.log("22222222222222");
				}
			);
			console.log("chart rendering");
			$(".gantt").gantt({
				//source: data,
				source: list,
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