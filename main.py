from os import path
import sys

import merchantsguidetogalaxy


class MerchantsGuideToGalaxyApp:
    def __init__(self):
        self._merchantsGuideToGalaxy = merchantsguidetogalaxy.MerchantsGuideToGalaxy()

    def runFromFile(self, fileName):
        if not path.exists(fileName):
            print("cannot find input file: {}".format(fileName))
            return

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
    merchantsGuideToGalaxyApp = MerchantsGuideToGalaxyApp()

    if len(sys.argv) == 2:
        merchantsGuideToGalaxyApp.runFromFile(sys.argv[1])
    else:
        merchantsGuideToGalaxyApp.runLive()


if __name__ == "__main__":
    main()
