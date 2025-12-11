# STT - Audio Transcription

import gradio as gr
from transformers import pipeline
import torch

# mapping
MODEL_MAP = {
    "Whisper - Tiny": "openai/whisper-tiny",
    "Whisper - Base": "openai/whisper-base",
    "Whisper - Small": "openai/whisper-small",
    "Whisper - Medium": "openai/whisper-medium",
    "Whisper - Large V2": "openai/whisper-large-v2",
    "Whisper - Large V3": "openai/whisper-large-v3"
}

# models in cache
stt_loaded_models = {}
summ_loaded_models = {}

# loaders
def load_stt_model(model_type):
  stt_pipe = pipeline(
      "automatic-speech-recognition",
      model=MODEL_MAP[model_type],
      chunk_length_s=30

  )

  return stt_pipe

def load_summarizer_model(model_name):
  summarizer_pipe = pipeline(
      "summarization",
      model="facebook/bart-large-cnn"
  )

  return summarizer_pipe

# getting models
def get_stt_model(model_type):
  if model_type not in stt_loaded_models:
    stt_loaded_models[model_type] = load_stt_model(model_type)

  return stt_loaded_models[model_type]

def get_summarizer_model(model_name):
  if model_name not in summ_loaded_models:
    summ_loaded_models[model_name] = load_summarizer_model(model_name)

  return summ_loaded_models[model_name]

# transcription
def audio_transcript(model_type, audio_file_path, return_timestamps=True):
  try:
    stt_pipe = get_stt_model(model_type)

    model_output = stt_pipe(audio_file_path, batch_size=16, return_timestamps=return_timestamps)
    text_output = model_output["text"]

    summary = summarize_text(text_output)

    return text_output, summary

  except Exception as e:
    return f"STT ERROR → {str(e)}", ""

# summarizer
def summarize_text(text_to_summarize, model_name="facebook/bart-large-cnn"):

  summarizer = get_summarizer_model(model_name)

  model_output = summarizer(text_to_summarize)
  text_output = model_output[0]["summary_text"]

  return text_output

# Gradio Interface
_ui = gr.Interface(
    fn=audio_transcript,
    inputs=[
        gr.Dropdown(
            choices=["Whisper - Tiny","Whisper - Base","Whisper - Small","Whisper - Medium","Whisper - Large V2","Whisper - Large V3"],
            label="Model Type",
            value="Whisper - Base"
        ),
        gr.Audio(label="Audio", sources="upload", type="filepath"),
        gr.Checkbox(label="Return Timestamps", value=True)
        ],
    outputs=[
        gr.Textbox(label="Text", lines=15, max_lines=40),
        gr.Textbox(label="Summary", lines=15, max_lines=40)
    ],
    title="Audio Transcription"
)

_ui.launch(server_name="0.0.0.0", server_port=7860, inbrowser=True)

