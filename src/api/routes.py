from flask import Blueprint, request, jsonify
from services.translator import Translator

api = Blueprint('api', __name__)
translator = Translator()

@api.route('/translate', methods=['POST'])
def translate():
    data = request.json
    json_data = data.get('json_data')
    target_language = data.get('target_language')

    if not json_data or not target_language:
        return jsonify({'error': 'json_data and target_language are required.'}), 400

    try:
        translated_json = translator.translate_json(json_data, target_language)
        return jsonify({'translated_json': translated_json}), 200
    except ValueError as e:
        return jsonify({'error': str(e)}), 400
    except Exception as e:
        return jsonify({'error': 'An error occurred during translation.'}), 500