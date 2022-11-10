def mult(l):
    prod=1
    for i in l:
        prod=prod*i
    return prod
f1 = open("spec.txt", "r",encoding='utf8')
ar=f1.readlines()
f1.close()
experiment_ids=[]
number_of_items=[]
number_of_conditions=[]
i=0
while(ar[i][0]=="E"):
    temp=ar[i].split(" ")
    experiment_ids.append(int(temp[1]))
    number_of_items.append(int(temp[2]))
    number_of_conditions.append(int(temp[3]))
    i=i+1
temp=ar[i].split(" ")
#print(experiment_ids,number_of_items,number_of_conditions)
number_of_fillers = int(temp[1])
i=i+1
tempp=ar[i].split(" ")
#print(experiment_ids,number_of_items,number_of_conditions)
number_of_pracitem = int(tempp[1])
i+=1
tempp=ar[i].split(" ")
#print(experiment_ids,number_of_items,number_of_conditions)
number_of_non_words = int(tempp[1])
i+=1
stimulus_duration = int(ar[i]);
f3 =open("specs_lexical_decision.js","w",encoding='utf8')
f3.write("var number_of_items = " + str(number_of_items) + ";\n")
f3.write("var number_of_fillers = " + str(number_of_fillers) + ";\n")
f3.write("var number_of_pracitem = " + str(number_of_pracitem) + ";\n")
f3.write("var number_of_non_words = " + str(number_of_non_words) + ";\n")
f3.write("var number_of_lists = " + str(max(number_of_conditions)) + ";\n")
f3.write("var trial_dur = " + str(stimulus_duration) + ";\n")
f3.write("var trial_dur_2 = " + str(int(ar[i+1])) + ";\n")
f3.write("var trial_dur_3 = " + str(int(ar[i+2])) + ";\n")
f3.write("var choiceofe = " + str(int(ar[i+3])) + ";\n")
f3.write("var list_number = 0" +  ";\n")
f3.write("var font_size = " + str(int(ar[i+4])) + ";\n")
f3.write("var color = " + ar[i+5][:-1] + ";\n")
f3.close()

#count_chunks = 0
#total_time = 0
#count_chunks_fillers = 0
#total_time_fillers = 0

alllists_nl=[]
alllists_de=[]
with open("lists_nl.txt", "r",encoding='utf8') as input:
    element_nl=input.read().split("\n\n")

with open("lists_de.txt", "r",encoding='utf8') as input:
    element_de=input.read().split("\n\n")

temp1_de=[]
temp1_nl=[]

for (stimuli_de,stimuli_nl) in zip(element_de,element_nl):
    stimuli_de=stimuli_de.split("\n")
    stimuli_nl=stimuli_nl.split("\n")
    temp2_de=[]
    temp2_nl=[]
    for (item_de,item_nl) in zip(stimuli_de,stimuli_nl):
        item_de=item_de.split("\t\t\t")
        item_nl=item_nl.split("\t\t\t")
        item_de[5]=item_de[5].split(" ")
        item_nl[5]=item_nl[5].split(" ")
        item_de.append(len(item_de[5]))
        item_nl.append(len(item_nl[5]))
        screentime = []
        for (word_de,word_nl) in zip(item_de[5],item_nl[5]):
            time_de = 190 + (len(word_de)*(20))
            time_nl = 190 + (len(word_nl)*(20))
            screentime.append(max([time_de,time_nl]))
        item_de.append(screentime)
        item_nl.append(screentime)
        temp2_de.append(item_de)
        temp2_nl.append(item_nl)
    temp1_de.append(temp2_de[0])
    temp1_nl.append(temp2_nl[0])

alllists_de=temp1_de
alllists_nl=temp1_nl

print(str(alllists_de)+"\n\n")
print(str(alllists_nl)+"\n\n")

alllistsn_de = []
for k in range(max(number_of_conditions)):
    temp=[]
    for item in alllists_de:
        if str(item[4])==str(k+1):
            temp.append(item)
    alllistsn_de.append(temp)

alllistsn_nl = []
for k in range(max(number_of_conditions)):
    temp=[]
    for item in alllists_nl:
        if str(item[4])==str(k+1):
            temp.append(item)
    alllistsn_nl.append(temp)

print(str(alllistsn_de)+"\n\n\n\n\n")
    

