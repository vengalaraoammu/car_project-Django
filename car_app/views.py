from django.shortcuts import render,redirect
from django.contrib.auth.forms import AuthenticationForm
import requests
from bs4 import BeautifulSoup
from django.contrib import messages
from django.contrib.auth.decorators import login_required,permission_required
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.models import User
from django.contrib.auth import logout
# Create your views here.

#@login_required(login_url='/my_login_page/')
@login_required
def home (request):

    return render(request,"index.html")

res = requests.get('https://www.cartrade.com/hyundai-cars/')
soup = BeautifulSoup(res.text,'html.parser')

name = soup.find_all('a',class_="car-list-title")
Name = []
for i in range(0,len(name)):
    Name.append(name[i].get_text())

divs = soup.find_all('a',class_="car-list-model-image")  # find all div tags
http_links = []
for div in divs:
    images = div.find_all('img')  # find all img tags within the div
    for img in images:
        src = img.get('src')  # get the src attribute value
        #alt = img.get('alt')  # get the alt attribute value
        if src.startswith('http'):
            http_links.append(src)


divs = soup.find_all('div',class_= 'car-list-details')  # find all div tags
Link = []
for div in divs:
    links = div.find_all('a')  # find all a tags within the div
    for link in links:
        href = "https://www.cartrade.com"+link.get('href')  # get the href attribute value
        Link.append(href)


price = soup.find_all("strong",class_="font-19")
Price = []
for i in range(0,len(price)):
    Price.append(price[i].get_text())
    Price=[string.replace("\n\t\t\t\t\t\t\t\t\t","") for string in Price] 



mylist=zip(Link,
Price,
Name,
http_links)

@login_required
def hyundai(request):
    return render(request,"hyundai.html",{'mylist':mylist})



res1 = requests.get('https://www.cartrade.com/marutisuzuki-cars/')
soup1 = BeautifulSoup(res1.text,'html.parser')

marutiname = soup1.find_all('a',class_="car-list-title")
marutiName = []
for k in range(0,len(marutiname)):
    marutiName.append(marutiname[k].get_text())

marutidivs = soup1.find_all('a',class_="car-list-model-image")  # find all div tags
img_links = []
for marutidiv in marutidivs:
    marutiimages = marutidiv.find_all('img')  # find all img tags within the div
    for imgs in marutiimages:
        src = imgs.get('src')  # get the src attribute value
        #alt = img.get('alt')  # get the alt attribute value
        if src.startswith('http'):
            img_links.append(src)


maruti_divs = soup1.find_all('div',class_= 'car-list-details')  # find all div tags
maruti_Link = []
for maruti_div in maruti_divs:
    maruti_links = maruti_div.find_all('a')  # find all a tags within the div
    for links in maruti_links:
        maruti_href = "https://www.cartrade.com"+links.get('href')  # get the href attribute value
        maruti_Link.append(maruti_href)


marutiprice = soup1.find_all("strong",class_="font-19")
marutiPrice = []
for j in range(0,len(marutiprice)):
    marutiPrice.append(marutiprice[j].get_text())
    marutiPrice=[string.replace("\n\t\t\t\t\t\t\t\t\t","") for string in marutiPrice] 



mylist1=zip(maruti_Link,
marutiPrice,
marutiName,
img_links)

@login_required
def Maruti (request):
    return render(request,"maruti.html",{'mylist1':mylist1})


res2 = requests.get('https://www.cartrade.com/tata-cars/')
soup2 = BeautifulSoup(res2.text,'html.parser')

tataname = soup2.find_all('a',class_="car-list-title")
tataName = []
for i1 in range(0,len(tataname)):
    tataName.append(tataname[i1].get_text())
    
tataprice = soup2.find_all("strong",class_="font-19")
tataPrice = []
for i2 in range(0,len(tataprice)):
    tataPrice.append(tataprice[i2].get_text())
    tataPrice=[string.replace("\n\t\t\t\t\t\t\t\t\t","") for string in tataPrice] 
    
tatadivs = soup2.find_all('a',class_="car-list-model-image")  # find all div tags
tataimg_links = []
for tatadiv in tatadivs:
    tataimages = tatadiv.find_all('img')  # find all img tags within the div
    for img in tataimages:
        src = img.get('src')  # get the src attribute value
        #alt = img.get('alt')  # get the alt attribute value
        if src.startswith('http'):
            tataimg_links.append(src)
            
tatadivs = soup2.find_all('div',class_= 'car-list-details')  # find all div tags
tata_Link = []
for tatadiv in tatadivs:
    tatalinks = tatadiv.find_all('a')  # find all a tags within the div
    for tatalink in tatalinks:
        tatahref = "https://www.cartrade.com"+tatalink.get('href')  # get the href attribute value
        tata_Link.append(tatahref)

mylist2=zip(tata_Link,
tataPrice,
tataName,
tataimg_links)

@login_required
def Tata (request):
    return render(request,"tata.html",{'mylist2':mylist2})


res3 = requests.get('https://www.cartrade.com/mahindra-cars/')
soup3 = BeautifulSoup(res3.text,'html.parser')

mahindraname = soup3.find_all('a',class_="car-list-title")
mahindraName = []
for iq in range(0,len(mahindraname)):
    mahindraName.append(mahindraname[iq].get_text())
    
mahindraprice = soup3.find_all("strong",class_="font-19")
mahindraPrice = []
for ia in range(0,len(mahindraprice)):
    mahindraPrice.append(mahindraprice[ia].get_text())
    mahindraPrice=[string.replace("\n\t\t\t\t\t\t\t\t\t","") for string in mahindraPrice] 
    
mahindradivs = soup3.find_all('a',class_="car-list-model-image")  # find all div tags
mahindraimg_links = []
for mahindradiv in mahindradivs:
    mahindraimages = mahindradiv.find_all('img')  # find all img tags within the div
    for img in mahindraimages:
        src = img.get('src')  # get the src attribute value
        #alt = img.get('alt')  # get the alt attribute value
        if src.startswith('http'):
            mahindraimg_links.append(src)
            
mahindradivs = soup3.find_all('div',class_= 'car-list-details')  # find all div tags
mahindra_Link = []
for mahindradiv in mahindradivs:
    mahindralinks = mahindradiv.find_all('a')  # find all a tags within the div
    for mahindralink in mahindralinks:
        mahindrahref = "https://www.cartrade.com"+mahindralink.get('href')  # get the href attribute value
        mahindra_Link.append(mahindrahref)

mylist3=zip(mahindra_Link,
mahindraPrice,
mahindraName,
mahindraimg_links)

@login_required
def mahindra (request):
    return render(request,"mahindra.html",{'mylist3':mylist3})



def register_user(request):
    if request.method == 'POST':
        # Get form data
        username = request.POST.get('username')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        email = request.POST.get('email')
        
        # Validate form data
        if password1 != password2:
            messages.error(request, "Passwords do not match.")
            return redirect('register_user')
        
        # Create user
        user = User.objects.create_superuser(username=username, password=password1, email=email)
        user.save()
        messages.success(request, "User created successfully.")
        return redirect('home')
    
    # Render registration form
    return render(request, 'registration/registration.html')

def logout_view(request):
    logout(request)
    return render(request,'registration/LogOut.html')

def index(request):
    return render(request,"index.html")

