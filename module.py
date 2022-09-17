def say(message):
	print(message)

def color(message, color):
	if color == "Gray":
		print("\033[1;30;40m", message, "\033[0;37;40m")
	elif color == "Yellow":
		print("\033[1;33;40m", message, "\033[0;37;40m")
	elif color == "Magenta":
		print("\033[1;35;40m", message, "\033[0;37;40m")
	elif color == "Cyan":
		print("\033[1;36;40m", message, "\033[0;37;40m")
	elif color == "White":
		print("\033[1;37;40m", message, "\033[0;37;40m")
	elif color == "Blue":
		print("\033[1;34;40m", message, "\033[0;37;40m")
	elif color == "Red":
		print("\033[1;31;40m", message, "\033[0;37;40m")
	elif color == "Green":
		print("\033[1;32;40m", message, "\033[0;37;40m")
	elif color == "Bright_Colour":
		print("\033[1;37;40m", message, "\033[0;37;40m")
	elif color == "Blinking_Text":
		print("\033[5;37;40m", message, "\033[0;37;40m")

def SetColor(color):
	if color == "Gray":
		print("\033[1;30;40m")
	elif color == "Yellow":
		print("\033[1;33;40m")
	elif color == "Magenta":
		print("\033[1;35;40m")
	elif color == "Cyan":
		print("\033[1;36;40m")
	elif color == "White":
		print("\033[1;37;40m")
	elif color == "Blue":
		print("\033[1;34;40m")
	elif color == "Red":
		print("\033[1;31;40m")
	elif color == "Green":
		print("\033[1;32;40m")
	elif color == "Bright":
		print("\033[1;37;40m", message, "\033[0;37;40m")
	elif color == "Blinking":
		print("\033[5;37;40m")