# i ahev created this file - 

# from http.client import HTTPResponse
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    # params = { 'name':'Swapandeep', 'place': 'Bangalore'}
    # return HttpResponse("Hello Django!! This is home") 
    # print(request.GET.get('text', 'default'))
    return render(request, 'index.html')

# def about(request):
#     return HttpResponse("<a href = https://www.djangoproject.com/foundation/> <h1>About Django!!</h1>") 

# def community(request):
#     return HttpResponse("<a href = https://forum.djangoproject.com/> <h1>Django Community!!</h1>") 

# def discordcommunity(request):
#     return HttpResponse("<a href = https://discord.gg/xcRH6mN4fa> <h1>Django Discord Community!!</h1>") 

def analyze(request):  
    #POST the text:  
    djtext = request.POST.get('text', 'default')
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    # print(djtext, removepunc)
    #Analyze the text - 
    # analyzed = djtext
	
	#Check which checkbox is on
    if removepunc == "on":	
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed += char
        params ={ 'purpose' : "Removed punctuations", 'analyzed_text': analyzed}        
        return render(request, 'analyze.html', params)
    
    elif fullcaps == "on":
        analyzed = ""
        for char in djtext:
            # if char not in fullca  ps:
            analyzed += char.upper()
        params ={ 'purpose' : "Chanegd to UpperCase", 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)
    
    elif newlineremover == "on":
        analyzed = ""
        for char in djtext:
            if char != "\n" and char != "\r":
                analyzed += char
                
        params ={ 'purpose' : "Removed NewLines", 'analyzed_text': analyzed}						  
        return render(request, 'analyze.html', params)    
									
    # elif fullcaps == "on":
    #     analyzed = ""
    #     for char in djtext:
    #         # if char not in fullcaps:
    #         analyzed += char.upper()
    #     params ={ 'purpose' : "Chanegd to UpperCase", 'analyzed_text': analyzed}
    #     return render(request, 'analyze.html', params)
        
    # elif fullcaps == "on":
    #     analyzed = ""
    #     for char in djtext:
    #         # if char not in fullcaps:
    #         analyzed += char.upper()
    #     params ={ 'purpose' : "Chanegd to UpperCase", 'analyzed_text': analyzed}
    #     return render(request, 'analyze.html', params)
        
    else:
        return HttpResponse('Error')

# def capitalizefirst(request):
#     djtext = request.GET.get('text', 'default')
#     print(djtext)
#     #Analyze the text - 
#     return HttpResponse("<a href = https://www.djangoproject.com/foundation/> <h1>capitalizefirst!!</h1>") 

# def newlineremove(request):
#     return HttpResponse("<a href = https://www.djangoproject.com/foundation/> <h1>newlineremove!!</h1>") 

# def spaceremover(request):
#     return HttpResponse("<h1>spaceremover</h1> <a href = '/'>back</a>") 

# def charcounter(request):
#     return HttpResponse("<a href = https://www.djangoproject.com/foundation/> <h1>charcounter!!</h1>") 

