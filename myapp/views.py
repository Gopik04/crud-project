from django.shortcuts import render
from .models import Student
from .forms import StudentForm
from django.views.generic import View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from.mixins import *
import json
@method_decorator(csrf_exempt,name='dispatch')

class StudentCBV(View,HttpResponseMixin,SerilizeMixin):
    # def 
    # try:
    #    stud=Student.objects.get(id=id)
    # except Exception:
    #     stud=None
    # return Stud

    def get(self,request,*args,**kwargs):
        data=request.body
        valid=is_json(data)
        if not valid:
            json_data=json.dumps({'msg':'invalid'})
            return self.render_to_http_response(json_data,status=404)
        pdata=json.loads(data)
        id=pdata.get('id',None)
        if id is not None:
            stud=self.get_rec_by_id(id)
            if stud is None:
                json_data=json.dumps({'msg':'invalid record'})
                return self.render_to_http_response(json_data)
            json_data=self.fun([stud])
            return self.render_to_http_response(json_data)
        qs=Student.objects.all()
        json_data=self.fun(qs)
        return self.render_to_http_response(json_data)
    
    def post(self,request,*args,**kwargs):
        data=request.body
        valid=is_json(data)
        if not valid:
            json_data=json.dumps({'msg':'not a json data'})
            return self.render_to_http_response(json_data,status=404)
        p_data=json.loads(data)
        form=StudentForm(p_data)
        if form.is_valid():
            form.save(commit=True)
            json_data=json.dumps({'msg':'Successfuly created the record'})
            return self.render_to_http_response(json_data)
        if form.errors():
            json_data=json.dumps({'msg':'Form Sunbmission error'})
            return self.render_to_http_response(json_data,status=404)
    
    def put(self,request,*args,**kwargs):
        data=request.body
        valid=is_json(data)
        if not valid:
            json_data=json.dumps({'msg':'not a json data'})
            return self.render_to_http_response(json_data,status=404)
        provided_data=json.loads(data)
        id=provided_data.get('id',None)
        if id is None:
            json_data=json.dumps({'msg':'invalid id'})
            return self.render_to_http_response(json_data,status=404)
        stud=self.get_rec_by_id(id)
        if stud is None:
            json_data=json.dumps({'msg':'invalid record'})
            return self.render_to_http_response(json_data,status=404)
        original_data={'name':stud.name,'rollno':stud.rollno,'marks':stud.marks,'addres':stud.address}
        original_data.update(provided_data)
        form=StudentForm(original_data,instance=stud)
        if form.is_valid():
            form.save(commit=True)
            json_data=json.dumps({'msg':'updation is successfull'})
            return self.render_to_http_response(json_data)
        if form.errors():
            json_data=json.dumps({'msg':'Error In Form Sunbmission'})
            return self.render_to_http_response(json_data,status=404)
    
    def delete(self,request,*args,**kwargs):
        data=request.body
        valid=is_json(data)
        if not valid:
            json_data=json.dumps({'msg':'not a json data'})
            return self.render_to_http_response(json_data,status=404) 
        