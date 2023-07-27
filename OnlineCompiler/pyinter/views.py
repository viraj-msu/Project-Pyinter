import sys

from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'index.html')

def runcode(request):

    if request.method == "POST":
        codeareadata = request.POST['codearea'] #get data from codearea

        try:
            
            original_stdout = sys.stdout
            sys.stdout = open('file.txt', 'w')

            exec(codeareadata) #for execution of code

            sys.stdout.close()

            sys.stdout = original_stdout  #for reset

           
            output = open('file.txt', 'r').read() #read data from file

        except Exception as e:
            sys.stdout = original_stdout
            output = e

    return render(request , 'index.html', {"code":codeareadata , "output":output})
