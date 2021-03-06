from tkinter import *
from tkinter import ttk
#from stopp_nupp import stardinupp
#from stopp_nupp import stopp
from ristike import unusta
import time


n = 0
#funktsioon üheks linnukesega tegevuse reaks
#see värk peaks käivituma iga kord kui vajutada nuppu 'lisa'
def do_do(raam, colour, tegevuse_sisestamine, aja_sisestamine, kiri, ajad, tegevused, ennustatud_ajad):
    def lisa_statistikasse(tegevuse_sisestamine, aja_sisestamine, ennustatud_ajad):
        ajad.append(aja_sisestamine.get())
        tegevused.append(tegevuse_sisestamine.get())
        ennustatud_ajad.append(aja_sisestamine.get())
    lisa_statistikasse(tegevuse_sisestamine, aja_sisestamine, ennustatud_ajad)

    global n      
    n=n+1
        
    var = IntVar()
    c = Checkbutton(raam, activebackground=colour,
                    background=colour, variable=var,
                    command=lambda: lisa_statistikasse(tegevuse_sisestamine, aja_sisestamine, ennustatud_ajad))
    c.grid(column=0, padx=5, pady=6)

    rida= c.grid_info()["row"]
    #võtame entry boxidest sisestatu

    tegevuse_sisestamine_tulemus = Label(raam, text=tegevuse_sisestamine.get(), background=colour, font=kiri)
    tegevuse_sisestamine_tulemus.grid(column=1, row = rida, padx=5, pady=6)

    aja_sisestamine_tulemus = Label(raam, text="Aeg:", background=colour, font=kiri)
    aja_sisestamine_tulemus.grid(column=2, row = rida,  padx=5, pady=6)
    #print(ajad)
    aja_sisestamine_tulemus = Label(raam, text=aja_sisestamine.get(), background=colour, font=kiri)
    aja_sisestamine_tulemus.grid(column=3, row = rida,  padx=5, pady=6)

# TIMERI SEKTSIOONID    
####################################################################################################################################################
    global olek
    olek = False
    global timer
    timer = [0, 0, 0]
    global pattern
    pattern = '{0:02d}:{1:02d}:{2:02d}'
    def countdown():
        if(olek):
            timer = lõppjärjend
            if (timer[2] > 0 or timer[1]>0 or timer[0]>0):
                if (timer[2] >0 ):
                    timer[2] -= 1
    
                elif (timer[2] == 0 and timer[1]>0):
                    timer[1] = timer[1]-1
                    timer[2] = 59
    
                elif (timer[2] == 0 and timer[1]==0 and timer[0]>0):
                    timer[0]=timer[0]-1
                    timer[1]=59
                    timer[2]=59

            timeString = pattern.format(timer[0], timer[1], timer[2])
            timeText.configure(text=timeString)
            ajad[0]=timeString
        raam.after(1000, countdown)
###############################################################################################################################################################################       
    global olek2
    olek2 = False
    global timer2
    timer2 = [0, 0, 0]
    def countdown2():
        if(olek2):
            timer2 = lõppjärjend2
            if (timer2[2] > 0 or timer2[1]>0 or timer2[0]>0):
                if (timer2[2] >0 ):
                    timer2[2] -= 1
    
                elif (timer2[2] == 0 and timer2[1]>0):
                    timer2[1] = timer2[1]-1
                    timer2[2] = 59
    
                elif (timer2[2] == 0 and timer2[1]==0 and timer2[0]>0):
                    timer2[0]=timer2[0]-1
                    timer2[1]=59
                    timer2[2]=59

            timeString2 = pattern.format(timer2[0], timer2[1], timer2[2])
            timeText2.configure(text=timeString2)
            ajad[1]=timeString2
        raam.after(1000, countdown2)
###############################################################################################################################################################################
    global olek3
    olek3 = False
    global timer3
    timer3 = [0, 0, 0]
    def countdown3():
        if(olek3):
            timer3 = lõppjärjend3
            if (timer3[2] > 0 or timer3[1]>0 or timer3[0]>0):
                if (timer3[2] >0 ):
                    timer3[2] -= 1
    
                elif (timer3[2] == 0 and timer3[1]>0):
                    timer3[1] = timer3[1]-1
                    timer3[2] = 59
    
                elif (timer3[2] == 0 and timer3[1]==0 and timer3[0]>0):
                    timer3[0]=timer3[0]-1
                    timer3[1]=59
                    timer3[2]=59

            timeString3 = pattern.format(timer3[0], timer3[1], timer3[2])
            timeText3.configure(text=timeString3)
            ajad[3]=timeString3
        raam.after(1000, countdown3)
