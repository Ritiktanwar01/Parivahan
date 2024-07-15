from django.db import models
from uuid import uuid4

# this model class is initialised to save states availabe on this website
class statelists(models.Model):
    id = models.IntegerField(auto_created=True,primary_key=True,editable=False)
    state = models.CharField(max_length = 200)
    def __str__(self):
        return self.state
    
class user_custom(models.Model):
    id = models.IntegerField(primary_key=True,auto_created=True)
    username = models.CharField(max_length = 120)
    password = models.CharField(max_length = 20)
    created_by = models.CharField(max_length = 280,default = "null")
    user_uuid = models.CharField(default = uuid4,editable = False, max_length = 280)
    show = models.BooleanField(default=True)
    def __str__(self):
        return self.username

class stateassigned(models.Model):
    user_name = models.ForeignKey(user_custom,on_delete= models.CASCADE,null = True)
    state_name = models.ForeignKey(statelists,on_delete= models.CASCADE,null = True)
    
class add_rajasthan(models.Model):
        id = models.AutoField(primary_key=True) 
        user_name = models.CharField(max_length = 120)
        vehicleno  = models.CharField(max_length = 120)
        chassisno  = models.CharField(max_length = 120)
        ownername  = models.CharField(max_length = 120)
        mobile  = models.CharField(max_length = 120)
        from_state =models.CharField(max_length = 120)
        VehicleType =models.CharField(max_length = 120)
        VehicleClass =models.CharField(max_length = 120)
        seating_c =models.CharField(max_length = 120)
        txt_sleeper_cap =models.CharField(max_length = 120)
        PermitType =models.CharField(max_length = 120)
        border_entry =models.CharField(max_length = 120)
        checkpost_name =models.CharField(max_length = 120)
        TaxMode =models.CharField(max_length = 120)
        txt_no_of_weeks =models.CharField(max_length = 120)
        tax_from =models.CharField(max_length = 120)
        tax_upto =models.CharField(max_length = 120)
        total_tax_amount =models.CharField(max_length = 120)
        civik_amount =models.CharField(max_length = 120)
        service_amount =models.CharField(max_length = 120)
        sleeper_Cap_Weight =models.CharField(max_length = 120)
        counter_fee = models.CharField(max_length = 120)
        create_date =models.CharField(max_length = 120)
        recipt_no = models.CharField(max_length = 120)
        total_amt_text = models.CharField(max_length = 180,default = "nothing")

        def __str__(self):
            return self.vehicleno
        
        
class add_punjab(models.Model):
    id = models.AutoField(primary_key=True)
    user_name = models.CharField(max_length = 80,default="default")
    vehicleno = models.CharField(max_length = 80,default="default")
    chassisno = models.CharField(max_length = 80,default="default")
    ownername = models.CharField(max_length = 80,default="default")
    mobile = models.CharField(max_length = 80,default="default")
    from_state= models.CharField(max_length = 80,default="default")
    VehicleType= models.CharField(max_length = 80,default="default")
    VehicleClass= models.CharField(max_length = 80,default="default")
    SeatingOrWeight= models.CharField(max_length = 80,default="default")
    seatingOrLaden= models.CharField(max_length = 80,default="default")
    unldweightOrSleeper= models.CharField(max_length = 80,default="default")
    ServiceType= models.CharField(max_length = 80,default="default")
    TaxMode= models.CharField(max_length = 80,default="default")
    border_entry= models.CharField(max_length = 80,default="default")
    districtname= models.CharField(max_length = 80,default="default")
    entrydate= models.CharField(max_length = 80,default="default")
    outdate= models.CharField(max_length = 80,default="default")
    total_amount= models.CharField(max_length = 80,default="default")
    usercharge= models.CharField(max_length = 80,default="default")
    infracess= models.CharField(max_length = 80,default="default")
    create_date= models.CharField(max_length = 80,default="default")
    recipt_no= models.CharField(max_length = 80,default="default")
    mv_tax= models.CharField(max_length = 80,default = 80)
    total_amt_text = models.CharField(max_length = 180,default = "nothing")
    
    def __str__(self):
        return self.vehicleno
    
    
