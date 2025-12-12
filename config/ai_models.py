# mapping

whisper_tts_models = {
    # --- Official OpenAI Whisper Models ---
    "Whisper - Tiny": "openai/whisper-tiny",
    "Whisper - Base": "openai/whisper-base",
    "Whisper - Small": "openai/whisper-small",
    "Whisper - Medium": "openai/whisper-medium",
    "Whisper - Large V1": "openai/whisper-large",
    "Whisper - Large V2": "openai/whisper-large-v2",
    "Whisper - Large V3": "openai/whisper-large-v3",

    # --- Distil-Whisper (faster, smaller) ---
    "Distil-Whisper - Tiny (EN)": "distil-whisper/distil-tiny.en",
    "Distil-Whisper - Base (EN)": "distil-whisper/distil-base.en",
    "Distil-Whisper - Small (EN)": "distil-whisper/distil-small.en",
    "Distil-Whisper - Medium (EN)": "distil-whisper/distil-medium.en",

    # Multilingual Distil versions
    "Distil-Whisper - Medium (Multilingual)": "distil-whisper/distil-medium",

    # --- Whisper Fine-Tuned Models (Community) ---
    "Whisper - Small (Turbo)": "Systran/faster-whisper-small",
    "Whisper - Medium (Turbo)": "Systran/faster-whisper-medium",
    "Whisper - Large-V2 (Turbo)": "Systran/faster-whisper-large-v2",

    # --- Faster-Whisper Models (very optimized for CPU/GPU) ---
    "Faster-Whisper - Tiny": "guillaumekln/faster-whisper-tiny",
    "Faster-Whisper - Base": "guillaumekln/faster-whisper-base",
    "Faster-Whisper - Small": "guillaumekln/faster-whisper-small",
    "Faster-Whisper - Medium": "guillaumekln/faster-whisper-medium",
    "Faster-Whisper - Large-V2": "guillaumekln/faster-whisper-large-v2",

    # --- Whisper Models for Noisy Audio ---
    "Whisper - Large-V2 (Noise-Robust)": "biodatlab/whisper-noise-large-v2",
}

summarizer_models = {

    # ---- BART ----
    "BART Large CNN": "facebook/bart-large-cnn",
    "BART Large XSum": "facebook/bart-large-xsum",

    # ---- T5 ----
    "T5 Small": "t5-small",
    "T5 Base": "t5-base",
    "T5 Large": "t5-large",

    # ---- Pegasus ----
    "Pegasus XSum": "google/pegasus-xsum",
    "Pegasus CNN/DailyMail": "google/pegasus-cnn_dailymail",
    "Pegasus MultiNews": "google/pegasus-multi_news",

    # ---- Long-form Summarization ----
    "Long T5 TGlobal-base": "pszemraj/long-t5-tglobal-base-16384-book-summary",
    "Long T5 XL TGlobal": "pszemraj/long-t5-tglobal-xl-16384-book-summary",

    # ---- Distilled models ----
    "DistilBART CNN": "sshleifer/distilbart-cnn-12-6",
    "DistilBART XSum": "sshleifer/distilbart-xsum-12-6",
}
