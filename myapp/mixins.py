from django.core.serializers import serialize
from django.http import HttpResponse
import json

class SerilizeMixin(object):
    def fun(self,qs):
        json_data=serialize('json',qs)
        pdata=json.loads(json_data)
        final_list=[]
        for ob in pdata:
            required_info=ob['fields']
            final_list.append(required_info)
        json_data=json.dumps(final_list)
        return json_data
        