class add_haryana(models.Model):
    id = models.AutoField(primary_key=True)
    created_username = models.CharField(max_length = 80,null = True)
    vehicleno = models.CharField(max_length = 80,null = True)
    chassisno = models.CharField(max_length = 80,null = True)
    ownername = models.CharField(max_length = 80,null = True)
    mobile = models.CharField(max_length = 80,null = True)
    from_state=models.CharField(max_length = 80,null = True)
    VehicleType=models.CharField(max_length = 80,null = True)
    VehicleClass=models.CharField(max_length = 80,null = True)
    seating_c=models.CharField(max_length = 80,null = True)
    ServiceType=models.CharField(max_length = 80,null = True)
    distance=models.CharField(max_length = 80,null = True)
    TaxMode=models.CharField(max_length = 80,null = True)
    border_entry=models.CharField(max_length = 80,null = True)
    entrydate=models.CharField(max_length = 80,null = True)
    outdate=models.CharField(max_length = 80,null = True)
    total_amount=models.CharField(max_length = 80,null = True)
    create_date = models.CharField(max_length = 80,null = True)
    total_amt_text = models.CharField(max_length = 180,default = "nothing")
    recipt_no = models.CharField(max_length=80,default="default")
    
    def __str__(self):
        return self.vehicleno
    
    
    
class add_bihar(models.Model):
    id = models.AutoField(primary_key=True)
    created_username = models.CharField(max_length = 80,default="default")
    vehicle = models.CharField(max_length = 80,default="default")
    chassis_no = models.CharField(max_length = 80,default="default")
    owner_name = models.CharField(max_length = 80,default="default")
    owner_mobile = models.CharField(max_length = 80,default="default")
    from_state=models.CharField(max_length = 80,default="default")
    vehicle_type=models.CharField(max_length = 80,default="default")
    vehicle_class=models.CharField(max_length = 80,default="default")
    permit_type=models.CharField(max_length = 80,default="default")
    sitting_capacity=models.CharField(max_length = 80,default="default")
    sleeper_capacity=models.CharField(max_length = 80,default="default")
    loading_capacity=models.CharField(max_length = 80,default="default")
    from_district=models.CharField(max_length = 80,default="default")
    payment_date=models.CharField(max_length = 80,default="default")
    barrier=models.CharField(max_length = 80,default="default")
    tax_mode=models.CharField(max_length = 80,default="default")
    tax_from=models.CharField(max_length = 80,default="default")
    tax_upto=models.CharField(max_length = 80,default="default")
    tax_total=models.CharField(max_length = 80,default="default")
    payment_mode=models.CharField(max_length = 80,default="default")
    client_name=models.CharField(max_length = 80,default="default")
    total_amt_text = models.CharField(max_length = 180,default = "nothing")
    recipt_no = models.CharField(max_length=80,default="none")
    
    def __str__(self):
        return self.vehicle
    
    
class add_gujrat(models.Model):
    id = models.AutoField(primary_key=True)
    created_username = models.CharField(max_length = 80,default="default")
    vehicleno = models.CharField(max_length = 80,default="default")
    chassisno = models.CharField(max_length = 80,default="default")
    ownername = models.CharField(max_length = 80,default="default")
    mobile = models.CharField(max_length = 80,default="default")
    from_state = models.CharField(max_length = 80,default="default")
    VehicleType = models.CharField(max_length = 80,default="default")
    VehicleClass = models.CharField(max_length = 80,default="default")
    ServiceType = models.CharField(max_length = 80,default="default")
    seating_c = models.CharField(max_length = 80,default="default")
    txt_sleeper_cap = models.CharField(max_length = 80,default="default")
    ownertype = models.CharField(max_length = 80,default="default")
    makerstatus = models.CharField(max_length = 80,default="default")
    ptype = models.CharField(max_length = 80,default="default")
    permit_upto = models.CharField(max_length = 80,default="default")
    TaxMode = models.CharField(max_length = 80,default="default")
    border_entry = models.CharField(max_length = 80,default="default")
    permit_no = models.CharField(max_length = 80,default="default")
    permit_ia = models.CharField(max_length = 80,default="default")
    tax_from = models.CharField(max_length = 80,default="default")
    tax_upto = models.CharField(max_length = 80,default="default")
    total_tax_amount = models.CharField(max_length = 80,default="default")
    payment_date = models.CharField(max_length = 80,default="default")
    total_tax_amount = models.CharField(max_length = 180,default = "nothing")
    recipt_no = models.CharField(max_length=80,default="none")
    total_amt_text = models.CharField(max_length=80,default="none")
    
    def __str__(self):
        return self.vehicleno
    
    
