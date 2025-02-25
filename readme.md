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

# Mapping delle Note per il Mozart Dice Game

In questo progetto, ogni frammento (espresso come numero intero) viene convertito in una nota MIDI usando la seguente formula:

-   **60** corrisponde al Do centrale (C4).
-   Il valore ottenuto da `(numero % 12)` determina l'intervallo da aggiungere a 60 per ottenere la nota finale.

Di seguito la tabella che mostra il mapping dal resto della divisione per 12 (ovvero, `numero % 12`) alla nota MIDI corrispondente e la relativa notazione musicale occidentale:

| Resto (`numero % 12`) | Pitch MIDI | Nota (notazione occidentale) |
| --------------------- | ---------- | ---------------------------- |
| 0                     | 60         | C4                           |
| 1                     | 61         | C#4 / Db4                    |
| 2                     | 62         | D4                           |
| 3                     | 63         | D#4 / Eb4                    |
| 4                     | 64         | E4                           |
| 5                     | 65         | F4                           |
| 6                     | 66         | F#4 / Gb4                    |
| 7                     | 67         | G4                           |
| 8                     | 68         | G#4 / Ab4                    |
| 9                     | 69         | A4                           |
| 10                    | 70         | A#4 / Bb4                    |
| 11                    | 71         | B4                           |

Questo mapping permette di trasformare in modo semplice un numero in una nota, utilizzando l'aritmetica modulare per ciclare attraverso le 12 note della scala cromatica.
