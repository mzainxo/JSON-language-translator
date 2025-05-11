import os
os.environ["TF_ENABLE_ONEDNN_OPTS"] = "0"
from fastapi import FastAPI
from pydantic import BaseModel
from typing import Dict, Any
from services.translator import Translator

app = FastAPI()

model_names = {
    "fr": "Helsinki-NLP/opus-mt-en-fr",
    "zh": "Helsinki-NLP/opus-mt-en-zh",
    "es": "Helsinki-NLP/opus-mt-en-es",
    "hi": "Helsinki-NLP/opus-mt-en-hi"
}

translator = Translator(model_names=model_names)

class TranslationRequest(BaseModel):
    json_data: Dict[str, Any]
    target_language: str

@app.post("/translate")
def translate_json(request: TranslationRequest):
    if request.target_language not in model_names:
        return {"error": "Unsupported target language."}
    translated_json = translator.translate_json(request.json_data, request.target_language)
    return {"translated_json": translated_json}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=int(os.environ.get("PORT", 8000)))