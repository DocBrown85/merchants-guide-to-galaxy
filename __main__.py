from MerchantsGuideToGalaxy import MerchantsGuideToGalaxy


def main():
    import sys
    from os.path import dirname, abspath

    sys.path.append(dirname(dirname(abspath(__file__))))

    merchantsGuideToGalaxy = MerchantsGuideToGalaxy()
    merchantsGuideToGalaxy.getHelp("glob means I")
    merchantsGuideToGalaxy.getHelp("prok means V")
    merchantsGuideToGalaxy.getHelp("pish means X")
    merchantsGuideToGalaxy.getHelp("tegj means L")
    merchantsGuideToGalaxy.getHelp("glob glob units of Silver are worth 34 Credits")
    merchantsGuideToGalaxy.getHelp("glob prok units of Gold are worth 57800 Credits")
    merchantsGuideToGalaxy.getHelp("pish pish units of Iron are worth 3910 Credits")
    print(merchantsGuideToGalaxy.getHelp("how much is pish tegj glob glob ?"))
    print(merchantsGuideToGalaxy.getHelp("how many Credits is glob prok Silver ?"))
    print(merchantsGuideToGalaxy.getHelp("how many Credits is glob prok Gold ?"))
    print(merchantsGuideToGalaxy.getHelp("how many Credits is glob prok Iron ?"))
    print(
        merchantsGuideToGalaxy.getHelp(
            "how much wood could a woodchuck chuck if a woodchuck could chuck wood ?"
        )
    )


if __name__ == "__main__":
    main()