import numpy as np
import scipy.io
import matplotlib.pyplot as plt

array = np.zeros((225-33, 47))

filter_wavelengths = [3595, 4640, 6122, 16620, 35075, 44366, 56281, 75892, 232096, 684448, 1525902, 2428218, 3408914, 4822548, 11991798] # Effective wavelengths from filter website 610 and 20cm need to be added (16500 is h, taken from wikipedia), 119917898 needs to be replaced with a better effective wavelength


SDSS = scipy.io.readsav('MULTIWAVE_allfluxes_final.sav')

threshold = 10000
#print SDSS['fr'][0]
#print SDSS.keys()

#key_names = ['f3', 'f4', 'f5', 'f8', 'f160', 'f70', 'df610', 'df20cm', 'smam', 'zs', 'df350', 'df250', 'dfu', 'dfr', 'epoch', 'dfh', 'f24', 'dfg', 'fr', 'f610', 'df160', 'fu', 'df70', 'rmag', 'f350', 'fg', 'fh', 'mips', 'f500', 'df8', 'df500', 'df5', 'df4', 'f250', 'df3', 'f20cm', 'df24', 'dsmam', 'ew7']

key_names = ['fu', 'dfu', 'fg', 'dfg', 'fr', 'dfr', 'fh', 'dfh', 'f3', 'df3', 'f4', 'df4', 'f5', 'df5', 'f8', 'df8', 'f24', 'df24', 'f70', 'df70', 'f160', 'df160', 'f250', 'df250', 'f350', 'df350', 'f500', 'df500', 'smam', 'dsmam'] # Have not added h band yet drmag does not actually exist, just to make sure program does not whine about this

# I have remove 'mips', 'zs' and 'rmag'

#R_bands = np.loadtxt('CHANGED_MULTIWAVE_RADEC_supersample_basics.txt', skiprows = 1, usecols = [0, 6])
#print R_bands
some_constant = 3080.e3 # R band Flux at m=0, unit: mJy

OTHER_BANDS = np.loadtxt('FLS_cat_1217131.txt', skiprows = 33)

#array[:,:-14] = OTHER_BANDS[:,:22]

#array[:,25:] = Filter_wavelengths

id_contribution = OTHER_BANDS[:, 0]
agn_contribution = OTHER_BANDS[:, 25] / 100.


SDSS['f3'] *= 1e-3
SDSS['df3'] *= 1e-3
SDSS['f4'] *= 1e-3
SDSS['df4'] *= 1e-3
SDSS['f5'] *= 1e-3
SDSS['df5'] *= 1e-3
SDSS['f8'] *= 1e-3
SDSS['df8'] *= 1e-3 

#print SDSS['dfr']


