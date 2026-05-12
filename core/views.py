from django.shortcuts import render
from django.http import JsonResponse
import json

def index(request):
    """View que serve o formulário com 20 perguntas"""
    return render(request, 'index.html')

def submit_form(request):
    """View que processa o envio do formulário"""
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            # Aqui você pode processar os dados do formulário
            # Por exemplo, salvar em um banco de dados
            return JsonResponse({
                'status': 'sucesso',
                'mensagem': 'Formulário enviado com sucesso!',
                'dados': data
            })
        except json.JSONDecodeError:
            return JsonResponse({
                'status': 'erro',
                'mensagem': 'Erro ao processar o formulário'
            }, status=400)
    return JsonResponse({'status': 'erro', 'mensagem': 'Método não permitido'}, status=405)
