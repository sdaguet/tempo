odoo.define('darb_puthod.responsivejson', function(require) {
    'use strict';
    require('website.website');
    require('web.ajax');

    $('.addvehicles').on('click', function(ev) {
        ev.preventDefault();
		var vehicle_id = $('#vehicle_id option:selected').val();
		var fiche_id = $('#fiche_id').val();
		var km = $(this).parents('tr').find(".vkm").val();
		$.ajax({
			type: "POST",
			url: "/addvehicles",
			async: false,
			data: JSON.stringify({"params": {'fiche': fiche_id, 'vehicle': vehicle_id, 'km': km}}),
			contentType: "application/json",
			complete: function (data) {
				console.log(data);
				if (data['responseJSON']["result"]["error_message"].length != 0){
				console.log("ereuuuuuuuuuuuuuuuuuuuuuuuur");
				$('#main_vehicle').before('<div class="col-md-12">'+
				  '<div id="error" class="alert alert-danger">'+
				      '<p>'+data['responseJSON']["result"]["error_message"]+'</p>'+
				  '</div>'+
				'</div>'
				);
				}
				else {
				$('#table_vehicle tr:last').before('<tr><td>'+ data['responseJSON']["result"]["vehicle"] +'</td><td>'+ data['responseJSON']["result"]["km"] +'</td><td><a class="btn btn-primary deletevehicles">Supprimer</a></td></tr>');
				$("#error").hide()
				$("#vehicle_id").val("");
				$('input.vkm').val('');
				}
			}
		});

    });

   
    $('.addmateriel').on('click', function(ev) {
        ev.preventDefault();
		console.log("IIIIIIIIIIIIIIIIIINNNNNNNNNNNNNNNN");
		var materiel_id = $('#materiel_id option:selected').val();
		var fiche_id = $('#fiche_id').val();
		var temps = $(this).parents('tr').find(".temps").val();
		$.ajax({
			type: "POST",
			url: "/addmateriel",
			async: false,
			data: JSON.stringify({"params": {'fiche': fiche_id, 'materiel': materiel_id, 'temps': temps}}),
			contentType: "application/json",
			complete: function (data) {
				console.log(data);
				if (data['responseJSON']["result"]["error_message"].length != 0){
				console.log("ereuuuuuuuuuuuuuuuuuuuuuuuur");
				$('#main_materiel').before('<div class="col-md-12">'+
				  '<div id="error" class="alert alert-danger">'+
				      '<p>'+data['responseJSON']["result"]["error_message"]+'</p>'+
				  '</div>'+
				'</div>'
				);
				}
				else {
				$('#table_materiel tr:last').before('<tr><td>'+ data['responseJSON']["result"]["materiel"] +'</td><td>'+ data['responseJSON']["result"]["temps"] +'</td><td><a class="btn btn-primary deletevehicles">Supprimer</a></td></tr>');
				$("#error").hide()
				$("#materiel_id").val("");
				$('input.temps').val('');
				}
			}
		});

    });
    

    $('.addmachine').on('click', function(ev) {
        ev.preventDefault();
		console.log("IIIIIIIIIIIIIIIIIINNNNNNNNNNNNNNNN");
		var machine_id = $('#machine_id option:selected').val();
		var fiche_id = $('#fiche_id').val();
		var temps = $(this).parents('tr').find(".mtemps").val();
		$.ajax({
			type: "POST",
			url: "/addmachine",
			async: false,
			data: JSON.stringify({"params": {'fiche': fiche_id, 'machine': machine_id, 'temps': temps}}),
			contentType: "application/json",
			complete: function (data) {
				console.log(data);
				if (data['responseJSON']["result"]["error_message"].length != 0){
				console.log("ereuuuuuuuuuuuuuuuuuuuuuuuur");
				$('#main_machine').before('<div class="col-md-12">'+
				  '<div id="error" class="alert alert-danger">'+
				      '<p>'+data['responseJSON']["result"]["error_message"]+'</p>'+
				  '</div>'+
				'</div>'
				);
				}
				else {
				$('#table_machine tr:last').before('<tr><td>'+ data['responseJSON']["result"]["machine"] +'</td><td>'+ data['responseJSON']["result"]["temps"] +'</td><td><a class="btn btn-primary deletevehicles">Supprimer</a></td></tr>');
				$("#error").hide()
				$("#machine_id").val("");
				$('input.mtemps').val('');
				}
			}
		});

    });
	
});
