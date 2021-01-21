Blockly.Blocks['gpio_set'] = {
    init: function() {
      this.appendDummyInput()
          .appendField("Set pin")
          .appendField(new Blockly.FieldNumber(7, 1, 40), "PIN")
          .appendField("to")
          .appendField(new Blockly.FieldCheckbox("TRUE"), "LED_STATE");
      this.setInputsInline(true);
      this.setPreviousStatement(true, null);
      this.setNextStatement(true, null);
      this.setColour(230);
   this.setTooltip("");
   this.setHelpUrl("");
    }
  };
  Blockly.Blocks['gpio_init'] = {
    init: function() {
      this.appendDummyInput()
          .appendField("Initialize GPIO");
      this.setNextStatement(true, null);
      this.setColour(230);
   this.setTooltip("");
   this.setHelpUrl("");
    }
  };
  Blockly.Blocks['gpio_cleanup'] = {
    init: function() {
      this.appendDummyInput()
          .appendField("GPIO Cleanup");
      this.setPreviousStatement(true, null);
      this.setColour(230);
   this.setTooltip("");
   this.setHelpUrl("");
    }
  };
  Blockly.Blocks['controls_sleep'] = {
    init: function() {
      this.appendValueInput("NAME")
          .setCheck("Number")
          .appendField("Wait for");
      this.appendDummyInput()
          .appendField("seconds");
      this.setInputsInline(true);
      this.setPreviousStatement(true, null);
      this.setNextStatement(true, null);
      this.setColour(230);
   this.setTooltip("");
   this.setHelpUrl("");
    }
  };

// Define the blocks behaviour
Blockly.Python['gpio_set'] = function(block) {
  var number_pin = block.getFieldValue('PIN');
  var checkbox_led_state = block.getFieldValue('LED_STATE') == 'TRUE';
  // TODO: Assemble Python into code variable.
  var code = 'GPIO.output(' + number_pin + ',' + (checkbox_led_state ? '1' : '0') + ')\n';
  code = 'GPIO.setup(' + number_pin + ',GPIO.OUT)\n' + code
  return code;
};
Blockly.Python['controls_sleep'] = function(block) {
  var value_name = Blockly.Python.valueToCode(block, 'NAME', Blockly.Python.ORDER_ATOMIC);
  // TODO: Assemble Python into code variable.
  var code = 'time.sleep(' + value_name + ')\n';
  return code;
};

Blockly.Python['controls_start'] = function(block) {
  return 'import RPi.GPIO as GPIO\nimport time\nGPIO.setmode(GPIO.BOARD)\n';
};
Blockly.Python['gpio_cleanup'] = function(block) {
  return 'GPIO.cleanup()\n';
};