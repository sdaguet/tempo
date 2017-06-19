odoo.define('darb_puthod.responsivejson', function(require) {
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


	$('.edit').on('click', function(ev) {
        ev.preventDefault();
        $(this).parents('tr').find(".edit").toggleClass('hidden');

        var vname = document.getElementById('vname');
        var knames = document.getElementById('kname');
        var submit_button = document.getElementById('edit');
        value_input.addEventListener('input', function(){
        submit_button.href = "/ficheviewer/?vnane=" + vname.value +"/?knane=" + kname.value ;
        }

		console.log($(this).parents('tr').find(".vname").val());
		$.ajax({
			type: "POST",
			url: "/ficheviewer",
			async: false,
			data: JSON.stringify({}),
			contentType: "application/json",
			complete: function (data) {
				console.log(data);
			}
		});
    });
});
