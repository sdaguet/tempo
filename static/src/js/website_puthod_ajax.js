odoo.define('darb_puthod.responsivejson', function(require) {
    'use strict';
    require('website.website');
    require('web.ajax');

    $('.ajaxi').on('click', function(ev) {
        ev.preventDefault();
		console.log($(this).parent().find(".kname").val());
		console.log("KKKKKKKKKKKKKK");
		var dt = $(this).parent().find(".kname").val();
		$.ajax({
			type: "POST",
			url: "/ajaxi",
			async: false,
			data: JSON.stringify({"params": {'fiche': dt}}),
			contentType: "application/json",
			complete: function (data) {
				console.log("mmmmmmmmmmmmmmm");
				$("<span>Hello world!</span>").insertAfter("p");
				var $span = $(this).parent().find(".tesxt");
				console.log($span); 
				console.log($(this).parent()); 
				var $add = $('<p>hhhhhhhhhhhhhhhhhhhhhhhhh</p>'); 
				$add.insertAfter($span);
				console.log("ggggggggggggggggg");  
			}
		});

    });
	
});
