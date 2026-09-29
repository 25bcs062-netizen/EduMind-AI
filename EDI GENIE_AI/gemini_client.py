import os
import time
from pathlib import Path
from dotenv import load_dotenv
from google import genai

# Load .env file from the current directory or parent directories
env_path = Path(__file__).resolve().parent / ".env"
load_dotenv(dotenv_path=env_path)

API_KEY = os.getenv("GEMINI_API_KEY", "").strip()
PRIMARY_MODEL = os.getenv("GEMINI_MODEL", "gemini-3.5-flash-lite").strip() or "gemini-3.5-flash-lite"

# Fallback models in case primary is overloaded (503 / 429)
FALLBACK_MODELS = ["gemini-3.8-flash", "gemini-3.6-flash", "gemini-3.7-flash"]

client = None
if API_KEY:
    try:
        client = genai.Client(api_key=API_KEY)
    except Exception as e:
        print(f"Warning: Failed to initialize Gemini client on startup: {e}")


def get_client() -> genai.Client:
    global client
    if client is not None:
        return client

    api_key = os.getenv("GEMINI_API_KEY", "").strip()
    if not api_key:
        raise RuntimeError("GEMINI_API_KEY is not set. Please add your GEMINI_API_KEY in the .env file.")

    client = genai.Client(api_key=api_key)
    return client


def generate_content(prompt: str) -> str:
    if not prompt or not prompt.strip():
        raise ValueError("Prompt cannot be empty.")

    ai_client = get_client()
    
    # Candidate models to try in sequence
    models_to_try = [PRIMARY_MODEL]
    for fb in FALLBACK_MODELS:
        if fb not in models_to_try:
            models_to_try.append(fb)

    last_error = None

    for model in models_to_try:
        for attempt in range(1, 3):
            try:
                response = ai_client.models.generate_content(
                    model=model,
                    contents=prompt
                )

                if response and response.text:
                    return response.text.strip()

                raise RuntimeError("Gemini returned an empty response.")

            except Exception as error:
                last_error = error
                err_msg = str(error)
                print(f"[{model} attempt {attempt}] Error: {err_msg}")

                # If transient high demand/rate limit, wait briefly and retry or move to fallback
                if "503" in err_msg or "429" in err_msg or "UNAVAILABLE" in err_msg or "RESOURCE_EXHAUSTED" in err_msg:
                    time.sleep(1.0)
                    continue
                else:
                    # For non-transient errors (like 404), move immediately to next candidate model
                    break

    if "503" in str(last_error) or "UNAVAILABLE" in str(last_error):
        raise RuntimeError(
            "Gemini AI is currently experiencing high demand. Please try again in a moment."
        ) from last_error

    raise RuntimeError(
        "Gemini AI is temporarily unavailable. Please try again in a few seconds."
    ) from last_error

