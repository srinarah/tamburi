import musicalbeeps
if __name__ == "__main__":
  player = musicalbeeps.Player(volume=1, mute_output=False)
  pa, mel_sa, sa = "D4", "G4", "G3"
  while True:
    player.play_note(pa, 1);
    player.play_note(mel_sa, .5);
    player.play_note(mel_sa, .5);
    player.play_note(sa, 1);