class add_gujrat_odc(models.Model):
    id = models.AutoField(primary_key=True)
    created_user = models.CharField(max_length = 280,default="default")
    vehicle = models.CharField(max_length = 80,default="default")
    chassis = models.CharField(max_length = 80,default="default")
    owner_type = models.CharField(max_length = 80,default="default")
    owner_name = models.CharField(max_length = 80,default="default")
    mobileno = models.CharField(max_length = 80,default="default")
    vehicle_type = models.CharField(max_length = 80,default="default")
    vehicle_class = models.CharField(max_length = 80,default="default")
    gross_wt = models.CharField(max_length = 80,default="default")
    unladen_wt = models.CharField(max_length = 80,default="default")
    body_type = models.CharField(max_length = 80,default="default")
    goods_nature_input = models.CharField(max_length = 80,default="default")
    over_dimension_input = models.CharField(max_length = 80,default="default")
    conHeight_input = models.CharField(max_length = 80,default="default")
    conWidth_input = models.CharField(max_length = 80,default="default")
    conLength_input = models.CharField(max_length = 80,default="default")
    permit_type_input = models.CharField(max_length = 80,default="default")
    txt_permit_no = models.CharField(max_length = 80,default="default")
    road_tax_val = models.CharField(max_length = 80,default="default")
    state_from = models.CharField(max_length = 80,default="default")
    district_input = models.CharField(max_length = 80,default="default")
    state_to = models.CharField(max_length = 80,default="default")
    to_district_input = models.CharField(max_length = 80,default="default")
    insurance_val = models.CharField(max_length = 80,default="default")
    fitness_val = models.CharField(max_length = 80,default="default")
    pucc_val = models.CharField(max_length = 80,default="default")
    permit_val = models.CharField(max_length = 80,default="default")
    lr_no = models.CharField(max_length = 80,default="default")
    lr_date = models.CharField(max_length = 80,default="default")
    goodd_description_input = models.CharField(max_length = 80,default="default")
    remarks = models.CharField(max_length = 80,default="default")
    total_tax_amount = models.CharField(max_length = 80,default="default")
    amount_text = models.CharField(max_length = 80,default="default")
    payment_date = models.CharField(max_length = 280,default="default")
    
    def __str__(self):
        return self.vehicle
    
    
class add_himachal(models.Model):
    id = models.AutoField(primary_key=True)
    created_username  = models.CharField(max_length = 80,default="default")
    vehicleno  = models.CharField(max_length = 80,default="default")
    chassisno  = models.CharField(max_length = 80,default="default")
    ownername  = models.CharField(max_length = 80,default="default")
    mobile  = models.CharField(max_length = 80,default="default")
    from_state =models.CharField(max_length = 80,default="default")
    VehicleType =models.CharField(max_length = 80,default="default")
    VehicleClass =models.CharField(max_length = 80,default="default")
    ServiceType =models.CharField(max_length = 80,default="default")
    seating_c =models.CharField(max_length = 80,default="default")
    border_entry =models.CharField(max_length = 80,default="default")
    TaxMode =models.CharField(max_length = 80,default="default")
    service_amount =models.CharField(max_length = 80,default="default")
    tax_from =models.CharField(max_length = 80,default="default")
    tax_upto =models.CharField(max_length = 80,default="default")
    total_tax_amount =models.CharField(max_length = 80,default="default")
    payment_date = models.CharField(max_length = 80,default="default")
    total_amt_text = models.CharField(max_length = 180,default = "nothing")
    recipt_no = models.CharField(max_length=70,default="default")
    
    def __str__(self):
        return self.vehicleno
    
