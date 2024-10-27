#!/bin/bash

# Crea una cartella in cui viene eseguito l'esercizio di Python
mkdir Esame_Pepe

# Copia il file
cp Esame_AIT_EP.py Esame_AIT_EP_c.py
cp Esecuzione_EP.sh Esecuzione_EP_c.sh

# Sposta i file copiati nella cartella
mv Esame_AIT_EP_c.py Esame_Pepe
mv Esecuzione_EP_c.sh Esame_Pepe

# Entra nella cartella
cd Esame_Pepe

# Imposta la cartella base dove si trovano gli script
APP_DIR=`pwd`

# Aggiunge la cartella Esame_Pepe al PYTHONPATH
export PYTHONPATH=$APP_DIR:$PYTHONPATH

# Aggiungi i permessi di esecuzione allo script Python e a quello Bash
chmod +x $APP_DIR/Esame_AIT_EP_c.py
chmod +x $APP_DIR/Esecuzione_EP_c.sh
