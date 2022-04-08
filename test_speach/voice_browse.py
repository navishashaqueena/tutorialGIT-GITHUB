import webbrowser as wb
import speech_recognition as sr

bicara = sr.Recognizer()


def suaraKeText():
    inputSuara = ''
    with sr.Microphone() as sumberSuara:
        bicara.adjust_for_ambient_noise(source=sumberSuara)
        try:
            suara = bicara.listen(source=sumberSuara)
            inputSuara = bicara.recognize_google(
                audio_data=suara, language='id-ID')
        except sr.UnknownValueError as uve:
            print(
                f'server pengenalan suara Google tidak dapat memahami audio, baik karena ucapan tidak jelas atau karena kebisingan sekitar {uve}')
        except sr.RequestError as re:
            print(
                f'permintaan pengenalan ucapan Google gagal, baik karena koneksi internet yang buruk atau karena server terlalu sibuk {re}')
        except sr.WaitTimeoutError as wte:
            print(
                f'skrip tidak mendeteksi audio apa pun dari mikrofon untuk waktu yang lama {wte}')
    return inputSuara


while True:
    print('Python sedang mendengarkan . . . .')
    inp = suaraKeText()
    print(f'kamu baru saja bilang : {inp}')
    if inp == 'berhenti':
        print('GOODBYE')
        break
    elif 'browsing' in inp:
        inp = inp.replace('browsing ', '')
        wb.open('http://'+inp)
        continue
