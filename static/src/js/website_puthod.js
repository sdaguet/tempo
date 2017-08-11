odoo.define('darb_puthod.responsivejson', function(require) {
    'use strict';
    require('website.website');
    require('web.ajax');

    $('.pointer').on('click', function(ev) {
        ev.preventDefault();
		console.log($(this).parents('tr').find(".membrid").val());
		var employee_id = $(this).closest('tr').attr('id'); // table row ID
   		var employee = employee_id.split("_").pop();
		console.log(employee);
        $("#pointer_"+employee).hide()
        $("#depointer_"+employee).show()
		$.ajax({
			type: "POST",
			url: "/pointer",
			async: false,
			data: JSON.stringify({"params": {'employee': employee}}),
			contentType: "application/json",
			complete: function (data) {
				console.log(data);
			}
		});

    });

	$('.depointer').on('click', function(ev) {
        ev.preventDefault();
		console.log($(this).parents('tr').find(".membrid").val());
		var employee_id = $(this).closest('tr').attr('id'); // table row ID
   		var employee = employee_id.split("_").pop();
		console.log(employee);
        $("#depointer_"+employee).hide()
        $("#pointer_"+employee).show()
		$.ajax({
			type: "POST",
			url: "/depointer",
			async: false,
			data: JSON.stringify({"params": {'employee': employee}}),
			contentType: "application/json",
			complete: function (data) {
				console.log(data);
			}
		});
    });

	$('.affecter').on('click', function(ev) {
        ev.preventDefault();
		var employee_id = $(this).closest('tr').attr('id'); // table row ID
   		var employee = employee_id.split("_").pop();
        var equipe_id = $('#equipe_id').val();
		console.log(employee);
		$.ajax({
			type: "POST",
			url: "/affecter",
			async: false,
			data: JSON.stringify({"params": {'equipe_id': equipe_id, 'employee_id': employee}}),
			contentType: "application/json",
			complete: function (data) {
				console.log(data);
				$("#" +employee_id).hide()
				$('#equipe_id').val(data['responseJSON']["result"]["equipe"]);
			}
		});
    });

    $('.edit').on('click', function(ev) {
        var text_value = $(".vname").val();
        if(text_value=='') {
        console.log("Enter Some Text In Input Field");
        }else{
        console.log(text_value);
        }
	});
	
});
