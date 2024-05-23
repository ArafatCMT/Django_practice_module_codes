from django.shortcuts import render
from datetime import datetime

def template_filters(requset):
    data = {
        'name': 'Rahim',
        'lst' : ['python', 'is', 'fun'], 
        'fruits':['Banana', 'Mango', 'Orange', 'Apple'], 
        'date': datetime.now(),
        'str': "",
        'number': 50,
        'word': 'Dhaka Is The Capital Of Bangladesh',
        'word2': 'January - February - March - April',
        'person': [
            {'name': 'Omar' , 'age': 20},
            {'name': 'Taufiq' , 'age': 22},
            {'name': 'Arafat' , 'age': 21},
            {'name': 'Bayezid' , 'age': 28},
            {'name': 'Prionty' , 'age': 21},
        ],
        'title': 'Django rest framework',
        }
    return render(requset,'index.html', data)
