odoo.define('darb_puthod', function(require) {
    'use strict';
    require('website.website');
	
	$('.pointer').on('click', function(ev) {
        ev.preventDefault();
        $(this).parents('tr').find(".pointer").toggleClass('hidden');
        $(this).parents('tr').find(".depointer").toggleClass('hidden',false);
		console.log($(this).parents('tr').find(".membrid").val());  
		$.ajax({
			type: "POST", 
			url: "/pointer", 
			async: false, 
			data: JSON.stringify({}), 
			contentType: "application/json", 
			complete: function (data) {
				console.log(data);  
			}
		});
		
    });
	
	
	$('.depointer').on('click', function(ev) {
        ev.preventDefault();
        $(this).parents('tr').find(".depointer").toggleClass('hidden');
        $(this).parents('tr').find(".pointer").toggleClass('hidden',false);
		
		console.log($(this).parents('tr').find(".membrid").val());  
		$.ajax({
			type: "POST", 
			url: "/pointer", 
			async: false, 
			data: JSON.stringify({}), 
			contentType: "application/json", 
			complete: function (data) {
				console.log(data);  
			}
		});
    });
});
