from django.http import HttpResponse,Http404,HttpResponseRedirect
from django.shortcuts import render
from myapp.models import sign

# Create your views here.
def test(req):
    return HttpResponse("hello")

def signup(request):
    if request.method == "POST":
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        uname = request.POST['uname']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        city = request.POST['city']
        state = request.POST['state']
        pincode = request.POST['pincode']
        role = request.POST.get('role')
        profile = request.POST.get('url')
        print(profile)
        # print(first_name,last_name,uname,email,password,confirm_password,city,state,pincode,role)
        ins= sign(first_name=first_name,last_name=last_name,uname=uname,email=email,password=password,confirm_password=confirm_password,city=city,state=state,pincode=pincode,role=role,profile_pic= profile)
        ins.save()
        print("Data saved successfully")
    return render(request, 'signup.html')

def home(request):
    return render(request, 'home.html')

def login(request):
    error = False
    if request.method == "POST":
        boole = False
        uname = request.POST['uname']
        password = request.POST['password']
        for each in sign.objects.all():
            if(each.uname == uname and each.password == password):
               
                request.session['uname'] = [uname]
                print(request.session.get('uname'))
                request.session.modified = True
                return HttpResponseRedirect('/home',{
                    #    error:
                })
            else:
                # errors.append('error')
                error=True

    return render(request, 'login.html',{
        'ename' : "Invalid username or password ",
        'error':error
    })

def home(request):
    active_user = request.session['uname'][0]
    return render(request,'home.html',{
        'profile': sign.objects.filter(uname=active_user)[0],
    })