odoo.define('darb_puthod.responsivejson', function(require) {
    'use strict';
    require('website.website');
    require('web.ajax');

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
        var text_value = $(".vname").val();
        if(text_value=='') {
        console.log("Enter Some Text In Input Field");
        }else{
        console.log(text_value);
        }
});
});
