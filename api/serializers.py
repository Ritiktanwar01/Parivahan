from rest_framework.serializers import ModelSerializer
from vhaanmain.models import *

class vechileInfo_serializer_raj(ModelSerializer):
    class Meta():
        model = add_rajasthan
        fields = ['vehicleno','chassisno','ownername','mobile','from_state','VehicleType','VehicleClass','seating_c','txt_sleeper_cap','PermitType']

class vechileInfo_serializer_up(ModelSerializer):
    class Meta():
        model = add_uttarpradesh
        fields = ['vehicleno','chassisno','ownername','mobile','from_state','VehicleType','VehicleClass','seating_c','txt_sleeper_cap','PermitType']

class vechileInfo_serializer_bihar(ModelSerializer):
    class Meta():
        model = add_bihar
        fields = ['vehicleno','chassisno','ownername','mobile','from_state','VehicleType','VehicleClass','seating_c','txt_sleeper_cap','PermitType']

class vechileInfo_serializer_Uk(ModelSerializer):
    class Meta():
        model = add_uttrakhand
        fields = ['vehicleno','chassisno','ownername','mobile','from_state','VehicleType','VehicleClass','seating_c','txt_sleeper_cap','PermitType']

class vechileInfo_serializer_Himachal(ModelSerializer):
    class Meta():
        model = add_himachal
        fields = ['vehicleno','chassisno','ownername','mobile','from_state','VehicleType','VehicleClass','seating_c','txt_sleeper_cap','PermitType']

class vechileInfo_serializer_Himachal(ModelSerializer):
    class Meta():
        model = add_himachal
        fields = ['vehicleno','chassisno','ownername','mobile','from_state','VehicleType','VehicleClass','seating_c','txt_sleeper_cap','PermitType']

class vechileInfo_serializer_Guj(ModelSerializer):
    class Meta():
        model = add_gujrat
        fields = ['vehicleno','chassisno','ownername','mobile','from_state','VehicleType','VehicleClass','seating_c','txt_sleeper_cap','PermitType']

class vechileInfo_serializer_Jhar(ModelSerializer):
    class Meta():
        model = add_jharkhand
        fields = ['vehicleno','chassisno','ownername','mobile','from_state','VehicleType','VehicleClass','seating_c','txt_sleeper_cap','PermitType']

class vechileInfo_serializer_har(ModelSerializer):
    class Meta():
        model = add_haryana
        fields = ['vehicleno','chassisno','ownername','mobile','from_state','VehicleType','VehicleClass','seating_c','txt_sleeper_cap','PermitType']

class vechileInfo_serializer_Karnatka(ModelSerializer):
    class Meta():
        model = add_karnataka
        fields = ['vehicleno','chassisno','ownername','mobile','from_state','VehicleType','VehicleClass','seating_c','txt_sleeper_cap','PermitType']

class vechileInfo_serializer_MadhyaPradesh(ModelSerializer):
    class Meta():
        model = add_madhyapradesh
        fields = ['vehicleno','chassisno','ownername','mobile','from_state','VehicleType','VehicleClass','seating_c','txt_sleeper_cap','PermitType']

class vechileInfo_serializer_Punjab(ModelSerializer):
    class Meta():
        model = add_punjab
        fields = ['vehicleno','chassisno','ownername','mobile','from_state','VehicleType','VehicleClass','seating_c','txt_sleeper_cap','PermitType']

class vechileInfo_serializer_Maharshtra(ModelSerializer):
    class Meta():
        model = add_maharashtra
        fields = ['vehicleno','chassisno','ownername','mobile','from_state','VehicleType','VehicleClass','seating_c','txt_sleeper_cap','PermitType']

class vechileInfo_serializer_Tamilnadu(ModelSerializer):
    class Meta():
        model = add_tamilnadu
        fields = ['vehicleno','chassisno','ownername','mobile','from_state','VehicleType','VehicleClass','seating_c','txt_sleeper_cap','PermitType']

class vechileInfo_serializer_Tripura(ModelSerializer):
    class Meta():
        model = add_tripura
        fields = ['vehicleno','chassisno','ownername','mobile','from_state','VehicleType','VehicleClass','seating_c','txt_sleeper_cap','PermitType']
