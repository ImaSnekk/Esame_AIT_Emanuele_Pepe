#!/bin/bash

# Scarica dati
wget https://raw.githubusercontent.com/MilenaValentini/TRM_Dati/main/Nemo_6670.dat
if [ $? -eq 0 ]
	then
		echo OK
	else
		echo FAULT
fi

# Mostra le caratteristiche del file scaricato
ls -l Nemo_6670.dat

export DATA_FILE_PATH=`pwd`/Nemo_6670.dat

# Assegna i permessi
chmod +rwx $DATA_FILE_PATH 

# Inizia esercizio di Python
python3 esameEP_c.py $DATA_FILE_PATH