'''
for i in range(len(OTHER_BANDS)):
    for j in range(len(SDSS['mips'])): #May need to be changed to len(R_bands)
        
        if(OTHER_BANDS[i][0] == SDSS['mips'][j]):
            
            # Have chosen units of mJ
            array[i][0] = OTHER_BANDS[i][0]

            for s in range(1, 9, 1):

                array[i][s] = OTHER_BANDS[i][s] * 1.e-3 #uJy

                

            for s in range(9, 21 , 1):

                array[i][s] = OTHER_BANDS[i][s]
                
                
            
            #array[i][25] = OTHER_BANDS[i][21] # Don't know where to get filter for MAMBO
            #array[i][26] = OTHER_BANDS[i][22] # Don't know where to get filter for MAMBO
            for t in range(len(R_bands)):
                if array[i][0]==R_bands[t][0]:
                    array[i][27] = some_constant * 10.**(-R_bands[t][1] / 2.5) # Still in units of magnitude Vega, not anymore but need to find reference flux for Rband
                    #print array[i][27]
                    #print
                    array[i][28] = array[i][27] / 10. # Do not have R_band error, look up if I have to fill in special number, or 0

                    if array[i][27] == 0:
                        array[i][27] = -99.
                        array[i][28] = -99.
                    break
                else:
                    array[i][27] = -99.
                    array[i][28] = -99.
            for s in range(31, 46, 1):
                array[i][s] = Filter_wavelengths[s-31]
            
            array[i][21] = SDSS['fr'][j]
            #print array[i][21]   Big R and small r almost same, this is probably actually true, meaning that there is another point that is not showing up
            #print
            array[i][23] = SDSS['fu'][j]
            array[i][25] = SDSS['fg'][j]
            array[i][22] = SDSS['dfr'][j]
            #print array[i][22]
            #print 
            if array[i][22]>threshold:
                array[i][22] = array[i][21] / 10.
            array[i][26] = SDSS['dfg'][j]
            if array[i][26]>threshold:
                array[i][26] = array[i][25] / 10.
            #print 'The error of filter g is: ' , SDSS['dfg'][j]
            array[i][24] = SDSS['dfu'][j]
            if array[i][24]>threshold:
                array[i][24] = array[i][23] / 10.

            array[i][29] = OTHER_BANDS[i][21] # Don't know where to get filter for MAMBO
            array[i][30] = OTHER_BANDS[i][22] # Don't know where to get filter for MAMBO            

            array[i][46] = OTHER_BANDS[i][23]
            #print 'The redshift of the ith is: ' , OTHER_BANDS[i][23]
            #print
            break

        else:
            
            # Have chosen units of mJ
            array[i][0] = OTHER_BANDS[i][0]

            for s in range(1, 9, 1):
                array[i][s] = OTHER_BANDS[i][s] * 1.e-3 #uJy
            

            for s in range(9, 21, 1):

                array[i][s+9] = OTHER_BANDS[i][s]
                
                
            #array[i][25] = OTHER_BANDS[i][21] # Don't know where to get filter for MAMBO
            #array[i][26] = OTHER_BANDS[i][22] # Don't know where to get filter for MAMBO
            
            for t in range(len(R_bands)):
                if array[i][0]==R_bands[t][0]:
                    array[i][27] = some_constant * 10.**(-R_bands[t][1]/2.5) # Still in units of magnitude Vega, not anymore but need to find reference flux for Rband
                    array[i][28] = array[i][27] / 10. # Do not have R_band error, look up if I have to fill in special number, or 0
                    if array[i][27] == 0:
                        array[i][27] = -99.
                        array[i][28] = -99.
                    break

                else:
                    array[i][27] = -99.
                    array[i][28] = -99.

            for s in range(31, 46, 1):
                array[i][s] = Filter_wavelengths[s-31]
            
            for s in range(21, 27, 1):                
                array[i][s] = -99.

            array[i][29] = OTHER_BANDS[i][21] # Don't know where to get filter for MAMBO
            array[i][30] = OTHER_BANDS[i][22] # Don't know where to get filter for MAMBO
            
            array[i][46] = OTHER_BANDS[i][23]
            
'''
#print len(SDSS['fg'])
#print SDSS['fr']
#print some_constant * 10.**(-SDSS['rmag']/2.5)


for i in range(0, len(SDSS['fg']), 1): #len(SDSS['fg'])

    array[i][0] = SDSS['mips'][i]
    #print SDSS['mips'][i]
    #print

    for j in range(0, len(key_names) + len(filter_wavelengths), 3):

        #print key_names[2 * j / 3]

        array[i][j+1] = filter_wavelengths[j / 3]
        
        if SDSS[key_names[2 * j / 3]][i] == 0. and SDSS[key_names[2 * j / 3 + 1]][i] == 0.:

            array[i][j+2] = -99.
            array[i][j+3] = -99.

        elif SDSS[key_names[2 * j / 3 + 1]][i] > threshold and SDSS[key_names[2 * j / 3 ]][i] > threshold:

            array[i][j+2] = -99.
            array[i][j+3] = -99.

        elif SDSS[key_names[2 * j / 3 + 1]][i] > threshold and SDSS[key_names[2 * j / 3 ]][i] == 0.:

            array[i][j+2] = -99.
            array[i][j+3] = -99.
        

        elif SDSS[key_names[2 * j / 3 + 1]][i] > threshold:

            array[i][j+2] = SDSS[key_names[2 * j / 3]][i]
            array[i][j+3] = SDSS[key_names[2 * j / 3]][i] / 10.
            #plt.errorbar(array[i][j+1], array[i][j+2], yerr = array[i][j+3], fmt = '')
            #plt.scatter(np.log10(array[i][j+1]), array[i][j+1] * array[i][j+2])#, ls = '-', alpha = 0.5)

        else:

            array[i][j+2] = SDSS[key_names[2 * j / 3]][i] 
            array[i][j+3] = SDSS[key_names[2 * j / 3 + 1]][i]
            #print SDSS[key_names[2 * j / 3]][i] 
            #print 
            #print SDSS[key_names[2 * j / 3 + 1]][i]
            #print

            #plt.errorbar(array[i][j+2], array[i][j+3], yerr = array[i][j+3], fmt = '')
            #plt.scatter(np.log10(array[i][j+1]), array[i][j+1] * array[i][j+2])#, ls='-', alpha=0.5)  
        #print array[i][j+2]
        #print array[i][j+2]
        #print j

    array[i][46] = SDSS['zs'][i]
    
    #print array[i][2:48:3]
    #plt.plot(np.log10(array[i][1:47:3]), array[i][1:47:3] * array[i][2:48:3], ls = '-', alpha = 0.5)
    #plt.ylim(bottom = 0.)

    #plt.show() 



