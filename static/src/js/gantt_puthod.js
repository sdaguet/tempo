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
				list.push({
					name: value.name,
					desc: value.desc,
					values: []
					});
				var i = 2
				$.each(value.values, function( key2, value2 ) {
					console.log(i);
					list[key]['values'].push({
						from: "/Date(" + value2.from + ")/",
						to: "/Date(" + value2.to + ")/",
						label: value2.label, 
						customClass: value2.customClass
						});
					});
				console.log("1111111111111");
				console.log(list);
				}
			);
			console.log("chart rendering");
			$(".gantt").gantt({
				//source: data,
				source: list,
				navigate: "buttons",
                scale: 'hours', 
                maxScale: 'days', 
                minScale: 'hours',
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
});