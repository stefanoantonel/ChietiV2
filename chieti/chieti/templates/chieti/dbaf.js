<!DOCTYPE html>
<html>
	
	<head>
		<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
		<title>Insert title here</title>
		<link href="css/bootstrap.min.css" rel="stylesheet" media="screen">
		<link href="css/ui-lightness/jquery-ui-1.10.3.custom.min.css" rel="stylesheet" media="screen">  
		
		<script src="css/js/jquery-1.9.1.js"></script>
		<script src="css/js/jquery-ui-1.10.3.custom.min.js"></script>
		<script src="css/js/bootstrap.min.js"></script>
		<script type="text/javascript">

		$(document).ready(function() {
				
			$("#clientes").autocomplete({
			      source: "getClientesJSON",
			      minLength: 2,
			      select: function( event, data ) {
			    	  $("#salida").html("Cliente: "+data.item.label+"<br/>Id: "+data.item.id);
			      }
			});
			$("#btnAgregaCliente").click(function(){
				$("#agregaCliente").attr("src","agregarCliente.jsp");
				$("#form").dialog({
					height: 300,
					width: 550,
					modal: true
				});
			});

		});


		</script>
	</head>
	
	<body>
	<div class="ui-widget" align="center">
	<br/><br/><br/>
  		<label for="clientes">Clientes: </label>
  		<input id="clientes" />
	
	<div id="salida"></div>
	<div class="btn" id="btnAgregaCliente">Agregar Cliente</div>
	<div id="form" style="display:none">
		<iframe id="agregaCliente" width="100%" height="100%" seamless="seamless"></iframe>
	</div>
	</div>
	</body>
	
</html>