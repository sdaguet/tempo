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
				$(".error_vehicle").remove()
				$('#main_vehicle').before('<div class="col-md-12">'+
				  '<div class="alert alert-danger error_vehicle">'+
				      '<p>'+data['responseJSON']["result"]["error_message"]+'</p>'+
				  '</div>'+
				'</div>'
				);
				}
				else {
				$('#table_vehicle tr:last').before('<tr id="vehicle_'+data['responseJSON']["result"]["fiche_veicule_id"]+'"><td>'+ data['responseJSON']["result"]["vehicle"] +'</td><td>'+ data['responseJSON']["result"]["km"] +'</td><td><a class="btn btn-primary deletevehicle">Supprimer</a></td></tr>');
				$(".error_vehicle").remove()
				$("#vehicle_id").val("");
				$('input.vkm').val('');
				var fiche_veicule_id = data['responseJSON']["result"]["fiche_veicule_id"];
				$('.deletevehicle').on('click', function(ev) {
			        ev.preventDefault();
					$.ajax({
						type: "POST",
						url: "/deletevehicles",
						async: false,
						data: JSON.stringify({"params": {'fiche': fiche_id, 'fiche_veicule': fiche_veicule_id}}),
						contentType: "application/json",
						complete: function (data) {
							console.log("#vehicle_"+fiche_veicule_id);
							$("#vehicle_"+fiche_veicule_id).remove()
						}
					});
			
			    });
				}
			}
		});

    });

   
    $('.addmateriel').on('click', function(ev) {
        ev.preventDefault();
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
				$(".error_materiel").remove()
				$('#main_materiel').before('<div class="col-md-12">'+
				  '<div class="alert alert-danger error_materiel">'+
				      '<p>'+data['responseJSON']["result"]["error_message"]+'</p>'+
				  '</div>'+
				'</div>'
				);
				}
				else {
				$('#table_materiel tr:last').before('<tr id="materiel_'+data['responseJSON']["result"]["fiche_materiel_id"]+'"><td>'+ data['responseJSON']["result"]["materiel"] +'</td><td>'+ data['responseJSON']["result"]["temps"] +'</td><td><a class="btn btn-primary deletemateriel">Supprimer</a></td></tr>');
				$(".error_materiel").remove()
				$("#materiel_id").val("");
				$('input.temps').val('');
				var fiche_materiel_id = data['responseJSON']["result"]["fiche_materiel_id"];
				$('.deletemateriel').on('click', function(ev) {
			        ev.preventDefault();
					$.ajax({
						type: "POST",
						url: "/deletemateriel",
						async: false,
						data: JSON.stringify({"params": {'fiche': fiche_id, 'fiche_materiel': fiche_materiel_id}}),
						contentType: "application/json",
						complete: function (data) {
							$("#materiel_" +fiche_materiel_id).remove()
						}
					});
			
			    });
				}
			}
		});

    });
    

    $('.addmachine').on('click', function(ev) {
        ev.preventDefault();
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
				$(".error_machine").remove()
				$('#main_machine').before('<div class="col-md-12">'+
				  '<div class="alert alert-danger error_machine">'+
				      '<p>'+data['responseJSON']["result"]["error_message"]+'</p>'+
				  '</div>'+
				'</div>'
				);
				}
				else {
				$('#table_machine tr:last').before('<tr id="machine_'+data['responseJSON']["result"]["fiche_machine_id"]+'"><td>'+ data['responseJSON']["result"]["machine"] +'</td><td>'+ data['responseJSON']["result"]["temps"] +'</td><td><a class="btn btn-primary deletemachine">Supprimer</a></td></tr>');
				$(".error_machine").remove()
				$("#machine_id").val("");
				$('input.mtemps').val('');
				var fiche_machine_id = data['responseJSON']["result"]["fiche_machine_id"];
			    $('.deletemachine').on('click', function(ev) {
			        ev.preventDefault();
					$.ajax({
						type: "POST",
						url: "/deletemachine",
						async: false,
						data: JSON.stringify({"params": {'fiche': fiche_id, 'fiche_machine': fiche_machine_id}}),
						contentType: "application/json",
						complete: function (data) {
							$("#machine_" +fiche_machine_id).remove() 
						}
					});
			
			    });
				}
			}
		});

    });
    

    $('.addfourniture').on('click', function(ev) {
        ev.preventDefault();
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
				$(".error_fourniture").remove()
				$('#main_fourniture').before('<div class="col-md-12">'+
				  '<div class="alert alert-danger error_fourniture">'+
				      '<p>'+data['responseJSON']["result"]["error_message"]+'</p>'+
				  '</div>'+
				'</div>'
				);
				}
				else {
				$('#table_fourniture tr:last').before('<tr id="fourniture_'+data['responseJSON']["result"]["fiche_fourniture_id"]+'"><td>'+ data['responseJSON']["result"]["fourniture"] +'</td><td>'+ data['responseJSON']["result"]["qty"] +'</td><td><a class="btn btn-primary deletefourniture">Supprimer</a></td></tr>');
				$(".error_fourniture").remove()
				$("#fourniture_id").val("");
				$('input.qty').val('');
				var fiche_fourniture_id = data['responseJSON']["result"]["fiche_fourniture_id"];
				$('.deletefourniture').on('click', function(ev) {
			        ev.preventDefault();
					$.ajax({
						type: "POST",
						url: "/deletefourniture",
						async: false,
						data: JSON.stringify({"params": {'fiche': fiche_id, 'fiche_fourniture': fiche_fourniture_id}}),
						contentType: "application/json",
						complete: function (data) {
							$("#fourniture_" +fiche_fourniture_id).remove() 
						}
					});
			
			    });
				}
			}
		});

    });


    $('.addkit').on('click', function(ev) {
        ev.preventDefault();
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
				$(".error_kit").remove()
				$('#main_kit').before('<div class="col-md-12">'+
				  '<div class="alert alert-danger error_kit">'+
				      '<p>'+data['responseJSON']["result"]["error_message"]+'</p>'+
				  '</div>'+
				'</div>'
				);
				}
				else {
				$('#table_kit tr:last').before('<tr id="kit_'+data['responseJSON']["result"]["fiche_kit_id"]+'"><td>'+ data['responseJSON']["result"]["kit"] +'</td><td>'+ data['responseJSON']["result"]["qty"] +'</td><td><a class="btn btn-primary deletekit">Supprimer</a></td></tr>');
				$(".error_kit").remove()
				$("#kit_id").val("");
				$('input.kqty').val('');
				var fiche_kit_id = data['responseJSON']["result"]["fiche_kit_id"];
			    $('.deletekit').on('click', function(ev) {
			        ev.preventDefault();
					$.ajax({
						type: "POST",
						url: "/deletekit",
						async: false,
						data: JSON.stringify({"params": {'fiche': fiche_id, 'fiche_kit': fiche_kit_id}}),
						contentType: "application/json",
						complete: function (data) {
							$("#kit_" +fiche_kit_id).remove() 
						}
					});
			
			    });
				}
			}
		});

    });


    $('.addtuteurage').on('click', function(ev) {
        ev.preventDefault();
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
				$(".error_tuteurage").remove()
				$('#main_tuteurage').before('<div class="col-md-12">'+
				  '<div class="alert alert-danger error_tuteurage">'+
				      '<p>'+data['responseJSON']["result"]["error_message"]+'</p>'+
				  '</div>'+
				'</div>'
				);
				}
				else {
				$('#table_tuteurage tr:last').before('<tr id="tuteurage_'+data['responseJSON']["result"]["fiche_tuteurage_id"]+'"><td>'+ data['responseJSON']["result"]["tuteurage"] +'</td><td>'+ data['responseJSON']["result"]["qty"] +'</td><td><a class="btn btn-primary deletetuteurage">Supprimer</a></td></tr>');
				$(".error_tuteurage").remove()
				$("#tuteurage_id").val("");
				$('input.tqty').val('');
				var fiche_tuteurage_id = data['responseJSON']["result"]["fiche_tuteurage_id"];
			    $('.deletetuteurage').on('click', function(ev) {
			        ev.preventDefault();
			        var fiche_id = $('#fiche_id').val();
			   		var fiche_tuteurage = $(this).closest('tr').attr('id'); // table row ID
			   		var fiche_tuteurage_id = fiche_tuteurage.split("_").pop();
					console.log(fiche_tuteurage_id);
					$.ajax({
						type: "POST",
						url: "/deletetuteurage",
						async: false,
						data: JSON.stringify({"params": {'fiche': fiche_id, 'fiche_tuteurage': fiche_tuteurage_id}}),
						contentType: "application/json",
						complete: function (data) {
							$("#tuteurage_" +fiche_tuteurage_id).remove() 
						}
					});
			
			    });
				}
			}
		});

    });


    $('.addvigitaux').on('click', function(ev) {
        ev.preventDefault();
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
				$(".error_vigitaux").remove()
				$('#main_vigitaux').before('<div class="col-md-12">'+
				  '<div class="alert alert-danger error_vigitaux">'+
				      '<p>'+data['responseJSON']["result"]["error_message"]+'</p>'+
				  '</div>'+
				'</div>'
				);
				}
				else {
				$('#table_vigitaux tr:last').before('<tr id="vigitau_'+data['responseJSON']["result"]["fiche_vigitaux_id"]+'"><td>'+ data['responseJSON']["result"]["date"] +'</td><td>'+ data['responseJSON']["result"]["vigitaux"] +'</td><td>'+ data['responseJSON']["result"]["comment"] +'</td><td><a class="btn btn-primary deletevigitau">Supprimer</a></td></tr>');
				$(".error_vigitaux").remove()
				$("#vigitaux_id").val("");
				$('input.date').val('');
				$('input.comment').val('');
				var fiche_vigitaux_id = data['responseJSON']["result"]["fiche_vigitaux_id"];
			    $('.deletevigitau').on('click', function(ev) {
			        ev.preventDefault();
					$.ajax({
						type: "POST",
						url: "/deletevigitaux",
						async: false,
						data: JSON.stringify({"params": {'fiche': fiche_id, 'fiche_vigitaux': fiche_vigitaux_id}}),
						contentType: "application/json",
						complete: function (data) {
							$("#vigitau_" +fiche_vigitaux_id).remove() 
						}
					});
			
			    });
				}
			}
			
		});

    });


    $('.addengrai').on('click', function(ev) {
        ev.preventDefault();
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
				$(".error_engrais").remove()
				$('#main_engrai').before('<div class="col-md-12">'+
				  '<div class="alert alert-danger error_engrais">'+
				      '<p>'+data['responseJSON']["result"]["error_message"]+'</p>'+
				  '</div>'+
				'</div>'
				);
				}
				else {
				$('#table_engrai tr:last').before('<tr id="engrai_'+data['responseJSON']["result"]["fiche_engrais_id"]+'"><td>'+ data['responseJSON']["result"]["engrais"] +'</td><td>'+ data['responseJSON']["result"]["qty"] +'</td><td><a class="btn btn-primary deleteengrai">Supprimer</a></td></tr>');
				$(".error_engrais").remove()
				$("#engrais_id").val("");
				$('input.eqty').val('');
				var fiche_engrais_id = data['responseJSON']["result"]["fiche_engrais_id"];
			    $('.deleteengrai').on('click', function(ev) {
			        ev.preventDefault();
					$.ajax({
						type: "POST",
						url: "/deleteengrai",
						async: false,
						data: JSON.stringify({"params": {'fiche': fiche_id, 'fiche_engrai': fiche_engrais_id}}),
						contentType: "application/json",
						complete: function (data) {
							$("#engrai_" +fiche_engrais_id).remove() 
						}
					});
			
			    });
				}
			}
		});

    });


    $('.addgazon').on('click', function(ev) {
        ev.preventDefault();
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
				$(".error_gazon").remove()
				$('#main_gazon').before('<div class="col-md-12">'+
				  '<div class="alert alert-danger error_gazon">'+
				      '<p>'+data['responseJSON']["result"]["error_message"]+'</p>'+
				  '</div>'+
				'</div>'
				);
				}
				else {
				$('#table_gazon tr:last').before('<tr id="gazon_'+data['responseJSON']["result"]["fiche_gazons_id"]+'"><td>'+ data['responseJSON']["result"]["gazons"] +'</td><td>'+ data['responseJSON']["result"]["qty"] +'</td><td><a class="btn btn-primary deletegazon">Supprimer</a></td></tr>');
				$(".error_gazon").remove()
				$("#gazons_id").val("");
				$('input.gqty').val('');
				var fiche_gazons_id = data['responseJSON']["result"]["fiche_gazons_id"];
			    $('.deletegazon').on('click', function(ev) {
			        ev.preventDefault();
					$.ajax({
						type: "POST",
						url: "/deletegazon",
						async: false,
						data: JSON.stringify({"params": {'fiche': fiche_id, 'fiche_gazon': fiche_gazons_id}}),
						contentType: "application/json",
						complete: function (data) {
							$("#gazon_" +fiche_gazons_id).remove() 
						}
					});
			
			    });
				}
			}
		});

    });


    $('.addgmateriel').on('click', function(ev) {
        ev.preventDefault();
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
				$(".error_gmateriel").remove()
				$('#main_gmateriel').before('<div class="col-md-12">'+
				  '<div class="alert alert-danger error_gmateriel">'+
				      '<p>'+data['responseJSON']["result"]["error_message"]+'</p>'+
				  '</div>'+
				'</div>'
				);
				}
				else {
				$('#table_gmateriel tr:last').before('<tr id="gmateriel_'+data['responseJSON']["result"]["fiche_gmateriel_id"]+'"><td>'+ data['responseJSON']["result"]["gmateriel"] +'</td><td>'+ data['responseJSON']["result"]["qty"] +'</td><td><a class="btn btn-primary deletegmateriel">Supprimer</a></td></tr>');
				$(".error_gmateriel").remove()
				$("#gmateriel_id").val("");
				$('input.gmqty').val('');
				var fiche_gmateriel_id = data['responseJSON']["result"]["fiche_gmateriel_id"];
			    $('.deletegmateriel').on('click', function(ev) {
			        ev.preventDefault();
					$.ajax({
						type: "POST",
						url: "/deletegmateriel",
						async: false,
						data: JSON.stringify({"params": {'fiche': fiche_id, 'fiche_gmaterie': fiche_gmateriel_id}}),
						contentType: "application/json",
						complete: function (data) {
							$("#gmateriel_" +fiche_gmateriel_id).remove() 
						}
					});
			
			    });
				}
			}
		});

    });


    $('.addescalier').on('click', function(ev) {
        ev.preventDefault();
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
				$(".error_escalier").remove()
				$('#main_escalier').before('<div class="col-md-12">'+
				  '<div class="alert alert-danger error_escalier">'+
				      '<p>'+data['responseJSON']["result"]["error_message"]+'</p>'+
				  '</div>'+
				'</div>'
				);
				}
				else {
				$('#table_escalier tr:last').before('<tr id="escalier_'+data['responseJSON']["result"]["fiche_escalier_id"]+'"><td>'+ data['responseJSON']["result"]["escalier"] +'</td><td>'+ data['responseJSON']["result"]["qty"] +'</td><td><a class="btn btn-primary deleteescalier">Supprimer</a></td></tr>');
				$(".error_escalier").remove()
				$("#escalier_id").val("");
				$('input.escqty').val('');
				var fiche_escalier_id = data['responseJSON']["result"]["fiche_escalier_id"];
			    $('.deleteescalier').on('click', function(ev) {
			        ev.preventDefault();
					$.ajax({
						type: "POST",
						url: "/deleteescalier",
						async: false,
						data: JSON.stringify({"params": {'fiche': fiche_id, 'fiche_escalier': fiche_escalier_id}}),
						contentType: "application/json",
						complete: function (data) {
							$("#escalier_" +fiche_escalier_id).remove() 
						}
					});
			
			    });
				
				}
			}
		});

    });


    $('.addoutils').on('click', function(ev) {
        ev.preventDefault();
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
				$(".error_outilss").remove()
				$('#main_outilss').before('<div class="col-md-12">'+
				  '<div class="alert alert-danger error_outilss">'+
				      '<p>'+data['responseJSON']["result"]["error_message"]+'</p>'+
				  '</div>'+
				'</div>'
				);
				}
				else {
				$('#table_outilss tr:last').before('<tr id="outil_'+data['responseJSON']["result"]["fiche_outils_id"]+'"><td>'+ data['responseJSON']["result"]["outils"] +'</td><td>'+ data['responseJSON']["result"]["qty"] +'</td><td><a class="btn btn-primary deleteoutil">Supprimer</a></td></tr>');
				$(".error_outilss").remove()
				$("#outils_id").val("");
				$('input.oqty').val('');
				var fiche_outils_id = data['responseJSON']["result"]["fiche_outils_id"];
				$('.deleteoutil').on('click', function(ev) {
			        ev.preventDefault();
					$.ajax({
						type: "POST",
						url: "/deleteoutilss",
						async: false,
						data: JSON.stringify({"params": {'fiche': fiche_id, 'fiche_outilss': fiche_outils_id}}),
						contentType: "application/json",
						complete: function (data) {
							$("#outil_" +fiche_outils_id).remove() 
						}
					});
			
			    });
				
				}
			}
		});

    });


    $('.addclotures').on('click', function(ev) {
        ev.preventDefault();
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
				$(".error_cloture").remove()
				$('#main_cloture').before('<div class="col-md-12">'+
				  '<div class="alert alert-danger error_cloture">'+
				      '<p>'+data['responseJSON']["result"]["error_message"]+'</p>'+
				  '</div>'+
				'</div>'
				);
				}
				else {
				$('#table_cloture tr:last').before('<tr id="cloture_'+data['responseJSON']["result"]["fiche_cloture_id"]+'"><td>'+ data['responseJSON']["result"]["cloture"] +'</td><td>'+ data['responseJSON']["result"]["qty"] +'</td><td><a class="btn btn-primary deletecloture">Supprimer</a></td></tr>');
				$(".error_cloture").remove()
				$("#cloture_id").val("");
				$('input.cqty').val('');
				var fiche_cloture_id = data['responseJSON']["result"]["fiche_cloture_id"];
			    $('.deletecloture').on('click', function(ev) {
			        ev.preventDefault();
					$.ajax({
						type: "POST",
						url: "/deletecloture",
						async: false,
						data: JSON.stringify({"params": {'fiche': fiche_id, 'fiche_cloture': fiche_cloture_id}}),
						contentType: "application/json",
						complete: function (data) {
							$("#cloture_" +fiche_cloture_id).remove() 
						}
					});
			
			    });
				}
			}
		});

    });


    $('.adddivers').on('click', function(ev) {
        ev.preventDefault();
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
				$(".error_diverss").remove()
				$('#main_diverss').before('<div class="col-md-12">'+
				  '<div class="alert alert-danger error_diverss">'+
				      '<p>'+data['responseJSON']["result"]["error_message"]+'</p>'+
				  '</div>'+
				'</div>'
				);
				}
				else {
				$('#table_diverss tr:last').before('<tr id="diver_'+data['responseJSON']["result"]["fiche_divers_id"]+'"><td>'+ data['responseJSON']["result"]["divers"] +'</td><td>'+ data['responseJSON']["result"]["qty"] +'</td><td><a class="btn btn-primary deletediver">Supprimer</a></td></tr>');
				$(".error_diverss").remove()
				$("#divers_id").val("");
				$('input.dqty').val('');
				var fiche_divers_id = data['responseJSON']["result"]["fiche_divers_id"];
			    $('.deletediver').on('click', function(ev) {
			        ev.preventDefault();
					$.ajax({
						type: "POST",
						url: "/deletediverss",
						async: false,
						data: JSON.stringify({"params": {'fiche': fiche_id, 'fiche_diverss': fiche_divers_id}}),
						contentType: "application/json",
						complete: function (data) {
							$("#diver_" +fiche_divers_id).remove() 
						}
					});
			
			    });
				}
			}
		});

    });


    $('.addterrasses').on('click', function(ev) {
        ev.preventDefault();
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
				$(".error_terrasse").remove()
				$('#main_terrasse').before('<div class="col-md-12">'+
				  '<div class="alert alert-danger error_terrasse">'+
				      '<p>'+data['responseJSON']["result"]["error_message"]+'</p>'+
				  '</div>'+
				'</div>'
				);
				}
				else {
				$('#table_terrasse tr:last').before('<tr id="terrasse_'+data['responseJSON']["result"]["fiche_terrasse_id"]+'"><td>'+ data['responseJSON']["result"]["terrasse"] +'</td><td>'+ data['responseJSON']["result"]["qty"] +'</td><td><a class="btn btn-primary deleteterrasse">Supprimer</a></td></tr>');
				$(".error_terrasse").remove()
				$("#terrasse_id").val("");
				$('input.terqty').val('');
				var fiche_terrasse_id = data['responseJSON']["result"]["fiche_terrasse_id"];
			    $('.deleteterrasse').on('click', function(ev) {
			        ev.preventDefault();
					$.ajax({
						type: "POST",
						url: "/deleteterrasse",
						async: false,
						data: JSON.stringify({"params": {'fiche': fiche_id, 'fiche_terrasse': fiche_terrasse_id}}),
						contentType: "application/json",
						complete: function (data) {
							$("#terrasse_" +fiche_terrasse_id).remove() 
						}
					});
			
			    });
				}
			}
		});

    });


    $('.addsclotures').on('click', function(ev) {
        ev.preventDefault();
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
				$(".error_sclotures").remove()
				$('#main_sclotures').before('<div class="col-md-12">'+
				  '<div class="alert alert-danger error_sclotures">'+
				      '<p>'+data['responseJSON']["result"]["error_message"]+'</p>'+
				  '</div>'+
				'</div>'
				);
				}
				else {
				$('#table_sclotures tr:last').before('<tr id="scloture_'+data['responseJSON']["result"]["fiche_scloture_id"]+'"><td>'+ data['responseJSON']["result"]["scloture"] +'</td><td>'+ data['responseJSON']["result"]["qty"] +'</td><td><a class="btn btn-primary deletescloture">Supprimer</a></td></tr>');
				$(".error_sclotures").remove()
				$("#scloture_id").val("");
				$('input.scqty').val('');
				var fiche_scloture_id = data['responseJSON']["result"]["fiche_scloture_id"];
			    $('.deletescloture').on('click', function(ev) {
			        ev.preventDefault();
					$.ajax({
						type: "POST",
						url: "/deletescloture",
						async: false,
						data: JSON.stringify({"params": {'fiche': fiche_id, 'fiche_scloture': fiche_scloture_id}}),
						contentType: "application/json",
						complete: function (data) {
							$("#scloture_" +fiche_scloture_id).remove() 
						}
					});
			
			    });
				}
			}
		});

    });

    
    $('.addcomment').on('click', function(ev) {
        ev.preventDefault();
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
			    $("#write").hide()
			    $(".read_comment").text(data['responseJSON']["result"]["comment"]);
			    $("#edit").show()
			    $("#editcomment").click(function(){
			    	$("#edit").hide()
			    	$("#write").show()
			});}
		});

    })



    $('.addwork').on('click', function(ev) {
        ev.preventDefault();
		var fiche_id = $('#fiche_id').val();
		var employee_id = $(this).closest('tr').attr('id'); // table row ID
   		var employee = employee_id.split("_").pop();
		var tesk_id = $('#tesk_'+ employee +' option:selected').val();
		var type = $('#type_'+ employee +' option:selected').val();
		var heure_deb = $('#heure_deb_'+ employee +' option:selected').val();
		var heure_fin = $('#heure_fin_'+ employee +' option:selected').val();

		$.ajax({
			type: "POST",
			url: "/addwork",
			async: false,
			data: JSON.stringify({"params": {'fiche': fiche_id, 'employee': employee, 'tesk': tesk_id, 'type': type, 'heure_deb': heure_deb, 'heure_fin': heure_fin}}),
			contentType: "application/json",
			complete: function (data) {
				console.log(data);
				if (data['responseJSON']["result"]["error_message"].length != 0){
				$(".error_pointage").remove()
				$('#main_pointage').before('<div class="col-md-12">'+
				  '<div class="alert alert-danger error_pointage">'+
				      '<p>'+data['responseJSON']["result"]["error_message"]+'</p>'+
				  '</div>'+
				'</div>'
				);
				}
				else {
				$(".error_pointage").remove()
				$("#tesk_"+ employee).val("");
				$("#type_"+ employee).val("p");
				$("#heure_deb_"+ employee).val("7:00");
				$("#heure_fin_"+ employee).val("7:00");
				getwebgantt();
				}
			}
		});

    });
	
});
