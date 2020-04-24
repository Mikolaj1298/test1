from win32com.client import Dispatch
s = Dispatch("SAPI.SpVoice")

x = "Helllo"
z = "Dis"
print(x + z)
s.Speak("szanuj DISA")

