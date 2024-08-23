from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(reques):
    return HttpResponse ("Hello, wolrd . You are at the olls index")