class add_jharkhand(models.Model):
    id = models.AutoField(primary_key=True)
    created_username = models.CharField(max_length = 80,default="default")
    vehicleno = models.CharField(max_length = 80,default="default")
    chassisno = models.CharField(max_length = 80,default="default")
    ownername = models.CharField(max_length = 80,default="default")
    mobile = models.CharField(max_length = 80,default="default")
    from_state = models.CharField(max_length = 80,default="default")
    VehicleType = models.CharField(max_length = 80,default="default")
    VehicleClass = models.CharField(max_length = 80,default="default")
    PermitType = models.CharField(max_length = 80,default="default")
    seating_c = models.CharField(max_length = 80,default="default")
    border_entry = models.CharField(max_length = 80,default="default")
    TaxMode = models.CharField(max_length = 80,default="default")
    txt_no_of_weeks = models.CharField(max_length = 80,default="default")
    tax_from = models.CharField(max_length = 80,default="default")
    tax_upto = models.CharField(max_length = 80,default="default")
    total_tax_amount = models.CharField(max_length = 80,default="default")
    payment_date = models.CharField(max_length = 80,default="default")
    recipt_no = models.CharField(max_length=80,default="none")
    total_amt_text = models.CharField(max_length = 180,default = "nothing")
    
    def __str__(self):
        return self.vehicleno
    
    
class add_karnataka(models.Model):
    id = models.AutoField(primary_key=True)
    created_username = models.CharField(max_length = 80,default="default") 
    vehicleno =  models.CharField(max_length = 80,default="default")
    chassisno =  models.CharField(max_length = 80,default="default")
    ownername = models.CharField(max_length = 80,default="default")
    mobile = models.CharField(max_length = 80,default="default")
    from_state  = models.CharField(max_length = 80,default="default")
    VehicleType  = models.CharField(max_length = 80,default="default")
    VehicleClass  = models.CharField(max_length = 80,default="default")
    ServiceType  = models.CharField(max_length = 80,default="default")
    PermitType  = models.CharField(max_length = 80,default="default")
    seating_c  = models.CharField(max_length = 80,default="default")
    txt_sleeper_cap  = models.CharField(max_length = 80,default="default")
    txt_floor_area  = models.CharField(max_length = 80,default="default")
    TaxMode  = models.CharField(max_length = 80,default="default")
    permit_upto  = models.CharField(max_length = 80,default="default")
    fitdate  = models.CharField(max_length = 80,default="default")
    ins_upto  = models.CharField(max_length = 80,default="default")
    tax_validity  = models.CharField(max_length = 80,default="default")
    border_entry  = models.CharField(max_length = 80,default="default")
    txt_no_of_weeks  = models.CharField(max_length = 80,default="default")
    service_amount  = models.CharField(max_length = 80,default="default")
    tax_from  = models.CharField(max_length = 80,default="default")
    tax_upto  = models.CharField(max_length = 80,default="default")
    total_tax_amount  = models.CharField(max_length = 80,default="default")
    infra_cess  = models.CharField(max_length = 80,default="default")
    permit_fee  = models.CharField(max_length = 80,default="default")
    permit_endoresment_variation  = models.CharField(max_length = 80,default="default")
    payment_date = models.CharField(max_length = 80,default="default")
    total_amt_text = models.CharField(max_length = 180,default = "nothing")
    
    def __str__(self):
        return self.vehicleno
    
    
class add_madhyapradesh(models.Model):
    id = models.AutoField(primary_key=True)
    created_username =  models.CharField(max_length = 80,default="default")
    VehicleType = models.CharField(max_length = 80,default="default") 
    from_state =  models.CharField(max_length = 80,default="default")
    ownername = models.CharField(max_length = 80,default="default")
    vehicleno = models.CharField(max_length = 80,default="default")
    gramin = models.CharField(max_length = 80,default="default")
    tax_mode = models.CharField(max_length = 80,default="default")
    tax_from = models.CharField(max_length = 80,default="default")
    tax_upto = models.CharField(max_length = 80,default="default")
    total_tax_amount = models.CharField(max_length = 80,default="default")
    tax_consessioner = models.CharField(max_length = 80,default="default")
    tax_ips = models.CharField(max_length = 80,default="default")
    mobile = models.CharField(max_length = 80,default="default")
    genby = models.CharField(max_length = 80,default="default")
    payment_date = models.CharField(max_length = 80,default="default")
    total_amt_text = models.CharField(max_length = 180,default = "nothing")
    
    def __str__(self):
        return self.vehicleno
    
    
