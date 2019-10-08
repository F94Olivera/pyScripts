import subprocess as sub
import time
def news():
  sub.Popen(["/Applications/Firefox.app/Contents/MacOS/firefox", "-private-window", "https://www.lanacion.com.ar"])
  time.sleep(1)
  sub.Popen(["/Applications/Firefox.app/Contents/MacOS/firefox", "-private-window", "https://www.infobae.com"])

news()