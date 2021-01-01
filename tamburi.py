import argparse
import musicalbeeps

def shruthi(s):
  swaras = {}
  if s == "1" or s == "C" or s == "c":
    swaras['pa'] = "G4"
    swaras['ma'] = "F4"
    swaras['ni'] = "B4"
    swaras['mel_sa'] = "C5"
    swaras['sa'] = "C4"
  if s == "1.5" or s == "C#" or s == "c#":
    swaras['pa'] = "G4#"
    swaras['ma'] = "F4#"
    swaras['ni'] = "C5"
    swaras['mel_sa'] = "C5#"
    swaras['sa'] = "C4#"
  if s == "2" or s == "D" or s == "d":
    swaras['pa'] = "A4"
    swaras['ma'] = "G4"
    swaras['ni'] = "C5#"
    swaras['mel_sa'] = "D5"
    swaras['sa'] = "D4"
  if s == "2.5" or s == "D#" or s == "d#":
    swaras['pa'] = "A4#"
    swaras['ma'] = "G4#"
    swaras['ni'] = "D5"
    swaras['mel_sa'] = "D5#"
    swaras['sa'] = "D4#"
  if s == "3" or s == "E" or s == "e":
    swaras['pa'] = "B4"
    swaras['ma'] = "A4"
    swaras['ni'] = "D5#"
    swaras['mel_sa'] = "E5"
    swaras['sa'] = "E4"
  if s == "4" or s == "F" or s == "f":
    swaras['pa'] = "C5"
    swaras['ma'] = "A4#"
    swaras['ni'] = "E5"
    swaras['mel_sa'] = "F5"
    swaras['sa'] = "F4"
  if s == "4.5" or s == "F#" or s == "f#":
    swaras['pa'] = "C5#"
    swaras['ma'] = "B4"
    swaras['ni'] = "F5"
    swaras['mel_sa'] = "F5#"
    swaras['sa'] = "F4#"
  if s == "5" or s == "G" or s == "g":
    swaras['pa'] = "D5"
    swaras['ma'] = "C5"
    swaras['ni'] = "F5#"
    swaras['mel_sa'] = "G5"
    swaras['sa'] = "G4"
  if s == "5.5" or s == "G#" or s == "g#":
    swaras['pa'] = "D5#"
    swaras['ma'] = "C5#"
    swaras['ni'] = "G5"
    swaras['mel_sa'] = "G5#"
    swaras['sa'] = "G4#"
  if s == "6" or s == "A" or s == "a":
    swaras['pa'] = "E5"
    swaras['ma'] = "D5"
    swaras['ni'] = "G5#"
    swaras['mel_sa'] = "A5"
    swaras['sa'] = "A4"
  if s == "6.5" or s == "A#" or s == "a#":
    swaras['pa'] = "F5"
    swaras['ma'] = "D5#"
    swaras['ni'] = "A5"
    swaras['mel_sa'] = "A5#"
    swaras['sa'] = "A4#"
  if s == "7" or s == "B" or s == "b":
    swaras['pa'] = "F5#"
    swaras['ma'] = "E5"
    swaras['ni'] = "A5#"
    swaras['mel_sa'] = "B5"
    swaras['sa'] = "B4"
  return swaras

if __name__ == "__main__":
  try:
    parser = argparse.ArgumentParser()
    parser.add_argument("-s", "--shruthi", help="yav pitch beku?", type=shruthi, default="C")
    parser.add_argument("--ma", help="madhyama shruthi", action="store_true", default=False)
    parser.add_argument("--ni", help="kakali shruthi", action="store_true", default=False)
    parser.add_argument("--off", help="bari sa galu", action="store_true", default=False)
    args = parser.parse_args()

    if args.shruthi:
      player = musicalbeeps.Player(volume=1, mute_output=False)
      while True:
        if args.ma:
          player.play_note(args.shruthi["ma"], 1);
        elif args.ni:
          player.play_note(args.shruthi["ni"], 1);
        elif not args.off:
          player.play_note(args.shruthi["pa"], 1);
        player.play_note(args.shruthi["mel_sa"], .5);
        player.play_note(args.shruthi["mel_sa"], .5);
        if args.off:
          player.play_note(args.shruthi["sa"], 2);
        else:
          player.play_note(args.shruthi["sa"], 1);
  except KeyboardInterrupt:
    print()
    exit()