##############################################################################################################################################################################
    global olek4
    olek4 = False
    global timer4
    timer4 = [0, 0, 0]
    def countdown4():
        if(olek4):
            timer4 = lõppjärjend4
            if (timer4[2] > 0 or timer4[1]>0 or timer4[0]>0):
                if (timer4[2] >0 ):
                    timer4[2] -= 1
    
                elif (timer4[2] == 0 and timer4[1]>0):
                    timer4[1] = timer4[1]-1
                    timer4[2] = 59
    
                elif (timer4[2] == 0 and timer4[1]==0 and timer4[0]>0):
                    timer4[0]=timer4[0]-1
                    timer4[1]=59
                    timer4[2]=59
            
            timeString4 = pattern.format(timer4[0], timer4[1], timer4[2])
            timeText4.configure(text=timeString4)
        raam.after(1000, countdown4)
# STARDI SEKTSIOONID
##############################################################################################################################################################################

    if n == 1:
        global stardi

        def stardi(raam,rida,kiri,n):
            nupp = Button(raam,cursor="hand2",text="stopp",font=kiri,bg="tomato",command=lambda loomise_hetke_n=n: stopp(raam,rida,kiri,loomise_hetke_n))
            nupp.grid(column=4, row = rida,  padx=5, pady=6)
            aeg = aja_sisestamine.get()
            järjend = aeg.split(":")
            global lõppjärjend
            lõppjärjend= []           
            timer = lõppjärjend
            for i in järjend:
                i = int(i)
                lõppjärjend +=[i]
            global timeText
            timeText = Label(raam, text=aeg, font=(50))
            timeText.grid(column=3,row=rida,padx=5, pady=6)
            global olek
            olek = True
            
            nupp.pack_forget()
            get_info(n,tegevuse_sisestamine_tulemus,aja_sisestamine,lõppjärjend)
        #nupp.invoke() nupp on halb sest leidub juba projekt failis
        stardi(raam,rida,kiri,n)
        #time.sleep(1)
        stopp(raam,rida,kiri,n)            
        countdown()
           

    # soovime, et nupp veniks nii laiuses kui ka kõrguses
        nupp = Button(raam,cursor="hand2", text=" Start ",font=kiri, bg="lime green", command=lambda loomise_hetke_n=n : start(raam,rida,kiri,loomise_hetke_n))
    #sulgudesse vaja ka command = alustab aja lugemist, mis on funktsioonis aeg
        nupp.grid(column=4, row = rida,  padx=5, pady=6)

    # soovime, et nupp muutuks peale vajutust
        progress = ttk.Progressbar(raam, orient='horizontal', length= 75, mode = 'indeterminate')
        progress.grid(column=5, row=rida, padx=5, pady=6)

    # #nupp, et soovimatud to_do-d kustutada
        ristike = Button(raam, text=" X ",bg="MediumVioletRed", command=lambda: unusta(timer,c,tegevuse_sisestamine_tulemus,aja_sisestamine_tulemus,nupp,progress,ristike))
        ristike.grid(column=6, row=rida, padx=5, pady=6)
        
#######################################################################################################################################################################
    elif n == 2:
        global stardi2

        def stardi2(raam,rida,kiri,n):
            nupp = Button(raam,cursor="hand2",text="stopp",font=kiri,bg="tomato",command=lambda loomise_hetke_n=n : stopp2(raam,rida,kiri,loomise_hetke_n))
            nupp.grid(column=4, row = rida,  padx=5, pady=6)
            aeg = aja_sisestamine.get()
            järjend = aeg.split(":")
            global lõppjärjend2
            lõppjärjend2= []
            timer2 = lõppjärjend2
            for i in järjend:
                i = int(i)
                lõppjärjend2 +=[i]
            global timeText2
            timeText2 = Label(raam, text=aeg, font=(50))
            timeText2.grid(column=3,row=rida,padx=5, pady=6)
            global olek2
            olek2 = True
            

            get_info(n,tegevuse_sisestamine_tulemus,aja_sisestamine,lõppjärjend2)
        stardi2(raam,rida,kiri,n)
        #time.sleep(1)
        stopp2(raam,rida,kiri,n)        
        countdown2()

    

    # soovime, et nupp veniks nii laiuses kui ka kõrguses
        nupp = Button(raam,cursor="hand2", text=" Start ",font=kiri, bg="lime green", command=lambda loomise_hetke_n=n: start2(raam,rida,kiri,loomise_hetke_n))
    #sulgudesse vaja ka command = alustab aja lugemist, mis on funktsioonis aeg
        nupp.grid(column=4, row = rida,  padx=5, pady=6)

    # soovime, et nupp muutuks peale vajutust
        progress = ttk.Progressbar(raam, orient='horizontal', length= 75, mode = 'indeterminate')
        progress.grid(column=5, row=rida, padx=5, pady=6)

    # #nupp, et soovimatud to_do-d kustutada
        ristike = Button(raam, text=" X ",bg="MediumVioletRed", command=lambda: unusta(clock,c,tegevuse_sisestamine_tulemus,aja_sisestamine_tulemus,nupp,progress,ristike))
        ristike.grid(column=6, row=rida, padx=5, pady=6)
        
