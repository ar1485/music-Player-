import pygame
import os
import time
from tkinter import Tk, filedialog

class MusicPlayer:
    def __init__(self):
        pygame.init()
        pygame.mixer.init()
        self.currently_playing = None

    def select_folder(self):
        root = Tk()
        root.withdraw()  # Hide the root window
        folder_path = filedialog.askdirectory()
        root.destroy()
        return folder_path

    def play_music(self, folder_path):
        if not folder_path:
            print("No folder selected!")
            return

        for file_name in os.listdir(folder_path):
            if file_name.endswith('.mp3'):
                file_path = os.path.join(folder_path, file_name)
                print(f"Playing {file_name}")
                pygame.mixer.music.load(file_path)
                pygame.mixer.music.play()
                while pygame.mixer.music.get_busy():
                    time.sleep(1)

    def stop_music(self):
        pygame.mixer.music.stop()

    def pause_music(self):
        pygame.mixer.music.pause()

    def unpause_music(self):
        pygame.mixer.music.unpause()

if __name__ == "__main__":
    player = MusicPlayer()
    folder = player.select_folder()
    player.play_music(folder)
