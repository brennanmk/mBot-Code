'use strict';

// Slider
/*const powerSlider = document.getElementById("motorPowerSlider");
const powerIndicator = document.getElementById("motorPowerValue");
powerSlider.oninput = function() {
	powerIndicator.innerHTML = this.value;
};
powerSlider.oninput();*/

// Arrow controls
const ARROW_BUTTONS = {
	ArrowUp: document.getElementById("BtnForwards"),
	ArrowDown: document.getElementById("BtnBackwards"),
	ArrowRight: document.getElementById("BtnRight"),
	ArrowLeft: document.getElementById("BtnLeft")
}
const STOP_BUTTON = document.getElementById("BtnStop");
// Add key listener
document.addEventListener('keypress', (e) => {
	if (e.code in ARROW_BUTTONS) {
		ARROW_BUTTONS[e.code].click();
	}
});
document.addEventListener('keyup', (e) => {
	if (e.code in ARROW_BUTTONS) {
		STOP_BUTTON.click();
	}
});


// Sensor value updater
setInterval(function () {
	$.ajax({
		url: '/update',
		type: 'POST',
		success: function (response) {
			//console.log(response);
			$("#linesen").html(response["lineValue"]);

			if (response["distValue"] < 0) {
				$("#distsen").html("[Sensor Timeout]");
			}else{
				$("#distsen").html(response["distValue"]);
			}

		},
		error: function (error) {
			console.log(error);
		}
	})
}, 1000);