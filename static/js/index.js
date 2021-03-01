'use strict';


// Setup arrow buttons
const DIRECTIONS = [ // These are the directions we need to address
	'forwards',
	'backwards',
	'right',
	'left',
	'stop'
];
const KEYNAMES = [ // These are the arrow keys we can use
	'ArrowUp',
	'ArrowDown',
	'ArrowRight',
	'ArrowLeft',
	'RobotStop'
];
let keyStates = {}; // States for keys
let keyButtonMapping = {}; // Used to link keys to buttons
const directionLabel = document.getElementById('direction');

for (let i=0;i<5;i++) {
	const dir = DIRECTIONS[i];
	const dirUpper = (dir.charAt(0).toUpperCase() + dir.slice(1));
	const btn = document.getElementById("Btn"+dirUpper);

	btn.addEventListener('click',(e) => {
		e.preventDefault();
		directionLabel.innerText = 'Moving: '+dirUpper;
		$.getJSON('/drive',{direction:dir}).done((d) => {});
	});

	keyButtonMapping[KEYNAMES[i]] = btn;
}

// Setup arrow keys
document.addEventListener('keydown',(e) => {
	if (KEYNAMES.includes(e.code) && !keyStates[e.code]) {
		console.log(e.code);
		keyStates[e.code] = true;

		// Press the appropriate on-screen button
		keyButtonMapping[e.code].click();
	}
});

document.addEventListener('keyup',(e) => {
	if (KEYNAMES.includes(e.code)) {
		keyStates[e.code] = false;
		// Stop the robot
		keyButtonMapping['RobotStop'].click();
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