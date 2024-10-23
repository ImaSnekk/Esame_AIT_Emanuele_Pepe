#importo moduli
import numpy as np
import matplotlib.pyplot as plt
import statistics as stat

##################################################### Estrazione dati

	#data_filename = "/home/s258303@DS.UNITS.IT/Desktop/lez10/datidiagramma.dat"
	#data_filename = "/home/claudia/Scrivania/AbInfo/esame/datidiagramma.dat"

#assegnazione del path del file
#path=input('Inserire il path che leggi nella riga precedente: ')
#data_filename = str(path)

path="/Users\emanu\.spyder-py3\AIT/Nemo_6670.dat"
data_filename = "/Users\emanu\.spyder-py3\AIT/Nemo_6670.dat"

data_filname = np.loadtxt(path,unpack=True)
#apro il file e leggo i dati
data = np.loadtxt(data_filename, delimiter=' ',unpack=True)
M_ass=data[4]
b_y=data[8]
age_parent=data[12]
MsuH=data[0]
m_ini=data[1]


#################################################### Diagramma H-R

colori = ['lightcoral','darkred','red','orangered','chocolate','sandybrown','tan','orange','goldenrod','gold','yellow','lawngreen','forestgreen','lime','aquamarine','cyan','deepskyblue','royalblue','navy','blue','mediumslateblue','blueviolet','darkorcid','plum','purple','fuchsia','mediumvioletred','hotpink','pink'] 
age_bin = np.array([0, 0.05, 0.11, 0.18, 0.26, 0.35, 0.45, 0.57, 0.71, 0.87, 1.07, 1.3, 1.65, 2, 2.5, 3, 3.75, 4.75, 6, 7.5, 9.25, 11.25, 13])

#Creazione diagramma H-R dividendo le stelle in base all'età
plt.figure()
plt.xlim(-0.1, 1)
plt.ylim(9, -4)

plt.xlabel('b-y')
plt.ylabel('M')
plt.title('Diagramma H-R')
plt.gcf().set_size_inches(13, 10)

# Ciclo per plottare i dati
for i in range(len(age_bin) - 1):
    age_min = age_bin[i]
    age_max = age_bin[i + 1]
    ind = np.where((age_parent <= age_max) & (age_parent > age_min))[0]
    labb = "{:.2f} Gyr - {:.2f} Gyr".format(age_min, age_max)
    colour = colori[i % len(colori)]
    plt.scatter(b_y[ind], M_ass[ind], s=4, label=labb, color=colour)


plt.legend(loc='upper right', ncol=2, fontsize='small') 
plt.savefig('diagHR.png')
plt.show()


#---------------------------------------------------------------istogramma metallicità 1 
#questa parte di esercizio non è svolta con un ciclo for per poter impostare per ogni popolazione stellare il numero di bin ottimale e le caratteristiche di ogni grafico in maniera indipendente

plt.figure(figsize=(10, 7))

#divisione delle stelle in 3 popolazioni in base all'età
pop1 = np.where(age_parent<=1)[0]
pop2 = np.where((age_parent<=5) & (age_parent>1))[0]
pop3 = np.where(age_parent>5)[0]

#labbette per le tre popolazioni stellati
labb1 = "Pop 1: < 1 Gyr"
labb2 = "Pop 2: 1 Gyr - 5 Gyr"
labb3 = "Pop 3: > 5 Gyr"

#istogramma della metallicità delle popolazioni stellari
hist1, bin_edges1 = np.histogram(MsuH[pop1], bins=9)
hist2, bin_edges2 = np.histogram(MsuH[pop2], bins=19)
hist3, bin_edges3 = np.histogram(MsuH[pop3], bins=7)

#il valore del bin viene centrato
bin_centers1 = (bin_edges1[:-1] + bin_edges1[1:]) / 2
bin_centers2 = (bin_edges2[:-1] + bin_edges2[1:]) / 2
bin_centers3 = (bin_edges3[:-1] + bin_edges3[1:]) / 2


# Creazione dei 3 subplots (3 righe e 1 colonna)
fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(8, 12))
fig.suptitle('Distribuzione della Metallicità per Popolazioni Stellari', fontsize=16)

# Istogramma per pop1
hist1, bin_edges1 = np.histogram(MsuH[pop1], bins=7)  # Ridotto il numero di bin a 7
bin_centers1 = (bin_edges1[:-1] + bin_edges1[1:]) / 2
ax1.bar(bin_centers1, hist1, width=0.2113, color='deepskyblue', edgecolor='k',alpha=1)  # Aumentato 'width' per maggiore separazione
ax1.set_title(labb1)
ax1.set_xlabel('Metallicità')
ax1.set_ylabel('Numero di stelle')

# Istogramma per pop2
hist2, bin_edges2 = np.histogram(MsuH[pop2], bins=10)  # Numero di bin ottimale per la popolazione 2
bin_centers2 = (bin_edges2[:-1] + bin_edges2[1:]) / 2
ax2.bar(bin_centers2, hist2, width=0.2112, color='forestgreen', edgecolor='k', alpha=1)  # Aumentato 'width' per evitare sovrapposizioni
ax2.set_title(labb2)
ax2.set_xlabel('Metallicità')
ax2.set_ylabel('Numero di stelle')

# Istogramma per pop3
hist3, bin_edges3 = np.histogram(MsuH[pop3], bins=8)  # Ridotto il numero di bin a 5
bin_centers3 = (bin_edges3[:-1] + bin_edges3[1:]) / 2
ax3.bar(bin_centers3, hist3, width=0.32, color='crimson', edgecolor='k', alpha=1)  # Aumentato 'width' per evitare sovrapposizioni
ax3.set_title(labb3)
ax3.set_xlabel('Metallicità')
ax3.set_ylabel('Numero di stelle')

