from client import client
from connect import make_request


def speech_to_text(pas: str):
    audio_file = open(pas, "rb")
    transcription = client.audio.transcriptions.create(
        model="whisper-1",
        file=audio_file
    )
    audio_file.close()
    make_request(transcription.text)

