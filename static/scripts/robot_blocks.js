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