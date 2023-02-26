from subprocess import call


class VolumeHandControl:
    def __init__(self):
        self.volume = 0

    def change(self, volume):
        try:
            if volume != self.volume:
                self.volume = int(volume)
                if volume <= 100 and volume >= 0:
                    call(["amixer", "-D", "pulse",
                         "sset", "Master", f"{volume}%"])
        except ValueError:
            pass


def main():
    control = VolumeHandControl()
    control.volume(100)


if __name__ == "__main__":
    main()
