def accesos(request):

    context = []
    accesos = ['profile']

    try:
        context = {
            'accesos': accesos
        }
    except:
        context = {
            'accesos': 'Error'
        }
    return context