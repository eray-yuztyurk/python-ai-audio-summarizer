# Python AI Audio Summarizer

A simple, professional, and easy-to-use tool for transcribing and summarizing audio files using AI models. This project is designed for developers, researchers, and anyone who needs to quickly convert speech to text and generate concise summaries in multiple languages.

---

## Table of Contents

- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Configuration](#configuration)
- [Project Structure](#project-structure)
- [Sample Audio Files](#sample-audio-files)
- [Logging & Flagged Data](#logging--flagged-data)
- [License](#license)
- [Contributing](#contributing)
- [Contact](#contact)

---

## Features

- Transcribe audio files to text using AI models
- Summarize transcribed text automatically
- Multi-language support
- Easy configuration and extension
- Logging of flagged or problematic files

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
├── audio_transcriber.py      # Main script for audio transcription
├── summarizer.py             # Main script for summarization
├── requirements.txt          # Python dependencies
├── config/                   # Configuration files
│   ├── ai_models.py
│   └── languages.py
├── flagged/                  # Log of flagged/problematic files
│   └── log.csv
├── sample_audio_files/       # Example audio files for testing
└── LICENSE                   # Project license
```

## Sample Audio Files

- Place your audio files in the `sample_audio_files/` directory for testing.

## Logging & Flagged Data

- Problematic or flagged files are logged in `flagged/log.csv` for review.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Please open issues or submit pull requests for improvements or bug fixes.

## Contact

For questions or support, please contact [Eray Yuztyurk](mailto:your.email@example.com).
