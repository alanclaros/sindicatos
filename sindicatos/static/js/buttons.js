/************************************************************************************/
/************************************************************************************/
/****************Desarrollador, Programador: Alan Claros Camacho ********************/
/****************E-mail: alan_Claros13@hotmail.com **********************************/
/************************************************************************************/
/************************************************************************************/

/** para ocultar los mensajes despues de 3 segundos */
setTimeout(function () {
	$('#message').fadeOut('slow');
}, 3000);

function objectAjaxNotify() {
	var xmlhttp = false;
	try {
		xmlhttp = new ActiveXObject("Msxml2.XMLHTTP");
	} catch (e) {
		try {
			xmlhttp = new ActiveXObject("Microsoft.XMLHTTP");
		} catch (E) {
			xmlhttp = false;
		}
	}

	if (!xmlhttp && typeof XMLHttpRequest != 'undefined') {
		xmlhttp = new XMLHttpRequest();
	}
	return xmlhttp;
}

//open module
function openModule(module) {
	document.forms["form_menu2"].elements["chapter"].value = module;
	document.forms["form_menu2"].submit();
}

//function send order
function sendOrder(order, type, field_order, field_type) {
	document.forms["form_order"].elements[field_order].value = order;
	document.forms["form_order"].elements[field_type].value = type;
	document.forms["form_order"].submit();
}

//confirmar eliminar
function confirmarEliminar() {
	if (confirm('Esta seguro de querer eliminar este elemento?')) {
		document.forms['formulario'].elements['add_button'].disabled = true;
		document.forms['formulario'].elements['button_cancel'].disabled = true;
		document.forms['formulario'].submit();
	}
}

function confirmarAnular() {
	if (confirm('Esta seguro de querer anular este elemento?')) {
		document.forms['formulario'].elements['add_button'].disabled = true;
		document.forms['formulario'].elements['button_cancel'].disabled = true;
		document.forms['formulario'].submit();
	}
}

// mandamos el formulario
function mandarFormulario(formulario, add_button, button_cancel) {

	if (verifyForm()) {
		//document.forms[formulario].elements[add_button].className= "button_disabled";
		document.forms[formulario].elements[add_button].disabled = true;

		//document.forms[formulario].elements[button_cancel].className= "button_disabled";
		document.forms[formulario].elements[button_cancel].disabled = true;

		document.forms[formulario].submit();
	}
}

//mandamos directamente el formulario
function mandarFormularioDirecto(formulario, add_button, button_cancel) {
	//document.forms[formulario].elements[add_button].className= "button_disabled";
	document.forms[formulario].elements[add_button].disabled = true;

	//document.forms[formulario].elements[button_cancel].className= "button_disabled";
	document.forms[formulario].elements[button_cancel].disabled = true;

	document.forms[formulario].submit();
}

function load_form(campo) {
	cFocus = document.getElementById(campo);
	cFocus.focus();
}

function cancelForm() {
	document.formulario.add_button.disabled = true;
	document.formulario.button_cancel.disabled = true;
	document.form_cancel.submit();
	return true;
}

//fucniones generales para los campos de la base de datos
function validarCadena(nombre) {

}

function validarFecha(nombre) {

}

function validarNumero(nombre) {
	tipo = typeof (nombre);
	if (tipo == 'object') {
		campo = nombre;
	}
	if (tipo == "string") {
		campo = document.getElementById(nombre);
	}
	//alert(campo);
	var tam = campo.value.length;
	var valor = "";
	var letra = "";
	var nuevo_valor = "";
	for (i = 0; i < tam; i++) {
		valor = campo.value.substring(i, (i + 1));
		letra = valor.toUpperCase();
		if (letra == "1" || letra == "2" || letra == "3" || letra == "4" || letra == "5" || letra == "6" || letra == "7" || letra == "8" || letra == "9" || letra == "0" || letra == "-") {
			nuevo_valor = nuevo_valor + letra;
		}
	}
	campo.value = nuevo_valor;
}

