from pygame import mixer

mixer.init()

mixer.music.load("Husnn Hai Suhaana New - Coolie No 1.mp3")

v = 0.5
mixer.music.set_volume(v)

mixer.music.play()

while True:
	print(" p\n r\n e\n u\n d\n\n\n")
	query = input()
	if query == 'u':
		v = v + 0.1
		if v > 1:
			v = 1.0
		mixer.music.set_volume(v)
	if query == 'd':
		v = v - 0.1
		if v < 0:
			v = 0.0
		mixer.music.set_volume(v)
	if query == 'p':
		mixer.music.pause()

	if query == 'r':
		mixer.music.unpause()

	if query == 'e':
		mixer.music.stop()
		break
