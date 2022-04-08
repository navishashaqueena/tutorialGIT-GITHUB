import speech_recognition as sr

ngomong = sr.Recognizer()


def suaraKeTeks():
    while True:
        suara_input = ''
        with sr.Microphone() as sumber:
            ngomong.adjust_for_ambient_noise(source=sumber)
            try:
                audio = ngomong.listen(source=sumber)
                suara_input = ngomong.recognize_google(
                    audio_data=audio, language='id-ID')
            except sr.UnknownValueError as uve:
                print(
                    f'server pengenalan suara Google tidak dapat memahami audio, baik karena ucapan tidak jelas atau karena kebisingan sekitar {uve}')
            except sr.RequestError as re:
                print(
                    f'permintaan pengenalan ucapan Google gagal, baik karena koneksi internet yang buruk atau karena server terlalu sibuk {re}')
            except sr.WaitTimeoutError as wte:
                print(
                    f'skrip tidak mendeteksi audio apa pun dari mikrofon untuk waktu yang lama {wte}')
        return suara_input