function validarNumeroPunto(nombre) {
	tipo = typeof (nombre);
	if (tipo == 'object') {
		campo = nombre;
	}
	if (tipo == "string") {
		campo = document.getElementById(nombre);
	}

	var tam = campo.value.length;
	var valor = "";
	var letra = "";
	var nuevo_valor = "";
	for (i = 0; i < tam; i++) {
		valor = campo.value.substring(i, (i + 1));
		letra = valor.toUpperCase();
		if (letra == "1" || letra == "2" || letra == "3" || letra == "4" || letra == "5" || letra == "6" || letra == "7" || letra == "8" || letra == "9" || letra == "0" || letra == "." || letra == "-") {
			nuevo_valor = nuevo_valor + letra;
		}
	}
	campo.value = nuevo_valor;
}

function validarText(nombre) {

}

function verifyForm() {
	//variables a controlar
	controlForm = TrimDerecha(TrimIzquierda(document.forms["formulario"].elements["control_form"].value));
	tam = controlForm.length;

	if (tam > 0) {
		var division = controlForm.split(";");
		tamC = division.length;

		for (i = 0; i < tamC; i++) {
			auxS = division[i];
			divisionC = auxS.split("|");
			tipoDato = divisionC[0];
			tamDato = parseInt(divisionC[1]);
			controlarDato = divisionC[2];
			nombreCampo = divisionC[3];

			campoForm = document.getElementById(nombreCampo);
			valor = TrimDerecha(TrimIzquierda(campoForm.value));
			tamValor = valor.length;

			if (tipoDato == "txt" && controlarDato == "S") {
				if (tamValor == 0) {
					alert('Debe llenar este campo');
					campoForm.focus();
					return false;
				}
				if (tamValor < tamDato) {
					alert('Este campo debe tener al menos ' + tamDato + ' letras');
					campoForm.focus();
					return false;
				}
			}

			if (tipoDato == "cbo" && controlarDato == "S") {
				if (valor == "0") {
					alert('Debe seleccionar un valor');
					campoForm.focus();
					return false;
				}
			}
		} //fin for
	} // fin if tam>0

	return controlModulo();
}

