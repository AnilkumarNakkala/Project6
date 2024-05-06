from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
data="""
    <table>
              <tr>
                <th>eid</th>
                <th>ename</th>
                <th>esal</th>
              </tr>
              <tr>
                <td>1001</td>
                <td>anil</td>
                <td>4000</td>
              </tr>
              <tr>
                <td>1002</td>
                <td>kumar</td>
                <td>6000</td>
              </tr>
              <tr>
                <td>1003</td>
                <td>praveen</td>
                <td>8000</td>
                </tr>
    </table>"""
class htmlview(View):
    def get(self,request):
        return HttpResponse(data,content_type="text/html")
class excelview(View):
    def get(self,request):
        return HttpResponse(data,content_type="application/vnd.ms-excel")
class xmlview(View):
    def get(self,request):
        return HttpResponse(data,content_type="application/xml")



# Create your views here.
