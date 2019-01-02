import traceback

def spam():
    bacon()

def bacon():
    raise Exception('This is the error message.')

try:
    spam()
except:
    errorFile = open('Files\\errorInfo.txt', 'w')
    errorFile.write(traceback.format_exc())
    errorFile.close()
    print('The traceback info was written to errorInfo.txt.')

try:
    podBayDoorStatus = 'open'
    assert podBayDoorStatus == 'open', 'The pod bay doors need to be "open".'
    podBayDoorStatus = 'I\'m sorry, Dave. I\'m afraid I can\'t do that.'
    assert podBayDoorStatus == 'open', 'The pod bay doors need to be "open".'
except:
    print(traceback.format_exc())