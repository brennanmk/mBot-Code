// Define robot blocks
Blockly.Blocks['robot_get_line'] = {
    init: function() {
      this.appendDummyInput()
          .appendField("Line sensor value");
      this.setOutput(true, "Boolean");
      this.setColour(330);
   this.setTooltip("");
   this.setHelpUrl("");
    }
  };
  
  Blockly.Blocks['robot_get_distance'] = {
    init: function() {
      this.appendDummyInput()
          .appendField("Distance sensor value in")
          .appendField(new Blockly.FieldDropdown([["cm","CM"], ["in","IN"]]), "UNITS");
      this.setOutput(true, "Number");
      this.setColour(330);
   this.setTooltip("");
   this.setHelpUrl("");
    }
  };
  
  Blockly.Blocks['robot_set_motor'] = {
    init: function() {
      this.appendValueInput("POWER")
          .setCheck("Number")
          .appendField("Set")
          .appendField(new Blockly.FieldDropdown([["left","LEFT"], ["right","RIGHT"]]), "MOTOR")
          .appendField("motor power to");
      this.setInputsInline(true);
      this.setPreviousStatement(true,null);
	this.setNextStatement(true,null);
      this.setColour(330);
   this.setTooltip("");
   this.setHelpUrl("");
    }
  };
  Blockly.Blocks['time_sleep'] = {
	init: function() {
	  this.appendValueInput("TIME")
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
  Blockly.Blocks['robot_drive'] = {
	init: function() {
	  this.appendDummyInput()
		  .appendField("Drive")
		  .appendField(new Blockly.FieldDropdown([["forwards","FWD"], ["backwards","BCK"]]), "DIRECTION");
	  this.appendValueInput("DURATION")
		  .setCheck("Number")
		  .appendField("for");
	  this.appendDummyInput()
		  .appendField("seconds");
	  this.setInputsInline(true);
	  this.setPreviousStatement(true, null);
	  this.setNextStatement(true, null);
	  this.setColour(330);
   this.setTooltip("");
   this.setHelpUrl("");
	}
  };
  
  Blockly.Blocks['robot_turn'] = {
	init: function() {
	  this.appendDummyInput()
		  .appendField("Turn")
		  .appendField(new Blockly.FieldDropdown([["right","RIGHT"], ["left","LEFT"]]), "DIRECTION");
	  this.appendValueInput("DURATION")
		  .setCheck("Number")
		  .appendField("for");
	  this.appendDummyInput()
		  .appendField("seconds");
	  this.setInputsInline(true);
	  this.setPreviousStatement(true, null);
	  this.setNextStatement(true, null);
	  this.setColour(330);
   this.setTooltip("");
   this.setHelpUrl("");
	}
  };

// Define block functionality
Blockly.Python['robot_get_line'] = function(block) {
    return ['robot.getLineSensor()', Blockly.Python.ORDER_NONE];
  };
  
  Blockly.Python['robot_get_distance'] = function(block) {
    const dropdown_units = block.getFieldValue('UNITS');
    return ['robot.getDistance'+dropdown_units+'()', Blockly.Python.ORDER_NONE];
  };
  
  Blockly.Python['robot_set_motor'] = function(block) {
    const dropdown_motor = block.getFieldValue('MOTOR');
    let value_power = Blockly.Python.valueToCode(block, 'POWER', Blockly.Python.ORDER_ATOMIC);
    const code = 'robot.setMotorPower(' + '\"'+ dropdown_motor +'\",' + value_power + ')\n';
    return code;
  };

  Blockly.Python['time_sleep'] = function(block) {
	const value_time = Blockly.Python.valueToCode(block, 'TIME', Blockly.Python.ORDER_ATOMIC);
	return 'time.sleep('+value_time+')\n';
  };
  Blockly.Python['robot_drive'] = function(block) {
	const dropdown_direction = block.getFieldValue('DIRECTION');
	const value_duration = Blockly.Python.valueToCode(block, 'DURATION', Blockly.Python.ORDER_ATOMIC);
	const spd = (dropdown_direction == 'FWD' ? 100 : -100);
	let code = 'robot.setMotorPower("LEFT",' + spd + ')\n';
	code += 'robot.setMotorPower("RIGHT",' + spd + ')\n';
	code += 'time.sleep(' + value_duration + ')\n'
	return code;
  };
  
  Blockly.Python['robot_turn'] = function(block) {
	const dropdown_direction = block.getFieldValue('DIRECTION');
	const value_duration = Blockly.Python.valueToCode(block, 'DURATION', Blockly.Python.ORDER_ATOMIC);
	const spd = (dropdown_direction == 'RIGHT' ? 100 : -100);
	let code = 'robot.setMotorPower("LEFT",' + (-spd) + ')\n';
	code += 'robot.setMotorPower("RIGHT",' + spd + ')\n';
	code += 'time.sleep(' + value_duration + ')\n'
	return code;
  };
