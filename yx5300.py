"""
	protocol defintion file for the CATALEX seriel MP3 player
	The board uses the YX5300 MP3 audio chip. It supports 8KHz to 48KHz sampling frequencies for MP3 and WAV file format
	
	Not all commands are mapped. 
	
	Command format
	
	Each command is 8 bytes
	Pos	Descrption 	Bytes	Value
	1 	Start		1		0x7E
	2	Version		1		0xFF
	3	Lenght		1		0x06
	4	Command		1		see below
	5	Feedback	1		0x00 for off, 0x01 On
	6	Data		2		depends of command
	8	End			1		0xEF
	
	Code 	Commands
	0x01	Next track
	0x02	Previous track
	0x03	Play with index, index given in data field
	0x04	Volume up by 1
	0x05	Volume down by 1
	0x06	Set volume to value provided in data field (0-30)
	0x0A	Put chip to sleep mode
	0x0B	Wake chip from sleep mode
	0x0C	Reset chip
	0x0D	Resume playback
	0x0E	Pause playback
	0x16	Stop playback
			
"""

def command_base():
	command=bytearray()
	command.append(0x7e)
	command.append(0xFF)
	command.append(0x06)
	command.append(0x00)
	command.append(0x00)
	command.append(0x00)
	command.append(0x00)
	command.append(0xEF)
	return command
	
def play_next():
	command=bytearray()
	command=command_base()
	command[3]=0x01
	return command

def play_previous():
	command=bytearray()
	command=command_base()
	command[3]=0x02
	return command
	
def play_track(track_id):
	command=bytearray()
	command=command_base()
	command[3]=0x03
	command[6]=track_id
	return command
	
def volume_up():
	command=bytearray()
	command=command_base()
	command[3]=0x04
	return command

def volume_down():
	command=bytearray()
	command=command_base()
	command[3]=0x05
	return command

def set_volume(level):
	command=bytearray()
	command=command_base()
	command[3]=0x06
	command[6]=level
	return command
	
def sleep_module():
	command=bytearray()
	command=command_base()
	command[3]=0x0A
	return command

def wake_module():
	command=bytearray()
	command=command_base()
	command[3]=0x0B
	return command	

def reset_module():
	command=bytearray()
	command=command_base()
	command[3]=0x0C
	return command	
	
def pause():
	command=bytearray()
	command=command_base()
	command[3]=0x0E
	return command	

def resume():
	command=bytearray()
	command=command_base()
	command[3]=0x0D
	return command		
	
def stop():
	command=bytearray()
	command=command_base()
	command[3]=0x16
	return command
