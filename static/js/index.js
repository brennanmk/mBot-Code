'use strict';

// Get elements
const blocklyDiv = document.getElementById('blocklyDiv');
const codePreviewDiv = document.getElementById('code-preview');
const statusMessage = document.getElementById('status');

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
}
workspace.addChangeListener(blocklyUpdateEvent);

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

// Shutdown the pi
document.getElementById('shutdown').onclick = function (e) {

	if (confirm("Are you sure you want to shut down?")) {

		$.post(
			'/execute', {
				action: 'shutdown'
			},
			// Return code
			function (data, status) {
				setTimeout(alert('It is now safe to unplug your pi'),5000);
			}
		)

	}

}