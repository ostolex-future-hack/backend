from client import client
from connect import make_request
from sqlalchemy.orm import Session


def speech_to_text(pas: str, id: int, db: Session):
    audio_file = open(pas, "rb")
    transcription = client.audio.transcriptions.create(
        model="whisper-1",
        file=audio_file
    )
    audio_file.close()
    make_request(transcription.text, id, db)
