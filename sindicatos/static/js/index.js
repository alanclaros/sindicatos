/************************************************************************************/
/************************************************************************************/
/****************Desarrollador, Programador: Alan Claros Camacho ********************/
/****************E-mail: alan_Claros13@hotmail.com **********************************/
/************************************************************************************/
/************************************************************************************/

function load_login(){
	document.forms["formulario"].user_name.focus();	
}

function verifyForm(){
	nombre= "user_name";
	objeto= document.forms["formulario"].elements[nombre];
	if(TrimDerecha(TrimIzquierda(objeto.value))==""){
		alert("Your must fill your User Name");
		objeto.focus();
		return false;
	}
	
	nombre= "user_password";
	objeto= document.forms["formulario"].elements[nombre];
	if(TrimDerecha(TrimIzquierda(objeto.value))==""){
		alert("Your must fill your Pasword");
		objeto.focus();
		return false;
	}
	
	document.forms["formulario"].submit();

	return true;
}