
class Printer:
    Formats = ['A0', 'A1', 'A2', 'A3', 'A4', 'A5']
    imprimant = []
    base_width = 200
    printer_count = 0
    devices = []


    def __init__(self, avail_paper):
        err = []
        for i in avail_paper:
            if i not in self.Formats:
                err.append(i)
        if err:
            print(f"Some formats are incorrect :{err}")
        
        if "A4" in avail_paper:
            self.format_defaut = 'A4'
        
        self.Fm_avail = avail_paper
        self.devices.append(f"Printer {self.__class__.printer_count}")
        self.__class__.printer_count += 1


    @classmethod
    def show_printers_system(cls):
        print(f"Formats: {cls.Formats},  cls.base_width={cls.base_width}, \n cls.devices={cls.devices}")
        return
    
    def imprimer(self, contenu, impression_format):
        if not impression_format:
            impression_format = self.format_defaut
    
        if impression_format not in self.Fm_avail:
            print(f"Format d'impression non disponible")
            return
        
        if impression_format == 'A4':
            largeur = 50
        elif impression_format == 'A2':
            largeur = 100
        elif impression_format == 'A0':
            largeur = 200

        print(f"{'#'*largeur}")
        i = 0
        contenu_new = contenu.replace('\n', '').replace('\r', '')
        contenu_new.strip()
        while i < len(contenu):
            print(f"{'#  ' + contenu_new[i:i+largeur-6] + '  #'}")
            i = i+largeur-6
        
        print(f"{'#'*largeur}")
        return


    def send(self, zen, *args, **kwargs):
        if args:
            arg = args[0]
        else:
            arg = None
        return self.imprimer(zen, arg)
    


class ColorPrinter(Printer):
    color_map = {
    "black": "30",
    "red": "31",
    "green": "32",
    "yellow": "33",
    "blue": "34",
    "magenta": "35",
    "cyan": "36",
    "white": "37"}
    def __init__(self, avail_paper, devices, color):
        super(ColorPrinter, self).__init__(avail_paper)
        self.color = self.color_map[color] if color in self.color_map else "30"
        self.devices = devices
       

    def imprimer(self, contenu, impression_format):
        if not impression_format:
            impression_format = self.format_defaut
    
        if impression_format not in self.Fm_avail:
            print(f"Format d'impression non disponible")
            return
        
        if impression_format == 'A4':
            largeur = 50
        elif impression_format == 'A2':
            largeur = 100
        elif impression_format == 'A0':
            largeur = 200

        print(f"\033[{self.color}m{'#'*largeur}\033[0m")
        i = 0
        contenu_new = contenu.replace('\n', '').replace('\r', '')
        contenu_new.strip()
        while i < len(contenu):
            print(f"\033[{self.color}m{'#  ' + contenu_new[i:i+largeur-6] + '  #'}\033[0m")
            i = i+largeur-6
        
        print(f"\033[{self.color}m{'#'*largeur}\033[0m")
        return


    def send(self, zen, *args, **kwargs):
        if args:
            arg = args[0]
        else:
            arg = None
        return self.imprimer(zen, arg)

        

    
    