#print array[0]

np.savetxt('something_new_new_new_new.txt', array)

'''
var = False

#print id_contribution[192]
#print array[192][0]

for i in range(len(id_contribution)):
    
    for j in range(len(array)):
    
        if id_contribution[i] == array[j][0]:

           array[j][50] = agn_contribution[i]
           var = True


    if var == False:
         
        array = np.delete(array, (j), axis = 0)

    var = False


list_contribution = np.arange(0.05, 1.05, 0.10).tolist()
#list_contribution[0] = -.1
list_contribution_name = np.arange(0., 1.10, 0.10).tolist()
#print list_contribution
#print 3.00e18/10.**(12.25)
#print
#for i in range(100):
#    print array[i][3*11+2]
#    print
#    print array[i][3*11+3]
#    print


#print array[1][2:48:3]
#print
#print array[1][3:49:3]

fractions = np.arange(0.0, 1.1, 0.1).tolist()


list1 = []
list2 = []
list3 = []
list4 = []
list5 = []
list6 = []
list7 = []
list8 = []
list9 = []
list10 = []
list11 = []
list12 = []
list13 = []
list14 = []
list15 = []
list16 = []

for j in range(0, len(list_contribution)-1, 1): # len(list_contribution)-1

    for i in range(0, len(array), 1): #len(array)
    
        #print array[i][50]
    
        #if array[i][50] <= 1. and array[i][50] > 0.95:
        
        #plt.figure(j)
        print array[i][50]   
            
        if array[i][50] <  list_contribution[j+1] and array[i][50] >= list_contribution[j]:

            #plt.errorbar(np.log10(3.00e18/(array[i][1:47:3])), (3.00e18/array[i][1:47:3]) * array[i][2:48:3], yerr=(3.00e18/array[i][1:47:3]) * array[i][3:49:3], ls = '-', alpha = 0.5)
            list1.append(3.00e18/filter_wavelengths[0] * array[i][2]* 1.e-29 *(array[i][49]*3.09e19)**2.)
            list2.append(3.00e18/filter_wavelengths[1] * array[i][5]* 1.e-29*(array[i][49]*3.09e19)**2.)
            list3.append(3.00e18/filter_wavelengths[2] * array[i][8]* 1.e-29*(array[i][49]*3.09e19)**2.)
            list4.append(3.00e18/filter_wavelengths[3] * array[i][11]* 1.e-29*(array[i][49]*3.09e19)**2.)
            list5.append(3.00e18/filter_wavelengths[4] * array[i][14]* 1.e-29*(array[i][49]*3.09e19)**2.)
            list6.append(3.00e18/filter_wavelengths[5] * array[i][17]* 1.e-29*(array[i][49]*3.09e19)**2.)
            list7.append(3.00e18/filter_wavelengths[6] * array[i][20]* 1.e-29*(array[i][49]*3.09e19)**2.)
            list8.append(3.00e18/filter_wavelengths[7] * array[i][23]* 1.e-29*(array[i][49]*3.09e19)**2.)
            list9.append(3.00e18/filter_wavelengths[8] * array[i][26]* 1.e-29*(array[i][49]*3.09e19)**2.)
            list10.append(3.00e18/filter_wavelengths[9] * array[i][29]* 1.e-29*(array[i][49]*3.09e19)**2.)
            list11.append(3.00e18/filter_wavelengths[10] * array[i][32]* 1.e-29*(array[i][49]*3.09e19)**2.)
            list12.append(3.00e18/filter_wavelengths[11] * array[i][35]* 1.e-29*(array[i][49]*3.09e19)**2.)
            list13.append(3.00e18/filter_wavelengths[12] * array[i][38]* 1.e-29*(array[i][49]*3.09e19)**2.)
            list14.append(3.00e18/filter_wavelengths[13] * array[i][41]* 1.e-29*(array[i][49]*3.09e19)**2.)
            list15.append(3.00e18/filter_wavelengths[14] * array[i][44]* 1.e-29*(array[i][49]*3.09e19)**2.)
            list16.append(3.00e18/filter_wavelengths[15] * array[i][47]* 1.e-29*(array[i][49]*3.09e19)**2.)
        #plt.title(str(array[i][0]))
        
    array1 = np.asarray(list1)
    array2 = np.asarray(list2)
    array3 = np.asarray(list3)
    array4 = np.asarray(list4)
    array5 = np.asarray(list5)
    array6 = np.asarray(list6)
    array7 = np.asarray(list7)
    array8 = np.asarray(list8)
    array9 = np.asarray(list9)
    array10 = np.asarray(list10)
    array11 = np.asarray(list11)
    array12 = np.asarray(list12)
    array13 = np.asarray(list13)
    array14 = np.asarray(list14)
    array15 = np.asarray(list15)
    array16 = np.asarray(list16)

    #print array16
    
    av_y = []
    
    av_y.append(np.average(array1))
    av_y.append(np.average(array2))
    av_y.append(np.average(array3))
    av_y.append(np.average(array4))
    av_y.append(np.average(array5))
    av_y.append(np.average(array6))
    av_y.append(np.average(array7))
    av_y.append(np.average(array8))
    av_y.append(np.average(array9))
    av_y.append(np.average(array10))
    av_y.append(np.average(array11))
    av_y.append(np.average(array12))
    av_y.append(np.average(array13))
    av_y.append(np.average(array14))
    av_y.append(np.average(array15))
    av_y.append(np.average(array16))
    
    av_y = np.asarray(av_y)

    #print av_y
    
    plt.plot(np.log10(3.00e18/(array[i][1:47:3])), av_y, linewidth = 6, ls = '-', alpha = 0.5)

    #print str(fractions[j])
    array123 = np.loadtxt('/home/dlzr/Desktop/Kirkpatrick Data/MIR'+str(fractions[j+1])+'.txt', skiprows=4)

    plt.plot(np.log10(3.00e14/array123[:, 0]), 0.2e-14*(3.00e14/array123[:, 0])*array123[:, 1], ls = '-', alpha = 0.5)
        
    plt.ylim(0.)
    plt.xlabel('log frequency')
    plt.ylabel('frequency * flux')
    plt.title('Contribution fraction is: ' + str(list_contribution_name[j+1]))
    plt.savefig(str(list_contribution_name[j+1]) + '.pdf')
    plt.show()
    
    list1 = []
    list2 = []
    list3 = []
    list4 = []
    list5 = []
    list6 = []
    list7 = []
    list8 = []
    list9 = []
    list10 = []
    list11 = []
    list12 = []
    list13 = []
    list14 = []
    list15 = []
    list16 = []
   


    
for i in range(0, len(array), 1): #len(array)
    
        #print array[i][50]
    
        #if array[i][50] <= 1. and array[i][50] > 0.95:
        
        #plt.figure(j)
        
    if array[i][50] < .05 and array[i][50] > -.1:
            
        #plt.plot(np.log10(3.00e18/(array[i][1:47:3])), (3.00e18/array[i][1:47:3]) * array[i][2:48:3], ls = '-', alpha = 0.5)
        list1.append(3.00e18/filter_wavelengths[0] * array[i][2])
        list2.append(3.00e18/filter_wavelengths[1] * array[i][5])
        list3.append(3.00e18/filter_wavelengths[2] * array[i][8])
        list4.append(3.00e18/filter_wavelengths[3] * array[i][11])
        list5.append(3.00e18/filter_wavelengths[4] * array[i][14])
        list6.append(3.00e18/filter_wavelengths[5] * array[i][17])
        list7.append(3.00e18/filter_wavelengths[6] * array[i][20])
        list8.append(3.00e18/filter_wavelengths[7] * array[i][23])
        list9.append(3.00e18/filter_wavelengths[8] * array[i][26])
        list10.append(3.00e18/filter_wavelengths[9] * array[i][29])
        list11.append(3.00e18/filter_wavelengths[10] * array[i][32])
        list12.append(3.00e18/filter_wavelengths[11] * array[i][35])
        list13.append(3.00e18/filter_wavelengths[12] * array[i][38])
        list14.append(3.00e18/filter_wavelengths[13] * array[i][41])
        list15.append(3.00e18/filter_wavelengths[14] * array[i][44])
        list16.append(3.00e18/filter_wavelengths[15] * array[i][47])
        #plt.title(str(array[i][0]))
        
array1 = np.asarray(list1)
array2 = np.asarray(list2)
array3 = np.asarray(list3)
array4 = np.asarray(list4)
array5 = np.asarray(list5)
array6 = np.asarray(list6)
array7 = np.asarray(list7)
array8 = np.asarray(list8)
array9 = np.asarray(list9)
array10 = np.asarray(list10)
array11 = np.asarray(list11)
array12 = np.asarray(list12)
array13 = np.asarray(list13)
array14 = np.asarray(list14)
array15 = np.asarray(list15)
array16 = np.asarray(list16)
    
av_y = []
    
av_y.append(np.average(array1))
av_y.append(np.average(array2))
av_y.append(np.average(array3))
av_y.append(np.average(array4))
av_y.append(np.average(array5))
av_y.append(np.average(array6))
av_y.append(np.average(array7))
av_y.append(np.average(array8))
av_y.append(np.average(array9))
av_y.append(np.average(array10))
av_y.append(np.average(array11))
av_y.append(np.average(array12))
av_y.append(np.average(array13))
av_y.append(np.average(array14))
av_y.append(np.average(array15))
av_y.append(np.average(array16))

av_y = np.asarray(av_y)
    
plt.plot(np.log10(3.00e18/(array[i][1:47:3])), 1.e-14*av_y*(3.09e19)**2., linewidth = 6, ls = '-', alpha = 0.5)

array123 = np.loadtxt('/home/dlzr/Desktop/Kirkpatrick Data/MIR'+str(fractions[0])+'.txt', skiprows=4)

plt.plot(np.log10(3.00e14/array123[:, 0]), (3.00e14/array123[:, 0])*array123[:, 1], ls = '-', alpha = 0.5)
        
plt.ylim(0.)
plt.xlabel('log frequency')
plt.ylabel('frequency * flux')
plt.title('Contribution fraction is: ' + str(0.))
plt.savefig(str(0.0) + '.pdf')
plt.show()


list1 = []
list2 = []
list3 = []
list4 = []
list5 = []
list6 = []
list7 = []
list8 = []
list9 = []
list10 = []
list11 = []
list12 = []
list13 = []
list14 = []
list15 = []
list16 = []
            
for i in range(0, len(array), 1): #len(array)
        
    if array[i][50] <= 1. and array[i][50] >= 0.95:
            
        #plt.plot(np.log10(3.00e18/(array[i][1:47:3])), (3.00e18/array[i][1:47:3]) * array[i][2:48:3], ls = '-', alpha = 0.5)
        list1.append(3.00e18/filter_wavelengths[0] * array[i][2])
        list2.append(3.00e18/filter_wavelengths[1] * array[i][5])
        list3.append(3.00e18/filter_wavelengths[2] * array[i][8])
        list4.append(3.00e18/filter_wavelengths[3] * array[i][11])
        list5.append(3.00e18/filter_wavelengths[4] * array[i][14])
        list6.append(3.00e18/filter_wavelengths[5] * array[i][17])
        list7.append(3.00e18/filter_wavelengths[6] * array[i][20])
        list8.append(3.00e18/filter_wavelengths[7] * array[i][23])
        list9.append(3.00e18/filter_wavelengths[8] * array[i][26])
        list10.append(3.00e18/filter_wavelengths[9] * array[i][29])
        list11.append(3.00e18/filter_wavelengths[10] * array[i][32])
        list12.append(3.00e18/filter_wavelengths[11] * array[i][35])
        list13.append(3.00e18/filter_wavelengths[12] * array[i][38])
        list14.append(3.00e18/filter_wavelengths[13] * array[i][41])
        list15.append(3.00e18/filter_wavelengths[14] * array[i][44])
        list16.append(3.00e18/filter_wavelengths[15] * array[i][47])
        #plt.title(str(array[i][0]))
        
array1 = np.asarray(list1)
array2 = np.asarray(list2)
array3 = np.asarray(list3)
array4 = np.asarray(list4)
array5 = np.asarray(list5)
array6 = np.asarray(list6)
array7 = np.asarray(list7)
array8 = np.asarray(list8)
array9 = np.asarray(list9)
array10 = np.asarray(list10)
array11 = np.asarray(list11)
array12 = np.asarray(list12)
array13 = np.asarray(list13)
array14 = np.asarray(list14)
array15 = np.asarray(list15)
array16 = np.asarray(list16)
    
av_y = []
    
av_y.append(np.average(array1))
av_y.append(np.average(array2))
av_y.append(np.average(array3))
av_y.append(np.average(array4))
av_y.append(np.average(array5))
av_y.append(np.average(array6))
av_y.append(np.average(array7))
av_y.append(np.average(array8))
av_y.append(np.average(array9))
av_y.append(np.average(array10))
av_y.append(np.average(array11))
av_y.append(np.average(array12))
av_y.append(np.average(array13))
av_y.append(np.average(array14))
av_y.append(np.average(array15))
av_y.append(np.average(array16))

av_y = np.asarray(av_y)

#print 1.e-26*av_y*(3.09e19)**2.
    
plt.plot(np.log10(3.00e18/(array[i][1:47:3])), 1.e-14*av_y*(3.09e19)**2., linewidth = 6, ls = '-', alpha = 0.5)

array123 = np.loadtxt('/home/dlzr/Desktop/Kirkpatrick Data/MIR'+str(fractions[len(fractions)-1])+'.txt', skiprows=4)

plt.plot(np.log10(3.00e14/array123[:, 0]), (3.00e14/array123[:, 0])*array123[:, 1], ls = '-', alpha = 0.5)
    
plt.ylim(0.)
plt.xlabel('log frequency')
plt.ylabel('frequency * flux')
plt.title('Contribution fraction is: ' + str(1.0))
plt.savefig(str(1.0) + '.pdf')
plt.show()
 
        

y_av = []

for i in range(2, 48, 3):
    
    #print array[:][i]    
    #print
    y_av.append(np.average(array[:][i]))

#print array[:][2:48:3]
#print
#print 3.00e18/(array[0][1:47:3]) * np.mean(array[:][2:48:3])
#print y_av
y_av = np.asarray(y_av)
'''

