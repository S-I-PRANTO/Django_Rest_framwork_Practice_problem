from django.shortcuts import redirect


def Root(request):
   return redirect('/api/')