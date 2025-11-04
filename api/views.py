from rest_framework.response import Response
from rest_framework.decorators import api_view
from backend.supabase_client import supabase

@api_view(['GET'])
def listar_dados(request):
    """
    Exemplo: busca dados da tabela 'clientes' no Supabase e retorna para o frontend.
    """
    try:
        data = supabase.table("inmetro_database").select("*").execute()
        return Response(data.data)
    except Exception as e:
        import traceback
        return Response({
            "erro": str(e),
            "trace": traceback.format_exc()
        }, status=500)
