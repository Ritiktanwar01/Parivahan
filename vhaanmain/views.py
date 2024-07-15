from django.shortcuts import render,HttpResponse,redirect
from .models import *
from datetime import datetime,timezone,timedelta
import qrcode
import random
from URLSearchParams import URLSearchParams
import requests
import jwt

# Create your views here.

mysite = 'https://www.kmsparivahan.com/'
secrete = "yzpkhickfhpgsmwstjayuxhhrire7236][[@"

def send_sms(mobile,date_from,date_to,payment_date,amount,vehicle_no):
    # try:
    #     api = "http://123.108.46.13/sms-panel/api/http/index.php"
    #     data_obj = {
    #         "apikey":"443C3-B8A76",
    #         "username":"Jitender",
    #         "apirequest":"Text",
    #         "format":"JSON",
    #         "sender":"TVAHAN",
    #         "route":"TRANS",
    #         "mobile":mobile,
    #         "TemplateID":"1207166903332799443",
    #         "message":f"Your Tax of Rs.{amount} has been paid for Vehicle No.{vehicle_no}, valid from {date_from} to {date_to} paid on {payment_date} -TVAHAN"
    #     }
    #     url = URLSearchParams(api).append(data_obj)
    #     res = requests.get(url)
    #     return res
    # except:
    #     print("somthing went wrong")
    return 0


def getrecipt():
  dates = datetime.now()

  # Get the day, month (full name), and year
  day = dates.day
  year = dates.year

  # Convert to strings
  daystr = str(day)
  monthstr = str(dates.month)
  monthstrzer = "0" + monthstr if len(monthstr) == 1 else monthstr
  yearstr = str(year)
  repttimems = yearstr[2:] + monthstrzer + daystr
  random_number = random.randint(1, 100000000)
  result = repttimems + str(random_number)
  return result

    

def verify_user(user):
    my_user = user_custom.objects.filter(user_uuid = user).exists()
    return my_user

