odoo.define('darb_puthod.responsivejson', function(require) {
    'use strict';
    require('website.website');
    require('web.ajax');

    $('.addvehicles').on('click', function(ev) {
        ev.preventDefault();
		console.log("IIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIII");
		var vehicle_id = $('#vehicle_id option:selected').val();
		var km = $(this).parents('tr').find(".kname").val();
		console.log(km);
		console.log("KKKKKKKKKKKKKKKKKKKKKKK");
		console.log(vehicle_id);
		$.ajax({
			type: "POST",
			url: "/ajaxi",
			async: false,
			data: JSON.stringify({"params": {'fiche': 'km'}}),
			contentType: "application/json",
			complete: function (data) {
				console.log("mmmmmmmmmmmmmmm");
			}
		});

    });
	
});
