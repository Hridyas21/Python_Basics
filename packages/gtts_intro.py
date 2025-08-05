from gtts import gTTS
import os

c="hello..sugamaano"
s=gTTS(text=c,lang="ml",slow=False)
s.save("test_audio.mp3")
os.system("start test_audio.mp3")