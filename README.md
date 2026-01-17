# Automated News Reader (Python)

A Python-based application that fetches live technology news using a REST API and reads the headlines aloud using text-to-speech.

## Technologies Used
- Python
- NewsAPI
- REST API
- JSON
- requests library
- pyttsx3 (Text-to-Speech)

## Features
- Fetches real-time technology news headlines
- Converts text headlines into speech
- Prints headlines to the console
- Uses external REST API for live data
- Simple and clean implementation

## Cross-Platform Support
- The application is **cross-platform** and can run on **Windows, Linux, and macOS**
- Text-to-speech functionality is implemented using **pyttsx3**, which supports multiple platforms
- Audio output works best when the program is executed using **native Windows Python**
- In WSL/Linux environments, the program runs correctly but audio output may be limited due to system constraints

## How It Works
1. Sends an HTTP request to the NewsAPI endpoint
2. Parses the JSON response
3. Extracts news headlines
4. Reads each headline aloud using text-to-speech

## How to Run
1. Install dependencies:
   ```bash
   pip install requests pyttsx3
