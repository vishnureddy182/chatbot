from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
import json
import os
import sys

# Add the parent directory to sys.path to import openrouter_llm
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# from openrouter_llm import call_openrouter

def index(request):
    """Render the main chat interface"""
    # Initialize chat history in session if it doesn't exist
    if 'chat_history' not in request.session:
        request.session['chat_history'] = []

    return render(request, 'chatapp/index.html', {
        'chat_history': request.session['chat_history']
    })

@csrf_exempt
@require_http_methods(["POST"])
def chat_endpoint(request):
    """Handle AJAX chat requests"""
    try:
        data = json.loads(request.body)
        user_message = data.get('message', '').strip()

        if not user_message:
            return JsonResponse({'error': 'Message cannot be empty'}, status=400)

        # Get existing chat history from session
        chat_history = request.session.get('chat_history', [])

        # Add user message to history
        chat_history.append({'role': 'user', 'content': user_message})

        # Get AI response using existing openrouter_llm function
        ai_response = call_openrouter(user_message)

        # Add AI response to history
        chat_history.append({'role': 'assistant', 'content': ai_response})

        # Save updated history back to session
        request.session['chat_history'] = chat_history

        return JsonResponse({
            'user_message': user_message,
            'ai_response': ai_response,
            'chat_history': chat_history
        })

    except json.JSONDecodeError:
        return JsonResponse({'error': 'Invalid JSON'}, status=400)
    except Exception as e:
        return JsonResponse({'error': f'Server error: {str(e)}'}, status=500)

@csrf_exempt
@require_http_methods(["POST"])
def clear_chat(request):
    """Clear chat history"""
    request.session['chat_history'] = []
    return JsonResponse({'status': 'success'})



import os
import requests
from dotenv import load_dotenv

# Load .env file
load_dotenv()

# Get API key
API_KEY = os.getenv("OPENROUTER_API_KEY")

def call_openrouter(prompt):
    url = "https://openrouter.ai/api/v1/chat/completions"

    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json",
        "HTTP-Referer": "http://localhost",
        "X-Title": "LangChain Chatbot"
    }

    data = {
        "model": "nvidia/nemotron-3-super-120b-a12b:free",
        "messages": [
            {"role": "user", "content": prompt}
        ]
    }
   

    response = requests.post(url, headers=headers, json=data)
    res_json = response.json()

    if "choices" not in res_json:
        return f"Error: {res_json}"

    return res_json["choices"][0]["message"]["content"]