function getwebgantt() {	
	"use strict";
	
	var fiche_id = $('#fiche_id').val();
	$.ajax({
		type: "POST",
		url: "/getgantt",
		async: false,
		data: JSON.stringify({"params": {'fiche': fiche_id}}),
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
				}
			);
			console.log(list);
			$(".gantt").gantt({
				//source: data,
				source: list,
				navigate: "buttons",
                scale: 'hours', 
                maxScale: 'days', 
                minScale: 'hours',
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
};

$(function() {getwebgantt();});