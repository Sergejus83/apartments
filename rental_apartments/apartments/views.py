from django.shortcuts import render
from django.http import HttpResponse

def index(requets):
    return HttpResponse("Sveiki atvyke!")

