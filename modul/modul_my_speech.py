import speech_recognition as sr

bicara = sr.Recognizer()


def suaraKeTeks():
    while True:
        voice_input = ''
        with sr.Microphone() as sumber:
            bicara.adjust_for_ambient_noise(source=sumber)
            try:
                audio = bicara.listen(source=sumber)
                voice_input = bicara.recognize_google(
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
        return voice_input
