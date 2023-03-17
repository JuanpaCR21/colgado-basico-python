import pyaudio
import wave

p = pyaudio.PyAudio()
stream = None
def play_sound(archivo):
    # Cargar archivo de sonido
    wf = wave.open(archivo, 'rb')

    # Inicializar PyAudio
    p = pyaudio.PyAudio()

    # Crear stream de audio
    stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                    channels=wf.getnchannels(),
                    rate=wf.getframerate(),
                    output=True)

    # Reproducir sonido
    data = wf.readframes(1024)
    while data:
        stream.write(data)
        data = wf.readframes(1024)

    # Detener stream de audio
    stream.stop_stream()
    stream.close()

    # Terminar PyAudio
    p.terminate()


def stop_sound():
    global stream  # definir la variable stream como global
    if stream is not None:
        stream.stop_stream()
        stream.close()
        p.terminate()
        stream = None
