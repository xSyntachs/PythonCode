import boto3
import speech_recognition as sr
from pydub import AudioSegment
from pydub.playback import play
from contextlib import closing

class TextToSpeech:
    def __init__(self):
        self.speech_recognizer = sr.Recognizer()
        self.aws_access_key_id = 'AKIASZERDXSCA4P3CJ5T'
        self.aws_secret_access_key = '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'
        self.region_name = 'eu-central-1'
        
        session = boto3.Session(
            aws_access_key_id=self.aws_access_key_id,
            aws_secret_access_key=self.aws_secret_access_key,
            region_name=self.region_name)
        self.polly = session.client("polly")
        self.transcribe = session.client("transcribe")

    def speak_answer(self, answer):
        response = self.polly.synthesize_speech(
            Text=answer,
            OutputFormat="pcm",
            VoiceId="Daniel",
            Engine="neural"
        )
        if "AudioStream" in response:
            with closing(response["AudioStream"]) as stream:
                audio = AudioSegment.from_file(stream, format="raw", frame_rate=16000, channels=1, sample_width=2)
                play(audio)

if __name__ == "__main__":
    text_to_speech = TextToSpeech()

    while True:
        user_input = input("Gib den Text ein, den du vorgelesen haben möchtest (oder 'exit' zum Beenden): ")
        if user_input.lower() == 'exit':
            break
        text_to_speech.speak_answer(user_input)