##################################################################################################################################################################

    elif n == 3:
        global stardi3

        def stardi3(raam,rida,kiri,n):
            nupp = Button(raam,cursor="hand2",text="stopp",font=kiri,bg="tomato",command=lambda loomise_hetke_n=n : stopp3(raam,rida,kiri,loomise_hetke_n))
            nupp.grid(column=4, row = rida,  padx=5, pady=6)
            aeg = aja_sisestamine.get()
            järjend = aeg.split(":")
            global lõppjärjend3
            lõppjärjend3= []
            timer3 = lõppjärjend3
            for i in järjend:
                i = int(i)
                lõppjärjend3 +=[i]            
            global timeText3
            timeText3 = Label(raam, text=aeg, font=(50))
            timeText3.grid(column=3,row=rida,padx=5, pady=6)
            global olek3
            olek3 = True
           

            get_info(n,tegevuse_sisestamine_tulemus,aja_sisestamine,lõppjärjend3)
        stardi3(raam,rida,kiri,n)
        #time.sleep(1)
        stopp3(raam,rida,kiri,n)        
        countdown3()

    

    # soovime, et nupp veniks nii laiuses kui ka kõrguses
        nupp = Button(raam,cursor="hand2", text=" Start ",font=kiri, bg="lime green", command=lambda loomise_hetke_n=n: start3(raam,rida,kiri,loomise_hetke_n))
    #sulgudesse vaja ka command = alustab aja lugemist, mis on funktsioonis aeg
        nupp.grid(column=4, row = rida,  padx=5, pady=6)

    # soovime, et nupp muutuks peale vajutust
        progress = ttk.Progressbar(raam, orient='horizontal', length= 75, mode = 'indeterminate')
        progress.grid(column=5, row=rida, padx=5, pady=6)

    # #nupp, et soovimatud to_do-d kustutada
        ristike = Button(raam, text=" X ",bg="MediumVioletRed", command=lambda: unusta(clock,c,tegevuse_sisestamine_tulemus,aja_sisestamine_tulemus,nupp,progress,ristike))
        ristike.grid(column=6, row=rida, padx=5, pady=6)
#######################################################################################################################################################################
    elif n == 4:
        global stardi4

        def stardi4(raam,rida,kiri,n):
            nupp = Button(raam,cursor="hand2",text="stopp",font=kiri,bg="tomato",command=lambda loomise_hetke_n=n : stopp4(raam,rida,kiri,loomise_hetke_n))
            nupp.grid(column=4, row = rida,  padx=5, pady=6)
            aeg = aja_sisestamine.get()
            järjend = aeg.split(":")
            global lõppjärjend4
            lõppjärjend4= []
            timer4 = lõppjärjend4
            for i in järjend:
                i = int(i)
                lõppjärjend4 +=[i]
            global timeText4
            timeText4 = Label(raam, text=aeg, font=(50))
            timeText4.grid(column=3,row=rida,padx=5, pady=6)
            global olek4
            olek4 = True
        

            get_info(n,tegevuse_sisestamine_tulemus,aja_sisestamine,lõppjärjend4)
        stardi4(raam,rida,kiri,n)
        #time.sleep(1)
        stopp4(raam,rida,kiri,n)        
        countdown4()

    

    # soovime, et nupp veniks nii laiuses kui ka kõrguses
        nupp = Button(raam,cursor="hand2", text=" Start ",font=kiri, bg="lime green", command=lambda loomise_hetke_n=n: start4(raam,rida,kiri,loomise_hetke_n))
    #sulgudesse vaja ka command = alustab aja lugemist, mis on funktsioonis aeg
        nupp.grid(column=4, row = rida,  padx=5, pady=6)

    # soovime, et nupp muutuks peale vajutust
        progress = ttk.Progressbar(raam, orient='horizontal', length= 75, mode = 'indeterminate')
        progress.grid(column=5, row=rida, padx=5, pady=6)

    # #nupp, et soovimatud to_do-d kustutada
        ristike = Button(raam, text=" X ",bg="MediumVioletRed", command=lambda: unusta(clock,c,tegevuse_sisestamine_tulemus,aja_sisestamine_tulemus,nupp,progress,ristike))
        ristike.grid(column=6, row=rida, padx=5, pady=6)
        
     
