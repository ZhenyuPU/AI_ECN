def contents(fichier_nom: str):
    f = open(fichier_nom, 'rb')
    try:
        text = f.read()
    finally:
        f.close()
    return text
