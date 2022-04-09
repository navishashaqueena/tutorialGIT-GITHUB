# identifikasi platform
import platform

# jika platform windows menggunakan pyttsx okehhhhhhhhhhhhhhhhhhhh
if platform.system() == 'Windows':
    import pyttsx3
    try:
        engine = pyttsx3.init()
    except ImportError:
        print('Error Import')
    except RuntimeError:
        print('Error Runtime')
    suara = engine.getProperty('suara')
    engine.setProperty(suara)
