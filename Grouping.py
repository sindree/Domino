import os 

in_file = r"C:\A_Prosjekt\Domino\Domino_Hasleveien50_newArea.csv"
out_file = r"C:\A_Prosjekt\Domino\Domino_Hasleveien50_Grouped.csv"
liste = []
prevAdresse = ""
prevLine = ""
teller = 0
min_husnr = 0
max_husnr = 0

w = open(out_file, "w")

with open(in_file) as f:
    for line in f:
        linje = line.split(",")
        adresseRute = linje[0] + linje[5]
        husnr = linje[1]
        
        if teller == 0:
            prevAdresse = adresseRute
            min_husnr = husnr
            max_husnr = husnr
            print "Første linje :)"
            teller = 1
            continue
        
        if adresseRute == prevAdresse:
            max_husnr = husnr
            prevAdresse = adresseRute
            prevLine = linje[0] + "," + str(min_husnr) + "," + str(max_husnr) + "," + linje[3] + "," + linje[4] + "," + linje[5] 
            
        if adresseRute != prevAdresse:
            w.write(prevLine)
            liste.append(prevLine)
            min_husnr = husnr
            max_husnr = husnr
            prevAdresse = adresseRute
            prevLine = linje[0] + "," + str(min_husnr) + "," + str(max_husnr) + "," + linje[3] + "," + linje[4] + "," + linje[5]

f.close()
w.close()
print liste





            
            
            
            
        
    
            
        
