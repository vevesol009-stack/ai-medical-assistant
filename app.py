from flask import Flask, render_template, request, jsonify
import requests
import os

app = Flask(__name__)

# MiMo API config
MIMO_API_URL = "https://token-plan-sgp.xiaomimimo.com/v1/chat/completions"
MIMO_API_KEY = "tp-s4isct4pyh7pkbmloaihe0qjwjj1pmstlfnnnb8ik53696tw"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/diagnose', methods=['POST'])
def diagnose():
    data = request.json
    symptoms = data.get('symptoms', '')
    
    if not symptoms:
        return jsonify({'error': 'Please provide symptoms'}), 400
    
    # Call MiMo API for diagnosis
    prompt = f"""You are an AI medical assistant. Based on the following symptoms, provide:
1. Possible diagnoses (top 3 with confidence %)
2. Recommended actions
3. When to seek immediate medical attention
4. General health advice

Symptoms: {symptoms}

Format your response clearly with sections."""

    try:
        response = requests.post(
            MIMO_API_URL,
            headers={
                'Authorization': f'Bearer {MIMO_API_KEY}',
                'Content-Type': 'application/json'
            },
            json={
                'model': 'mimo-v2.5-pro',
                'messages': [
                    {'role': 'system', 'content': 'You are a helpful medical AI assistant. Always remind users to consult real doctors for serious conditions.'},
                    {'role': 'user', 'content': prompt}
                ],
                'temperature': 0.7
            },
            timeout=30
        )
        
        if response.status_code == 200:
            result = response.json()
            diagnosis = result['choices'][0]['message']['content']
            return jsonify({
                'success': True,
                'diagnosis': diagnosis
            })
        else:
            return jsonify({'error': f'API error: {response.status_code}'}), 500
            
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
