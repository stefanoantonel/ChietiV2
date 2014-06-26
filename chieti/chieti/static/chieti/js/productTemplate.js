
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
			//prod=data.prod;
			//items=$('#img'+id).find('.prodItems').removeAttr('style');
			items=$('#img'+id+'').parent('.divImg').find('.prodItems').clone();
			$(items).removeAttr('style');
			console.log(items);
			//popUpAutoComplete(id,prod.name,prod.um,prod.saleP,items);
			popUpAutoComplete(id,data.name,data.um,data.saleP,items);
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

	labelProdPromos=$(template).find("#itemPromo").append(items);
	/*
	for(i=0;i<items.length;i++){
		$(labelProdPromos).append('<br>',items[i].prod,' ',items[i].quantity,' ',items[i].mu);
	}
	*/

	//---------------------------
	
	//CENTRAR
	//$(template).css({position: "absolute",top:'30%',left:'35%'});
	$(template).css("display","");

	$("#divAutoComplete").append(template);
	$('.divInvisible').click(function(event){
		//event.stopPropagation();
		//console.log("se detuvo");
	});

	$('.add').click(addClick);
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

	

	$('.divImg').click(function(event){
		//event.stopPropagation();
	});	

	
	setQuantity();
	
		
	$(".l").click(function() {
		$.ajax({
			//url: '/chieti/getproducts/',
			url: '/chieti/getproducts/',
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
			
			popUpAutoComplete(data.item.id,data.item.name,data.item.um,data.item.saleP);
		}
	});
		
	//  $( ".productImg" ).unbind('click').bind('click', popUp($(this).attr("name")));
	$("#close").click(function() {
		
		$(this).parent("#divInvisible").remove();
	});


	recargar();
	reloadTotalPrice();
});

function checkQuantOk(quant){
	num=$(quant).val();
	um=$(quant).siblings("#um").html();
	if(!$.isNumeric(num)){
		return false;
	}
	if(num < 0.1)
		return false;
	if (um=="Un"){
		if(!(num % 1 === 0)){
			return false
		}
	}
	return true;
}

function addClick(){
	console.log('çlick')
	quant= $(this).siblings('input[name=quantity]');
	if(!checkQuantOk(quant)){
		  //chequear aveces no lo llama
		alert("Cantidad incorrecta");
		$(this).focus();
		return;
	}
	var ids= $(this).siblings("input[name=ids]").attr("id");
	
	var quant= $(this).siblings('input[name=quantity]').val()
	var quantAcheck= $(this).siblings('input[name=quantity]')
	divActual=$(this);
	if(checkQuantOk(quantAcheck)==true){
		$.ajax({
			url: '/chieti/addToOrder/',
			type: 'get', 
			data: {
				'ids':ids,
				'quantity':quant,
				//'csrfmiddlewaretoken': $('input[name=csrfmiddlewaretoken]').val(),
			},
			success: function(data) {
				
				if (data != 'true'){
					$('body').html(data);
			/* var w  = 400;
			var h = 300;
			var left = (screen.width/2)-(w/2);
			var top = (screen.height/2)-(h/2);
			var myWindow = window.open('/chieti/singIn/?ventana=1','','toolbar=no, location=no, directories=no, status=no, menubar=no, scrollbars=yes, resizable=no, copyhistory=no, width='+w+', height='+h+', top='+top+', left='+left);*/
				}
				else{
					// Agregar efecto
					$(divActual).parents(".divActual").remove();                	
				}
			}


		});
	}
	else{
		alert("Cantidad incorrecta");
		$(this).focus();
	}
	reloadTotalPrice();
}

function setQuantity(){
	$('.quantity').change(function(){
		var ant=$(this).siblings(".price").attr('title');
		var cant=$(this).val()            
		var dsp=ant*cant
		dsp = dsp.toFixed(2);
		
		
		$(this).siblings('.price').html(dsp) 
		 
	});
}

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