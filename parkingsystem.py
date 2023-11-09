list1=[]
class parking():
    def __init__(self,pb,psc,pmc,plc):
        self.pb=pb
        self.psc=psc
        self.pmc=pmc
        self.plc=plc
        self.totalslots=self.pb+self.psc+self.pmc+self.plc
    def displayslots(self):1
        print("parking slots alloated for bikes define it by 1",self.pb)
        print("parking slots alloated for small cars 2",self.psc)
        print("parking slots alloated for medium cars 3",self.pmc)
        print("parking slots alloated for large cars 4",self.plc)
        print("total slots",self.totalslots)
class orig(parking):
    def __init__(self,regno,cartype):
        parking.__init__(self,pb,psc,pmc,plc)
        self.regno=regno
        self.cartype=cartype
    def park(self,regno,cartype):
        while self.totalslots>0:
            if cartype==1 and self.pb>0:
                list1.append(regno)
                self.pb-=1
                break
            elif cartype==2 and self.psc>0:
                list1.append(regno)
                self.psc-=1
                break
            elif cartype==3 and self.pmc>0:
                list1.append(regno)
                self.pmc-=1
                break
            elif cartype==4 and self.plc>0:
                list1.append(regno)
                self.plc-=1
                break
            elif cartype==1 and self.pb==0:
                print("no place is available to park a bike")
                break
            elif cartype==2 and self.psc==0:
                print("no place is available to park a small car")
                break
            elif cartype==3 and self.pmc==0:
                print("no place is available to park a medium car")
                break
            else:
                print("no place is available to park a large car")
                break
        else:
            print("no slots are available")
class orig2(parking):
    def __init__(self,regno,cartype):
        parking.__init__(self,pb,psc,pmc,plc)
        self.regno=regno
        self.cartype=cartype
    def unpark(self,regno,cartype):
        if cartype==1:
            list1.remove(regno)
            self.pb+=1
        elif cartype==2:
            list1.remove(regno)
            self.psc+=1
        elif cartype==3:
            list1.remove(regno)
            self.pmc+=1
        else:
            list1.remove(regno)
            self.plc+=1
class orig3(parking):
    def __init__(self,regno):
        parking.__init__(self,pb,psc,pmc,plc)
        self.regno=regno
    def fetchdata(self,regno):
        index1=list1.index(regno)
        print("the vehicle is parked at",index1)
pb=int(input("total slots available for bike"))
psc=int(input("total slots available for small cars"))
pmc=int(input("total slots available for medium cars"))
plc=int(input("total slots available for large cars"))
obj1=parking(pb,psc,pmc,plc)
obj1.displayslots()
n=int(input("number of vehiles to park"))
for i in range(n):
    cartype=int(input('''enter the vehicle type - 1 - bike,
2 - small car,
3-medium car,
4-large car
'''))
    regno=int(input("enter regno"))
    obj2=orig(regno,cartype)
    obj2.park(regno,cartype)
p=int(input("number of vehicles to unpark"))
for i in range(p):
    cartype=int(input('''enter the vehicle type - 1 - bike,
2 - small car,
3-medium car,
4-large car
'''))
    regno=int(input("enter the regno"))
    obj3=orig2(regno,cartype)
    obj3.unpark(regno,cartype)
regno=int(input("enter regno of car of which u need to find the info"))
obj4=orig3(regno)
obj4.fetchdata(regno)
