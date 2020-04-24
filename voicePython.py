from win32com.client import Dispatch
s = Dispatch("SAPI.SpVoice")

x = "Helllo"
a = "Diss"

print(x + a)
s.Speak("szanuj DISA")

