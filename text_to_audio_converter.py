# TTS - Text to Speech Conversion

import gradio as gr
from transformers import pipeline
import torch

languages = [
    "English - ENG",
    "German - DEU",
    "Turkish - TUR",
    "French - FRA",
    "Spanish - SPA",
    "Italian - ITA",
    "Portuguese - POR",
    "Dutch - NLD",
    "Swedish - SWE",
    "Norwegian - NOR",
    "Finnish - FIN",
    "Russian - RUS",
    "Arabic - ARA",
    "Chinese - ZHO",
    "Japanese - JPN",
    "Korean - KOR",
    "Hindi - HIN",
    "Bengali - BEN",
    "Vietnamese - VIE",
    "Polish - POL",
    "Ukrainian - UKR",
    "Romanian - RON",
    "Greek - ELL",
    "Czech - CES",
    "Slovak - SLK",
    "Bulgarian - BUL",
    "Hungarian - HUN",
    "Serbian - SRP",
    "Croatian - HRV",
    "Hebrew - HEB",
]




def convert_TTS_output(audio, sample_rate=16000):

    # 1) float32 → int16
    if audio.dtype != np.int16:
        audio = np.clip(audio, -1.0, 1.0)   # taşmayı engelle
        audio = (audio * 32767).astype(np.int16)

    # 2) Mono değilse → Mono yap
    if len(audio.shape) > 1:
        audio = audio.mean(axis=1).astype(np.int16)

    return sample_rate, audio


def tts_converter(text_to_convert, lang="eng"):

  lang_code = lang.split("-")[-1].strip().lower()

  tts_pipe = pipeline(
      "text-to-speech",
      model=f"facebook/mms-tts-{lang_code}",

  )

  model_output = tts_pipe(text_to_convert)

  sample_rate, final_audio = convert_TTS_output(model_output)

  print(type(model_output["audio"]), len(model_output["audio"]))

  with open("output.wav", "wb") as file:
    file.write(model_output["audio"])

  return (sample_rate, final_audio)

_ui = gr.Interface(
    fn=tts_converter,
    inputs=[
        gr.Textbox(label="Please paste your text here..."),
        gr.Dropdown(
            languages,
            label="Language",
            value="English - ENG"
        )
    ],
        outputs=gr.Audio(label="Converted Speech", type="filepath"),
        title="Convert Text to Speech"
)

_ui.launch(server_name="0.0.0.0", server_port=7861, inbrowser=True)