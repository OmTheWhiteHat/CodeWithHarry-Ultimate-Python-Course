import pyttsx3
engine = pyttsx3.init()

exitKeywords = ['exit', 'quit']

while True:
    text = input('Enter The Text To Speack: ')
    text = text.lower()

    if text in exitKeywords:
        engine.say(text+'ing')
        engine.runAndWait()
        print('Exiting...')
        break

    elif text:
        engine.say(text)
        engine.runAndWait()

    else:
        print('Error')
        engine.say('You Got Error')
        engine.runAndWait()

    
