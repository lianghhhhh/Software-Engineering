class HomeTheaterFacade:
    def __init__(self, dvd_player, projector, sound_system, lights):
        self.dvd_player = dvd_player
        self.projector = projector
        self.sound_system = sound_system
        self.lights = lights

    def watch_movie(self, movie):
        print("Get ready to watch a movie...")
        self.lights.dim(10)
        self.projector.on()
        self.sound_system.on()
        self.sound_system.set_volume(5)
        self.dvd_player.on()
        self.dvd_player.play(movie)

    def end_movie(self):
        print("Shutting down the home theater...")
        self.lights.on()
        self.projector.off()
        self.sound_system.off()
        self.dvd_player.stop()
        self.dvd_player.off()

class DVDPlayer:
    def on(self):
        print("DVD Player is now ON.")

    def off(self):
        print("DVD Player is now OFF.")

    def play(self, movie):
        print(f"Playing movie: {movie}")

    def stop(self):
        print("Stopping the movie.")

class Projector:
    def on(self):
        print("Projector is now ON.")

    def off(self):
        print("Projector is now OFF.")

class SoundSystem:
    def on(self):
        print("Sound System is now ON.")

    def off(self):
        print("Sound System is now OFF.")

    def set_volume(self, level):
        print(f"Setting volume to {level}.")

class Lights:
    def dim(self, level):
        print(f"Dimming lights to {level}%.")

    def on(self):
        print("Lights are now ON.")

# Example usage:
if __name__ == "__main__":
    dvd_player = DVDPlayer()
    projector = Projector()
    sound_system = SoundSystem()
    lights = Lights()

    home_theater = HomeTheaterFacade(dvd_player, projector, sound_system, lights)
    home_theater.watch_movie("Avatar")
    print("\n--- Movie is playing ---\n")
    home_theater.end_movie()