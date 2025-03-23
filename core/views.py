import threading  # Add this import at the top
import pyttsx3
import os
import logging
from django.conf import settings
from django.shortcuts import render
from django.http import FileResponse
from gtts import gTTS
# Your existing views code...


def cover_page(request):
    return render(request, 'core/cover.html')

def map_page(request):
    return render(request, 'core/map.html')

def country_view(request, country_name):
    return render(request, f'core/{country_name}.html', {'country': country_name})

def reflection_page(request):
    return render(request, 'core/reflection.html')


def us_page(request):
    return render(request, 'core/us.html')

# Set up logging
logger = logging.getLogger(__name__)

def generate_speech():
    text = "Sources confirm an intergalactic visitor named Zuno has arrived on a mission to study human behavior."
    try:
        tts = gTTS(text=text, lang='en')
        audio_path = os.path.join(BASE_DIR, 'core/static/audio/speech.mp3')
        tts.save(audio_path)
        print(f"Audio saved to: {audio_path}")
    except Exception as e:
        print(f"Error generating speech: {e}")


def generate_speech():
    text = "Sources confirm an intergalactic visitor named Zuno has arrived on a mission to study human behavior."
    try:
        tts = gTTS(text=text, lang='en')
        audio_path = os.path.join(settings.BASE_DIR, 'core/static/audio/speech.mp3')
        tts.save(audio_path)
        print(f"Audio saved to: {audio_path}")
    except Exception as e:
        print(f"Error generating speech: {e}")

def cover_page(request):
    # Ensure the speech is generated
    generate_speech()
    return render(request, 'core/cover.html')

def speech_audio(request):
    """Serve the generated speech file."""
    try:
        audio_path = os.path.join(settings.BASE_DIR, "static", "audio", "speech.mp3")
        
        if not os.path.exists(audio_path):
            logger.debug("Audio file not found, generating...")
            audio_path = generate_speech()

        if audio_path is None:
            logger.error("Failed to find or generate speech file.")
            return FileResponse(None)

        logger.debug("Serving audio file from path: %s", audio_path)
        return FileResponse(open(audio_path, 'rb'), content_type='audio/mpeg')

    except Exception as e:
        logger.error("Error serving speech audio: %s", e)
        return FileResponse(None)