function charcountupdate(str) {
	var lng = str.length;
	document.getElementById("charcount").innerHTML = lng + ' out of 320 characters';
}

function confirmMsg(){
	if (confirm("Would you like to send the messages?")) {
		alert("It will just be a moment.");
	  } else {
		alert("Messages not sent");
	  }
}