class add_maharashtra(models.Model):
      id = models.AutoField(primary_key=True)
      created_username = models.CharField(max_length = 80,default="default")
      vehicleno  = models.CharField(max_length = 80,default="default")
      chassisno  = models.CharField(max_length = 80,default="default")
      ownername = models.CharField(max_length = 80,default="default")
      mobile  = models.CharField(max_length = 80,default="default")
      from_state = models.CharField(max_length = 80,default="default")
      VehicleType = models.CharField(max_length = 80,default="default")
      VehicleClass = models.CharField(max_length = 80,default="default")
      ServiceType = models.CharField(max_length = 80,default="default")
      seating_c = models.CharField(max_length = 80,default="default")
      txt_sleeper_cap = models.CharField(max_length = 80,default="default")
      TaxMode = models.CharField(max_length = 80,default="default")
      districtname = models.CharField(max_length = 80,default="default")
      checkpost = models.CharField(max_length = 80,default="default")
      tax_from = models.CharField(max_length = 80,default="default")
      tax_upto = models.CharField(max_length = 80,default="default")
      total_tax_amount = models.CharField(max_length = 80,default="default")
      service_amount = models.CharField(max_length = 80,default="default")
      create_date = models.CharField(max_length = 80,default="default")
      total_amt_text = models.CharField(max_length = 180,default = "nothing")
      grand_tottal = models.IntegerField(default=0)
      recipt_no = models.CharField(max_length=120,default="none")
      
      def __str__(self):
          return self.vehicleno
      
      
class add_tamilnadu(models.Model):
    id = models.AutoField(primary_key=True)
    created_username  = models.CharField(max_length = 80,default="default")
    vehicleno  = models.CharField(max_length = 80,default="default")
    chassisno = models.CharField(max_length = 80,default="default")
    ownername = models.CharField(max_length = 80,default="default")
    mobile  = models.CharField(max_length = 80,default="default")
    from_state = models.CharField(max_length = 80,default="default")
    VehicleType = models.CharField(max_length = 80,default="default")
    VehicleClass = models.CharField(max_length = 80,default="default")
    recipt_no = models.CharField(max_length = 80,default="default")
    PermitType = models.CharField(max_length = 80,default="default")
    issuing_authority = models.CharField(max_length = 80,default="default")
    txt_seat_cap = models.CharField(max_length = 80,default="default")
    txt_sleeper_cap = models.CharField(max_length = 80,default="default")
    Extra_seat_cap = models.CharField(max_length = 80,default="default")
    ins_validity_input = models.CharField(max_length = 80,default="default")
    fitness_valid_input = models.CharField(max_length = 80,default="default")
    pucc_validity_input = models.CharField(max_length = 80,default="default")
    TaxMode = models.CharField(max_length = 80,default="default")
    txt_permit_auth_no = models.CharField(max_length = 80,default="default")
    permit_authorization_vali = models.CharField(max_length = 80,default="default")
    Greentax = models.CharField(max_length = 80,default="default")
    regn_date = models.CharField(max_length = 80,default="default")
    districtname = models.CharField(max_length = 80,default="default")
    permit_upto_input = models.CharField(max_length = 80,default="default")
    cal_tax_from_input = models.CharField(max_length = 80,default="default")
    cal_tax_to_input = models.CharField(max_length = 80,default="default")
    checkpost_name = models.CharField(max_length = 80,default="default")
    txt_permit_no = models.CharField(max_length = 80,default="default")
    total_tax_amount = models.CharField(max_length = 80,default="default")
    mv_tax = models.CharField(max_length = 80,default="default")
    serviceusercharge = models.CharField(max_length = 80,default="default")
    welfaretax = models.CharField(max_length = 80,default="default")
    permitfree = models.CharField(max_length = 80,default="default")
    create_date = models.CharField(max_length = 80,default="default")
    total_amt_text = models.CharField(max_length = 180,default = "nothing")
    
    def __str__(self):
        return self.vehicleno
    
    
