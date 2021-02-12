'use strict';

// Slider
const powerSlider = document.getElementById("motorPowerSlider");
const powerIndicator = document.getElementById("motorPowerValue");
powerSlider.oninput = function() {
	powerIndicator.innerHTML = this.value;
};
powerSlider.oninput();


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