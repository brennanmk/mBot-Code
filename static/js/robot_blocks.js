// Define robot blocks
Blockly.Blocks['robot_get_line'] = {
  init: function () {
    this.appendDummyInput()
      .appendField("Line sensor value");
    this.setOutput(true, "Boolean");
    this.setColour(330);
    this.setTooltip("");
    this.setHelpUrl("");
  }
};

Blockly.Blocks['robot_get_distance'] = {
  init: function () {
    this.appendDummyInput()
      .appendField("Distance sensor value in")
      .appendField(new Blockly.FieldDropdown([
        ["cm", "CM"],
        ["in", "IN"]
      ]), "UNITS");
    this.setOutput(true, "Number");
    this.setColour(330);
    this.setTooltip("");
    this.setHelpUrl("");
  }
};

Blockly.Blocks['robot_set_motor'] = {
  init: function () {
    this.appendValueInput("POWER")
      .setCheck("Number")
      .appendField("Set")
      .appendField(new Blockly.FieldDropdown([
        ["left", "LEFT"],
        ["right", "RIGHT"]
      ]), "MOTOR")
      .appendField("motor power to");
    this.setInputsInline(true);
    this.setPreviousStatement(true, null);
    this.setNextStatement(true, null);
    this.setColour(330);
    this.setTooltip("");
    this.setHelpUrl("");
  }
};
Blockly.Blocks['time_sleep'] = {
  init: function () {
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
Blockly.Blocks['robot_drive_time'] = {
  init: function () {
    this.appendDummyInput()
      .appendField("Drive")
      .appendField(new Blockly.FieldDropdown([
        ["forwards", "FWD"],
        ["backwards", "BCK"]
      ]), "DIRECTION");
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
Blockly.Blocks['robot_drive'] = {
  init: function () {
    this.appendDummyInput()
      .appendField("Drive")
      .appendField(new Blockly.FieldDropdown([
        ["forwards", "FWD"],
        ["backwards", "BCK"]
      ]), "DIRECTION");
    this.setInputsInline(true);
    this.setPreviousStatement(true, null);
    this.setNextStatement(true, null);
    this.setColour(330);
    this.setTooltip("");
    this.setHelpUrl("");
  }
};

Blockly.Blocks['robot_turn'] = {
  init: function () {
    this.appendDummyInput()
      .appendField("Turn")
      .appendField(new Blockly.FieldDropdown([
        ["right", "RIGHT"],
        ["left", "LEFT"]
      ]), "DIRECTION");
    this.setInputsInline(true);
    this.setPreviousStatement(true, null);
    this.setNextStatement(true, null);
    this.setColour(330);
    this.setTooltip("");
    this.setHelpUrl("");
  }
};

Blockly.Blocks['robot_turn_time'] = {
  init: function () {
    this.appendDummyInput()
      .appendField("Turn")
      .appendField(new Blockly.FieldDropdown([
        ["right", "RIGHT"],
        ["left", "LEFT"]
      ]), "DIRECTION");
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

Blockly.Blocks['robot_set_led'] = {
  init: function () {
    this.appendValueInput("VALUE")
      .setCheck("Boolean")
      .appendField("Set LED state to");
    this.setInputsInline(true);
    this.setPreviousStatement(true, null);
    this.setNextStatement(true, null);
    this.setColour(330);
    this.setTooltip("");
    this.setHelpUrl("");
  }
};

Blockly.Blocks['robot_gpio_output'] = {
  init: function () {
    this.appendValueInput("VALUE")
      .setCheck("Boolean")
      .appendField("Set GPIO pin")
      .appendField(new Blockly.FieldNumber(1, 1, 27, 1), "PIN")
      .appendField("to");
    this.setInputsInline(true);
    this.setPreviousStatement(true, null);
    this.setNextStatement(true, null);
    this.setColour(330);
    this.setTooltip("");
    this.setHelpUrl("");
  }
};

Blockly.Blocks['robot_gpio_input'] = {
  init: function () {
    this.appendDummyInput()
      .appendField("Get value of GPIO pin")
      .appendField(new Blockly.FieldNumber(1, 1, 27, 1), "PIN");
    this.setInputsInline(true);
    this.setOutput(true, "Boolean");
    this.setColour(330);
    this.setTooltip("");
    this.setHelpUrl("");
  }
};
Blockly.Blocks['robot_stop'] = {
  init: function () {
    this.appendDummyInput()
      .appendField("Stop the robot");
    this.setPreviousStatement(true, null);
    this.setNextStatement(true, null);
    this.setColour(330);
    this.setTooltip("");
    this.setHelpUrl("");
  }
};
Blockly.Blocks['robot_motor_power'] = {
  init: function () {
    this.appendValueInput("POWER")
      .setCheck("Number")
      .appendField("Set motor power to");
    this.setInputsInline(true);
    this.setPreviousStatement(true, null);
    this.setNextStatement(true, null);
    this.setColour(330);
    this.setTooltip("");
    this.setHelpUrl("");
  }
};

// Define block functionality
Blockly.Python['robot_get_line'] = function (block) {
  return ['robot.getLineSensor()', Blockly.Python.ORDER_NONE];
};

Blockly.Python['robot_get_distance'] = function (block) {
  const dropdown_units = block.getFieldValue('UNITS');
  return ['robot.getDistance' + dropdown_units + '()', Blockly.Python.ORDER_NONE];
};

Blockly.Python['robot_set_motor'] = function (block) {
  const dropdown_motor = block.getFieldValue('MOTOR');
  let value_power = Blockly.Python.valueToCode(block, 'POWER', Blockly.Python.ORDER_ATOMIC);
  const code = 'robot.setMotorPower(' + '\"' + dropdown_motor + '\",' + value_power + ')\n';
  return code;
};

Blockly.Python['time_sleep'] = function (block) {
  const value_time = Blockly.Python.valueToCode(block, 'TIME', Blockly.Python.ORDER_ATOMIC);
  return 'time.sleep(' + value_time + ')\n';
};
Blockly.Python['robot_drive'] = function (block) {
  const dropdown_direction = block.getFieldValue('DIRECTION');
  const dir = (dropdown_direction == 'FWD' ? 1 : -1);
  let code = 'robot.drive('+dir+')\n';
  return code;
};
Blockly.Python['robot_drive_time'] = function (block) {
  let code = Blockly.Python['robot_drive'](block);
  const value_duration = Blockly.Python.valueToCode(block, 'DURATION', Blockly.Python.ORDER_ATOMIC);
  code += 'time.sleep(' + value_duration + ')\nrobot.stop()\n';
  return code;
};
Blockly.Python['robot_motor_power'] = function (block) {
  const value_power = Math.max(Math.min(Blockly.Python.valueToCode(block, 'POWER', Blockly.Python.ORDER_ATOMIC), 100), 0);
  // TODO: Assemble Python into code variable.
  var code = 'override_power = ' + value_power + '\n';
  return code;
};

Blockly.Python['robot_turn'] = function (block) {
  const dropdown_direction = block.getFieldValue('DIRECTION');
  const spd = (dropdown_direction == 'RIGHT' ? 1 : -1);
  let code = 'robot.turn(' + (-spd) + ')\n';
  return code;
};

Blockly.Python['robot_turn_time'] = function (block) {
  let code = Blockly.Python['robot_turn'](block);
  const value_duration = Blockly.Python.valueToCode(block, 'DURATION', Blockly.Python.ORDER_ATOMIC);
  code += 'time.sleep(' + value_duration + ')\nrobot.stop()\n'
  return code;
};

Blockly.Python['robot_stop'] = function (block) {
  var code = 'robot.stop()\n';
  return code;
};

Blockly.Python['robot_set_led'] = function (block) {
  const value = Blockly.Python.valueToCode(block, 'VALUE', Blockly.Python.ORDER_ATOMIC);
  return 'robot.setLed(' + value + ')\n';
};

Blockly.Python['robot_gpio_output'] = function (block) {
  const number_pin = block.getFieldValue('PIN');
  const statements_value = Blockly.Python.valueToCode(block, 'VALUE', Blockly.Python.ORDER_ATOMIC);
  return 'GPIO.output(' + number_pin + ',' + statements_value + ')';
};

Blockly.Python['robot_gpio_input'] = function (block) {
  const number_pin = block.getFieldValue('PIN');
  // TODO: Assemble Python into code variable.
  const code = 'GPIO.input(' + number_pin + ')';
  // TODO: Change ORDER_NONE to the correct strength.
  return [code, Blockly.Python.ORDER_NONE];
};