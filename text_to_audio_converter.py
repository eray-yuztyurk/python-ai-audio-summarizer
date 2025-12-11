# TTS - Text to Speech Conversion

import gradio as gr
from transformers import pipeline
import torch
import numpy as np
import soundfile as sf

# language mapping
languages = {
    "English": "eng",
    "German": "ger",
    "Turkish": "tur",
    "Arabic": "arb",
    "Bengali": "ben",
    "Bulgarian": "bul",
    "Chinese": "chn",
    "Croatian": "hrv",
    "Czech": "czh",
    "Finnish": "fin",
    "French": "fra",
    "Greek": "grk",
    "Hebrew": "heb",
    "Hindi": "hin",
    "Hungarian": "hun",
    "Italian": "ita",
    "Japanese": "jpn",
    "Korean": "kor",
    "Norwegian": "nor",
    "Polish": "pol",
    "Portuguese": "por",
    "Romanian": "rom",
    "Russian": "rus",
    "Serbian": "srb",
    "Slovak": "svk",
    "Spanish": "spa",
    "Swedish": "swe",
    "Ukrainian": "ukr",
    "Vietnamese": "vie"
}

# models in cache
tts_models = {}

# loader
def load_tts_model(lang_code):
    tts_pipe = pipeline(
        "text-to-speech",
        model=f"facebook/mms-tts-{lang_code}",
    
    )
    
    return tts_pipe

# getting model
def get_tts_model(lang_code):
    if lang_code not in tts_models:
        tts_models[lang_code] = load_tts_model(lang_code)

    return tts_models[lang_code]

# conversion to gradio audio format
def convert_TTS_output(audio, sample_rate=16000):

    audio = np.squeeze(audio)
    audio = np.clip(audio, -1, 1)
    audio = (audio * 32767).astype(np.int16)

    return sample_rate, audio

# conversion to audio
def tts_converter(text_to_convert, lang="English"):

    lang_code = languages[lang]

    tts_pipe = get_tts_model(lang_code)

    model_output = tts_pipe(text_to_convert)

    sample_rate, final_audio = convert_TTS_output(model_output["audio"], model_output["sampling_rate"])

    print(type(sample_rate), len(final_audio))

    #with open("output.wav", "wb") as file:
    #    file.write(model_output["audio"])
    sf.write("output.wav",final_audio, sample_rate)

    return (sample_rate, final_audio)

_ui = gr.Interface(
    fn=tts_converter,
    inputs=[
        gr.Textbox(label="Please paste your text here...", lines=10, max_lines=40),
        gr.Dropdown(
            list(languages.keys()),
            label="Language",
            value="English"
        )
    ],
        outputs=gr.Audio(label="Converted Speech", type="numpy"),
        title="Convert Text to Speech"
)

_ui.launch(server_name="0.0.0.0", server_port=7861, inbrowser=True)