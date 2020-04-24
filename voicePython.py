from win32com.client import Dispatch
s = Dispatch("SAPI.SpVoice")

x = "Helllo"
b = "Worlddddd"
print(x + b)
s.Speak("szanuj DISA")

