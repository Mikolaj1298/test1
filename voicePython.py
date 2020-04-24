from win32com.client import Dispatch
s = Dispatch("SAPI.SpVoice")

x = "Helllo"
y = "World"
print(x + y)
s.Speak("szanuj DISA")

