from peli import Peli


def main():
    while True:
        print("Valitse pelataanko"
              "\n (a) Ihmistä vastaan"
              "\n (b) Tekoälyä vastaan"
              "\n (c) Parannettua tekoälyä vastaan"
              "\nMuilla valinnoilla lopetetaan"
              )

        vastaus = input()

        print(
                "Peli loppuu kun pelaaja antaa virheellisen siirron eli jonkun muun kuin k, p tai s"
            )

        if vastaus.endswith("a"):
            kaksinpeli = Peli.pvp()
            kaksinpeli.pelaa()
        elif vastaus.endswith("b"):
            yksinpeli = Peli.tekoaly()
            yksinpeli.pelaa()
        elif vastaus.endswith("c"):
            haastava_yksinpeli = Peli.parempi_tekoaly()
            haastava_yksinpeli.pelaa()
        else:
            break


if __name__ == "__main__":
    main()
