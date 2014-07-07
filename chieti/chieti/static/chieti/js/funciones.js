// addClick
// setQuantity
// checkQuantOk

function checkQuantOk(quant){
	num=$(quant).val();
	um=$(quant).siblings("#um").html();
	console.log("num:",num);
	console.log("um:",um);
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


function addClick(contexto){
	//console.log('çlick')
	quant= $(contexto).siblings('input[name=quantity]');
	if(!checkQuantOk(quant)){
		  //chequear aveces no lo llama
		alert("Cantidad incorrecta");
		$(contexto).focus();
		return;
	}
	var ids= $(contexto).siblings("input[name=ids]").attr("id");
	
	var quant= $(contexto).siblings('input[name=quantity]').val()
	var quantAcheck= $(contexto).siblings('input[name=quantity]')
	divActual=$(contexto);
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
		$(contexto).focus();
	}
	
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

