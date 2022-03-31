# This is a sample Python script.

# Press Umschalt+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

liste_mit_namen = ['Janis', 'Jens', 'Albert', 'Paul']
liste_mit_nachnamen = ["Golombek", "Golombek", "Blazek", "Glaysher"]

#def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    #print(f'Hi, {name}')  # Press Strg+F8 to toggle the breakpoint.

def get_tuple():
    return (1, 5)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    erster_wert, zweiter_wert = get_tuple()
    print("Mein erster Wert is {} und zweiter Wert ist {}".format(erster_wert, zweiter_wert))
    # for i, (vorname, nachname) in enumerate(zip(liste_mit_namen, liste_mit_nachnamen)):
    #     print(str(i) + " " + vorname + " " + nachname)



# See PyCharm help at https://www.jetbrains.com/help/pycharm/