def number_to_text(num):
  num = int(num)
  ones = [
      'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight',
      'nine'
  ]
  tens = [
      '', 'ten', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy',
      'eighty', 'ninety'
  ]
  teens = [
      'ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen',
      'seventeen', 'eighteen', 'nineteen'
  ]

  if num < 10:
    return ones[num]
  elif num < 20:
    return teens[num - 10]
  elif num < 100:
    return tens[num // 10] + ('' if num % 10 == 0 else ' ' + ones[num % 10])
  elif num < 1000:
    return ones[num // 100] + ' hundred' + ('' if num % 100 == 0 else ' ' +
                                            number_to_text(num % 100))
  elif num < 1000000:
    return number_to_text(num // 1000) + ' thousand' + (
        '' if num % 1000 == 0 else ' ' + number_to_text(num % 1000))
  else:
    return 'Number out of range'

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

def home(request):
    return render(request, 'home/home.html')
def login(request):
    token = request.COOKIES.get('token')
    if (token == '' or token == None):  
        return render(request,'Login/login.html')
    else:
        decoded_payload = jwt.decode(token, secrete, algorithms=["HS256"])
        username = decoded_payload.get("username")
        password = decoded_payload.get("password")
        if (user_custom.objects.filter(username=username,password = password)):
            user_id = user_custom.objects.filter(username = username).values('id')
            user_id_filterd = user_id[0]['id']
            statedata = stateassigned.objects.filter(user_name = user_id_filterd).values('state_name')
            length_state_list = len(statedata)
            state_list = []
            for state in range(length_state_list):
                state_name = statelists.objects.filter(id = statedata[state]['state_name']).values('state')
                state_list.append(state_name[0]['state'])
            return render(request,'stateselection/stateselection.html',{'states':state_list})
        else:
            return render(request, 'Login/login.html')
        

def stateselection(request):
    if (request.method == "POST"):
        username = request.POST.get('username')
        password = request.POST.get('password')
        user_check = user_custom.objects.filter(username = username, password = password,show = True).exists()
        if (not user_check):
            return redirect("/login")
        else:
            token = jwt.encode({"username":username,"password":password}, secrete, algorithm="HS256")
            user_id = user_custom.objects.filter(username = username).values('id')
            user_id_filterd = user_id[0]['id']
            statedata = stateassigned.objects.filter(user_name = user_id_filterd).values('state_name')
            length_state_list = len(statedata)
            state_list = []
            for state in range(length_state_list):
                state_name = statelists.objects.filter(id = statedata[state]['state_name']).values('state')
                state_list.append(state_name[0]['state'])
            response = render(request,'stateselection/stateselection.html',{'states':state_list})
            response.set_cookie(key="token",value=token)
            return response
    else:
        return HttpResponse("Wrong method")
    
    
def stateform(request):
    if (request.method == 'POST'):
        state_name = request.POST.get('ib_state_input')
        if (state_name == "Rajasthan"):
            return render(request, 'rajasthan/rajasthan.html')
        elif (state_name == "Haryana"):
            return render(request, 'Haryana/haryana.html')
        elif (state_name == "Punjab"):
            return render(request, 'Punjab/punjab.html')
        elif (state_name == "Maharashtra"):
            return render(request, 'Maharashtra/maharashtra.html')
        elif (state_name == "Tamilnadu"):
            return render(request, 'Tamilnadu/TamilNaduForm.html')
        elif (state_name == "Madhyapradesh"):
            return render(request, 'Madhyapradesh/madhyapradesh.html')
        elif (state_name == "Karnatka"):
            return render(request, 'Karnatka/karnataka.html')
        elif (state_name == "Jharkhand"):
            return render(request, 'Jharkhand/jharkhand.html')
        elif (state_name == "Himachal Pradesh"):
            return render(request, 'Himachal/himachalpradesh.html')
        elif (state_name == "Bihar"):
            # return render(request, 'Bihar/bihar.html')
            return HttpResponse("this site is under devlopment")
        elif (state_name == "Gujrat"):
            return render(request, 'Gujrat/gujarat.html')
        elif (state_name == "Uttarpradesh"):
            return render(request, 'Uttarpradesh/uttarpradesh.html')
        elif (state_name == "Uttrakhand"):
            return render(request, 'Uttrakhand/uttrakhand.html')
        elif (state_name == "Tripura"):
            return render(request,'Tripura/tripuraform.html')
        elif (state_name == "Gujrat_ODC"):
            return render(request,'Gujrat_ODC/gujrat_odc_form.html')
        elif (state_name == "Gujrat"):
            return render(request,'Gujrat/gujarat.html')
        elif (state_name == "Madhya Pradesh"):
            return HttpResponse("<h1>Sorry This Site Is Under Maintinence Press Back Button To Exit This Page</h1>")
        elif (state_name == "Karnataka"):
            # return render(request,'Karnatka/karnataka.html')
            return HttpResponse("this site is under devlopment")
        else:
            return HttpResponse("invalid state")
    else:
        return HttpResponse("Wrong method")    
def rajasthan_data(request):
        token = request.COOKIES.get('token')
        vehicleno  = request.POST.get('vehicleno').upper()
        chassisno  = request.POST.get('chassisno').upper()
        ownername  = request.POST.get('ownername').upper()
        mobile  = request.POST.get('mobile').upper()
        from_state =request.POST.get('from_state').upper()
        VehicleType =request.POST.get('VehicleType').upper()
        VehicleClass =request.POST.get('VehicleClass').upper()
        seating_c =request.POST.get('seating_c').upper()
        txt_sleeper_cap =request.POST.get('txt_sleeper_cap').upper()
        PermitType =request.POST.get('PermitType').upper()
        border_entry =request.POST.get('border_entry').upper()
        checkpost_name =request.POST.get('checkpost_name').upper()
        TaxMode =request.POST.get('TaxMode').upper()
        txt_no_of_weeks =request.POST.get('txt_no_of_weeks').upper()
        tax_from =request.POST.get('tax_from').upper()
        tax_upto =request.POST.get('tax_upto').upper()
        civik_amount =request.POST.get('civik_amount')
        service_amount =request.POST.get('service_amount')
        sleeper_Cap_Weight =request.POST.get('sleeper_Cap_Weight')
        counter_fee = request.POST.get('counterfee')
        create_date = getdatetime()
        decoded_payload = jwt.decode(token, secrete, algorithms=["HS256"])
        username = decoded_payload.get("username")
        password = decoded_payload.get("password")
        user_uuid = user_custom.objects.filter(username = username,password=password).values("user_uuid")[0].get('user_uuid')
        recipt_no = getrecipt().upper()
        total_tax_amount = int(civik_amount) + int(service_amount) + int(counter_fee)
        total_amt_text = number_to_text(total_tax_amount).upper()
        data = add_rajasthan(user_name = user_uuid,vehicleno = vehicleno,chassisno=chassisno,ownername=ownername,mobile=mobile,from_state=from_state,VehicleType=VehicleType,VehicleClass=VehicleClass,seating_c=seating_c,txt_sleeper_cap=txt_sleeper_cap,PermitType=PermitType,border_entry=border_entry,checkpost_name=checkpost_name,TaxMode = TaxMode, txt_no_of_weeks = txt_no_of_weeks,tax_from = tax_from,tax_upto = tax_upto,total_tax_amount =total_tax_amount,civik_amount = civik_amount,service_amount = service_amount,sleeper_Cap_Weight= sleeper_Cap_Weight,counter_fee =counter_fee,create_date = create_date, recipt_no = recipt_no,total_amt_text=total_amt_text)
        data.save()
        send_sms(mobile,tax_from,tax_upto,create_date,total_tax_amount,vehicleno)
        id = str(data.id)
        return redirect('rajasthan_recipt'+'/'+id)
    
def rajasthan_pdf(request,id):
    get_data = add_rajasthan.objects.filter(id = id).values('vehicleno','chassisno','ownername','mobile','from_state','VehicleType','VehicleClass','seating_c','txt_sleeper_cap','PermitType','border_entry','checkpost_name','TaxMode','txt_no_of_weeks','tax_from','tax_upto','total_tax_amount','civik_amount','service_amount','sleeper_Cap_Weight','create_date','recipt_no','counter_fee','total_amt_text')
    qr_code = qrcode.make(mysite+"rajasthan_scan/"+id)
    id_str = str(id)
    qr_code.save('./media/qrcode/rajasthan/'+id_str+'.png')
    return render(request,'rajasthan/rajastha-pdf.html',{'data':get_data[0],'qr_code':id})

def rajasthan_scan(request,id):
    get_data = add_rajasthan.objects.filter(id = id).values('vehicleno','chassisno','ownername','mobile','from_state','VehicleType','VehicleClass','seating_c','txt_sleeper_cap','PermitType','border_entry','checkpost_name','TaxMode','txt_no_of_weeks','tax_from','tax_upto','total_tax_amount','civik_amount','service_amount','sleeper_Cap_Weight','create_date','recipt_no','counter_fee','total_amt_text')
    return render(request,'rajasthan/rajastha-pdf-scan..html',{'data':get_data[0]})


def punjab_data(request):
        token = request.COOKIES.get('token')
        vehicleno = request.POST.get('vehicleno').upper()
        chassisno = request.POST.get('chassisno').upper()
        ownername = request.POST.get('ownername').upper()
        mobile = request.POST.get('mobile').upper()
        from_state=request.POST.get('from_state').upper()
        VehicleType=request.POST.get('VehicleType').upper()
        VehicleClass=request.POST.get('VehicleClass').upper()
        seatingOrLaden=request.POST.get('seatingOrLaden')
        unldweightOrSleeper=request.POST.get('unldweightOrSleeper')
        ServiceType=request.POST.get('ServiceType').upper()
        TaxMode=request.POST.get('TaxMode').upper()
        border_entry=request.POST.get('border_entry').upper()
        districtname=request.POST.get('districtname').upper()
        entrydate=request.POST.get('entrydate').upper()
        outdate=request.POST.get('outdate')
        usercharge=request.POST.get('usercharge')
        infracess=request.POST.get('infracess')
        create_date=request.POST.get('create_date')
        recipt_no=getrecipt()
        mv_tax = request.POST.get('mv_tax')
        decoded_payload = jwt.decode(token, secrete, algorithms=["HS256"])
        username = decoded_payload.get("username")
        password = decoded_payload.get("password")
        user_uuid = user_custom.objects.filter(username = username,password=password).values("user_uuid")[0].get('user_uuid')
        total_amount = int(usercharge) + int(infracess) +int(mv_tax)
        total_amt_text = number_to_text(total_amount).upper()
        data = add_punjab(user_name = user_uuid,vehicleno = vehicleno,chassisno=chassisno,ownername=ownername,mobile=mobile,from_state=from_state,VehicleType=VehicleType,VehicleClass=VehicleClass,border_entry=border_entry,seatingOrLaden=seatingOrLaden,unldweightOrSleeper=unldweightOrSleeper,ServiceType=ServiceType,TaxMode=TaxMode,districtname=districtname,entrydate=entrydate,outdate=outdate,total_amount=total_amount,usercharge=usercharge,create_date=create_date,infracess=infracess,recipt_no=recipt_no,mv_tax = mv_tax,total_amt_text=total_amt_text)
        data.save()
        send_sms(mobile,entrydate,outdate,create_date,total_amount,vehicleno)
        id = str(data.id)
        return redirect('punjab_recipt'+'/'+id)
    
def punjab_pdf(request,id):
    get_data = add_punjab.objects.filter(id = id).values('vehicleno','chassisno','ownername','mobile','from_state','VehicleType','VehicleClass','SeatingOrWeight','seatingOrLaden','unldweightOrSleeper','ServiceType','TaxMode','border_entry','districtname','entrydate','outdate','total_amount','usercharge','infracess','create_date','recipt_no','mv_tax','total_amt_text')
    qr_code = qrcode.make(mysite+'/punjab_scan/'+id)
    id_str = str(id)
    qr_code.save('./media/qrcode/punjab/'+id_str+'.png')
    return render(request,'Punjab/punjab-pdf.html',{'data':get_data[0],'qr_code':id})

def punjab_scan(request,id):
    get_data = add_punjab.objects.filter(id = id).values('vehicleno','chassisno','ownername','mobile','from_state','VehicleType','VehicleClass','SeatingOrWeight','seatingOrLaden','unldweightOrSleeper','ServiceType','TaxMode','border_entry','districtname','entrydate','outdate','total_amount','usercharge','infracess','create_date','recipt_no','mv_tax','total_amt_text')
    return render(request,'Punjab/punjab-pdf.html',{'data':get_data[0]})



def haryana_data(request):
        created_username = request.COOKIES.get('token')
        vehicleno = request.POST.get('vehicleno').upper()
        chassisno = request.POST.get('chassisno').upper()
        ownername = request.POST.get('ownername').upper()
        mobile = request.POST.get('mobile').upper()
        from_state=request.POST.get('from_state').upper()
        VehicleType=request.POST.get('VehicleType').upper()
        VehicleClass=request.POST.get('VehicleClass').upper()
        seating_c=request.POST.get('seating_c').upper()
        ServiceType=request.POST.get('ServiceType').upper()
        distance=request.POST.get('distance').upper()
        TaxMode=request.POST.get('TaxMode').upper()
        border_entry=request.POST.get('border_entry').upper()       
        entrydate=request.POST.get('entrydate').upper()
        outdate=request.POST.get('outdate').upper()
        total_amount=request.POST.get('total_amount')
        create_date = getdatetime()
        total_amt_text = number_to_text(total_amount).upper()
        recipt_no = getrecipt()
        data = add_haryana(recipt_no=recipt_no,created_username = created_username,vehicleno = vehicleno,chassisno = chassisno,ownername = ownername,mobile = mobile,from_state = from_state,VehicleType = VehicleType,VehicleClass = VehicleClass,seating_c = seating_c,ServiceType = ServiceType,distance = distance,TaxMode = TaxMode,border_entry = border_entry,entrydate = entrydate,outdate = outdate,total_amount = total_amount,create_date=create_date,total_amt_text=total_amt_text)
        data.save()
        send_sms(mobile,entrydate,outdate,create_date,total_amount,vehicleno)
        id = str(data.id)
        return redirect('haryana_recipt'+'/'+id)
    
    
def haryana_pdf(request,id):
    get_data = add_haryana.objects.filter(id = id).values('recipt_no','created_username','vehicleno','chassisno','ownername','mobile','from_state','VehicleType','VehicleClass','seating_c','ServiceType','distance','TaxMode','border_entry','entrydate','outdate','total_amount','create_date','total_amt_text')
    qr_code = qrcode.make(mysite+'haryana_scan/'+id)
    id_str = str(id)
    qr_code.save('./media/qrcode/haryana/'+id_str+'.png')
    return render(request,'Haryana/haryana-pdf.html',{'data':get_data[0],'qr_code':id})


def haryana_pdf_scan(request,id):
    get_data = add_haryana.objects.filter(id = id).values('recipt_no','created_username','vehicleno','chassisno','ownername','mobile','from_state','VehicleType','VehicleClass','seating_c','ServiceType','distance','TaxMode','border_entry','entrydate','outdate','total_amount','create_date','total_amt_text')
    qr_code = qrcode.make(mysite+'haryana_scan/'+id)
    id_str = str(id)
    qr_code.save('./media/qrcode/haryana/'+id_str+'.png')
    return render(request,'Haryana/haryana-pdf.html',{'data':get_data[0],'qr_code':id})


def bihar_data(request):
    token = request.COOKIES.get('token')
    vehicle = request.POST.get('vehicle').upper()
    chassis_no = request.POST.get('chassis_no').upper()
    owner_name = request.POST.get('owner_name').upper()
    owner_mobile = request.POST.get('owner_mobile').upper()
    from_state=request.POST.get('from_state').upper()
    vehicle_type=request.POST.get('vehicle_type').upper()
    vehicle_class=request.POST.get('vehicle_class').upper()
    permit_type=request.POST.get('permit_type').upper()
    sitting_capacity=request.POST.get('sitting_capacity').upper()
    sleeper_capacity=request.POST.get('sleeper_capacity').upper()
    loading_capacity=request.POST.get('loading_capacity').upper()
    from_district=request.POST.get('from_district').upper()
    barrier=request.POST.get('barrier').upper()
    tax_mode=request.POST.get('tax_mode')
    tax_from=request.POST.get('tax_from')
    tax_upto=request.POST.get('tax_upto')
    tax_total=request.POST.get('tax_total')
    payment_mode=request.POST.get('payment_mode').upper()
    client_name=request.POST.get('client_name').upper()
    payment_date = getdatetime()
    total_amt_text = number_to_text(int(tax_total)).upper()
    recipt_no = getrecipt()
    decoded_payload = jwt.decode(token, secrete, algorithms=["HS256"])
    username = decoded_payload.get("username")
    password = decoded_payload.get("password")
    user_uuid = user_custom.objects.filter(username = username,password=password).values("user_uuid")[0].get('user_uuid')
    data = add_bihar(recipt_no=recipt_no,created_username = user_uuid,vehicle = vehicle,chassis_no = chassis_no,owner_name = owner_name,owner_mobile = owner_mobile ,from_state=from_state,vehicle_type=vehicle_type,vehicle_class=vehicle_class,permit_type=permit_type,sitting_capacity=sitting_capacity,sleeper_capacity=sleeper_capacity,loading_capacity=loading_capacity,from_district=from_district,barrier=barrier,tax_mode=tax_mode,tax_from=tax_from,tax_upto=tax_upto,tax_total=tax_total,payment_mode=payment_mode,client_name=client_name,payment_date = payment_date,total_amt_text=total_amt_text)
    data.save()
    send_sms(owner_mobile,tax_from,tax_upto,payment_date,tax_total,vehicle)
    id = data.id
    return redirect('bihar_recipt'+'/'+str(id))

def bihar_recipt(request,id):
    get_data = add_bihar.objects.filter(id = id).values('recipt_no','vehicle','chassis_no','owner_name','owner_mobile','from_state','vehicle_type','vehicle_class','sitting_capacity','sleeper_capacity','loading_capacity','from_district','tax_from','barrier','tax_mode','tax_from','tax_upto','tax_total','payment_mode','client_name','payment_date','total_amt_text')
    qr_code = qrcode.make(mysite+'/bihar_scan/'+id)
    id_str = str(id)
    qr_code.save('./media/qrcode/bihar/'+id_str+'.png')
    return render(request,'Bihar/bihar-pdf.html',{'data':get_data[0],'qr_code':id})

def bihar_scan(request,id):
    get_data = add_bihar.objects.filter(id = id).values('recipt_no','UsersId','vehicle','chassis_no','owner_name','owner_mobile','from_state','vehicle_type''vehicle_class','sitting_capacity','sleeper_capacity','loading_capacity','from_district','tax_from','barrier','tax_mode','tax_from','tax_upto','tax_total','payment_mode','client_name','payment_date','total_amt_text')
    return render(request,'Bihar/bihar-pdf.html',{'data':get_data[0]})

def gujrat_data(request):
    token = request.COOKIES.get('token')
    vehicleno = request.POST.get('vehicleno').upper()
    chassisno = request.POST.get('chassisno').upper()
    ownername = request.POST.get('ownername').upper()
    mobile = request.POST.get('mobile')
    from_state = request.POST.get('from_state').upper()
    VehicleType = request.POST.get('VehicleType').upper()
    VehicleClass = request.POST.get('VehicleClass').upper()
    ServiceType = request.POST.get('ServiceType').upper()
    seating_c = request.POST.get('seating_c').upper()
    txt_sleeper_cap = request.POST.get('txt_sleeper_cap').upper()
    ownertype = request.POST.get('ownertype').upper()
    makerstatus = request.POST.get('makerstatus').upper()
    ptype = request.POST.get('ptype').upper()
    permit_upto = request.POST.get('permit_upto').upper()
    TaxMode = request.POST.get('TaxMode').upper()
    border_entry = request.POST.get('border_entry').upper()
    permit_no = request.POST.get('permit_no').upper()
    permit_ia = request.POST.get('permit_ia').upper()
    tax_from = request.POST.get('tax_from')
    tax_upto = request.POST.get('tax_upto')
    total_tax_amount = request.POST.get('total_tax_amount')
    payment_date = getdatetime()
    total_amt_text = number_to_text(total_tax_amount).upper()
    recipt_no = getrecipt()
    decoded_payload = jwt.decode(token, secrete, algorithms=["HS256"])
    username = decoded_payload.get("username")
    password = decoded_payload.get("password")
    user_uuid = user_custom.objects.filter(username = username,password=password).values("user_uuid")[0].get('user_uuid')
    data = add_gujrat(recipt_no = recipt_no,created_username = user_uuid,vehicleno = vehicleno,chassisno = chassisno,ownername = ownername,mobile = mobile,from_state=from_state,VehicleType=VehicleType,VehicleClass=VehicleClass,ServiceType=ServiceType,seating_c=seating_c,txt_sleeper_cap=txt_sleeper_cap,ownertype=ownertype,makerstatus=makerstatus,ptype=ptype,permit_upto=permit_upto,TaxMode=TaxMode,border_entry=border_entry,permit_no=permit_no,permit_ia=permit_ia,tax_from=tax_from,tax_upto=tax_upto,total_tax_amount=total_tax_amount,payment_date = payment_date,total_amt_text=total_amt_text)
    data.save()
    send_sms(mobile,tax_from,tax_upto,payment_date,total_tax_amount,vehicleno)
    id = str(data.id)
    return redirect('gujrat_recipt'+'/'+id)

def gujrat_pdf(request,id):
    # correct values
    get_data = add_gujrat.objects.filter(id = id).values('recipt_no','created_username','vehicleno','chassisno' ,'ownername','mobile' ,'from_state','VehicleType','VehicleClass','ServiceType','seating_c','txt_sleeper_cap','ownertype','makerstatus','ptype','permit_upto','TaxMode','border_entry','permit_no','permit_ia','tax_from','tax_upto','total_tax_amount','total_amt_text','payment_date')
    qr_code = qrcode.make(mysite+'/gujrat_scan/'+id)
    id_str = str(id)
    qr_code.save('./media/qrcode/gujrat/'+id_str+'.png')
    return render(request,'Gujrat/Gujarat-pdf.html',{'data':get_data[0],'qr_code':id})

def gujrat_scan(request,id):
    # correct values
    get_data = add_gujrat.objects.filter(id = id).values('recipt_no','created_username','vehicleno','chassisno' ,'ownername','mobile' ,'from_state','VehicleType','VehicleClass','ServiceType','seating_c','txt_sleeper_cap','ownertype','makerstatus','ptype','permit_upto','TaxMode','border_entry','permit_no','permit_ia','tax_from','tax_upto','total_tax_amount','total_amt_text','payment_date')
    return render(request,'Gujrat/Gujarat-pdf.html',{'data':get_data[0]})


def gujrat_odc_data(request):
    token = request.COOKIES.get('token')
    vehicle = request.POST.get('vehicle').upper()
    chassis = request.POST.get('chassis').upper()
    owner_type = request.POST.get('owner_type').upper()
    owner_name = request.POST.get('owner_name').upper()
    mobileno = request.POST.get('mobileno').upper()
    vehicle_type = request.POST.get('vehicle_type').upper()
    vehicle_class = request.POST.get('vehicle_class').upper()
    gross_wt = request.POST.get('gross_wt').upper()
    unladen_wt = request.POST.get('unladen_wt').upper()
    body_type = request.POST.get('body_type').upper()
    goods_nature_input = request.POST.get('goods_nature_input').upper()
    over_dimension_input = request.POST.get('over_dimension_input').upper()
    conHeight_input = request.POST.get('conHeight_input').upper()
    conWidth_input = request.POST.get('conWidth_input').upper()
    conLength_input = request.POST.get('conLength_input').upper()
    permit_type_input = request.POST.get('permit_type_input').upper()
    txt_permit_no = request.POST.get('txt_permit_no').upper()
    road_tax_val = request.POST.get('road_tax_val').upper()
    state_from = request.POST.get('state_from')
    district_input = request.POST.get('district_input').upper()
    state_to = request.POST.get('state_to').upper()
    to_district_input = request.POST.get('to_district_input').upper()
    insurance_val = request.POST.get('insurance_val').upper()
    fitness_val = request.POST.get('fitness_val').upper()
    pucc_val = request.POST.get('pucc_val').upper()
    permit_val = request.POST.get('permit_val').upper()
    lr_no = request.POST.get('lr_no').upper()
    goodd_description_input = request.POST.get('goodd_description_input').upper()
    remarks = request.POST.get('remarks').upper()
    lr_date = request.POST.get('lr_date').upper()
    total_tax_amount = int(request.POST.get('total_tax_amount'))
    amount_text = number_to_text(total_tax_amount).upper()
    payment_date = getdatetime().upper()
    decoded_payload = jwt.decode(token, secrete, algorithms=["HS256"])
    username = decoded_payload.get("username")
    password = decoded_payload.get("password")
    user_uuid = user_custom.objects.filter(username = username,password=password).values("user_uuid")[0].get('user_uuid')
    data = add_gujrat_odc(created_user = user_uuid ,vehicle = vehicle,chassis = chassis,owner_type = owner_type,owner_name = owner_name,mobileno = mobileno,vehicle_type = vehicle_type,vehicle_class = vehicle_class,gross_wt = gross_wt,unladen_wt = unladen_wt,body_type = body_type,goods_nature_input = goods_nature_input,over_dimension_input = over_dimension_input,conHeight_input = conHeight_input,conWidth_input = conWidth_input,conLength_input = conLength_input,permit_type_input = permit_type_input,txt_permit_no = txt_permit_no,road_tax_val = road_tax_val,state_from = state_from,district_input = district_input,state_to = state_to,to_district_input = to_district_input,insurance_val = insurance_val,fitness_val = fitness_val,pucc_val = pucc_val,permit_val = permit_val,lr_no = lr_no,goodd_description_input = goodd_description_input,remarks = remarks,total_tax_amount = total_tax_amount,payment_date = payment_date,lr_date = lr_date,amount_text = amount_text)
    Id = data.save()
    Id = data.id
    return redirect('gujrat_odc_recipt'+'/'+str(Id))

def gujrat_odc_recipt(request,id):
    data = add_gujrat_odc.objects.filter(id = id).values('vehicle','chassis','owner_type','owner_name','mobileno','vehicle_type','vehicle_class','gross_wt','unladen_wt','body_type','goods_nature_input','over_dimension_input','conHeight_input','conWidth_input','conLength_input','permit_type_input','txt_permit_no','road_tax_val','state_from','district_input','state_to','to_district_input','insurance_val','fitness_val','pucc_val','permit_val','lr_no','goodd_description_input','remarks','total_tax_amount','payment_date','lr_date','amount_text')
    qr_code = qrcode.make(mysite+'gujrat_odc_scan'+'/'+id)
    id_str = str(id)
    qr_code.save('./media/qrcode/gujrat_odc/'+id_str+'.png')
    return render(request,'Gujrat_ODC/gujrat_odc_recipt.html',{'data':data[0],'qrcode':id},)

def gujrat_odc_scan(request,id):
    return render(request,'Gujrat_ODC/err_scan.html')

def himachal_data(request):
    token = request.COOKIES.get('token')
    vehicleno = request.POST.get('vehicleno').upper()
    chassisno = request.POST.get('chassisno').upper()
    ownername = request.POST.get('ownername').upper()
    mobile = request.POST.get('mobile')
    from_state=request.POST.get('from_state').upper()
    VehicleType=request.POST.get('VehicleType').upper()
    VehicleClass=request.POST.get('VehicleClass').upper()
    ServiceType=request.POST.get('ServiceType').upper()
    seating_c=request.POST.get('seating_c')
    border_entry=request.POST.get('border_entry').upper()
    TaxMode=request.POST.get('TaxMode').upper()
    service_amount=request.POST.get('service_amount')
    tax_from=request.POST.get('tax_from')
    tax_upto=request.POST.get('tax_upto')
    total_tax_amount=request.POST.get('total_tax_amount')
    payment_date = getdatetime()
    recipt_no = getrecipt()
    total_amt_text = number_to_text(total_tax_amount)
    decoded_payload = jwt.decode(token, secrete, algorithms=["HS256"])
    username = decoded_payload.get("username")
    password = decoded_payload.get("password")
    user_uuid = user_custom.objects.filter(username = username,password=password).values("user_uuid")[0].get('user_uuid')
    data = add_himachal(recipt_no=recipt_no,created_username = user_uuid,vehicleno =vehicleno,chassisno =chassisno,ownername =ownername,mobile =mobile,from_state=from_state,VehicleType=VehicleType,VehicleClass=VehicleClass,ServiceType=ServiceType,seating_c=seating_c,border_entry=border_entry,TaxMode=TaxMode,service_amount=service_amount,tax_from=tax_from,tax_upto=tax_upto,total_tax_amount=total_tax_amount,payment_date = payment_date,total_amt_text=total_amt_text)
    data.save()
    send_sms(mobile,tax_from,tax_upto,payment_date,total_tax_amount,vehicleno)
    id = data.id
    return redirect('himachal_recipt'+'/'+str(id))

def himachal_recipt(request,id):
    get_data = add_himachal.objects.filter(id = id).values('created_username','vehicleno' ,'chassisno','ownername','mobile','from_state','VehicleType','VehicleClass','ServiceType','seating_c','border_entry','TaxMode','service_amount','tax_from','tax_upto','total_tax_amount','total_amt_text','payment_date','recipt_no')
    qr_code = qrcode.make(mysite+'/himachal_scan/'+id)
    id_str = str(id)
    qr_code.save('./media/qrcode/himachal/'+id_str+'.png')
    return render(request,'Himachal/himachal-pdf.html',{'data':get_data[0],'qr_code':id})

def himachal_scan(request,id):
    get_data = add_himachal.objects.filter(id = id).values('created_username','vehicleno' ,'chassisno','ownername','mobile','from_state','VehicleType','VehicleClass','ServiceType','seating_c','border_entry','TaxMode','service_amount','tax_from','tax_upto','total_tax_amount','total_amt_text','payment_date','recipt_no')
    return render(request,'Himachal/himachal-pdf.html',{'data':get_data[0]})


def jharkhand_data(request):
    token = request.COOKIES.get('token')
    vehicleno = request.POST.get('vehicleno').upper()
    chassisno = request.POST.get('chassisno').upper()
    ownername = request.POST.get('ownername').upper()
    mobile = request.POST.get('mobile')
    from_state=request.POST.get('from_state').upper()
    VehicleType=request.POST.get('VehicleType').upper()
    VehicleClass=request.POST.get('VehicleClass').upper()
    PermitType=request.POST.get('PermitType').upper()
    seating_c=request.POST.get('seating_c')
    border_entry=request.POST.get('border_entry').upper()
    TaxMode=request.POST.get('TaxMode').upper()
    txt_no_of_weeks=request.POST.get('txt_no_of_weeks')
    tax_from=request.POST.get('tax_from')
    tax_upto=request.POST.get('tax_upto')
    total_tax_amount=request.POST.get('total_tax_amount')
    payment_date = getdatetime()
    total_amt_text = number_to_text(total_tax_amount).upper()
    recipt_no = getrecipt()
    decoded_payload = jwt.decode(token, secrete, algorithms=["HS256"])
    username = decoded_payload.get("username")
    password = decoded_payload.get("password")
    user_uuid = user_custom.objects.filter(username = username,password=password).values("user_uuid")[0].get('user_uuid')
    data = add_jharkhand(recipt_no=recipt_no,created_username=user_uuid,vehicleno =vehicleno,chassisno =chassisno,ownername =ownername,mobile =mobile,from_state=from_state,VehicleType=VehicleType,VehicleClass=VehicleClass,PermitType=PermitType,seating_c=seating_c,border_entry=border_entry,TaxMode=TaxMode,txt_no_of_weeks=txt_no_of_weeks,tax_from=tax_from,tax_upto=tax_upto,total_tax_amount=total_tax_amount,payment_date=payment_date,total_amt_text = total_amt_text)
    data.save()
    send_sms(mobile,tax_from,tax_upto,payment_date,total_tax_amount,vehicleno)
    id = data.id
    return redirect('jharkhand_recipt'+'/'+str(id))

def jharkhand_recipt(request,id):
    get_data = add_jharkhand.objects.filter(id = id).values('recipt_no','vehicleno','chassisno','ownername','mobile','from_state','VehicleType','VehicleClass','seating_c','border_entry','TaxMode','txt_no_of_weeks','tax_from','tax_upto','total_tax_amount','total_amt_text','payment_date')
    qr_code = qrcode.make(mysite+'/jharkhand_scan/'+id)
    id_str = str(id)
    qr_code.save('./media/qrcode/jharkhand/'+id_str+'.png')
    return render(request,'Jharkhand/jharkhand-pdf.html',{'data':get_data[0],'qr_code':id})

def jharkhand_scan(request,id):
    get_data = add_jharkhand.objects.filter(id = id).values('recipt_no','vehicleno' ,'chassisno','ownername','mobile','from_state','VehicleType','VehicleClass','seating_c','border_entry','TaxMode','txt_no_of_weeks','tax_from','tax_upto','total_tax_amount','total_amt_text','payment_date')
    return render(request,'Jharkhand/jharkhand-pdf.html',{'data':get_data[0]})

def karnatka_data(request):
    token = request.COOKIES.get('token')
    vehicleno = request.POST.get('vehicleno')
    chassisno = request.POST.get('chassisno')
    ownername = request.POST.get('ownername')
    mobile = request.POST.get('mobile')
    from_state = request.POST.get('from_state')
    VehicleType = request.POST.get('VehicleType')
    VehicleClass = request.POST.get('VehicleClass')
    ServiceType = request.POST.get('ServiceType')
    PermitType = request.POST.get('PermitType')
    seating_c = request.POST.get('seating_c')
    txt_sleeper_cap = request.POST.get('txt_sleeper_cap')
    txt_floor_area = request.POST.get('txt_floor_area')
    TaxMode = request.POST.get('TaxMode')
    permit_upto = request.POST.get('permit_upto')
    fitdate = request.POST.get('fitdate')
    ins_upto = request.POST.get('ins_upto')
    tax_validity = request.POST.get('tax_validity')
    border_entry = request.POST.get('border_entry')
    txt_no_of_weeks = request.POST.get('txt_no_of_weeks')
    service_amount = request.POST.get('service_amount')
    tax_from = request.POST.get('tax_from')
    tax_upto = request.POST.get('tax_upto')
    total_tax_amount = request.POST.get('total_tax_amount')
    infra_cess = request.POST.get('infra_cess')
    permit_fee = request.POST.get('permit_fee')
    permit_endoresment_variation = request.POST.get('permit_endoresment_variation')
    payment_date = getdatetime()
    total_amt_text = number_to_text(total_tax_amount)
    decoded_payload = jwt.decode(token, secrete, algorithms=["HS256"])
    username = decoded_payload.get("username")
    password = decoded_payload.get("password")
    user_uuid = user_custom.objects.filter(username = username,password=password).values("user_uuid")[0].get('user_uuid')
    data = add_karnataka(created_username =  user_uuid,vehicleno =  vehicleno,chassisno =  chassisno,ownername =  ownername,mobile =  mobile,from_state =  from_state,VehicleType =  VehicleType,VehicleClass =  VehicleClass,ServiceType =  ServiceType,PermitType =  PermitType,seating_c =  seating_c,txt_sleeper_cap =  txt_sleeper_cap,txt_floor_area =  txt_floor_area,TaxMode =  TaxMode,permit_upto =  permit_upto,fitdate =  fitdate,ins_upto =  ins_upto,tax_validity =  tax_validity,border_entry =  border_entry,txt_no_of_weeks =  txt_no_of_weeks,service_amount =  service_amount,tax_from =  tax_from,tax_upto =  tax_upto,total_tax_amount =  total_tax_amount,infra_cess =  infra_cess,permit_fee =  permit_fee,permit_endoresment_variation =  permit_endoresment_variation,payment_date = payment_date,total_amt_text=total_amt_text)
    data.save()
    send_sms(mobile,tax_from,tax_upto,payment_date,total_tax_amount,vehicleno)
    id = data.id
    return redirect('karnataka_recipt'+'/'+id)
    
def karnataka_recipt(request,id):
    get_data = add_karnataka.objects.filter(id=id).values('created_username' ,'vehicleno','chassisno','ownername','mobile','from_state','VehicleType','VehicleClass','ServiceType','PermitType','seating_c','txt_sleeper_cap','txt_floor_area','TaxMode','permit_upto','fitdate','ins_upto','tax_validity','border_entry','txt_no_of_weeks','service_amount','tax_from','tax_upto','total_tax_amount','infra_cess','permit_fee','permit_endoresment_variation','total_amt_text')
    qr_code = qrcode.make(mysite+'/karnataka_scan/'+id)
    id_str = str(id)
    qr_code.save('./media/qrcode/karnatka/'+id_str+'.png')
    return render(request,'Karnatka/karnataka-pdf.html',{'data':get_data[0],'qr_code':id})

def karnataka_scan(request,id):
    get_data = add_karnataka.objects.filter(id=id).values('created_username' ,'vehicleno','chassisno','ownername','mobile','from_state','VehicleType','VehicleClass','ServiceType','PermitType','seating_c','txt_sleeper_cap','txt_floor_area','TaxMode','permit_upto','fitdate','ins_upto','tax_validity','border_entry','txt_no_of_weeks','service_amount','tax_from','tax_upto','total_tax_amount','infra_cess','permit_fee','permit_endoresment_variation','total_amt_text')
    return render(request,'Karnatka/karnataka-pdf.html',{'data':get_data[0]})

def madhyapradesh_data(request):
    token = request.COOKIES.get('token')
    VehicleType = request.POST.get('VehicleType')
    from_state = request.POST.get('from_state')
    ownername = request.POST.get('ownername')
    vehicleno = request.POST.get('vehicleno')
    gramin = request.POST.get('gramin')
    tax_mode = request.POST.get('tax_mode')
    tax_from = request.POST.get('tax_from')
    tax_upto = request.POST.get('tax_upto')
    total_tax_amount = request.POST.get('total_tax_amount')
    tax_consessioner = request.POST.get('tax_consessioner')
    tax_ips = request.POST.get('tax_ips')
    mobile = request.POST.get('mobile')
    genby = request.POST.get('genby')
    payment_date = getdatetime()
    total_amt_text = number_to_text(total_tax_amount)
    decoded_payload = jwt.decode(token, secrete, algorithms=["HS256"])
    username = decoded_payload.get("username")
    password = decoded_payload.get("password")
    user_uuid = user_custom.objects.filter(username = username,password=password).values("user_uuid")[0].get('user_uuid')
    data = add_madhyapradesh(created_username = user_uuid,VehicleType = VehicleType,from_state = from_state,ownername = ownername,vehicleno = vehicleno,gramin = gramin,tax_mode = tax_mode,tax_from = tax_from,tax_upto = tax_upto,total_tax_amount = total_tax_amount,tax_consessioner = tax_consessioner,tax_ips = tax_ips,mobile = mobile,genby = genby,payment_date = payment_date,total_amt_text = total_amt_text)
    data.save()
    send_sms(mobile,tax_from,tax_upto,payment_date,total_tax_amount,vehicleno)
    id = data.id
    return redirect('madhyapradesh_recipt'+'/'+id)


def madhyapradesh_recipt(request,id):
    get_data = add_madhyapradesh.objects.filter(id=id).values('created_username' ,'vehicleno','chassisno','ownername','mobile','from_state','VehicleType','VehicleClass','ServiceType','PermitType','seating_c','txt_sleeper_cap','txt_floor_area','TaxMode','permit_upto','fitdate','ins_upto','tax_validity','border_entry','txt_no_of_weeks','service_amount','tax_from','tax_upto','total_tax_amount','infra_cess','permit_fee','permit_endoresment_variation','total_amt_text')
    qr_code = qrcode.make(mysite+'/madhyapradesh_scan/'+id)
    id_str = str(id)
    qr_code.save('./media/qrcode/MP/'+id_str+'.png')
    return render(request,'Madhyapradesh/madhyapradesh-pdf.html',{'data':get_data[0],'qr_code':id})

def madhyapradesh_scan(request,id):
    get_data = add_madhyapradesh.objects.filter(id=id).values('created_username' ,'vehicleno','chassisno','ownername','mobile','from_state','VehicleType','VehicleClass','ServiceType','PermitType','seating_c','txt_sleeper_cap','txt_floor_area','TaxMode','permit_upto','fitdate','ins_upto','tax_validity','border_entry','txt_no_of_weeks','service_amount','tax_from','tax_upto','total_tax_amount','infra_cess','permit_fee','permit_endoresment_variation','total_amt_text')
    return render(request,'Madhyapradesh/madhyapradesh-pdf.html',{'data':get_data[0]})

def maharashtra_data(request):
    token =  request.COOKIES.get('token')
    vehicleno =  request.POST.get('vehicleno').upper()
    chassisno =  request.POST.get('chassisno').upper()
    ownername =  request.POST.get('ownername').upper()
    mobile =  request.POST.get('mobile').upper()
    from_state = request.POST.get('from_state').upper()
    VehicleType = request.POST.get('VehicleType').upper()
    VehicleClass = request.POST.get('VehicleClass').upper()
    ServiceType = request.POST.get('ServiceType').upper()
    seating_c = request.POST.get('seating_c')
    txt_sleeper_cap = request.POST.get('txt_sleeper_cap')
    TaxMode = request.POST.get('TaxMode').upper()
    districtname = request.POST.get('districtname').upper()
    checkpost = request.POST.get('checkpost').upper()
    tax_from = request.POST.get('tax_from')
    tax_upto = request.POST.get('tax_upto')
    total_tax_amount = request.POST.get('total_tax_amount')
    service_amount = request.POST.get('service_amount')
    grand_tottal = int(service_amount) + int(total_tax_amount)
    total_amt_text = number_to_text(int(grand_tottal)).upper()
    payment_date = getdatetime()
    recipt_no = getrecipt()
    decoded_payload = jwt.decode(token, secrete, algorithms=["HS256"])
    username = decoded_payload.get("username")
    password = decoded_payload.get("password")
    user_uuid = user_custom.objects.filter(username = username,password=password).values("user_uuid")[0].get('user_uuid')
    data = add_maharashtra(recipt_no=recipt_no,grand_tottal=grand_tottal,created_username = user_uuid,vehicleno = vehicleno,chassisno = chassisno,ownername = ownername,mobile = mobile,from_state=from_state,VehicleType=VehicleType,VehicleClass=VehicleClass,ServiceType=ServiceType,seating_c=seating_c,txt_sleeper_cap=txt_sleeper_cap,TaxMode=TaxMode,districtname=districtname,checkpost=checkpost,tax_from=tax_from,tax_upto=tax_upto,total_tax_amount=total_tax_amount,service_amount=service_amount,create_date = payment_date,total_amt_text=total_amt_text)
    data.save()
    send_sms(mobile,tax_from,tax_upto,payment_date,total_tax_amount,vehicleno)
    id = data.id
    return redirect('maharashtra_recipt'+'/'+str(id))
    
def maharashtra_recipt(request,id):
    get_data = add_maharashtra.objects.filter(id=id).values('recipt_no','grand_tottal','created_username','vehicleno','chassisno','ownername','mobile','from_state','VehicleType','VehicleClass','ServiceType','seating_c','txt_sleeper_cap','TaxMode','districtname','checkpost','tax_from','tax_upto','total_tax_amount','service_amount','create_date','total_amt_text')
    qr_code = qrcode.make(mysite+'/maharashtra_scan/'+id)
    id_str = str(id)
    qr_code.save('./media/qrcode/Maharashtra/'+id_str+'.png')
    return render(request,'Maharashtra/maharashtra-pdf.html',{'data':get_data[0],'qr_code':id})

def maharashtra_scan(request,id):
    get_data = add_maharashtra.objects.filter(id=id).values('recipt_no','grand_tottal','created_username','vehicleno','chassisno','ownername','mobile','from_state','VehicleType','VehicleClass','ServiceType','seating_c','txt_sleeper_cap','TaxMode','districtname','checkpost','tax_from','tax_upto','total_tax_amount','service_amount','create_date','total_amt_text')
    return render(request,'Maharashtra/maharashtra-pdf.html',{'data':get_data[0]})


def tamilnadu_data(request):
     token = request.COOKIES.get('token')
     vehicleno =  request.POST.get('vehicleno')
     chassisno =  request.POST.get('chassisno')
     ownername =  request.POST.get('ownername')
     mobile =  request.POST.get('mobile')
     from_state = request.POST.get('from_state')
     VehicleType = request.POST.get('VehicleType')
     VehicleClass = request.POST.get('VehicleClass')
     recipt_no = request.POST.get('recipt_no')
     PermitType = request.POST.get('PermitType')
     issuing_authority = request.POST.get('issuing_authority')
     txt_seat_cap = request.POST.get('txt_seat_cap')
     txt_sleeper_cap = request.POST.get('txt_sleeper_cap')
     Extra_seat_cap = request.POST.get('Extra_seat_cap')
     ins_validity_input = request.POST.get('ins_validity_input')
     fitness_valid_input = request.POST.get('fitness_valid_input')
     pucc_validity_input = request.POST.get('pucc_validity_input')
     TaxMode = request.POST.get('TaxMode')
     txt_permit_auth_no = request.POST.get('txt_permit_auth_no')
     permit_authorization_vali = request.POST.get('permit_authorization_vali')
     Greentax = request.POST.get('Greentax')
     regn_date = request.POST.get('regn_date')
     districtname = request.POST.get('districtname')
     permit_upto_input = request.POST.get('permit_upto_input')
     cal_tax_from_input = request.POST.get('cal_tax_from_input')
     cal_tax_to_input = request.POST.get('cal_tax_to_input')
     checkpost_name = request.POST.get('checkpost_name')
     txt_permit_no = request.POST.get('txt_permit_no')
     total_tax_amount = request.POST.get('total_tax_amount')
     mv_tax = request.POST.get('mv_tax')
     serviceusercharge = request.POST.get('serviceusercharge')
     welfaretax = request.POST.get('welfaretax')
     permitfree = request.POST.get('permitfree')
     payment_date = getdatetime()
     total_amt_text = number_to_text(total_tax_amount)
     decoded_payload = jwt.decode(token, secrete, algorithms=["HS256"])
     username = decoded_payload.get("username")
     password = decoded_payload.get("password")
     user_uuid = user_custom.objects.filter(username = username,password=password).values("user_uuid")[0].get('user_uuid')
     data = add_tamilnadu(created_username = user_uuid,vehicleno =  vehicleno,chassisno =  chassisno,ownername =  ownername,mobile =  mobile,from_state = from_state,VehicleType = VehicleType,VehicleClass = VehicleClass,recipt_no = recipt_no,PermitType = PermitType,issuing_authority = issuing_authority,txt_seat_cap = txt_seat_cap,txt_sleeper_cap = txt_sleeper_cap,Extra_seat_cap = Extra_seat_cap,ins_validity_input = ins_validity_input,fitness_valid_input = fitness_valid_input,pucc_validity_input = pucc_validity_input,TaxMode = TaxMode,txt_permit_auth_no = txt_permit_auth_no,permit_authorization_vali = permit_authorization_vali,Greentax = Greentax,regn_date = regn_date,districtname = districtname,permit_upto_input = permit_upto_input,cal_tax_from_input = cal_tax_from_input,cal_tax_to_input = cal_tax_to_input,checkpost_name = checkpost_name,txt_permit_no = txt_permit_no,total_tax_amount = total_tax_amount,mv_tax = mv_tax,serviceusercharge = serviceusercharge,welfaretax = welfaretax,permitfree = permitfree,create_date = payment_date,total_amt_text=total_amt_text)
     send_sms(mobile,cal_tax_from_input,cal_tax_to_input,payment_date,total_tax_amount,vehicleno)
     data.save()
     id = data.id
     return redirect('tamilnadu_recipt'+'/'+str(id))

     
def tamilnadiu_recipt(request,id):
    get_data = add_tamilnadu.objects.filter(id=id).values('created_username' ,'vehicleno' ,'chassisno','ownername','mobile' ,'from_state','VehicleType','VehicleClass','recipt_no','PermitType','issuing_authority','txt_seat_cap','txt_sleeper_cap','Extra_seat_cap','ins_validity_input','fitness_valid_input','pucc_validity_input','TaxMode','txt_permit_auth_no','permit_authorization_vali','Greentax','regn_date','districtname','permit_upto_input','cal_tax_from_input','cal_tax_to_input','checkpost_name','txt_permit_no','total_tax_amount','mv_tax','serviceusercharge','welfaretax','permitfree','create_date','total_amt_text')
    qr_code = qrcode.make(mysite+'/tamilnadu_scan/'+id)
    id_str = str(id)
    qr_code.save('./media/qrcode/tamilnadu/'+id_str+'.png')
    return render(request,'Tamilnadu/TamilNAduRecipt.html',{'data':get_data[0],'qr_code':id})

def tamilnadiu_scan(request,id):
    get_data = add_tamilnadu.objects.filter(id=id).values('created_username' ,'vehicleno' ,'chassisno','ownername','mobile' ,'from_state','VehicleType','VehicleClass','recipt_no','PermitType','issuing_authority','txt_seat_cap','txt_sleeper_cap','Extra_seat_cap','ins_validity_input','fitness_valid_input','pucc_validity_input','TaxMode','txt_permit_auth_no','permit_authorization_vali','Greentax','regn_date','districtname','permit_upto_input','cal_tax_from_input','cal_tax_to_input','checkpost_name','txt_permit_no','total_tax_amount','mv_tax','serviceusercharge','welfaretax','permitfree','create_date','total_amt_text')
    return render(request,'Tamilnadu/TamilNAduRecipt.html',{'data':get_data[0]})


def tripura_data(request):
    token = request.COOKIES.get('token')
    vehicle = request.POST.get('vehicle')
    chassis = request.POST.get('chassis')
    owner = request.POST.get('owner')
    mobileno = request.POST.get('mobileno')
    statename = request.POST.get('statename')
    vehicleType = request.POST.get('vehicleType')
    vehicleClass = request.POST.get('vehicleClass')
    grossWeight = request.POST.get('grossWeight')
    district = request.POST.get('district')
    barrier = request.POST.get('barrier')
    payment_mode = request.POST.get('cmb_payment_mode_input')
    cal_tax_from_input = request.POST.get('cal_tax_from_input')
    cal_tax_to_input = request.POST.get('cal_tax_to_input')
    mv_tax = int(request.POST.get('mv_amount'))
    Service_charge = int(request.POST.get('surcharge'))
    tax_tottal_int = mv_tax + Service_charge
    text_amt = number_to_text(tax_tottal_int)
    payment_date = getdatetime()
    datetime_main = str(datetime.now())
    date_month_year = datetime_main[slice(10)]
    date = date_month_year[slice(8,10)]
    month = date_month_year[slice(5,-3)]
    year = date_month_year[slice(4)]
    recipt_no = "TR"+str(year)+str(month)+str(date)
    decoded_payload = jwt.decode(token, secrete, algorithms=["HS256"])
    username = decoded_payload.get("username")
    password = decoded_payload.get("password")
    user_uuid = user_custom.objects.filter(username = username,password=password).values("user_uuid")[0].get('user_uuid')
    data = add_tripura(recipt_no = recipt_no,created_user = user_uuid ,vehicle = vehicle ,chassis = chassis ,owner = owner ,mobileno = mobileno ,statename = statename ,vehicleType = vehicleType ,vehicleClass = vehicleClass ,grossWeight = grossWeight,district = district ,barrier = barrier ,payment_mode = payment_mode ,cal_tax_from_input = cal_tax_from_input ,cal_tax_to_input = cal_tax_to_input ,mv_tax = mv_tax,Service_charge = Service_charge,total_tax_amount = tax_tottal_int ,text_amt  = text_amt,payment_date = payment_date )
    data.save()
    send_sms(mobileno,cal_tax_from_input,cal_tax_to_input,payment_date,tax_tottal_int,vehicle)
    return redirect('tripura_recipt'+'/'+str(data.id))

def tripura_recipt(request,id):
    get_data = add_tripura.objects.filter(id=id).values('vehicle','vehicleClass','chassis','owner','mobileno','statename','vehicleType','vehicleClass','grossWeight','district','barrier','payment_mode','cal_tax_from_input','cal_tax_to_input','total_tax_amount','mv_tax','Service_charge','payment_date','recipt_no','text_amt')
    qr_code = qrcode.make(mysite+'/tripura_scan/'+str(id))
    id_str = str(id)
    qr_code.save('./media/qrcode/tripura/'+id_str+'.png')
    return render(request,'Tripura/tripura-pdf.html',{'data':get_data[0],'qr_code':id})
    

def uttarpradesh_data(request):
    token =  request.COOKIES.get('token')
    vehicleno =    request.POST.get('vehicleno').upper()
    chassisno =    request.POST.get('chassisno').upper()
    ownername =    request.POST.get('ownername').upper()
    mobile =    request.POST.get('mobile').upper()
    from_state =   request.POST.get('from_state').upper()
    VehicleType =   request.POST.get('VehicleType').upper()
    VehicleClass =   request.POST.get('VehicleClass').upper()
    seating_c =   request.POST.get('seating_c').upper()
    txt_sleeper_cap =   request.POST.get('txt_sleeper_cap').upper()
    ServiceType =   request.POST.get('ServiceType').upper()
    TaxMode =   request.POST.get('TaxMode').upper()
    border_entry =   request.POST.get('border_entry').upper()
    tax_from =   request.POST.get('tax_from')
    tax_upto =   request.POST.get('tax_upto')
    PermitType =   request.POST.get('PermitType').upper()
    permit_upto =   request.POST.get('permit_upto').upper()
    permit_no =   request.POST.get('permit_no').upper()
    total_tax_amount =   int(request.POST.get('total_tax_amount'))
    payment_date = getdatetime()
    total_amt_text = number_to_text(total_tax_amount).upper()
    recipt_no = getrecipt()
    decoded_payload = jwt.decode(token, secrete, algorithms=["HS256"])
    username = decoded_payload.get("username")
    password = decoded_payload.get("password")
    user_uuid = user_custom.objects.filter(username = username,password=password).values("user_uuid")[0].get('user_uuid')
    data = add_uttarpradesh(recipt_no = recipt_no,created_username  = token,vehicleno  =   vehicleno,chassisno  =   chassisno,ownername  =   ownername,mobile  =   mobile,from_state =  from_state,VehicleType =  VehicleType,VehicleClass =  VehicleClass,seating_c =  seating_c,txt_sleeper_cap =  txt_sleeper_cap,ServiceType =  ServiceType,TaxMode =  TaxMode,border_entry =  border_entry,tax_from =  tax_from,tax_upto =  tax_upto,PermitType =  PermitType,permit_upto =  permit_upto,permit_no =  permit_no,total_tax_amount =  total_tax_amount,payment_date = payment_date,total_amt_text=total_amt_text)
    data.save()
    send_sms(mobile,tax_from,tax_upto,payment_date,total_tax_amount,vehicleno)
    id = data.id
    return redirect('uttarpradesh_recipt'+'/'+str(id))

    
def uttarpradesh_recipt(request,id):
    get_data = add_uttarpradesh.objects.filter(id=id).values('recipt_no','created_username','vehicleno','chassisno','ownername','mobile','from_state','VehicleType','VehicleClass','seating_c','txt_sleeper_cap','ServiceType','TaxMode','border_entry','tax_from','tax_upto','PermitType','permit_upto','permit_no','total_tax_amount','payment_date','total_amt_text','payment_date')
    qr_code = qrcode.make(mysite+'/uttarpradesh_scan/'+id)
    id_str = str(id)
    qr_code.save('./media/qrcode/uttarpradesh/'+id_str+'.png')
    return render(request,'Uttarpradesh/uttar-pradesh-pdf.html',{'data':get_data[0],'qr_code':id})

def uttarpradesh_scan(request,id):
    get_data = add_uttarpradesh.objects.filter(id=id).values('recipt_no','created_username','vehicleno','chassisno','ownername','mobile','from_state','VehicleType','VehicleClass','seating_c','txt_sleeper_cap','ServiceType','TaxMode','border_entry','tax_from','tax_upto','PermitType','permit_upto','permit_no','total_tax_amount','payment_date','total_amt_text')
    return render(request,'Uttarpradesh/uttar-pradesh-pdf.html',{'data':get_data[0]})

def uttrakhand_data(request):
    token =   request.COOKIES.get('token')
    vehicleno =   request.POST.get('vehicleno').upper()
    chassisno =   request.POST.get('chassisno').upper()
    ownername =   request.POST.get('ownername').upper()
    mobile =   request.POST.get('mobile')
    from_state =  request.POST.get('from_state').upper()
    VehicleType =  request.POST.get('VehicleType').upper()
    VehicleClass =  request.POST.get('VehicleClass').upper()
    seating_c =  request.POST.get('seating_c')
    txt_sleeper_cap =  request.POST.get('txt_sleeper_cap')
    ServiceType =  request.POST.get('ServiceType').upper()
    TaxMode =  request.POST.get('TaxMode').upper()
    border_entry =  request.POST.get('border_entry').upper()
    tax_from =  request.POST.get('tax_from')
    tax_upto =  request.POST.get('tax_upto')
    PermitType =  request.POST.get('PermitType').upper()
    permit_upto =  request.POST.get('permit_upto')
    permit_no =  request.POST.get('permit_no').upper()
    districtname =  request.POST.get('districtname').upper()
    fitdate =  request.POST.get('fitdate')
    permit_from =  request.POST.get('permit_from')
    txt_no_of_weeks =  request.POST.get('txt_no_of_weeks')
    total_tax_amount =  request.POST.get('total_tax_amount')
    service_amount =  request.POST.get('service_amount')
    civik_amount =  request.POST.get('civik_amount')
    payment_date = getdatetime()
    recipt_no = getrecipt()
    grand_tottal = int(total_tax_amount) + int(civik_amount) +int(service_amount)
    total_amt_text = number_to_text(grand_tottal).upper()
    decoded_payload = jwt.decode(token, secrete, algorithms=["HS256"])
    username = decoded_payload.get("username")
    password = decoded_payload.get("password")
    user_uuid = user_custom.objects.filter(username = username,password=password).values("user_uuid")[0].get('user_uuid')
    data = add_uttrakhand(grand_tottal=grand_tottal,recipt_no=recipt_no,created_username =  user_uuid,vehicleno =   vehicleno,chassisno =   chassisno,ownername =   ownername,mobile =   mobile,from_state =  from_state,VehicleType =  VehicleType,VehicleClass =  VehicleClass,seating_c =  seating_c,txt_sleeper_cap =  txt_sleeper_cap,ServiceType =  ServiceType,TaxMode =  TaxMode,border_entry =  border_entry,tax_from =  tax_from,tax_upto =  tax_upto,PermitType =  PermitType,permit_upto =  permit_upto,permit_no =  permit_no,districtname =  districtname,fitdate =  fitdate,permit_from =  permit_from,txt_no_of_weeks =  txt_no_of_weeks,total_tax_amount =  total_tax_amount,service_amount =  service_amount,civik_amount =  civik_amount,payment_date = payment_date,total_amt_text=total_amt_text)
    data.save()
    send_sms(mobile,tax_from,tax_upto,payment_date,total_tax_amount,vehicleno)
    id = data.id
    return redirect('uttrakhand_recipt'+'/'+str(id))


def uttrakhand_recipt(request,id):
    get_data = add_uttrakhand.objects.filter(id=id).values('grand_tottal','created_username','vehicleno','chassisno','ownername','mobile','from_state','VehicleType','VehicleClass','seating_c','txt_sleeper_cap','ServiceType','TaxMode','border_entry','tax_from','tax_upto','PermitType','permit_upto','permit_no','districtname','fitdate','permit_from','txt_no_of_weeks','total_tax_amount','service_amount','civik_amount','payment_date','total_amt_text','recipt_no')
    qr_code = qrcode.make(mysite+'/uttrakhand_scan/'+id)
    id_str = str(id)
    qr_code.save('./media/qrcode/Uttrakhand/'+id_str+'.png')
    return render(request,'Uttrakhand/uttrakhand-pdf.html',{'data':get_data[0],'qr_code':id})

def uttrakhand_scan(request,id):
    get_data = add_uttrakhand.objects.filter(id=id).values('grand_tottal','created_username','vehicleno','chassisno','ownername','mobile','from_state','VehicleType','VehicleClass','seating_c','txt_sleeper_cap','ServiceType','TaxMode','border_entry','tax_from','tax_upto','PermitType','permit_upto','permit_no','districtname','fitdate','permit_from','txt_no_of_weeks','total_tax_amount','service_amount','civik_amount','payment_date','total_amt_text','recipt_no')
    return render(request,'Uttrakhand/uttrakhand-pdf.html',{'data':get_data[0]})

def all_recipt_history(request,statename):
    token = request.COOKIES.get('token')
    decoded_payload = jwt.decode(token, secrete, algorithms=["HS256"])
    username = decoded_payload.get("username")
    password = decoded_payload.get("password")
    user_id = user_custom.objects.filter(username = username,password=password).values("user_uuid")[0].get('user_uuid')
    if (statename == "rajasthan"):
        if (verify_user(user_id)):
            data = add_rajasthan.objects.filter(user_name=user_id).values("vehicleno","total_tax_amount","chassisno","mobile","from_state","ownername","id")
            return render(request,'Haryana/haryanaview.html',{"data":data,"state_name":statename,"site_url":"rajasthan_recipt"})
        else:
            return redirect('login')
    elif(statename == "gujrat"):
        
        if (verify_user(user_id)):
            data = add_gujrat.objects.filter(created_username=user_id).values("id","vehicleno","total_tax_amount","chassisno","mobile","from_state")
            return render(request,'Haryana/haryanaview.html',{"data":data,"sate_name":statename,"site_url":"gujrat_recipt"})
    elif(statename == "bihar"):
        
        if (verify_user(user_id)):
            data = add_bihar.objects.filter(created_username=user_id).values("id","vehicle","tax_total","chassis_no","owner_mobile","from_state")
            return render(request,'Haryana/haryanaview.html',{"data":data,"sate_name":statename,"site_url":"bihar_recipt"})
    elif(statename == "gujrat_odc"):
        
        if (verify_user(user_id)):
            data = add_gujrat_odc.objects.filter(created_user=user_id).values("id","vehicle","total_tax_amount","chassis","mobileno","state_from")
            # return render(request,'Haryana/haryanaview.html',{"data":data,"sate_name":statename,"site_url":"gujrat_odc_recipt"})
            return HttpResponse("this site is under devlopment")
    elif(statename == "haryana"):
        
        if (verify_user(user_id)):
            data = add_haryana.objects.filter(created_username=user_id).values("id","vehicleno","total_amount","chassisno","mobile","from_state")
            return render(request,'Haryana/haryanaview.html',{"data":data,"sate_name":statename,"site_url":"gujrat_recipt"})
    elif(statename == "himachalpradesh"):
        
        if (verify_user(user_id)):
            data = add_himachal.objects.filter(created_username=user_id).values("id","vehicleno","total_tax_amount","chassisno","mobile","from_state")
            return render(request,'Haryana/haryanaview.html',{"data":data,"sate_name":statename,"site_url":"himachal_recipt"})
    elif(statename == "jharkhand"):
        
        if (verify_user(user_id)):
            data = add_jharkhand.objects.filter(created_username=user_id).values("id","vehicleno","total_tax_amount","chassisno","mobile","from_state")
            return render(request,'Haryana/haryanaview.html',{"data":data,"sate_name":statename,"site_url":"jharkhand_recipt"})
    elif(statename == "karnatka"):
        
        if (verify_user(user_id)):
            data = add_karnataka.objects.filter(created_username = user_id).values("id","vehicleno","total_tax_amount","chassisno","mobile","from_state")
            return render(request,'Haryana/haryanaview.html',{"data":data,"sate_name":statename,"site_url":"karnataka_recipt"})
    elif(statename == "madhyapradesh"):
        
        if (verify_user(user_id)):
            data = add_madhyapradesh.objects.filter(created_username=user_id).values("id","vehicleno","total_tax_amount","mobile","from_state")
            return render(request,'Haryana/haryanaview.html',{"data":data,"sate_name":statename,"site_url":"madhyapradesh_recipt"})
    elif(statename == "maharashtra"):
        
        if (verify_user(user_id)):
            data = add_maharashtra.objects.filter(created_username=user_id).values("id","vehicleno","total_tax_amount","chassisno","mobile","from_state")
            return render(request,'Haryana/haryanaview.html',{"data":data,"sate_name":statename,"site_url":"maharashtra_recipt"})
    elif(statename == "punjab"):
        
        if (verify_user(user_id)):
            data = add_punjab.objects.filter(user_name=user_id).values("id","vehicleno","chassisno","mobile","from_state","total_amount")
            return render(request,'Haryana/haryanaview.html',{"data":data,"sate_name":statename,"site_url":"punjab_recipt"})
    elif(statename == "tamilnadu"):
        
        if (verify_user(user_id)):
            data = add_tamilnadu.objects.filter(created_username=user_id).values("id","vehicleno","chassisno","mobile","from_state","total_tax_amount")
            return render(request,'Haryana/haryanaview.html',{"data":data,"sate_name":statename,"site_url":"tamilnadu_recipt"})
    elif(statename == "uttarpradesh"):
        
        if (verify_user(user_id)):
            data = add_uttarpradesh.objects.filter(created_username=user_id).values("id","vehicleno","chassisno","mobile","from_state","total_tax_amount")
            return render(request,'Haryana/haryanaview.html',{"data":data,"sate_name":statename,"site_url":"uttarpradesh_recipt"})
    elif(statename == "uttrakhand"):
        
        if (verify_user(user_id)):
            data = add_uttrakhand.objects.filter(created_username=user_id).values("id","vehicleno","chassisno","mobile","from_state","total_tax_amount")
            return render(request,'Haryana/haryanaview.html',{"data":data,"sate_name":statename,"site_url":"maharashtra_recipt"})
    elif(statename == "tripura"):
        
        if (verify_user(user_id)):
            data = add_tripura.objects.filter(created_user=user_id).values("id","vehicle","chassis","mobileno","statename","total_tax_amount")
            # return render(request,'Haryana/haryanaview.html',{"data":data,"sate_name":statename,"site_url":"maharashtra_recipt"})
            return HttpResponse("this page is under devlopment")
    else:
        return HttpResponse("invalid state")
    
def logout_admin(request):
    request.session['useruuid'] = 'none'
    return redirect('/')