#START STOP SEKTSIOONID
#############################################################################################################################################
        #esimene start stopp sektsioon
def start(raam,rida,kiri,n):
    global olek
    olek = True

    nupp = Button(raam,cursor="hand2",text="Stopp",font=kiri,bg="tomato",command=lambda loomise_hetke_n=n : stopp(raam,rida,kiri,loomise_hetke_n))
    nupp.grid(column=4, row=rida,  padx=5, pady=6)
    nupp.pack_forget()
def stopp(raam,rida,kiri,n):
    global olek
    olek = False

    # soovime, et nupp veniks nii laiuses kui ka kõrguses
    nupp = Button(raam, cursor="hand2", text=" Start ",font=kiri, bg="lime green", command=lambda loomise_hetke_n=n : start(raam,rida,kiri,loomise_hetke_n))
    nupp.grid(column=4, row=rida, padx=5, pady=6)
    nupp.pack_forget()
###########################################################################################################################################################################
    #teine start stopp sektsioon
def start2(raam,rida,kiri,n):
    global olek2
    olek2 = True

    nupp = Button(raam,cursor="hand2",text=" Stopp",font=kiri,bg="tomato",command=lambda loomise_hetke_n=n : stopp2(raam,rida,kiri,loomise_hetke_n))
    nupp.grid(column=4, row=rida,  padx=5, pady=6)
    nupp.pack_forget()
def stopp2(raam,rida,kiri,n):
    global olek2
    olek2 = False

    # soovime, et nupp veniks nii laiuses kui ka kõrguses
    nupp = Button(raam, cursor="hand2", text=" Start ",font=kiri, bg="lime green", command=lambda loomise_hetke_n=n : start2(raam,rida,kiri,loomise_hetke_n))
    nupp.grid(column=4, row=rida, padx=5, pady=6)
    nupp.pack_forget()
###########################################################################################################################################################################

    #kolmas start stopp sektsioon
def start3(raam,rida,kiri,n):
    global olek3
    olek3 = True

    nupp = Button(raam,cursor="hand2",text="Stopp",font=kiri,bg="tomato",command=lambda loomise_hetke_n=n : stopp3(raam,rida,kiri,loomise_hetke_n))
    nupp.grid(column=4, row=rida,  padx=5, pady=6)
    nupp.pack_forget()
def stopp3(raam,rida,kiri,n):
    global olek3
    olek3 = False

    # soovime, et nupp veniks nii laiuses kui ka kõrguses
    nupp = Button(raam, cursor="hand2", text=" Start ",font=kiri, bg="lime green", command=lambda loomise_hetke_n=n : start3(raam,rida,kiri,loomise_hetke_n))
    nupp.grid(column=4, row=rida, padx=5, pady=6)
    nupp.pack_forget()
###########################################################################################################################################################################
    #neljas start stopp sektsioon
def start4(raam,rida,kiri,n):
    global olek4
    olek4 = True
    nupp = Button(raam,cursor="hand2",text="Stopp",font=kiri,bg="tomato",command=lambda loomise_hetke_n=n : stopp4(raam,rida,kiri,loomise_hetke_n))
    nupp.grid(column=4, row=rida,  padx=5, pady=6)
    nupp.pack_forget()
def stopp4(raam,rida,kiri,n):
    global olek4
    olek4 = False
    # soovime, et nupp veniks nii laiuses kui ka kõrguses
    nupp = Button(raam, cursor="hand2", text=" Start ",font=kiri, bg="lime green", command=lambda loomise_hetke_n=n : start4(raam,rida,kiri,loomise_hetke_n))
    nupp.grid(column=4, row=rida, padx=5, pady=6)
    nupp.pack_forget()
########################################################################################################################################################################### 
järjend = []
def get_info(n,tegevuse_sisestamine_tulemus,aja_sisestamine,lõppjärjend):
    alam_list = [n,tegevuse_sisestamine_tulemus,aja_sisestamine,lõppjärjend]
    #print(alam_list)
    global järjend
    järjend+= alam_list
    #print(alam_list)






