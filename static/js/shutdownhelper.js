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