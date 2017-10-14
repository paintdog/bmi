def get_bmi(m, l):
    return m / (l ** 2)


def get_bmi_category(bmi):
    if bmi < 16:
        return "starkes Untergewicht"
    elif bmi < 17:
        return "mäßiges Untergewicht"
    elif bmi < 18.5:
        return "leichtes Untergewicht"
    elif bmi < 25:
        return "Normalgewicht"
    elif bmi < 30:
        return "Präadipositas (Übergewicht)"
    elif bmi < 35:
        return "Adipositas Grad I"
    elif bmi < 40:
        return "Adipositas Grad II"
    elif bmi >= 40:
        return "Adipositas Grad III"

    
def main():
    m = input("Bitte geben Sie Ihr Gewicht in kg ein: ")
    m = float(m)
    l = input("Bitte geben Sie Ihre Körpergröße in m ein: ")
    l = float(l)

    print("Ihr BMI beträgt {:.1f} kg/m².\nSie haben {}.".format(get_bmi(m, l), get_bmi_category(get_bmi(m, l))))


if __name__ == "__main__":
    main()
