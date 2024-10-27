#!/bin/bash

#scarico dati
wget https://raw.githubusercontent.com/MilenaValentini/TRM_Dati/main/Nemo_6670.dat
if [ $? -eq 0 ]
	then
		echo OK
	else
		echo FAULT
fi

#mostro le caratteristiche del file scaricato
ls -l Nemo_6670.dat

export DATA_FILE_PATH=`pwd`/Nemo_6670.dat

#assegno i permessi
chmod +rwx $DATA_FILE_PATH 

#inizia esercizio di Python
python3 Esame_AIT_EP_c.py $DATA_FILE_PATH
