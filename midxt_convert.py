import mido as m
import sys

buffer = ""

if not sys.argv[1]:
    midifile = input("midi file: ")
else:
    midifile = sys.argv[1]

def append(data):
    buffer = buffer + data + "\n"

fl = m.MidiFile(midifile)
for msg in fl:
    match msg.type:
        case "note_on":
            append(msg.type)
            append(msg.channel)
            append(msg.note)
            append(msg.channel)
            append(msg.time)
        case "note_off":
            append(msg.type)
            append(msg.time)
        case "program_change":
            append(msg.type)
            append(msg.channel)
            append(msg.time)
        case "set_tempo":
            append(msg.type)
            append(msg.tempo)
        case "end_of_track":
            append(msg.type)
        case _:
            append("wait")
            append(msg.time)