from rest_framework.decorators import api_view
from vhaanmain.models import *
from .serializers import *
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

@api_view(['POST'])
def senddata(request):
    vechile = request.data['vehicle']
    find_raj = add_rajasthan.objects.filter(vehicleno = vechile).exists()
    print("Faild on line 13")
    find_UP = add_uttarpradesh.objects.filter(vehicleno = vechile).exists()
    print("Faild on line 15")
    find_GUJ = add_gujrat.objects.filter(vehicleno = vechile).exists()
    print("Faild on line 17")
    find_Himachal = add_himachal.objects.filter(vehicleno = vechile).exists()
    print("Faild on line 19")
    find_Bihar = add_bihar.objects.filter(vehicle = vechile).exists()
    find_Jhark = add_jharkhand.objects.filter(vehicle = vechile).exists()
    print("Faild on line 23")
    find_Har = add_haryana.objects.filter(vehicleno = vechile).exists()
    print("Faild on line 25")
    find_Maharashtra = add_maharashtra.objects.filter(vehicleno = vechile).exists()
    print("Faild on line 27")
    find_MadhyaPradesh = add_madhyapradesh.objects.filter(vehicleno = vechile).exists()
    print("Faild on line 29")
    find_punjab = add_punjab.objects.filter(vehicleno = vechile).exists()
    print("Faild on line 31")
    find_kar = add_karnataka.objects.filter(vehicleno = vechile).exists()
    print("Faild on line 33")
    find_tripura = add_tripura.objects.filter(vehicle = vechile).exists()
    print("Faild on line 34")
    find_UK = add_uttrakhand.objects.filter(vehicleno = vechile).exists()
    print("Faild on line 37")
    find_tamilnadu = add_tamilnadu.objects.filter(vehicleno = vechile).exists()
    print("Faild on line 39")
    if (find_raj):
            vechile_info = add_rajasthan.objects.filter(vehicleno = vechile).values('vehicleno','chassisno','ownername','mobile','from_state','VehicleType','VehicleClass','seating_c','txt_sleeper_cap','PermitType')
            data = vechileInfo_serializer_raj(vechile_info,many = True)
            return Response({"status":200,"payload":data.data})
    elif (find_UP):
            vechile_info = add_uttarpradesh.objects.filter(vehicleno = vechile).values('vehicleno','chassisno','ownername','mobile','from_state','VehicleType','VehicleClass','seating_c','txt_sleeper_cap','PermitType')
            data = vechileInfo_serializer_up(vechile_info,many = True)
            return Response({"status":200,"payload":data.data})
    elif (find_GUJ):
            vechile_info = add_gujrat.objects.filter(vehicleno = vechile).values('vehicleno','chassisno','ownername','mobile','from_state','VehicleType','VehicleClass','seating_c','txt_sleeper_cap','PermitType')
            data = vechileInfo_serializer_Guj(vechile_info,many = True)
            return Response({"status":200,"payload":data.data})        
    elif (find_Himachal):
            vechile_info = add_himachal.objects.filter(vehicleno = vechile).values('vehicleno','chassisno','ownername','mobile','from_state','VehicleType','VehicleClass','seating_c','txt_sleeper_cap','PermitType')
            data = vechileInfo_serializer_Himachal(vechile_info,many = True)
            return Response({"status":200,"payload":data.data})        
    elif (find_Bihar):
            vechile_info = add_bihar.objects.filter(vehicleno = vechile).values('vehicleno','chassisno','ownername','mobile','from_state','VehicleType','VehicleClass','seating_c','txt_sleeper_cap','PermitType')
            data = vechileInfo_serializer_Himachal(vechile_info,many = True)
            return Response({"status":200,"payload":data.data})        
    elif (find_Jhark):
            vechile_info = add_jharkhand.objects.filter(vehicleno = vechile).values('vehicleno','chassisno','ownername','mobile','from_state','VehicleType','VehicleClass','seating_c','txt_sleeper_cap','PermitType')
            data = vechileInfo_serializer_Jhar(vechile_info,many = True)
            return Response({"status":200,"payload":data.data})        
    elif (find_Har):
            vechile_info = add_haryana.objects.filter(vehicleno = vechile).values('vehicleno','chassisno','ownername','mobile','from_state','VehicleType','VehicleClass','seating_c','txt_sleeper_cap','PermitType')
            data = vechileInfo_serializer_har(vechile_info,many = True)
            return Response({"status":200,"payload":data.data})        
    elif (find_Maharashtra):
            vechile_info = add_maharashtra.objects.filter(vehicleno = vechile).values('vehicleno','chassisno','ownername','mobile','from_state','VehicleType','VehicleClass','seating_c','txt_sleeper_cap','PermitType')
            data = vechileInfo_serializer_Maharshtra(vechile_info,many = True)
            return Response({"status":200,"payload":data.data})        
    elif (find_MadhyaPradesh):
            vechile_info = add_madhyapradesh.objects.filter(vehicleno = vechile).values('vehicleno','chassisno','ownername','mobile','from_state','VehicleType','VehicleClass','seating_c','txt_sleeper_cap','PermitType')
            data = vechileInfo_serializer_MadhyaPradesh(vechile_info,many = True)
            return Response({"status":200,"payload":data.data})        
    elif (find_punjab):
            vechile_info = add_punjab.objects.filter(vehicleno = vechile).values('vehicleno','chassisno','ownername','mobile','from_state','VehicleType','VehicleClass','seating_c','txt_sleeper_cap','PermitType')
            data = vechileInfo_serializer_Punjab(vechile_info,many = True)
            return Response({"status":200,"payload":data.data})        
    elif (find_kar):
            vechile_info = add_karnataka.objects.filter(vehicleno = vechile).values('vehicleno','chassisno','ownername','mobile','from_state','VehicleType','VehicleClass','seating_c','txt_sleeper_cap','PermitType')
            data = vechileInfo_serializer_Karnatka(vechile_info,many = True)
            return Response({"status":200,"payload":data.data})        
    elif (find_tripura):
            vechile_info = add_tripura.objects.filter(vehicle = vechile).values('vehicleno','chassisno','ownername','mobile','from_state','VehicleType','VehicleClass','seating_c','txt_sleeper_cap','PermitType')
            data = vechileInfo_serializer_Tripura(vechile_info,many = True)
            return Response({"status":200,"payload":data.data})        
    elif (find_UK):
            vechile_info = add_uttrakhand.objects.filter(vehicleno = vechile).values('vehicleno','chassisno','ownername','mobile','from_state','VehicleType','VehicleClass','seating_c','txt_sleeper_cap','PermitType')
            data = vechileInfo_serializer_Uk(vechile_info,many = True)
            return Response({"status":200,"payload":data.data})        
    elif (find_tamilnadu):
            vechile_info = add_tamilnadu.objects.filter(vehicleno = vechile).values('vehicleno','chassisno','ownername','mobile','from_state','VehicleType','VehicleClass','seating_c','txt_sleeper_cap','PermitType')
            data = vechileInfo_serializer_Tamilnadu(vechile_info,many = True)
            return Response({"status":200,"payload":data.data})        
    else:
        return Response({"status":200,"payload":"vechile never registerd"})