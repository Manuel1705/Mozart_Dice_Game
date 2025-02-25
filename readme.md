## Mozart Dice Game

Questo script implementa il gioco dei dadi musicali di Mozart.
Per ogni una delle 16 misure viene simulato il lancio di due dadi che,
in base ad una tabella predefinita, seleziona un frammento musicale.
Il frammento (un numero) viene poi utilizzato per generare una misura MIDI
(semplificata, in questo esempio: 4 note con altezza determinata dal numero).
Infine, il file MIDI viene scritto su disco e riprodotto.

# how to run

to set up the env run ./init.sh

to execute the script run ./run.sh
