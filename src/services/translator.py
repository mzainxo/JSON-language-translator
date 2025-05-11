import torch
from transformers import MarianMTModel, MarianTokenizer

class Translator:
    def __init__(self, model_names):
        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        self.models = {}
        self.tokenizers = {}

        for lang, model_name in model_names.items():
            tokenizer = MarianTokenizer.from_pretrained(model_name, use_fast=True)
            model = MarianMTModel.from_pretrained(model_name).to(self.device)
            model.eval()
            self.tokenizers[lang] = tokenizer
            self.models[lang] = model

    def translate_json(self, data, target_lang):
        if target_lang not in self.models:
            raise ValueError(f"No model loaded for language '{target_lang}'")

        model = self.models[target_lang]
        tokenizer = self.tokenizers[target_lang]
        skip_keys = {'id', 'uid', 'localid', 'inspectionlocalid'}

        def _recurse(obj, key=None):
            if obj is None or isinstance(obj, (bool, int, float)):
                return obj

            if isinstance(obj, dict):
                return {k: _recurse(v, key=k) for k, v in obj.items()}

            if isinstance(obj, list):
                return [_recurse(item) for item in obj]

            if isinstance(obj, str):
                if not obj.strip():
                    return obj
                kl = (key or "").lower()
                if kl in skip_keys or any(x in kl for x in ('image','file','blob')):
                    return obj

                with torch.no_grad():
                    batch = tokenizer([obj],
                                      return_tensors="pt",
                                      padding=True,
                                      truncation=True).to(self.device)
                    gen = model.generate(**batch)
                    return tokenizer.decode(gen[0], skip_special_tokens=True)

            return obj

        return _recurse(data)