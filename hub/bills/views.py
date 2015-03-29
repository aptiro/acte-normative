import json
import hashlib

from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from models import Bill, Institution

@csrf_exempt
def receive_bills(request):
    received_bills = json.loads(request.body)
    for received_bill in received_bills:
        # TODO: use authorization by API key
        institution = Institution.objects.first()
        bill = Bill(title=received_bill['title'],
                    url=received_bill['url'],
                    key=hashlib.sha1(received_bill['title'].encode('utf-8')),
                    institution=institution)
        bill.save()
    return JsonResponse({'status': 'ok'})
