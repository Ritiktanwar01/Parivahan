from django.shortcuts import render,redirect,HttpResponse,HttpResponseRedirect
from .models import *
from vhaanmain.models import *
from datetime import datetime,timezone,timedelta
# Create your views here.

def verify_user(user):
    my_user = user_custom.objects.filter(user_uuid = user).exists()
    return my_user

def getdatetime():
    tz = timezone(timedelta(hours=5, minutes=30))
    now = datetime.now(tz)
    
    date = now.strftime("%d")
    month = now.strftime("%m")
    year = now.strftime("%Y")
    hour = now.strftime("%I")
    minute = now.strftime("%M")
    am_pm = now.strftime("%p").upper()  # Use "%p" for AM/PM
    
    # Create a dictionary to map month numbers to month names
    month_names = {
        "01": "January",
        "02": "February",
        "03": "March",
        "04": "April",
        "05": "May",
        "06": "June",
        "07": "July",
        "08": "August",
        "09": "September",
        "10": "October",
        "11": "November",
        "12": "December"
    }
    
    # Get the month name from the dictionary (default to "invalid month" if not found)
    month_name = month_names.get(month, "invalid month")
    
    formatted_datetime = f"{date}-{month_name[:3].upper()}-{year} {hour}:{minute} {am_pm}"
    return formatted_datetime

def verify_admin(request):
    user_token = request.session.get('useruuid')
    get_admin = admin_list.objects.filter(auth_token = user_token).exists()
    return get_admin
def custom_admin_login(request):
    return render(request, 'CustomAdmin/adminlogin.html')
    
def admin_login(request):
    admin_name = request.POST.get('adminName')
    admin_password = request.POST.get('admin_pass')
    verify_data = admin_list.objects.filter(admin_name = admin_name,admin_password=admin_password).exists()
    if (verify_data):
        created_token = admin_list.objects.filter(admin_name = admin_name,admin_password=admin_password).values('auth_token')
        string_uuid = str(created_token[0].get('auth_token'))
        request.session['useruuid'] = string_uuid
        get_my_user_list = user_custom.objects.filter(created_by = string_uuid).values('username','password')
        get_state_count = len(statelists.objects.all())
        return render(request, 'CustomAdmin/myadmin.html',{'data':admin_name,'usercount':len(get_my_user_list),'statecount':get_state_count})
    else:
        return redirect('/admin/login')
            

def user_list(request):
    auth_token = request.session.get('useruuid')
    admin_id = verify_admin(request)
    if (admin_id):
        get_my_user_list = user_custom.objects.filter(created_by = auth_token,show = True).values('username','password','user_uuid')
        user_data = admin_list.objects.filter(auth_token = request.session.get('useruuid')).values('admin_name')[0].get('admin_name')
        return render(request, 'CustomAdmin/myadminuserlist.html',{'data':user_data,'userdata':get_my_user_list})
    else:
        return redirect('/admin')
def add_user_temp(request):
    uid = request.session.get('useruuid')
    if (verify_admin(request)):
        admin_mine = admin_list.objects.get(auth_token = uid)
        states = stateAssign_admin_custom.objects.filter(admin_name = admin_mine).values("state_name")
        state_list = []
        for i in range(len(states)):
            state_list.append(statelists.objects.filter(id = states[i].get('state_name')).values("id","state")[0])
        return render(request,'CustomAdmin/add_users.html',{"states":state_list})
    else:
        return redirect('admin')
    
def add_users(request):
    auth_token = request.session.get('useruuid')
    get_admin = admin_list.objects.filter(auth_token = auth_token).exists()
    if (get_admin):
        username = request.POST.get('username')
        password = request.POST.get('password')
        states = request.POST.get('stateSelectedId').split(',')
        duplicate_user = user_custom.objects.filter(created_by = auth_token,username = username,password=password).exists()
        if (duplicate_user):
            get_my_user_list = user_custom.objects.filter(created_by = auth_token,show = True).values('username','password')
            return render(request,'CustomAdmin/myadminuserlist.html',{'messege':"User already exists",'userdata':get_my_user_list[0]})
        else :
                try:
                    add_new_user = user_custom(created_by = auth_token,username = username,password=password)
                    add_new_user.save()
                    for m in range(len(states)):
                            my_assignment = stateassigned(user_name = user_custom.objects.get(username = username,created_by = auth_token),state_name = statelists.objects.get(id = states[m]) )
                            my_assignment.save()
                except:
                    print("somthing went wroong")
                    
                return redirect('/user_list')
    else:
        return redirect('/admin')
def logout(request):
        response = HttpResponseRedirect('/login')
        response.delete_cookie('token')
        return response
    
def user_recipt(request):
    user = request.POST.get('user_id')
    get_user_info = user_custom.objects.filter(user_uuid=user).values('username','password')
    get_tax_rajasthan = add_rajasthan.objects.filter(user_name = user).values('total_tax_amount','create_date','id','ownername','chassisno','mobile','from_state')
    get_tax_amt = 0
    for amount in get_tax_rajasthan:
        get_tax_amt = get_tax_amt + int(amount.get('total_tax_amount'))
    return render(request,'CustomAdmin/tabels.html',{'rajasthan':get_tax_rajasthan,'userinfo':get_user_info,'tottal_tax_collected':get_tax_amt})

def delete_user(request):
    admin = verify_admin(request)
    if (admin):
        user = request.POST.get('user_id')
        if (user != ''):
            check_exist = user_custom.objects.filter(user_uuid = user).exists()
            if (check_exist):
                user_custom.objects.filter(user_uuid = user).update(show=False)
                return redirect('/user_list')
        else:
            print("not exist")