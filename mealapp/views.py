from .models import Clothes
from mealapp.models import *
from .serializers import ClothesSerializer
from rest_framework import generics
from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from .api import *
from collections import Counter
# Create your views here.

Clothes
class ClothesAPIList(generics.ListCreateAPIView):
    queryset = Clothes.objects.all()
    serializer_class = ClothesSerializer

class ClothesAPIUpdate(generics.UpdateAPIView):
    queryset = Clothes.objects.all()
    serializer_class = ClothesSerializer

class ClothesAPIDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = Clothes.objects.all()
    serializer_class = ClothesSerializer



def index(request):
    return render(request, 'index1.html' ,{'zipped_lst':zipped_lst})
def catalog(request):
    return render(request, 'catalog.html')
def contackts(request):
    return render(request, 'contackts.html')
def questions(request):
    return render(request, 'questions.html')
def about(request):
    return render(request, 'about.html')

def message(request):
    if request.method=='POST':
        send=Contact()
        send.name=request.POST.get('name')
        send.email=request.POST.get('email')
        send.address=request.POST.get('address')
        send.message=request.POST.get('message')
        send.save()
        return HttpResponseRedirect('/')


def signUp(request):
    if request.method == 'POST':
        user = UserCreationForm(request.POST  )
        if user.is_valid():
            user.save()
            return HttpResponseRedirect('/')

    else:
        user = UserCreationForm()
    return render(request, 'signup.html', {'user':user})
def signin(request):
    try:
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request , username=username, password=password)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect('/')

        else:
            form = AuthenticationForm()
        return render(request, 'auth.html', {'user':form})
    except UnboundLocalError:
        return render(request, 'error.html')

def signout(request):
    logout(request)
    return HttpResponseRedirect('/')

def addCart(request, id):
    cart_session = request.session.get('cart_session', [])
    cart_session.append(id)
    request.session['cart_session'] = cart_session
    return HttpResponseRedirect('/')

def cart(request):
    cart_session = request.session.get('cart_session', [])
    count_of_product = len(cart_session)
    products_cart =[]
    all_products_sum = 0
    for j in cart_session:
        for i in zipped_lst:
            if i[0] == j:
                products_cart.append(i)
                all_products_sum+=i[4]
    
    product = Counter(products_cart)
    lst = []
    for p, c in product.items():
        lst.append([p,c])
    return render(request, 'cart.html',{'count_of_product': count_of_product, 'all_products_sum': all_products_sum , 'lst':lst} )


def removeCart(request ,id):
    try:
        cart_session = request.session.get('cart_session', [])
        carts = []
        carts = cart_session
        carts.remove(id)
        request.session['cart_session'] = carts
        return HttpResponseRedirect('/cart')
    except:
        return HttpResponseRedirect('/cart')


def search(request):
    try:
        if request.method=='POST':
            meal = request.POST.get('meal')
            FOOD_API=f"https://Kubatbek.pythonanywhere.com/api/v1/Clothes={meal}"
            res = requests.get(FOOD_API)
            jeyson = res.json()
            run = len(jeyson['meals'])
            i = 0
            ii = []
            while i != run:
                i=i+1
                ii.append(i)
            ii.insert(0,0)
            ii.pop()
            all_meals = []
            all_img = []
            all_id = []
            zip_meal = zip(all_meals, all_img, all_id)
            for y in ii:
                all_img.append(jeyson['meals'][y]['strMealThumb'])
                all_meals.append(jeyson['meals'][y]['strMeal'])
                all_id.append(jeyson['meals'][y]['strCategory'])
            return render(request, "index1.html", {'zip_meal': zip_meal})
    except:
        return render(request, 'error.html')



def order(request):
    cart_session = request.session.get('cart_session', [])
    if request.method == 'POST':
        if len(cart_session) == 0:
            messages.error(request, 'Ваша карзина пустая',  extra_tags='danger')
            return redirect('cart')
        else:
            customer = Customer()
            customer.name = request.POST.get('c_name')
            customer.last_name = request.POST.get('c_lastname')
            customer.number = request.POST.get('c_number')
            customer.address = request.POST.get('c_addres')
            customer.message = request.POST.get('c_message')
            customer.save()
            for i in range(len(cart_session)):
                order = Order()
                cart_session = request.POST.get('cart_session', [])
                cart_session_lst = cart_session
                set_list = set(cart_session_lst)
                product_names_and_counts = []
                for i in set_list:
                    product=SneakerCard.objects.get(id = i)
                    product_name = product.tittle
                    count = cart_session_lst.count(i)
                    products = f"{product_name}-{count}"
                    product_names_and_counts.append(products)
                    products_cart = SneakerCard.objects.filter(id__in= cart_session)
                    all_products_sum = 0
                    for i in products_cart:
                        i.count = cart_session.count(i.id)
                        i.sum = i.count * i.price
                        all_products_sum += i.sum
                    order.product = product_names_and_counts
                    order.customer = customer
                    order.total_price = all_products_sum
                    order.phone = customer.number
                    order.address = customer.address
                    order.save()
                request.session['cart_session'] = []
                messages.error(request,'Заказ успешно отправлен', extra_tags='success')
                return redirect('cart')