##alllistsn = []
##
##for i in range(max(number_of_conditions)):
##        temp=[]
##        for j in range(len(number_of_items)):
##            for k in range(number_of_items[j]):
##                alllists[j][k][(k+i+experiment_ids[j]-1)%number_of_conditions[j]].append(str(j+1))
##                alllists[j][k][(k+i+experiment_ids[j]-1)%number_of_conditions[j]].append(str(k+1))
##                alllists[j][k][(k+i+experiment_ids[j]-1)%number_of_conditions[j]].append(chr(97+(k+i)%number_of_conditions[j]))
##                temp.append(alllists[j][k][(k+i)%number_of_conditions[j]])
##        alllistsn.append(temp)
##
##print(alllistsn)

if(number_of_fillers!= 0):
    with open("fillers_de.txt", "r",encoding='utf8') as input:
        allfillers_de = input.read().split("\n\n")
    with open("fillers_nl.txt", "r",encoding='utf8') as input:
        allfillers_nl = input.read().split("\n\n")

    all_fillers_de=[]
    all_fillers_nl=[]
    for (alist_de,alist_nl) in zip(alllistsn_de,alllistsn_nl):
        count=0
        for j in range(number_of_fillers):
            filler_de =allfillers_de[j]
            filler_nl =allfillers_nl[j]
            count=count+1
            fillitem_de=filler_de.split("\t\t\t")
            fillitem_nl=filler_nl.split("\t\t\t")
            fillitem_de[5]=fillitem_de[5].split(" ")
            fillitem_nl[5]=fillitem_nl[5].split(" ")
            fillitem_de.append(len(fillitem_de[5]))
            fillitem_nl.append(len(fillitem_nl[5]))

            screentime = []
            for (word_de,word_nl) in zip(fillitem_de[5],fillitem_nl[5]):
                time_de = 190 + (len(word_de)*(20))
                time_nl = 190 + (len(word_nl)*(20))
                screentime.append(max([time_de,time_nl]))
            fillitem_de.append(screentime)
            fillitem_nl.append(screentime)
            
            alist_de.append(fillitem_de)
            alist_nl.append(fillitem_nl)
            all_fillers_de.append(fillitem_de)
            all_fillers_nl.append(fillitem_nl)
print(alllistsn_de)

print(len(alllistsn_de[2]))

if(number_of_pracitem!= 0):
    with open("practice_de.txt", "r",encoding='utf8') as input:
        allprac_de = input.read().split("\n\n")
    with open("practice_nl.txt", "r",encoding='utf8') as input:
        allprac_nl = input.read().split("\n\n")

    all_prac_de=[]
    all_prac_nl=[]
    count=0
    for i in range(number_of_pracitem):
        count+=1
        pracitem_de=allprac_de[i].split("\t\t\t")
        pracitem_nl=allprac_nl[i].split("\t\t\t")
        pracitem_de[5]=pracitem_de[5].split(" ")
        pracitem_nl[5]=pracitem_nl[5].split(" ")
        pracitem_de.append(len(pracitem_de[5]))
        pracitem_nl.append(len(pracitem_nl[5]))
        screentime = []
        for (word_de,word_nl) in zip(pracitem_de[5],pracitem_nl[5]):
            time_de = 190 + (len(word_de)*(20))
            time_nl = 190 + (len(word_nl)*(20))
            screentime.append(max([time_de,time_nl]))
        pracitem_de.append(screentime)
        pracitem_nl.append(screentime)
        
        all_prac_de.append(pracitem_de)
        all_prac_nl.append(pracitem_nl)


f4 = open("lists_RSVP_German.js","w",encoding="utf-8")
f4.write("var lists =")
f4.write(str(alllistsn_de))
f4.write(";\n")
f4.write("var praclist =")
f4.write(str(all_prac_de))
f4.write(";\n")
f4.close()

f5 = open("lists_RSVP_Dutch.js","w",encoding="utf-8")
f5.write("var lists =")
f5.write(str(alllistsn_nl))
f5.write(";\n")
f5.write("var praclist =")
f5.write(str(all_prac_nl))
f5.write(";\n")
f5.close()

##print(count_chunks)
##print(total_time)
##print(count_chunks_fillers)
##print(total_time_fillers)
##
###### Copy items from google list to list_de and list_nl; control spacing etc. accordingly; also fillers and prac
