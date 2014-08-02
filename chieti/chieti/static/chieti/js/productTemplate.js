
var prevID;

function popUp(id) {
	if(prevID!=undefined){Desaparecer(prevID);}
	prevID=id;	
	findProductById(id);
}

function findProductById(id){
	$.ajax({
		url: '/chieti/findProductById/',
		type: 'get', 
		data: {
			'id':id,
		},
		dataType: 'json',
		success: function(data) {		
			
			//popUpAutoComplete(id,data.name,data.um,data.saleP);
			//----------------------
			prod=data.prod;
			//items=$('#img'+id).find('.prodItems').removeAttr('style');
			items=$('#img'+id+'').parent('.divImg').find('.prodItems').clone();
			$(items).removeAttr('style');
			console.log(items);
			popUpAutoComplete(id,prod.name,prod.um,prod.saleP,data.items)
			//popUpAutoComplete(id,data.name,data.um,data.saleP,items);
			//-------------------
		}	
	});
}

function popUpAutoComplete(id,nameProd,um,saleP,items) {

	if(prevID!=undefined){Desaparecer(prevID);}
	prevID=id;	
	template= $(".divAuto").clone();
	$(template).removeClass("divAuto");
	$(template).addClass("divActual");
	$(template).prepend("<img  src='/static/chieti/productImages/"+id+".png'  class='productImg2'>");
	$(template).attr("id","div"+id);
	$(template).attr("name",id);
	name=$(template).attr("name");
	$(template).attr("value","visible");
	ids= $(template).find("input[name='ids']");
	$(ids).attr("id",id);
	nameLabel= $(template).find(".product");
	nameLabelTT= $(template).find(".productTT");
	$(nameLabel).html(nameProd);
	unidadMedida= $(template).find("[name='UnidadMedida']");
	$(unidadMedida).html(um);
	pr= $(template).find(".price");
	$(pr).html(saleP);
	$(pr).attr("title",saleP);

	//--------------------------

	//labelProdPromos=$(template).find("#itemPromo").append(items);
	
	for(i=0;i<items.length;i++){
		$(template).find("#itemPromo").append('<br>',items[i].prod,' ',items[i].quantity,' ',items[i].mu);
	}
	

	//---------------------------
	
	//CENTRAR
	//$(template).css({position: "absolute",top:'30%',left:'35%'});
	$(template).css("display","");

	$("#divAutoComplete").append(template);
	$('.divInvisible').click(function(event){
		//event.stopPropagation();
		//console.log("se detuvo");
	});

	$('.add').click(function(){ addClick(this);
	reloadTotalPrice();
	});
	$('#close').click(function(){
		$(".divActual").remove();
	});
	setQuantity();

	$(template).keyup(function(e) { 
		if (e.which == 27) {
			//alert('esc');
			$(".divActual").remove();
		}
	});
	
	$(template).find('.quantity').focus();
}

function Desaparecer(id){
	$("#div"+id).remove();
}

$(document).ready(function() {

	$(document).on('click','.navbar-collapse.in',function(e) {
		console.log(this);
	    if( $(e.target).is('a') ) {
	        $(this).collapse('hide');
	        console.log(this);
	    }
	});

	$('.divImg').click(function(event){
		//event.stopPropagation();
	});	

	
	setQuantity();
	
		
	$(".l").click(function() {
		$.ajax({
			url: '/chieti/getProducts/',
			//url: '/chieti/getproducts/',
			type: 'get', 
			data: {
				'id': $(this).attr("id"),
				  //'id': $(this).val(),
				},
				success: function(data) {
				  //console.log("todo ok! AJAX")
				  //console.log(data)
				  $("body").find('.allProducts').parent('section').html(data);
				  recargar();
			  }
		});    
	});
	
	$("#carrito").click(function() {
		$(location).attr('href','/chieti/changeOrder');       			
	});
	
		
	$( "#tags" ).autocomplete({
		source:"/chieti/complete/",
		minLength:2,
		select: function( event, data ) {
			findProductById(data.item.id);
			//popUpAutoComplete(data.item.id,data.item.name,data.item.um,data.item.saleP);
		}
	});
		
	//  $( ".productImg" ).unbind('click').bind('click', popUp($(this).attr("name")));
	$("#close").click(function() {
		
		$(this).parent("#divInvisible").remove();
	});


	recargar();
	reloadTotalPrice();
});





function recargar(){
	//tooltip
	$( ".divImg").hover(
		function(){
			
			eleOffset = $(this).find(".productImg").offset();
				//console.log("eleOffset",eleOffset);
				//Revisar
			offTop=eleOffset.top-30;
			//console.log("offTop",offTop);
			//console.log("eleOffset.top",eleOffset.top);
			productTT=$(this).find(".productTT")
			$(productTT).fadeIn("fast").css({
				left: eleOffset.left,
				top: offTop
			});
			$(productTT).click(function(){
				id=$(this).attr('name');
				console.log(this);
				findProductById(id);
			});
			//$(productTT).delay(10000).fadeOut();
		}, 
		function(){
		    $(this).find(".productTT").delay(10).fadeOut();
		  }
	);		
				
		//$('input[name=quantity]').change(function(){
		
	//  $( ".productImg" ).unbind('click').bind('click', popUp($(this).attr("name")));
	
	$('img.productImg').lazyload({
		threshold : 200,
		effect : "fadeIn"
		
	});
}

function reloadTotalPrice(){
	
	$.ajax({
		url: '/chieti/getTotalPriceOrder/',
		type: 'get',
		success: function(data) {		
			$('#totalPrice').html(data);
		}	
	});
}