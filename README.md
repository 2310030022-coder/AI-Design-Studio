# 🎨 AI Design Studio — Generative AI Poster and Banner Generator

A colorful Gradio web app that generates promotional artwork from text prompts using the OpenAI Image API.

## Features
- Prompt-to-image artwork creation
- Five art directions (cinematic, neon, minimalist, fantasy, luxury)
- Square, landscape, and poster layouts
- Downloadable image result
- Form validation and API error messages

## Project context
A course-end project originally specifying `gpt-image-1`. That model was retired October 23, 2026; the current implementation defaults to `gpt-image-2.5-flare`.

## Run locally
```bash
pip install -r requirements.txt
export OPENAI_API_KEY='your-key'  # on Windows PowerShell: $env:OPENAI_API_KEY='your-key'
python app.py
```
Or open `AI_Design_Studio_Colab.ipynb` in Google Colab and set `OPENAI_API_KEY` in Colab Secrets.

## Hosting on Hugging Face Spaces
1. Create a Space at https://huggingface.co/new-space using the **Gradio** SDK.
2. Upload `app.py`, `requirements.txt`, and `README.md`.
3. Add `OPENAI_API_KEY` under Space **Settings → Variables and secrets → Secrets**; do not put it in code or repository files.
4. Keep the Space private while testing, and be aware public usage may incur API charges. Spaces may sleep on free hardware but retain their page URL.

## Security
Never commit an OpenAI API key. API requests cost money and a public app could be used by strangers. Do not upload `.env`, Colab outputs containing secrets, or credentials.

## Testing status
Interface implementation is supplied. Live generation requires a valid API key, suitable API access and billing; do not report a successful live image request until verified.
