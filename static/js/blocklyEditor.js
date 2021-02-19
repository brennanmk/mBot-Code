'use strict';

const SAVE_NAME = "robot-code";

// Get elements
const blocklyDiv = document.getElementById('blocklyDiv');
const codePreviewDiv = document.getElementById('code-preview');
const statusMessage = document.getElementById('status');
const saveMessage = document.getElementById('save-status');

let saveTimeout;

// Inject workspace
const workspace = Blockly.inject(blocklyDiv, {
	toolbox: document.getElementById('toolbox'),
	scrollbars: true,
	trashcan: true,
	grid: {
		spacing: 20,
		length: 3,
		colour: '#ccc',
		snap: true
	}
});

// Setup realtime code preview
function blocklyUpdateEvent(e) {
	const code = Blockly.Python.workspaceToCode(workspace);
	codePreviewDiv.textContent = code;
	hljs.highlightBlock(codePreviewDiv);

	//saveWorkspace();
	// Queue a save event
	if (saveTimeout != null) {
		clearTimeout(saveTimeout);
	}
	saveTimeout = setTimeout(saveWorkspace,1000);
	saveMessage.innerText = 'Saving...';
}
workspace.addChangeListener(blocklyUpdateEvent);


// Save the workspace to local storage
function saveWorkspace() {
	if (typeof(Storage) !== "undefined") {
		const xml = Blockly.Xml.workspaceToDom(Blockly.mainWorkspace);
		localStorage.setItem(SAVE_NAME,Blockly.Xml.domToText(xml));

		saveMessage.innerText = 'Saved';
	}else{
		console.log("Error saving workspace");
	}
}

function loadWorkspace() {
	if (typeof(Storage) !== "undefined") {
		if (localStorage.hasOwnProperty(SAVE_NAME)) {
			const xml = Blockly.Xml.textToDom(localStorage.getItem(SAVE_NAME));
			Blockly.Xml.domToWorkspace(Blockly.mainWorkspace,xml);
			console.log("Loaded saved workspace!");

			blocklyUpdateEvent(null);
		}else{
			console.log("LocalStorage is null");
		}
	}else{
		console.log("Error loading workspace");
	}
}


// Send code on button press
document.getElementById('run-code').onclick = function (e) {
	const code = Blockly.Python.workspaceToCode(workspace);
	statusMessage.textContent = 'Running...';

	document.getElementById('stop-code').disabled = false;

	$.post(
		'/execute', {
			action: 'execute',
			code: code
		},
		// Return code
		function (data, status) {
			if (data == 'DONE') {
				statusMessage.textContent = 'Execution completed!';
			} else if (data == 'BUSY') {
				statusMessage.textContent = 'The robot is already running code!';
			} else if (data == 'ERROR') {
				statusMessage.textContent = 'There was a problem running your code!';
			} else if (data == 'STOPPED') {
				statusMessage.textContent = 'Program stopped';
			}


			document.getElementById('stop-code').disabled = true;
			setTimeout(() => statusMessage.textContent = 'Idle', 3000);
		}
	);
}

// Stop code manually
document.getElementById('stop-code').onclick = function (e) {

	$.post(
		'/execute', {
			action: 'stop'
		},
		// Return code
		function (data, status) {

		}
	)
}

window.onload = loadWorkspace;