#for i in range(len(filter_wavelengths)):  # To check if values were taken over good enough, seems to be true!
#    plt.scatter(np.log10(3.00e18 / filter_wavelengths[i]), (3.00e18 / filter_wavelengths[i]) * SDSS[key_names[2*i]][1])

#plt.plot(np.log10(3.00e8/(array[0][1:47:3]*1.e-10)), 3.00e18/(array[0][1:47:3]) * y_av, ls = '-', alpha = 0.5, linewidth = 50.0)
#plt.gca().invert_xaxis()

#plt.show()

'''
for i in range(len(SDSS['fg'])):
        for j in range(len(key_names)-1):

            if j != len(key_names) - 2:
                array[i][j] = SDSS[key_names[j]][i]

            elif j == len(key_names) - 2:
                array[i][j] = some_constant * 10.**(-SDSS[key_names[j]][i] / 2.5)
                array[i][j+1] = array[i][j] / 10.
                

            if array[i][j] > threshold:
                array[i][j] = array[i][j-1] / 10.

            if j != 0 and j%2 == 0 and array[i][j-1] == 0 and array[i][j] == 0:
                #array[i][j-1] = -99.   # This line does not seem to work for some reason??               
                array[i][j] = 1. # So the point equal to zero does have an error. This will hopefully not have an effect on plotting? Will need to change this soon to mark as no data points!
                

            #print array[i][j] 
            
        #print array[i][len(key_names)-1]
    

        #print len(key_names)
        #print len(filter_wavelengths)

        for s in range(len(filter_wavelengths)):
            array[i][len(key_names) + s] = filter_wavelengths[s]
            #print s
            #print array[i][j]
        
        
        array[i][len(key_names) + len(filter_wavelengths)] = SDSS['zs'][i]
'''

#np.savetxt('something_new.txt', array)
#np.savetxt('something.txt', array)