# Ottimizzazione layout
plt.tight_layout(rect=[0, 0, 1, 0.96])

# Salva e mostra l'immagine
plt.savefig('pop_distrib_split.png')
plt.show()


##########################istogramma metallicità 2 + statistica

#media e mediana per ogni popolazione stellare
	#pop1
plt.plot(bin_centers1, hist1, drawstyle = 'steps-mid', marker='',color='deepskyblue',linewidth=2,label=labb1, alpha=0.6)    
plt.plot([stat.median(MsuH[pop1]),stat.median(MsuH[pop1])],[0,1250],color='deepskyblue',linewidth=2, linestyle = 'dashed',label='Pop 1 mediana')
plt.plot([stat.mean(MsuH[pop1]),stat.mean(MsuH[pop1])],[0,1250],color='deepskyblue',linewidth=2, linestyle = 'dotted',label='Pop 1 media')

	#pop2
plt.plot(bin_centers2, hist2, drawstyle = 'steps-mid', marker='',color='forestgreen',linewidth=2,label=labb2, alpha=0.6)
plt.plot([stat.median(MsuH[pop2]),stat.median(MsuH[pop2])],[0,1250],color='forestgreen',linewidth=2, linestyle = 'dashed',label='Pop 2 mediana')
plt.plot([stat.mean(MsuH[pop2]),stat.mean(MsuH[pop2])],[0,1250],color='forestgreen',linewidth=2, linestyle = 'dotted',label='Pop 2 media')

	#pop3
plt.plot(bin_centers3, hist3, drawstyle = 'steps-mid', marker='',color='crimson',linewidth=2,label=labb3, alpha=0.6)
plt.plot([stat.median(MsuH[pop3]),stat.median(MsuH[pop3])],[0,1250],color='crimson',linewidth=2, linestyle = 'dashed',label='Pop 3 mediana')
plt.plot([stat.mean(MsuH[pop3]),stat.mean(MsuH[pop3])],[0,1250],color='crimson',linewidth=2, linestyle = 'dotted',label='Pop 3 media')

#configurazione grafico
plt.autoscale()
plt.xlabel('Metallicità')
plt.ylabel('Numero di stelle')
plt.legend()
plt.title('Popolazioni stellari')

plt.savefig('pop_distrib2.png')
plt.show()

#valori di media e mediana per ogni popolazione
print("POP1 median metallicity:{}, mean metallicity:{}".format( stat.median(MsuH[pop1]), stat.mean(MsuH[pop1]) ) )
print("POP2 median metallicity:{}, mean metallicity:{}".format( stat.median(MsuH[pop2]), stat.mean(MsuH[pop2]) ) )
print("POP3 median metallicity:{}, mean metallicity:{}".format( stat.median(MsuH[pop3]), stat.mean(MsuH[pop3]) ) )

#--------------------------------------------------------------------------------------------------------metallicità vs massa
#grafico metallicità in funzione della massa per ogni popolazione stellare
plt.figure(figsize=(20, 14))
	#con 'alpha' viene impostata trasparenza per rendere il grafico leggibile
plt.scatter(m_ini[pop1], MsuH[pop1], color = 'deepskyblue',marker = '.', s = 300, edgecolor='k', alpha=1, label=labb1) 
plt.scatter(m_ini[pop2], MsuH[pop2], color = 'forestgreen', marker = '.', s = 300, edgecolor='k', alpha=1, label=labb2)
plt.scatter(m_ini[pop3], MsuH[pop3], color = 'crimson', marker = '.', s = 300, edgecolor='k', alpha=1, label=labb3)

#configurazione grafico
plt.xlim(0.5,7)
plt.ylim(-2,0.65)
plt.autoscale()
plt.xlabel('Massa')
plt.ylabel('Metallicità')
plt.legend()
plt.title('Popolazioni stellari')

plt.savefig('metallicity_mass.png')
plt.show()

#---------------------------------------------------------------------------------------------ottimizzazione visualizzazione
#la visualizzazione del grafico precedente viene ottimizzata spacchettandolo in 3 subplots, graficati vicini per rendere facile il confronto tra loro e il grafico copltessivo

fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(15, 10))
fig.suptitle('Metallicità vs Massa')

#configurazione grafico pop1
ax1.scatter(m_ini[pop1], MsuH[pop1],color = 'deepskyblue', marker = '.', s = 20, label=labb1, alpha=0.6)
ax1.set_ylabel('pop1')
ax1.set(xlim=(0.5,7), ylim=(-2,0.65))

#configurazione grafico pop2
ax2.scatter(m_ini[pop2], MsuH[pop2],color = 'forestgreen', marker = '.', s = 20, label=labb2, alpha=0.4)
ax2.set(xlim=(0.5,7), ylim=(-2,0.65))
ax2.set_ylabel('pop2')

#configurazione grafico pop3
ax3.scatter(m_ini[pop3], MsuH[pop3],color = 'crimson', marker = '.', s = 20, label=labb3, alpha=0.5)
ax3.set(xlim=(0.5,7), ylim=(-2,0.65))
ax3.set_ylabel('pop3')
plt.savefig('pop_metallicity_mass.png')
plt.show()


#link dei dati
#https://raw.githubusercontent.com/MilenaValentini/TRM_Dati/main/Nemo_6670.dat
