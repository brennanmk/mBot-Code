const tiltSlider = document.getElementById("motorTiltSlider");
const speedSlider = document.getElementById("motorSpeedSlider");

const tiltOutput = document.getElementById("tiltReadout");
const speedOutput = document.getElementById("speedReadout");


tiltSlider.oninput = function () {
	tiltOutput.innerText = this.value;
	saveSliderVals();
}
speedSlider.oninput = function () {
	speedOutput.innerHTML = this.value;
	saveSliderVals();
}

function saveSliderVals() {
	Cookies.set('tilt',tiltSlider.value);
	Cookies.set('speed',speedSlider.value);
}

function loadSliderVals() {
	tiltSlider.value = Cookies.get('tilt') || 0;
	speedSlider.value = Cookies.get('speed') || 100;
	tiltOutput.innerText = tiltSlider.value;
	speedOutput.innerText = speedSlider.value;
}
loadSliderVals();