/*
//recordatorios
//recordatorios
//recordatorios
var inicioNotify=0;
var inicioMostrar=0;
var myVar;
var myVar2;
var tiempoDuracion=10000; // milisegundos
var tiempoRecarga= 60; //segundos para recargar datos
var tiempoAviso= 65; //segundos, para volver a mostrar el aviso

function verificarEntregaRecogos(){
	myVar= setInterval(function(){
			if(inicioNotify<tiempoRecarga){
				inicioNotify= inicioNotify+1;
				//alert(inicioNotify);
			}
			else{
				inicioNotify=0;
				try{
					p_window="page.php?chapter=notify";
					divResult = document.getElementById("div_notify");
					divResult.innerHTML= '<img src="images/pass/loading2.gif">';
					ajax=objectAjaxNotify();
					ajax.open("POST", p_window,true);
					ajax.onreadystatechange=function() {
						if (ajax.readyState==4) {
							divResult.innerHTML = ajax.responseText;
						}
					}
				
					va_id= "id";
					ajax.setRequestHeader("Content-Type","application/x-www-form-urlencoded");
					ajax.send("id="+va_id);
				}
				catch(error){
					console.error(error);
				}				
			}
	} ,1000);
	
	myVar2= setInterval(function(){
		if(inicioMostrar<tiempoAviso){
			inicioMostrar= inicioMostrar+1;
		}
		else{
			inicioMostrar=0;
			try{
				ev_cant=parseInt(document.frm_notificacion.ev_cant.value);
				ep_cant= parseInt(document.frm_notificacion.ep_cant.value);
				rv_cant=parseInt(document.frm_notificacion.rv_cant.value);
				rp_cant= parseInt(document.frm_notificacion.rp_cant.value);
				
				div_iep= document.getElementById("div_iep");
				div_iep.innerHTML='<font class="icono_ep">EP: '+ep_cant+'</font>';
				
				div_iev= document.getElementById("div_iev");
				div_iev.innerHTML='<font class="icono_ev">EV: '+ev_cant+'</font>';
				
				div_irp= document.getElementById("div_irp");
				div_irp.innerHTML='<font class="icono_rp">RP: '+rp_cant+'</font>';
				
				div_irv= document.getElementById("div_irv");
				div_irv.innerHTML='<font class="icono_rv">RV: '+rv_cant+'</font>';
				
				lista_entrega_vencidos="";
				lista_entrega_pendientes="";
				lista_recogo_vencidos="";
				lista_recogo_pendientes="";
				
				//entrega vencidos
				aux_s= document.frm_notificacion.entrega_vencidos.value;
				tamanio= aux_s.length;
				if(tamanio>0){
					var division= aux_s.split(";");
					cant_entrega_vencidos= division.length;
					for(i=0; i<cant_entrega_vencidos; i++){
						lista_entrega_vencidos= lista_entrega_vencidos + division[i] + "<br>";
					}
				}
				
				//entrega pendientes
				aux_s= document.frm_notificacion.entrega_pendientes.value;
				tamanio= aux_s.length;
				if(tamanio>0){
					var division= aux_s.split(";");
					cant_entrega_pendientes= division.length;
					for(i=0; i<cant_entrega_pendientes; i++){
						lista_entrega_pendientes= lista_entrega_pendientes + division[i] + "<br>";
					}
				}
				
				//recogo vencidos
				aux_s= document.frm_notificacion.recogo_vencidos.value;
				tamanio= aux_s.length;
				if(tamanio>0){
					var division= aux_s.split(";");
					cant_recogo_vencidos= division.length;
					for(i=0; i<cant_recogo_vencidos; i++){
						lista_recogo_vencidos= lista_recogo_vencidos + division[i] + "<br>";
					}
				}
				
				//recogo pendientes
				aux_s= document.frm_notificacion.recogo_pendientes.value;
				tamanio= aux_s.length;
				if(tamanio>0){
					var division= aux_s.split(";");
					cant_recogo_pendientes= division.length;
					for(i=0; i<cant_recogo_pendientes; i++){
						lista_recogo_pendientes= lista_recogo_pendientes + division[i] + "<br>";
					}
				}
				
				//settings
				$.notifyDefaults({
					delay: tiempoDuracion
				});
			
				//entregas vencidas
				if(ev_cant>0){
					$.notify({
						title: '<div style="color:#000000;"><b>ENTREGAS VENCIDAS</b></div>',
						message: lista_entrega_vencidos
						},
						{
							type: 'danger',
							animate: {
								enter: 'animated fadeInRight',
								exit: 'animated fadeOutRight'
							}
						}
					);
				}				
			
				//recojos vencidos
				if(rv_cant>0){
					$.notify({
						title: '<div style="color:#000000;"><b>RECOJOS VENCIDOS</b></div>',
						message: lista_recogo_vencidos
						},
						{
							type: 'danger',
							animate: {
								enter: 'animated fadeInRight',
								exit: 'animated fadeOutRight'
							}
						}
					);
				}
				
				//entregas pendientes
				if(ep_cant>0){
					$.notify({
						title: '<div style="color:#000000;"><b>ENTREGAS PENDIENTES</b></div>',
						message: lista_entrega_pendientes
						},
						{
							type: 'success',
							animate: {
								enter: 'animated fadeInRight',
								exit: 'animated fadeOutRight'
							}
						}
					);
				}
				
				//recojos pendientes
				if(rp_cant>0){
					$.notify({
						title: '<div style="color:#000000;"><b>RECOJOS PENDIENTES</b></div>',
						message: lista_recogo_pendientes
						},
						{
							type: 'success',
							animate: {
								enter: 'animated fadeInRight',
								exit: 'animated fadeOutRight'
							}
						}
					);
				}
				
			}
			catch(error){
				console.error(error);
			}
		}
	},1000);
	
	//myVar= setInterval(cargarEntregaRecogos(), 3000);
	//setTimeout(mostrarEntregaRecogos(), 1000);
}

//fin recordatorios
//fin recordatorios
//fin recordatorios
*/

