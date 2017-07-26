odoo.define('darb_puthod.responsivejson', function(require) {
    'use strict';
    require('website.website');
    require('web.ajax');

    $('.deletevehicles').on('click', function(ev) {
        ev.preventDefault();
        var fiche_id = $('#fiche_id').val();
        var fiche_veicule_id = $('#fiche_veicule_id').val();
		console.log("INNNNNNNNNNN");
		console.log(fiche_veicule_id);
		$.ajax({
			type: "POST",
			url: "/deletevehicles",
			async: false,
			data: JSON.stringify({"params": {'fiche': fiche_id, 'fiche_veicule': fiche_veicule_id}}),
			contentType: "application/json",
			complete: function (data) {
				console.log("mmmmmmmmmmmmmmm");  
			}
		});

    });
	
});
