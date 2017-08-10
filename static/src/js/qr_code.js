odoo.define('darb_puthod.responsivejson', function(require) {
    'use strict';
    require('website.website');
    require('web.ajax');

    $('.qrcode').on('click', function(ev) {
        ev.preventDefault();
        var qrcode = $('#qrcode').val();
        var qty = $('#qty').val();
        var fiche_id = $('#fiche_id').val();
		console.log(fiche_id);
		$.ajax({
			type: "POST",
			url: "/qrcode",
			async: false,
			data: JSON.stringify({"params": {'fiche': fiche_id, 'qrcode': qrcode, 'qty': qty}}),
			contentType: "application/json",
			complete: function (data) {
				console.log(data);
				if (data['responseJSON']["result"]["error_message"].length != 0){
				$(".error_qrcode").remove();
				$('#main_qrcode').before(
				'<div class="col-md-12">'+
				  '<div class="alert alert-danger error_qrcode">'+
				      '<p>'+data['responseJSON']["result"]["error_message"]+'</p>'+
				  '</div>'+
				'</div>'
				);
				}
				else {
				$(".error_qrcode").remove();
				$("#qrcode").val("");
				$("#qty").val("");
				}
			}
		});

    });
	
});
