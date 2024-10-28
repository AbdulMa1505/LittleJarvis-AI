# LittleJarvis AI

LittleJarvis is a simple AI assistant script that uses Python to perform basic tasks such as speaking, announcing the current time, fetching Wikipedia summaries, and recognizing voice commands. This project demonstrates the basics of speech recognition, text-to-speech synthesis, and using external APIs like Wikipedia.

## Features

- Text-to-Speech: Reads out text with a natural-sounding voice.
- Current Time Announcement: Tells you the current time in a spoken format.
- Wikipedia Summaries: Fetches and speaks a brief summary of a given topic from Wikipedia.
- Voice Command Recognition: Listens to your voice commands and recognizes them.

## Installation

1. Clone this repository or download the code.
2. Install the required libraries using `pip`:

    ``bash
    pip install pyttsx3 wikipedia SpeechRecognition
    

3. **Note**: The `speech_recognition` library requires `PyAudio` for microphone access. Install `PyAudio` as follows:

    ```bash
    pip install PyAudio
    

# Usage

To use LittleJarvis, run the script:

```bash
python jarvis.py
