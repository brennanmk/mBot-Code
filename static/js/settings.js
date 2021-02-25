var slider1 = document.getElementById("leftMotor");
var slider2 = document.getElementById("rightMotor");

var output1 = document.getElementById("left");
var output2 = document.getElementById("right");


slider1.oninput = function () {
	output1.innerHTML = this.value;
	saveSliderVals();
}
slider2.oninput = function () {
	output2.innerHTML = this.value;
	saveSliderVals();
}

function saveSliderVals() {
	Cookies.set('slider1',slider1.value);
	Cookies.set('slider2',slider2.value);
}

function loadSliderVals() {
	slider1.value = Cookies.get('slider1') || 100;
	slider2.value = Cookies.get('slider2') || 100;
	output1.innerText = slider1.value;
	output2.innerText = slider2.value;
}
loadSliderVals();