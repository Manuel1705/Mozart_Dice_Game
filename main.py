#!/usr/bin/env python3
"""
Mozart Dice Game – Minuetto
---------------------------
Questo script implementa il gioco dei dadi musicali di Mozart.
Per ogni una delle 16 misure viene simulato il lancio di due dadi che,
in base ad una tabella predefinita, seleziona un frammento musicale.
Il frammento (un numero) viene poi utilizzato per generare una misura MIDI
(semplificata, in questo esempio: 4 note con altezza determinata dal numero).
Infine, il file MIDI viene scritto su disco e riprodotto.
"""

import random
import time
from midiutil import MIDIFile
import pygame

# Tabella del Minuetto del Mozart Dice Game
# Per ogni misura (1..16) è indicata una lista di 11 valori corrispondenti alla somma dei dadi (da 2 a 12)
minuet_table = {
    1:  [96, 32, 69, 40, 148, 104, 152, 119, 98, 3, 54],
    2:  [22, 6, 95, 47, 141, 128, 113, 163, 27, 167, 74],
    3:  [141, 128, 113, 163, 27, 167, 74, 116, 68, 106, 15],
    4:  [41, 63, 3, 72, 69, 40, 148, 104, 152, 119, 98],
    5:  [105, 146, 35, 107, 25, 155, 16, 65, 145, 152, 90],
    6:  [45, 100, 20, 108, 122, 146, 40, 110, 125, 101, 83],
    7:  [2, 86, 52, 95, 142, 150, 178, 127, 97, 105, 75],
    8:  [160, 99, 150, 40, 120, 15, 8, 136, 167, 67, 97],
    9:  [96, 32, 69, 40, 148, 104, 152, 119, 98, 3, 54],
    10: [22, 6, 95, 47, 141, 128, 113, 163, 27, 167, 74],
    11: [141, 128, 113, 163, 27, 167, 74, 116, 68, 106, 15],
    12: [41, 63, 3, 72, 69, 40, 148, 104, 152, 119, 98],
    13: [105, 146, 35, 107, 25, 155, 16, 65, 145, 152, 90],
    14: [45, 100, 20, 108, 122, 146, 40, 110, 125, 101, 83],
    15: [2, 86, 52, 95, 142, 150, 178, 127, 97, 105, 75],
    16: [160, 99, 150, 40, 120, 15, 8, 136, 167, 67, 97]
}


def roll_two_dices():
    """Simula il lancio di due dadi e restituisce la somma (tra 2 e 12)"""
    return random.randint(1,6) + random.randint(1,6)

def generate_composition():
    """Genera la composizione secondo il Mozart Dice Game.
       Restituisce una lista di 16 numeri (i frammenti scelti)."""
    composition = []
    for measure in range(1, 17):
        dice_sum = roll_two_dices()
        # L'indice nella lista parte da 0 (per somma 2) fino a 10 (per somma 12)
        fragment = minuet_table[measure][dice_sum - 2]
        composition.append(fragment)
    return composition

def create_midi(composition, filename="mozart_dice_game.mid"):
    """Crea un file MIDI a partire dalla composizione.
       Per ogni misura vengono generate 4 note (quarter notes) con una nota calcolata in base al frammento."""
    tempo = 120       # BPM
    track = 0
    channel = 0
    time_start = 0    # inizio della traccia
    duration = 1      # durata in battiti (quarter note)
    volume = 100

    midi = MIDIFile(1)  # una traccia
    midi.addTempo(track, time_start, tempo)

    current_time = 0
    for fragment in composition:
        # Mappa il numero del frammento in un pitch:
        # ad esempio, si parte da 60 (C4) e si aggiunge il resto della divisione per 12.
        pitch = 60 + (fragment % 12)
        # Genera 4 note consecutive (una misura in 4/4)
        for i in range(4):
            midi.addNote(track, channel, pitch, current_time, duration, volume)
            current_time += duration

    # Salva il file MIDI
    with open(filename, "wb") as f:
        midi.writeFile(f)
    print(f"File MIDI creato: {filename}")

def play_midi(filename="mozart_dice_game.mid"):
    """Riproduce il file MIDI usando pygame.
       Attenzione: la riproduzione dei MIDI con pygame dipende dal sistema."""
    pygame.init()
    pygame.mixer.init()
    try:
        pygame.mixer.music.load(filename)
        pygame.mixer.music.play()
        print("Riproduzione in corso...")
        # Attende che la riproduzione termini
        while pygame.mixer.music.get_busy():
            time.sleep(0.1)
    except Exception as e:
        print("Errore durante la riproduzione MIDI:", e)
    finally:
        pygame.mixer.music.stop()
        pygame.quit()

def main():
    print("Generazione della composizione secondo il Mozart Dice Game...")
    composition = generate_composition()
    print("Frammenti scelti per le 16 misure:", composition)

    midi_filename = "composition.mid"
    create_midi(composition, midi_filename)
    play_midi(midi_filename)

if __name__ == '__main__':
    main()