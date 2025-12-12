
# Python AI Audio Summarizer

A professional, user-friendly tool for transcribing and summarizing audio files using AI models. Designed for developers, researchers, and anyone needing fast, accurate speech-to-text and summarization in multiple languages.

---
<p>
<img width="1522" height="980" alt="audio_transcriber_summarizer" src="https://github.com/user-attachments/assets/30c19b12-cd9e-4ff2-a32e-92e1f1252506" />
</p>

---

## Table of Contents

- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Configuration](#configuration)
- [Project Structure](#project-structure)
- [Sample Audio Files](#sample-audio-files)
- [License](#license)
- [Contributing](#contributing)
- [Contact](#contact)

---


## Features

- Transcribe audio files to text using AI models
- Summarize transcribed text automatically
- Multi-language support
- Easy configuration and extension
- Visual workflow diagram included

## Requirements

- Python 3.8+
- See `requirements.txt` for all dependencies

## Installation

1. **Clone the repository:**
   ```bash
   git clone <repo-url>
   cd python-ai-audio-summarizer
   ```
2. **Create and activate a virtual environment:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```
3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

## Usage

- **Transcribe an audio file:**
  ```bash
  python audio_transcriber.py --input path/to/audiofile.wav
  ```
- **Summarize a transcript:**
  ```bash
  python summarizer.py --input path/to/transcript.txt
  ```
- **Configuration:**
  Edit files in the `config/` directory to adjust AI models and language settings.

## Configuration

- `config/ai_models.py`: Configure or add AI models for transcription and summarization.
- `config/languages.py`: Manage supported languages.


## Project Structure

```
python-ai-audio-summarizer/
├── audio_transcriber.py                # Main script for audio transcription
├── summarizer.py                       # Main script for summarization
├── requirements.txt                    # Python dependencies
├── config/                             # Configuration files
│   ├── ai_models.py
│   └── languages.py
├── sample_audio_files/                 # Example audio files for testing
│   └── meeting_sample_audio.mp3
├── audio_transcriber_summarizer.png    # Visual workflow diagram
├── LICENSE                             # Project license
├── .gitignore                          # Git ignore rules
└── venv/                               # Virtual environment (ignored by git)
```


## Sample Audio Files

- Place your audio files in the `sample_audio_files/` directory for testing.


## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.


## Contributing

Contributions are welcome! Please open issues or submit pull requests for improvements or bug fixes.


## Contact

For questions or support, please contact [Eray Yuztyurk](mailto:your.email@example.com).
