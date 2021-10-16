import json
import time

import django_rq
from django.core.cache import cache
from rest_framework.response import Response
from rest_framework.views import APIView

from ..models import Hotel


def insert_data(r_data):
    date_cache = cache.get(r_data["booking_date"])
    if not date_cache:
        check_booking = Hotel.objects.filter(booking_date=r_data["booking_date"], status=True)
        if len(check_booking) == 0:
            Hotel.objects.create(booking_date=r_data["booking_date"], status=True, first_name=r_data["first_name"], last_name=r_data["last_name"], email=r_data["email"])
            cache.set(r_data["booking_date"], "Booked", None)
            return "Successfully Booked"
        else:
            cache.set(r_data["booking_date"], "Booked", None)
            return "Already Booked"
    else:
        return "Already Booked"


class BookRoom(APIView):
  
    def post(self, request):
        # req_data = json.dumps(request.data)
        # print(req_data)
        queue = django_rq.get_queue('default', default_timeout=800)
        job = queue.enqueue(insert_data, request.data)
        while True:
            if job.is_finished:
                print(job.return_value)
                break
            else:
              time.sleep(0.01)
        context = {"msg" : job.return_value}
        return Response(context)
