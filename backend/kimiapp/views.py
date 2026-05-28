from django.shortcuts import render
from django.conf import settings
from rest_framework.decorators import api_view 
from rest_framework.response import Response
import google.generativeai as genai

genai.configure(api_key=settings.GEMINI_API_KEY)

model = genai.GenerativeModel("gemini-2.5-flash")
def load_system_prompts():
    with open('prompts/kimihelp_template.md','r',encoding='utf-8') as f:
        return f.read()
@api_view(['POST'])
def chat_with_kimihelp(request):
    try:
        system_template=load_system_prompts()
        user_msg=request.data.get('message','')
        promp_input=f"{system_template}\n\nUser: {user_msg}"
        response = model.generate_content(
         contents=promp_input,
        generation_config={
                "temperature": 0.2,
                "max_output_tokens": 500,
            }
                           )
        answer=response.text
        return  Response({'response':answer})
    except Exception as e:
        return Response(
            {"error": f'An unexpected error occured . {str(e)}'},status=500
        )