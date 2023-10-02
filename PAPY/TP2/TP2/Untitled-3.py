class Printer:
    formats_autorises = ["A0", "A1", "A2", "A3", "A4", "A5"]
    imprimantes = []
    base_width = 200

    @classmethod
    def show_printers_system(cls):
        system_info = f"Formats: {cls.formats_autorises}, cls.base_width={cls.base_width},\n cls.devices={cls.imprimantes}"
        return system_info

    def __init__(self, avail_paper):
        invalid_formats = set(avail_paper) - set(self.formats_autorises)
        if invalid_formats:
            raise ValueError(f"Some formats are incorrect :{invalid_formats}")
        
        if "A4" in avail_paper:
            self.format_par_defaut = "A4"
        else:
            self.format_par_defaut = avail_paper[0]
        
        self.avail_paper = avail_paper
        self.__class__.imprimantes.append(f"Printer {len(self.__class__.imprimantes)}")

    def imprimer(self, contenu, format_impression=None):
        if format_impression is None:
            format_impression = self.format_par_defaut
        
        if format_impression not in self.avail_paper:
            raise ValueError(f"Format d'impression non disponible")
        
        largeur = self.base_width // (2 ** (self.formats_autorises.index(format_impression) - self.formats_autorises.index("A0")))
        print(f"Imprimante - Format : {format_impression}, Largeur : {largeur} caractères")
        print(contenu)
        print("=" * largeur)

# Exemple d'utilisation
generic_printer = Printer(avail_paper=["B1", "A4", "A0"])
system_info = Printer.show_printers_system()
print(system_info)
