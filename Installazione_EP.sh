#!/bin/bash

# Crea una cartella in cui viene eseguito l'esercizio di Python
mkdir -p Esame_Pepe

# Copia i file necessari nella nuova cartella
cp Esame_AIT_EP.py Esame_Pepe/esameEP_c.py
cp esecuzione_EP.sh Esame_Pepe/esecuzione_EP_c.sh

# Entra nella cartella
cd Esame_Pepe

# Imposta la cartella base dove si trovano gli script
APP_DIR=$(pwd)

# Aggiunge la cartella Esame_Pepe al PYTHONPATH
export PYTHONPATH=$APP_DIR:$PYTHONPATH

# Aggiunge la cartella Esame_Pepe al PATH (se ci sono script eseguibili da chiamare direttamente)
export PATH=$APP_DIR:$PATH

# Aggiungi i permessi di esecuzione allo script Python e a quello Bash
chmod +x esameEP_c.py
chmod +x esecuzione_EP_c.sh

# Conferma che il PATH e il PYTHONPATH sono stati aggiornati
echo "Il PYTHONPATH è: $PYTHONPATH"
echo "Il PATH è: $PATH"

