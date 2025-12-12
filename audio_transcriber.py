"""
STT - Audio Transcription
This module provides functionality to transcribe audio files into text using various Whisper models.
"""

from config.ai_models import whisper_tts_models
from summarizer import summarize_text
import gradio as gr
from transformers import pipeline
import torch

# models in cache
stt_loaded_models = {}
summ_loaded_models = {}

# loaders
def load_stt_model(model_type):
  """
  Load STT model for the specified model type.
  Keyword arguments:
      model_type -- type of the STT model
      Return: STT pipeline
  """

  stt_pipe = pipeline(
      "automatic-speech-recognition",
      model=whisper_tts_models[model_type],
      chunk_length_s=30

  )

  return stt_pipe

# getting models
def get_stt_model(model_type):
  """
  Get STT model from cache or load if not present.
  Keyword arguments:
      model_type -- type of the STT model
      Return: STT pipeline
  """

  if model_type not in stt_loaded_models:
    stt_loaded_models[model_type] = load_stt_model(model_type)

  return stt_loaded_models[model_type]

# transcription
def audio_transcript(model_type, audio_file_path):
  """
  Transcribe the input audio file using the specified STT model.
  Keyword arguments:
      model_type -- type of the STT model
      audio_file_path -- path to the input audio file
      return_timestamps -- whether to return timestamps in the transcription
  """
  
  try:

    stt_pipe = get_stt_model(model_type)

    model_output = stt_pipe(audio_file_path, batch_size=16, return_timestamps=True)
    text_output = model_output["text"]

    summary = summarize_text(text_output)

    return text_output, summary

  except Exception as e:
    return f"STT ERROR → {str(e)}", ""

# Gradio Interface
_ui = gr.Interface(
    fn=audio_transcript,
    inputs=[
        gr.Dropdown(
            choices=list(whisper_tts_models.keys()),
            label="Model Type",
            value="Whisper - Base"
        ),
        gr.Audio(label="Audio", sources="upload", type="filepath"),
        ],
    outputs=[
        gr.Textbox(label="Text", lines=15, max_lines=40),
        gr.Textbox(label="Summary", lines=15, max_lines=40)
    ],
    title="🎤 Audio Transcriber & Summarizer 📝",
    description="""
                Transcribe your audio files into text and get a concise summary using Whisper and BART models.
                """
)

_ui.launch(server_name="0.0.0.0", server_port=7860, inbrowser=True)

