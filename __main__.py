import sys
from os.path import dirname, abspath

sys.path.append(dirname(dirname(abspath(__file__))))

from MerchantsGuideToGalaxy import MerchantsGuideToGalaxy


class App:
    def __init__(self):
        self._merchantsGuideToGalaxy = MerchantsGuideToGalaxy()

    def runFromFile(self, fileName):
        with open(fileName) as fp:
            lines = fp.readlines()
            for line in lines:
                self._runMerchantsGuideToGalaxy(line)

    def runLive(self):
        print("running live, type <quit> to exit.\n")
        while True:
            userInput = input()
            if userInput == "quit":
                break
            self._runMerchantsGuideToGalaxy(userInput)

    def _runMerchantsGuideToGalaxy(self, userInput):
        response = self._merchantsGuideToGalaxy.getHelp(userInput)
        if response:
            print(response)


def main():
    app = App()

    if len(sys.argv) == 2:
        app.runFromFile(sys.argv[1])
    else:
        app.runLive()


if __name__ == "__main__":
    main()
