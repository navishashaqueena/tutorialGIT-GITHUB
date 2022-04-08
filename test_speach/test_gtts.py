from gtts import gTTS
from vlc import MediaPlayer
from time import sleep

while True:
    inp = input('apa yang ingin anda convert ke suara ? > ').upper()
    if inp == 'STOP':
        suara = gTTS(
            f'anda baru saja berkata {inp} baiklah ... selamat tinggal ...', lang='id')
        suara.save('stop.mp3')
        player = MediaPlayer('stop.mp3')
        player.play()
        print(f'anda baru saja berkata {inp} baiklah ... selamat tinggal ...')
        sleep(5)
        break
    else:
        suara = gTTS(inp, lang='id')
        suara.save('hello.mp3')
        player = MediaPlayer('hello.mp3')
        player.play()
        print(f'anda baru saja berkata {inp}')
        continue
