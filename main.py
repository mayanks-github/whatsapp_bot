import eel

eel.init('web')


@eel.expose
def generate_qr():
    print("QR code generation successful.")


eel.start('index.html', size=(1010, 600))
