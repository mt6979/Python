from django.shortcuts import render
from django.http import HttpResponse

def main(req):
    return HttpResponse("这是网站主页！！")