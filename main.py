import eel
import whatsapp

eel.init('web')


@eel.expose
def generate_qr():
    print("hello Raya.")
    whatsapp.bot()


eel.start('index.html', size=(1010, 700))
