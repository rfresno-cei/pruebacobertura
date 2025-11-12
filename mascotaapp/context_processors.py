def cookie_tema(request):
    tema = request.COOKIES.get('tema', 'nada')
    return {'tema': tema}