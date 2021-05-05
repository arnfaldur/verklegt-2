from django.shortcuts import render

breakfasts = [
   {'name': 'Cheerios', 'price': '200'},
   {'name': 'CocoPuffs', 'price': '250'},
   {'name': 'Corn Flakes', 'price': '200'},
   {'name': 'Lucky Charms', 'price': '300'}
]

# Create your views here.
def index(request):
   return render(request, 'breakfast/index.html', context={'breakfasts': breakfasts})