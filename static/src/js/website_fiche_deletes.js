odoo.define('darb_puthod.responsivejson', function(require) {
    'use strict';
    require('website.website');
    require('web.ajax');

    $('.deletevehicles').on('click', function(ev) {
        ev.preventDefault();
        var fiche_id = $('#fiche_id').val();
   		var fiche_veicule = $(this).closest('tr').attr('id'); // table row ID
   		var fiche_veicule_id = fiche_veicule.split("_").pop();
		console.log("1111111111111111");
		console.log(fiche_veicule_id);
		console.log("22222222222222222222");
		$.ajax({
			type: "POST",
			url: "/deletevehicles",
			async: false,
			data: JSON.stringify({"params": {'fiche': fiche_id, 'fiche_veicule': fiche_veicule_id}}),
			contentType: "application/json",
			complete: function (data) {
				$("#" +fiche_veicule).hide() 
			}
		});

    });


    $('.deletemateriel').on('click', function(ev) {
        ev.preventDefault();
        var fiche_id = $('#fiche_id').val();
   		var fiche_materiel = $(this).closest('tr').attr('id'); // table row ID
   		var fiche_materiel_id = fiche_materiel.split("_").pop();
		console.log("1111111111111111");
		console.log(fiche_materiel_id);
		console.log("22222222222222222222");
		$.ajax({
			type: "POST",
			url: "/deletemateriel",
			async: false,
			data: JSON.stringify({"params": {'fiche': fiche_id, 'fiche_materiel': fiche_materiel_id}}),
			contentType: "application/json",
			complete: function (data) {
				$("#" +fiche_materiel).hide()
			}
		});

    });


    $('.deletemachine').on('click', function(ev) {
        ev.preventDefault();
        var fiche_id = $('#fiche_id').val();
   		var fiche_machine = $(this).closest('tr').attr('id'); // table row ID
   		var fiche_machine_id = fiche_machine.split("_").pop();
		console.log("1111111111111111");
		console.log(fiche_machine_id);
		console.log("22222222222222222222");
		$.ajax({
			type: "POST",
			url: "/deletemachine",
			async: false,
			data: JSON.stringify({"params": {'fiche': fiche_id, 'fiche_machine': fiche_machine_id}}),
			contentType: "application/json",
			complete: function (data) {
				$("#" +fiche_machine).hide() 
			}
		});

    });


    $('.deletefourniture').on('click', function(ev) {
        ev.preventDefault();
        var fiche_id = $('#fiche_id').val();
   		var fiche_fourniture = $(this).closest('tr').attr('id'); // table row ID
   		var fiche_fourniture_id = fiche_fourniture.split("_").pop();
		console.log("1111111111111111");
		console.log(fiche_fourniture_id);
		console.log("22222222222222222222");
		$.ajax({
			type: "POST",
			url: "/deletefourniture",
			async: false,
			data: JSON.stringify({"params": {'fiche': fiche_id, 'fiche_fourniture': fiche_fourniture_id}}),
			contentType: "application/json",
			complete: function (data) {
				$("#" +fiche_fourniture).hide() 
			}
		});

    });


    $('.deletekit').on('click', function(ev) {
        ev.preventDefault();
        var fiche_id = $('#fiche_id').val();
   		var fiche_kit = $(this).closest('tr').attr('id'); // table row ID
   		var fiche_kit_id = fiche_kit.split("_").pop();
		console.log("1111111111111111");
		console.log(fiche_kit_id);
		console.log("22222222222222222222");
		$.ajax({
			type: "POST",
			url: "/deletekit",
			async: false,
			data: JSON.stringify({"params": {'fiche': fiche_id, 'fiche_kit': fiche_kit_id}}),
			contentType: "application/json",
			complete: function (data) {
				$("#" +fiche_kit).hide() 
			}
		});

    });


    $('.deletetuteurage').on('click', function(ev) {
        ev.preventDefault();
        var fiche_id = $('#fiche_id').val();
   		var fiche_tuteurage = $(this).closest('tr').attr('id'); // table row ID
   		var fiche_tuteurage_id = fiche_tuteurage.split("_").pop();
		console.log("1111111111111111");
		console.log(fiche_tuteurage_id);
		console.log("22222222222222222222");
		$.ajax({
			type: "POST",
			url: "/deletetuteurage",
			async: false,
			data: JSON.stringify({"params": {'fiche': fiche_id, 'fiche_tuteurage': fiche_tuteurage_id}}),
			contentType: "application/json",
			complete: function (data) {
				$("#" +fiche_tuteurage).hide() 
			}
		});

    });


    $('.deletevigitaux').on('click', function(ev) {
        ev.preventDefault();
        var fiche_id = $('#fiche_id').val();
   		var fiche_vigitaux = $(this).closest('tr').attr('id'); // table row ID
   		var fiche_vigitaux_id = fiche_vigitaux.split("_").pop();
		console.log("1111111111111111");
		console.log(fiche_vigitaux_id);
		console.log("22222222222222222222");
		$.ajax({
			type: "POST",
			url: "/deletevigitaux",
			async: false,
			data: JSON.stringify({"params": {'fiche': fiche_id, 'fiche_vigitaux': fiche_vigitaux_id}}),
			contentType: "application/json",
			complete: function (data) {
				$("#" +fiche_vigitaux).hide() 
			}
		});

    });


    $('.deleteengrai').on('click', function(ev) {
        ev.preventDefault();
        var fiche_id = $('#fiche_id').val();
   		var fiche_engrai = $(this).closest('tr').attr('id'); // table row ID
   		var fiche_engrai_id = fiche_engrai.split("_").pop();
		console.log("1111111111111111");
		console.log(fiche_engrai_id);
		console.log("22222222222222222222");
		$.ajax({
			type: "POST",
			url: "/deleteengrai",
			async: false,
			data: JSON.stringify({"params": {'fiche': fiche_id, 'fiche_engrai': fiche_engrai_id}}),
			contentType: "application/json",
			complete: function (data) {
				$("#" +fiche_engrai).hide() 
			}
		});

    });


    $('.deletegazon').on('click', function(ev) {
        ev.preventDefault();
        var fiche_id = $('#fiche_id').val();
   		var fiche_gazon = $(this).closest('tr').attr('id'); // table row ID
   		var fiche_gazon_id = fiche_gazon.split("_").pop();
		console.log("1111111111111111");
		console.log(fiche_gazon_id);
		console.log("22222222222222222222");
		$.ajax({
			type: "POST",
			url: "/deletegazon",
			async: false,
			data: JSON.stringify({"params": {'fiche': fiche_id, 'fiche_gazon': fiche_gazon_id}}),
			contentType: "application/json",
			complete: function (data) {
				$("#" +fiche_gazon).hide() 
			}
		});

    });


    $('.deletegmateriel').on('click', function(ev) {
        ev.preventDefault();
        var fiche_id = $('#fiche_id').val();
   		var fiche_gmaterie = $(this).closest('tr').attr('id'); // table row ID
   		var fiche_gmaterie_id = fiche_gmaterie.split("_").pop();
		console.log("1111111111111111");
		console.log(fiche_gmaterie_id);
		console.log("22222222222222222222");
		$.ajax({
			type: "POST",
			url: "/deletegmateriel",
			async: false,
			data: JSON.stringify({"params": {'fiche': fiche_id, 'fiche_gmaterie': fiche_gmaterie_id}}),
			contentType: "application/json",
			complete: function (data) {
				$("#" +fiche_gmaterie).hide() 
			}
		});

    });


    $('.deleteescalier').on('click', function(ev) {
        ev.preventDefault();
        var fiche_id = $('#fiche_id').val();
   		var fiche_escalier = $(this).closest('tr').attr('id'); // table row ID
   		var fiche_escalier_id = fiche_escalier.split("_").pop();
		console.log("1111111111111111");
		console.log(fiche_escalier_id);
		console.log("22222222222222222222");
		$.ajax({
			type: "POST",
			url: "/deleteescalier",
			async: false,
			data: JSON.stringify({"params": {'fiche': fiche_id, 'fiche_escalier': fiche_escalier_id}}),
			contentType: "application/json",
			complete: function (data) {
				$("#" +fiche_escalier).hide() 
			}
		});

    });


    $('.deleteoutilss').on('click', function(ev) {
        ev.preventDefault();
        var fiche_id = $('#fiche_id').val();
   		var fiche_outilss = $(this).closest('tr').attr('id'); // table row ID
   		var fiche_outilss_id = fiche_outilss.split("_").pop();
		console.log("1111111111111111");
		console.log(fiche_outilss_id);
		console.log("22222222222222222222");
		$.ajax({
			type: "POST",
			url: "/deleteoutilss",
			async: false,
			data: JSON.stringify({"params": {'fiche': fiche_id, 'fiche_outilss': fiche_outilss_id}}),
			contentType: "application/json",
			complete: function (data) {
				$("#" +fiche_outilss).hide() 
			}
		});

    });


    $('.deletecloture').on('click', function(ev) {
        ev.preventDefault();
        var fiche_id = $('#fiche_id').val();
   		var fiche_cloture = $(this).closest('tr').attr('id'); // table row ID
   		var fiche_cloture_id = fiche_cloture.split("_").pop();
		console.log("1111111111111111");
		console.log(fiche_cloture_id);
		console.log("22222222222222222222");
		$.ajax({
			type: "POST",
			url: "/deletecloture",
			async: false,
			data: JSON.stringify({"params": {'fiche': fiche_id, 'fiche_cloture': fiche_cloture_id}}),
			contentType: "application/json",
			complete: function (data) {
				$("#" +fiche_cloture).hide() 
			}
		});

    });


    $('.deletediverss').on('click', function(ev) {
        ev.preventDefault();
        var fiche_id = $('#fiche_id').val();
   		var fiche_diverss = $(this).closest('tr').attr('id'); // table row ID
   		var fiche_diverss_id = fiche_diverss.split("_").pop();
		console.log("1111111111111111");
		console.log(fiche_diverss_id);
		console.log("22222222222222222222");
		$.ajax({
			type: "POST",
			url: "/deletediverss",
			async: false,
			data: JSON.stringify({"params": {'fiche': fiche_id, 'fiche_diverss': fiche_diverss_id}}),
			contentType: "application/json",
			complete: function (data) {
				$("#" +fiche_diverss).hide() 
			}
		});

    });


    $('.deleteterrasse').on('click', function(ev) {
        ev.preventDefault();
        var fiche_id = $('#fiche_id').val();
   		var fiche_terrasse = $(this).closest('tr').attr('id'); // table row ID
   		var fiche_terrasse_id = fiche_terrasse.split("_").pop();
		console.log("1111111111111111");
		console.log(fiche_terrasse_id);
		console.log("22222222222222222222");
		$.ajax({
			type: "POST",
			url: "/deleteterrasse",
			async: false,
			data: JSON.stringify({"params": {'fiche': fiche_id, 'fiche_terrasse': fiche_terrasse_id}}),
			contentType: "application/json",
			complete: function (data) {
				$("#" +fiche_terrasse).hide() 
			}
		});

    });


    $('.deletescloture').on('click', function(ev) {
        ev.preventDefault();
        var fiche_id = $('#fiche_id').val();
   		var fiche_scloture = $(this).closest('tr').attr('id'); // table row ID
   		var fiche_scloture_id = fiche_scloture.split("_").pop();
		console.log("1111111111111111");
		console.log(fiche_scloture_id);
		console.log("22222222222222222222");
		$.ajax({
			type: "POST",
			url: "/deletescloture",
			async: false,
			data: JSON.stringify({"params": {'fiche': fiche_id, 'fiche_scloture': fiche_scloture_id}}),
			contentType: "application/json",
			complete: function (data) {
				$("#" +fiche_scloture).hide() 
			}
		});

    });
	
});
