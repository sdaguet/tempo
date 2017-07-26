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
				  '<div id="error_vehicle" class="alert alert-danger">'+
				      '<p>'+data['responseJSON']["result"]["error_message"]+'</p>'+
				  '</div>'+
				'</div>'
				);
				}
				else {
				$('#table_vehicle tr:last').before('<tr><td>'+ data['responseJSON']["result"]["vehicle"] +'</td><td>'+ data['responseJSON']["result"]["km"] +'</td><td><a class="btn btn-primary deletevehicles">Supprimer</a></td></tr>');
				$("#error_vehicle").hide()
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
				  '<div id="error_materiel" class="alert alert-danger">'+
				      '<p>'+data['responseJSON']["result"]["error_message"]+'</p>'+
				  '</div>'+
				'</div>'
				);
				}
				else {
				$('#table_materiel tr:last').before('<tr><td>'+ data['responseJSON']["result"]["materiel"] +'</td><td>'+ data['responseJSON']["result"]["temps"] +'</td><td><a class="btn btn-primary deletevehicles">Supprimer</a></td></tr>');
				$("#error_materiel").hide()
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
				  '<div id="error_machine" class="alert alert-danger">'+
				      '<p>'+data['responseJSON']["result"]["error_message"]+'</p>'+
				  '</div>'+
				'</div>'
				);
				}
				else {
				$('#table_machine tr:last').before('<tr><td>'+ data['responseJSON']["result"]["machine"] +'</td><td>'+ data['responseJSON']["result"]["temps"] +'</td><td><a class="btn btn-primary deletevehicles">Supprimer</a></td></tr>');
				$("#error_machine").hide()
				$("#machine_id").val("");
				$('input.mtemps').val('');
				}
			}
		});

    });
    

    $('.addfourniture').on('click', function(ev) {
        ev.preventDefault();
		console.log("IIIIIIIIIIIIIIIIIINNNNNNNNNNNNNNNN");
		var fourniture_id = $('#fourniture_id option:selected').val();
		var fiche_id = $('#fiche_id').val();
		var qty = $(this).parents('tr').find(".qty").val();
		$.ajax({
			type: "POST",
			url: "/addfourniture",
			async: false,
			data: JSON.stringify({"params": {'fiche': fiche_id, 'fourniture': fourniture_id, 'qty': qty}}),
			contentType: "application/json",
			complete: function (data) {
				console.log(data);
				if (data['responseJSON']["result"]["error_message"].length != 0){
				console.log("ereuuuuuuuuuuuuuuuuuuuuuuuur");
				$('#main_fourniture').before('<div class="col-md-12">'+
				  '<div id="error_fourniture" class="alert alert-danger">'+
				      '<p>'+data['responseJSON']["result"]["error_message"]+'</p>'+
				  '</div>'+
				'</div>'
				);
				}
				else {
				$('#table_fourniture tr:last').before('<tr><td>'+ data['responseJSON']["result"]["fourniture"] +'</td><td>'+ data['responseJSON']["result"]["qty"] +'</td><td><a class="btn btn-primary deletevehicles">Supprimer</a></td></tr>');
				$("#error_fourniture").hide()
				$("#fourniture_id").val("");
				$('input.qty').val('');
				}
			}
		});

    });


    $('.addkit').on('click', function(ev) {
        ev.preventDefault();
		console.log("IIIIIIIIIIIIIIIIIINNNNNNNNNNNNNNNN");
		var kit_id = $('#kit_id option:selected').val();
		var fiche_id = $('#fiche_id').val();
		var qty = $(this).parents('tr').find(".kqty").val();
		$.ajax({
			type: "POST",
			url: "/addkit",
			async: false,
			data: JSON.stringify({"params": {'fiche': fiche_id, 'kit': kit_id, 'qty': qty}}),
			contentType: "application/json",
			complete: function (data) {
				console.log(data);
				if (data['responseJSON']["result"]["error_message"].length != 0){
				console.log("ereuuuuuuuuuuuuuuuuuuuuuuuur");
				$('#main_kit').before('<div class="col-md-12">'+
				  '<div id="error_kit" class="alert alert-danger">'+
				      '<p>'+data['responseJSON']["result"]["error_message"]+'</p>'+
				  '</div>'+
				'</div>'
				);
				}
				else {
				$('#table_kit tr:last').before('<tr><td>'+ data['responseJSON']["result"]["kit"] +'</td><td>'+ data['responseJSON']["result"]["qty"] +'</td><td><a class="btn btn-primary deletevehicles">Supprimer</a></td></tr>');
				$("#error_kit").hide()
				$("#kit_id").val("");
				$('input.kqty').val('');
				}
			}
		});

    });


    $('.addtuteurage').on('click', function(ev) {
        ev.preventDefault();
		console.log("IIIIIIIIIIIIIIIIIINNNNNNNNNNNNNNNN");
		var tuteurage_id = $('#tuteurage_id option:selected').val();
		var fiche_id = $('#fiche_id').val();
		var qty = $(this).parents('tr').find(".tqty").val();
		$.ajax({
			type: "POST",
			url: "/addtuteurage",
			async: false,
			data: JSON.stringify({"params": {'fiche': fiche_id, 'tuteurage': tuteurage_id, 'qty': qty}}),
			contentType: "application/json",
			complete: function (data) {
				console.log(data);
				if (data['responseJSON']["result"]["error_message"].length != 0){
				console.log("ereuuuuuuuuuuuuuuuuuuuuuuuur");
				$('#main_tuteurage').before('<div class="col-md-12">'+
				  '<div id="error_tuteurage" class="alert alert-danger">'+
				      '<p>'+data['responseJSON']["result"]["error_message"]+'</p>'+
				  '</div>'+
				'</div>'
				);
				}
				else {
				$('#table_tuteurage tr:last').before('<tr><td>'+ data['responseJSON']["result"]["tuteurage"] +'</td><td>'+ data['responseJSON']["result"]["qty"] +'</td><td><a class="btn btn-primary deletevehicles">Supprimer</a></td></tr>');
				$("#error_tuteurage").hide()
				$("#tuteurage_id").val("");
				$('input.tqty').val('');
				}
			}
		});

    });


    $('.addvigitaux').on('click', function(ev) {
        ev.preventDefault();
		console.log("IIIIIIIIIIIIIIIIIINNNNNNNNNNNNNNNN");
		var date = $(this).parents('tr').find(".date").val();
		var vigitaux_id = $('#vigitaux_id option:selected').val();
		var fiche_id = $('#fiche_id').val();
		var comment = $(this).parents('tr').find(".comment").val();
		$.ajax({
			type: "POST",
			url: "/addvigitaux",
			async: false,
			data: JSON.stringify({"params": {'fiche': fiche_id, 'date': date, 'vigitaux': vigitaux_id, 'comment': comment}}),
			contentType: "application/json",
			complete: function (data) {
				console.log(data);
				if (data['responseJSON']["result"]["error_message"].length != 0){
				console.log("ereuuuuuuuuuuuuuuuuuuuuuuuur");
				$('#main_vigitaux').before('<div class="col-md-12">'+
				  '<div id="error_vigitaux" class="alert alert-danger">'+
				      '<p>'+data['responseJSON']["result"]["error_message"]+'</p>'+
				  '</div>'+
				'</div>'
				);
				}
				else {
				$('#table_vigitaux tr:last').before('<tr><td>'+ data['responseJSON']["result"]["date"] +'</td><td>'+ data['responseJSON']["result"]["vigitaux"] +'</td><td>'+ data['responseJSON']["result"]["comment"] +'</td><td><a class="btn btn-primary deletevehicles">Supprimer</a></td></tr>');
				$("#error_vigitaux").hide()
				$("#vigitaux_id").val("");
				$('input.date').val('');
				$('input.comment').val('');
				}
			}
			
		});

    });


    $('.addengrai').on('click', function(ev) {
        ev.preventDefault();
		console.log("IIIIIIIIIIIIIIIIIINNNNNNNNNNNNNNNN");
		var engrais_id = $('#engrais_id option:selected').val();
		var fiche_id = $('#fiche_id').val();
		var qty = $(this).parents('tr').find(".eqty").val();
		$.ajax({
			type: "POST",
			url: "/addengrai",
			async: false,
			data: JSON.stringify({"params": {'fiche': fiche_id, 'engrais': engrais_id, 'qty': qty}}),
			contentType: "application/json",
			complete: function (data) {
				console.log(data);
				if (data['responseJSON']["result"]["error_message"].length != 0){
				console.log("ereuuuuuuuuuuuuuuuuuuuuuuuur");
				$('#main_engrai').before('<div class="col-md-12">'+
				  '<div id="error_engrais" class="alert alert-danger">'+
				      '<p>'+data['responseJSON']["result"]["error_message"]+'</p>'+
				  '</div>'+
				'</div>'
				);
				}
				else {
				$('#table_engrai tr:last').before('<tr><td>'+ data['responseJSON']["result"]["engrais"] +'</td><td>'+ data['responseJSON']["result"]["qty"] +'</td><td><a class="btn btn-primary deletevehicles">Supprimer</a></td></tr>');
				$("#error_engrais").hide()
				$("#engrais_id").val("");
				$('input.eqty').val('');
				}
			}
		});

    });


    $('.addgazon').on('click', function(ev) {
        ev.preventDefault();
		console.log("IIIIIIIIIIIIIIIIIINNNNNNNNNNNNNNNN");
		var gazons_id = $('#gazons_id option:selected').val();
		var fiche_id = $('#fiche_id').val();
		var qty = $(this).parents('tr').find(".gqty").val();
		$.ajax({
			type: "POST",
			url: "/addgazon",
			async: false,
			data: JSON.stringify({"params": {'fiche': fiche_id, 'gazons': gazons_id, 'qty': qty}}),
			contentType: "application/json",
			complete: function (data) {
				console.log(data);
				if (data['responseJSON']["result"]["error_message"].length != 0){
				console.log("ereuuuuuuuuuuuuuuuuuuuuuuuur");
				$('#main_gazon').before('<div class="col-md-12">'+
				  '<div id="error_gazon" class="alert alert-danger">'+
				      '<p>'+data['responseJSON']["result"]["error_message"]+'</p>'+
				  '</div>'+
				'</div>'
				);
				}
				else {
				$('#table_gazon tr:last').before('<tr><td>'+ data['responseJSON']["result"]["gazons"] +'</td><td>'+ data['responseJSON']["result"]["qty"] +'</td><td><a class="btn btn-primary deletevehicles">Supprimer</a></td></tr>');
				$("#error_gazon").hide()
				$("#gazons_id").val("");
				$('input.gqty').val('');
				}
			}
		});

    });


    $('.addgmateriel').on('click', function(ev) {
        ev.preventDefault();
		console.log("IIIIIIIIIIIIIIIIIINNNNNNNNNNNNNNNN");
		var gmateriel_id = $('#gmateriel_id option:selected').val();
		var fiche_id = $('#fiche_id').val();
		var qty = $(this).parents('tr').find(".gmqty").val();
		$.ajax({
			type: "POST",
			url: "/addgmateriel",
			async: false,
			data: JSON.stringify({"params": {'fiche': fiche_id, 'gmateriel': gmateriel_id, 'qty': qty}}),
			contentType: "application/json",
			complete: function (data) {
				console.log(data);
				if (data['responseJSON']["result"]["error_message"].length != 0){
				console.log("ereuuuuuuuuuuuuuuuuuuuuuuuur");
				$('#main_gmateriel').before('<div class="col-md-12">'+
				  '<div id="error_gmateriel" class="alert alert-danger">'+
				      '<p>'+data['responseJSON']["result"]["error_message"]+'</p>'+
				  '</div>'+
				'</div>'
				);
				}
				else {
				$('#table_gmateriel tr:last').before('<tr><td>'+ data['responseJSON']["result"]["gmateriel"] +'</td><td>'+ data['responseJSON']["result"]["qty"] +'</td><td><a class="btn btn-primary deletevehicles">Supprimer</a></td></tr>');
				$("#error_gmateriel").hide()
				$("#gmateriel_id").val("");
				$('input.gmqty').val('');
				}
			}
		});

    });


    $('.addescalier').on('click', function(ev) {
        ev.preventDefault();
		console.log("IIIIIIIIIIIIIIIIIINNNNNNNNNNNNNNNN");
		var escalier_id = $('#escalier_id option:selected').val();
		var fiche_id = $('#fiche_id').val();
		var qty = $(this).parents('tr').find(".escqty").val();
		$.ajax({
			type: "POST",
			url: "/addescalier",
			async: false,
			data: JSON.stringify({"params": {'fiche': fiche_id, 'escalier': escalier_id, 'qty': qty}}),
			contentType: "application/json",
			complete: function (data) {
				console.log(data);
				if (data['responseJSON']["result"]["error_message"].length != 0){
				console.log("ereuuuuuuuuuuuuuuuuuuuuuuuur");
				$('#main_escalier').before('<div class="col-md-12">'+
				  '<div id="error_escalier" class="alert alert-danger">'+
				      '<p>'+data['responseJSON']["result"]["error_message"]+'</p>'+
				  '</div>'+
				'</div>'
				);
				}
				else {
				$('#table_escalier tr:last').before('<tr><td>'+ data['responseJSON']["result"]["escalier"] +'</td><td>'+ data['responseJSON']["result"]["qty"] +'</td><td><a class="btn btn-primary deletevehicles">Supprimer</a></td></tr>');
				$("#error_escalier").hide()
				$("#escalier_id").val("");
				$('input.escqty').val('');
				}
			}
		});

    });


    $('.addoutils').on('click', function(ev) {
        ev.preventDefault();
		console.log("IIIIIIIIIIIIIIIIIINNNNNNNNNNNNNNNN");
		var outils_id = $('#outils_id option:selected').val();
		var fiche_id = $('#fiche_id').val();
		var qty = $(this).parents('tr').find(".oqty").val();
		$.ajax({
			type: "POST",
			url: "/addoutils",
			async: false,
			data: JSON.stringify({"params": {'fiche': fiche_id, 'outils': outils_id, 'qty': qty}}),
			contentType: "application/json",
			complete: function (data) {
				console.log(data);
				if (data['responseJSON']["result"]["error_message"].length != 0){
				console.log("ereuuuuuuuuuuuuuuuuuuuuuuuur");
				$('#main_outilss').before('<div class="col-md-12">'+
				  '<div id="error_outilss" class="alert alert-danger">'+
				      '<p>'+data['responseJSON']["result"]["error_message"]+'</p>'+
				  '</div>'+
				'</div>'
				);
				}
				else {
				$('#table_outilss tr:last').before('<tr><td>'+ data['responseJSON']["result"]["outils"] +'</td><td>'+ data['responseJSON']["result"]["qty"] +'</td><td><a class="btn btn-primary deletevehicles">Supprimer</a></td></tr>');
				$("#error_outilss").hide()
				$("#outils_id").val("");
				$('input.oqty').val('');
				}
			}
		});

    });


    $('.addclotures').on('click', function(ev) {
        ev.preventDefault();
		console.log("IIIIIIIIIIIIIIIIIINNNNNNNNNNNNNNNN");
		var cloture_id = $('#cloture_id option:selected').val();
		var fiche_id = $('#fiche_id').val();
		var qty = $(this).parents('tr').find(".cqty").val();
		$.ajax({
			type: "POST",
			url: "/addclotures",
			async: false,
			data: JSON.stringify({"params": {'fiche': fiche_id, 'cloture': cloture_id, 'qty': qty}}),
			contentType: "application/json",
			complete: function (data) {
				console.log(data);
				if (data['responseJSON']["result"]["error_message"].length != 0){
				console.log("ereuuuuuuuuuuuuuuuuuuuuuuuur");
				$('#main_cloture').before('<div class="col-md-12">'+
				  '<div id="error_cloture" class="alert alert-danger">'+
				      '<p>'+data['responseJSON']["result"]["error_message"]+'</p>'+
				  '</div>'+
				'</div>'
				);
				}
				else {
				$('#table_cloture tr:last').before('<tr><td>'+ data['responseJSON']["result"]["cloture"] +'</td><td>'+ data['responseJSON']["result"]["qty"] +'</td><td><a class="btn btn-primary deletevehicles">Supprimer</a></td></tr>');
				$("#error_cloture").hide()
				$("#cloture_id").val("");
				$('input.cqty').val('');
				}
			}
		});

    });


    $('.adddivers').on('click', function(ev) {
        ev.preventDefault();
		console.log("IIIIIIIIIIIIIIIIIINNNNNNNNNNNNNNNN");
		var divers_id = $('#divers_id option:selected').val();
		var fiche_id = $('#fiche_id').val();
		var qty = $(this).parents('tr').find(".dqty").val();
		$.ajax({
			type: "POST",
			url: "/adddivers",
			async: false,
			data: JSON.stringify({"params": {'fiche': fiche_id, 'divers': divers_id, 'qty': qty}}),
			contentType: "application/json",
			complete: function (data) {
				console.log(data);
				if (data['responseJSON']["result"]["error_message"].length != 0){
				console.log("ereuuuuuuuuuuuuuuuuuuuuuuuur");
				$('#main_diverss').before('<div class="col-md-12">'+
				  '<div id="error_diverss" class="alert alert-danger">'+
				      '<p>'+data['responseJSON']["result"]["error_message"]+'</p>'+
				  '</div>'+
				'</div>'
				);
				}
				else {
				$('#table_diverss tr:last').before('<tr><td>'+ data['responseJSON']["result"]["divers"] +'</td><td>'+ data['responseJSON']["result"]["qty"] +'</td><td><a class="btn btn-primary deletevehicles">Supprimer</a></td></tr>');
				$("#error_diverss").hide()
				$("#divers_id").val("");
				$('input.dqty').val('');
				}
			}
		});

    });


    $('.addterrasses').on('click', function(ev) {
        ev.preventDefault();
		console.log("IIIIIIIIIIIIIIIIIINNNNNNNNNNNNNNNN");
		var terrasse_id = $('#terrasse_id option:selected').val();
		var fiche_id = $('#fiche_id').val();
		var qty = $(this).parents('tr').find(".terqty").val();
		$.ajax({
			type: "POST",
			url: "/addterrasses",
			async: false,
			data: JSON.stringify({"params": {'fiche': fiche_id, 'terrasse': terrasse_id, 'qty': qty}}),
			contentType: "application/json",
			complete: function (data) {
				console.log(data);
				if (data['responseJSON']["result"]["error_message"].length != 0){
				console.log("ereuuuuuuuuuuuuuuuuuuuuuuuur");
				$('#main_terrasse').before('<div class="col-md-12">'+
				  '<div id="error_terrasse" class="alert alert-danger">'+
				      '<p>'+data['responseJSON']["result"]["error_message"]+'</p>'+
				  '</div>'+
				'</div>'
				);
				}
				else {
				$('#table_terrasse tr:last').before('<tr><td>'+ data['responseJSON']["result"]["terrasse"] +'</td><td>'+ data['responseJSON']["result"]["qty"] +'</td><td><a class="btn btn-primary deletevehicles">Supprimer</a></td></tr>');
				$("#error_terrasse").hide()
				$("#terrasse_id").val("");
				$('input.terqty').val('');
				}
			}
		});

    });


    $('.addsclotures').on('click', function(ev) {
        ev.preventDefault();
		console.log("IIIIIIIIIIIIIIIIIINNNNNNNNNNNNNNNN");
		var scloture_id = $('#scloture_id option:selected').val();
		var fiche_id = $('#fiche_id').val();
		var qty = $(this).parents('tr').find(".scqty").val();
		$.ajax({
			type: "POST",
			url: "/addsclotures",
			async: false,
			data: JSON.stringify({"params": {'fiche': fiche_id, 'scloture': scloture_id, 'qty': qty}}),
			contentType: "application/json",
			complete: function (data) {
				console.log(data);
				if (data['responseJSON']["result"]["error_message"].length != 0){
				console.log("ereuuuuuuuuuuuuuuuuuuuuuuuur");
				$('#main_sclotures').before('<div class="col-md-12">'+
				  '<div id="error_sclotures" class="alert alert-danger">'+
				      '<p>'+data['responseJSON']["result"]["error_message"]+'</p>'+
				  '</div>'+
				'</div>'
				);
				}
				else {
				$('#table_sclotures tr:last').before('<tr><td>'+ data['responseJSON']["result"]["scloture"] +'</td><td>'+ data['responseJSON']["result"]["qty"] +'</td><td><a class="btn btn-primary deletevehicles">Supprimer</a></td></tr>');
				$("#error_sclotures").hide()
				$("#scloture_id").val("");
				$('input.scqty').val('');
				}
			}
		});

    });


    $('.addcomment').on('click', function(ev) {
        ev.preventDefault();
		console.log("IIIIIIIIIIIIIIIIIINNNNNNNNNNNNNNNN");
		var fiche_id = $('#fiche_id').val();
		var comment = $('#comment').val();
		$.ajax({
			type: "POST",
			url: "/addcomment",
			async: false,
			data: JSON.stringify({"params": {'fiche': fiche_id, 'comment': comment}}),
			contentType: "application/json",
			complete: function (data) {
				console.log(data);
				$('input.comment').val(data['responseJSON']["result"]["scloture"]);
			}
		});

    });
	
});
