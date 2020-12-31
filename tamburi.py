import argparse
import musicalbeeps

def shruthi(s):
  if s == "1" or s == "C" or s == "c":
    return ["G4", "C5", "C4"]
  if s == "1.5" or s == "C#" or s == "c#":
    return ["G4#", "C5#", "C4#"]
  if s == "2" or s == "D" or s == "d":
    return ["A4", "D5", "D4"]
  if s == "2.5" or s == "D#" or s == "d#":
    return ["A4#", "D5#", "D4#"]
  if s == "3" or s == "E" or s == "e":
    return ["B4", "E5", "E4"]
  if s == "4" or s == "F" or s == "f":
    return ["C5", "F5", "F4"]
  if s == "4.5" or s == "F#" or s == "f#":
    return ["C5#", "F5#", "F4#"]
  if s == "5" or s == "G" or s == "g":
    return ["D5", "G5", "G4"]
  if s == "5.5" or s == "G#" or s == "g#":
    return ["D5#", "G5#", "G4#"]
  if s == "6" or s == "A" or s == "a":
    return ["E5", "A5", "A4"]
  if s == "6.5" or s == "A#" or s == "a#":
    return ["F5", "A5#", "A4#"]
  if s == "7" or s == "B" or s == "b":
    return ["F5#", "B5", "B4"]

if __name__ == "__main__":
  try:
    parser = argparse.ArgumentParser()
    parser.add_argument("-s", "--shruthi", help="yav pitch beku?", type=shruthi, default="C")
    args = parser.parse_args()

    if args.shruthi:
      pa, mel_sa, sa = args.shruthi
      player = musicalbeeps.Player(volume=1, mute_output=False)
      while True:
        player.play_note(pa, 1);
        player.play_note(mel_sa, .5);
        player.play_note(mel_sa, .5);
        player.play_note(sa, 1);
  except KeyboardInterrupt:
    print()
    exit()