class add_uttarpradesh(models.Model):
    id = models.AutoField(primary_key=True)
    created_username = models.CharField(max_length = 80,default="default")
    vehicleno = models.CharField(max_length = 80,default="default")
    chassisno = models.CharField(max_length = 80,default="default")
    ownername = models.CharField(max_length = 80,default="default")
    mobile = models.CharField(max_length = 80,default="default")
    from_state =  models.CharField(max_length = 80,default="default")
    VehicleType =  models.CharField(max_length = 80,default="default")
    VehicleClass =  models.CharField(max_length = 80,default="default")
    seating_c = models.CharField(max_length = 80,default="default")
    txt_sleeper_cap = models.CharField(max_length = 80,default="default")
    ServiceType = models.CharField(max_length = 80,default="default")
    TaxMode = models.CharField(max_length = 80,default="default")
    border_entry = models.CharField(max_length = 80,default="default")
    tax_from = models.CharField(max_length = 80,default="default")
    tax_upto = models.CharField(max_length = 80,default="default")
    PermitType = models.CharField(max_length = 80,default="default")
    permit_upto = models.CharField(max_length = 80,default="default")
    permit_no = models.CharField(max_length = 80,default="default")
    total_tax_amount = models.CharField(max_length = 80,default="default")
    payment_date = models.CharField(max_length = 80,default="default")
    total_amt_text = models.CharField(max_length = 180,default = "nothing")
    recipt_no = models.CharField(max_length=70,default="default")
    
    def __str__(self):
        return self.vehicleno
    
    
class add_uttrakhand(models.Model):
    id = models.AutoField(primary_key=True)
    created_username  = models.CharField(max_length = 80,default="default")  
    vehicleno  = models.CharField(max_length = 80,default="default")  
    chassisno  = models.CharField(max_length = 80,default="default")  
    ownername  = models.CharField(max_length = 80,default="default")  
    mobile  = models.CharField(max_length = 80,default="default")  
    from_state  = models.CharField(max_length = 80,default="default") 
    VehicleType  = models.CharField(max_length = 80,default="default") 
    VehicleClass  = models.CharField(max_length = 80,default="default") 
    seating_c  = models.CharField(max_length = 80,default="default")
    txt_sleeper_cap  = models.CharField(max_length = 80,default="default") 
    ServiceType  = models.CharField(max_length = 80,default="default")
    TaxMode  = models.CharField(max_length = 80,default="default") 
    border_entry =models.CharField(max_length = 80,default="default") 
    tax_from  = models.CharField(max_length = 80,default="default") 
    tax_upto = models.CharField(max_length = 80,default="default") 
    PermitType = models.CharField(max_length = 80,default="default") 
    permit_upto  = models.CharField(max_length = 80,default="default")
    permit_no  = models.CharField(max_length = 80,default="default")
    districtname  = models.CharField(max_length = 80,default="default")
    fitdate  = models.CharField(max_length = 80,default="default")
    permit_from  = models.CharField(max_length = 80,default="default")
    txt_no_of_weeks = models.CharField(max_length = 80,default="default") 
    total_tax_amount  = models.CharField(max_length = 80,default="default") 
    service_amount  = models.CharField(max_length = 80,default="default") 
    civik_amount = models.CharField(max_length = 80,default="default") 
    recipt_no = models.CharField(max_length=40,default="none")
    payment_date  = models.CharField(max_length = 80,default="default")
    total_amt_text = models.CharField(max_length = 180,default = "nothing")
    grand_tottal = models.IntegerField(default=0)
    
    def __str__(self):
        return self.vehicleno
    
    
class add_tripura(models.Model):
    id = models.AutoField(primary_key=True)
    recipt_no = models.CharField(max_length = 280,default="default")
    created_user = models.CharField(max_length = 280,default="default")
    vehicle = models.CharField(max_length = 280,default="default")
    chassis = models.CharField(max_length = 280,default="default")
    owner = models.CharField(max_length = 280,default="default")
    mobileno = models.CharField(max_length = 280,default="default")
    statename = models.CharField(max_length = 280,default="default")
    vehicleType = models.CharField(max_length = 280,default="default")
    vehicleClass = models.CharField(max_length = 280,default="default")
    grossWeight = models.CharField(max_length = 280,default="default")
    district = models.CharField(max_length = 280,default="default")
    barrier = models.CharField(max_length = 280,default="default")
    payment_mode = models.CharField(max_length = 280,default="default")
    cal_tax_from_input = models.CharField(max_length = 280,default="default")
    cal_tax_to_input = models.CharField(max_length = 280,default="default")
    mv_tax = models.CharField(max_length = 280,default="default")
    Service_charge = models.CharField(max_length = 280,default="default")
    total_tax_amount = models.CharField(max_length = 280,default="default")
    text_amt = models.CharField(max_length = 280,default="default")
    payment_date = models.CharField(max_length = 280,default="default")
    
    def __str__(self):
        return self.vehicle
    
    