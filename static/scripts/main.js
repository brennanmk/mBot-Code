/**
 * @license
 * Copyright 2017 Google LLC
 * SPDX-License-Identifier: Apache-2.0
 */
 (function() {

  // Run the blockly code
  function executeBlocks(event) {
    let code = Blockly.Python.workspaceToCode(Blockly.getMainWorkspace());
    
    // Send POST request
    $.ajax({
      url: "/editor",
      method: "POST",
      data: {
        code: code
      },
      success: function(res) {
        alert("Code deployed successfully!");
      }
    });

  }

  document.querySelector('#run').addEventListener('click', executeBlocks);

  // Actually inject main code into page
  Blockly.inject('blocklyDiv', {
    toolbox: document.getElementById('toolbox'),
    scrollbars: false,
    trashcan: true
  });
})();
