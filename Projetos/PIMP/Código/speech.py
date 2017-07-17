try:
    import speech_recognition as sr
    found_module = True
except ModuleNotFoundError:
    print('Couldn\'t import speechrecognition')
    found_module = False


def transcribe(language='en-US'):
    # obtain audio from the microphone
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something!")
        audio = r.listen(source)

    try:
        return r.recognize_google(audio, language=language)
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
        try:
            return r.recognize_sphinx(audio, language=language)
        except sr.UnknownValueError:
            print("Sphinx could not understand audio")
        except sr.RequestError as e:
            print("Sphinx error; {0}".format(e))
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
        try:
            print('Trying with sphinx')
            return r.recognize_sphinx(audio, language=language)
        except sr.UnknownValueError:
            print("Sphinx could not understand audio")
        except sr.RequestError as e:
            print("Sphinx error; {0}".format(e))
