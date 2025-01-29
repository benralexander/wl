import sounddevice

from whisper_live.client import Client,TranscriptionClient
import sounddevice as sd
s=sd.query_devices()
while True:
    transcription_client = TranscriptionClient(host="0.0.0.0", port=9090)
    transcription_client()
