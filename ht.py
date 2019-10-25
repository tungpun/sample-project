# from django.conf.urls import url
import base64
from car import do_smt

def code_execution(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name', '')
        do_smt(first_name)
        do_smt(base64.decodestring(first_name))

        added_first_name = first_name + "hahaha"
        do_smt(added_first_name)
        # exec(base64.decodestring(first_name))