function TrimDerecha(str) {
	var resultStr = "";
	var i = 0;

	// Return immediately if an invalid value was passed in
	if (str + "" == "undefined" || str == null)
		return null;

	// Make sure the argument is a string
	str += "";

	if (str.length == 0)
		resultStr = "";
	else {
		// Loop through string starting at the end as long as there
		// are spaces.
		i = str.length - 1;
		while ((i >= 0) && (str.charAt(i) == " "))
			i--;

		// When the loop is done, we're sitting at the last non-space char,
		// so return that char plus all previous chars of the string.
		resultStr = str.substring(0, i + 1);
	}

	return resultStr;
}

function TrimIzquierda(str) {
	var resultStr = "";
	var i = len = 0;

	// Return immediately if an invalid value was passed in
	if (str + "" == "undefined" || str == null)
		return null;

	// Make sure the argument is a string
	str += "";

	if (str.length == 0)
		resultStr = "";
	else {
		// Loop through string starting at the beginning as long as there
		// are spaces.
		//	  	len = str.length - 1;
		len = str.length;

		while ((i <= len) && (str.charAt(i) == " "))
			i++;

		// When the loop is done, we're sitting at the first non-space char,
		// so return that char plus the remaining chars of the string.
		resultStr = str.substring(i, len);
	}

	return resultStr;
}


/**impresion, dialogo modal */
function closeModalPrint() {
	modal = document.getElementById("printModal");
	modal.style.display = "none";
}

function openModalPrint() {
	modal = document.getElementById("printModal");
	modal.style.display = "block";
}

// Get the modal
var modal = document.getElementById("printModal");

// Get the button that opens the modal
//var btn = document.getElementById("myBtn");

// Get the <span> element that closes the modal
//var spanClosePrint = document.getElementsByClassName("spanClosePrint")[0];
//var spanCloseP = document.getElementById("spanClosePrint");

// When the user clicks the button, open the modal 
/*btn.onclick = function() {
modal.style.display = "block";
}*/

// When the user clicks on <span> (x), close the modal
/*spanCloseP.onclick = function() {
	modal.style.display = "none";
}*/

// When the user clicks anywhere outside of the modal, close it
window.onclick = function (event) {
	if (event.target == modal) {
		modal.style.display = "none";
	}
}

/**labels para cambiar el texto: apellidos a ape:, para version movil */
window.addEventListener('resize', cambiarTexto);

var arrayLabels = Array();
var arrayLabelsPeque = Array();
cantLabels = 100;

function cargarLabels() {
	for (k = 0; k <= cantLabels; k++) {
		aux = document.getElementById('label' + k);
		nombre = 'label' + k + '_c';
		hidd = document.getElementById(nombre);
		if (aux != null) {
			arrayLabels[k] = aux.innerHTML;
			arrayLabelsPeque[k] = hidd.value;
		}
	}
}


function cambiarTexto() {
	var width = document.documentElement.clientWidth;
	if (width <= 768) {
		for (i = 0; i <= cantLabels; i++) {
			aux = document.getElementById('label' + i);
			if (aux != null) {
				aux.innerHTML = arrayLabelsPeque[i];
			}
		}
	} else {
		for (i = 0; i <= cantLabels; i++) {
			aux = document.getElementById('label' + i);
			if (aux != null) {
				aux.innerHTML = arrayLabels[i];
			}
		}
	}
}

/**fin label */

function redondeo(numero, decimales) {
	var flotante = parseFloat(numero);
	var resultado = Math.round(flotante * Math.pow(10, decimales)) / Math.pow(10, decimales);
	resultado2 = resultado;
	var aux_c = "" + resultado;
	if (aux_c.indexOf('.') != -1) {
		//si hay decimales
		var division = aux_c.split(".");
		ta = division[1].length;
		if (ta == 1) {
			resultado2 = resultado + "0";
		}
	}
	else {
		//sin decimales
		resultado2 = resultado + ".00";
	}

	return resultado2;
}
