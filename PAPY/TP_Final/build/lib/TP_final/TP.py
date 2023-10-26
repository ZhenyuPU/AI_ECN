import matplotlib.pyplot as plt
import numpy as np
from PIL import Image


# constants:
candidat = 0.5
parametre = 0.5

def suite(z,c, max_iter)-> complex:
    """Générateur des éléments de la suite $z_{n+1}=z_n^2+c$
    
    c.f. Chapitre 2"""
    for _ in range(max_iter):
        yield z
        z = z ** 2 + c

def suite_mandelbrot(max_iter, z=0,c = candidat)-> complex:
    """Renvoie la suite de Mandelbrot"""
    return suite(z,c, max_iter)

def suite_julia(max_iter, z=candidat,c=parametre)-> complex:
    """Renvoie la suite de julia pour candidat et parametre"""
    if z == 0:
        raise ValueError("z ne peut pas être 0")
    return suite(z,c, max_iter)

def is_in_Mandelbrot(c, max_iter = 50):
    list = suite_mandelbrot(z = 0, c = c, max_iter = max_iter)
    timer = 0
    r = 2     # rayon
    for item in list:
        timer += 1
        if timer >= max_iter:
            return True
        if abs(item) > r:
            return False
        

def is_in_Mandelbrot_new(c, max_iter = 50):
    r = 2     # rayon
    list = suite_mandelbrot(z = 0, c = c, max_iter = max_iter)
    for item in list:
        if abs(item) > r:
            return False
    return True

def is_in_Julia(z, c, max_iter = 50):
    list = suite_julia(z = z, c = c, max_iter = max_iter)
    timer = 0
    r = 2    # rayon
    for item in list:
        timer += 1
        if timer >= max_iter:
            return True
        if abs(item) > 2:
            return False

def is_in_Julia_new(z, c, max_iter = 50):
    r = 2     # rayon
    list = suite_julia(z = z, c = c, max_iter = max_iter)
    for item in list:
        if abs(item) > r:
            return False
    return True



def plot_mandelbrot(zmin = -2-2j, zmax = 2+2j, 
                    pixel_size = 0.001, max_iter = 50, 
                    figname = 'Mandelbrot.png'):
    w = int(1 / pixel_size)  # 在实部上均匀分隔的点数
    h = int(1 / pixel_size)  # 在虚部上均匀分隔的点数
    bitmap = Image.new("RGB", (w, h), "white")
    pix = bitmap.load()
    
    # 在实部和虚部上创建等间距的值
    real_values = np.linspace(zmin.real, zmax.real, w)
    imag_values = np.linspace(zmin.imag, zmax.imag, h)

    for x in range(w):
        for y in range(h):
            real_value = real_values[x]
            imag_value = imag_values[y]
            c = complex(real_value, imag_value)
            if is_in_Mandelbrot_new(c, max_iter = max_iter):
                pix[x, y] = (0, 0, 0)
    bitmap.save(figname)
    bitmap.show()


def plot_julia(c, zmin = -1, zmax = 1, 
               pixel_size = None, max_iter = 50, 
               figname = "Julia.png"):
    w = int(1 / pixel_size)  # 在实部上均匀分隔的点数
    h = int(1 / pixel_size)  # 在虚部上均匀分隔的点数
    bitmap = Image.new("RGB", (w, h), "white")
    pix = bitmap.load()

    # 在实部和虚部上创建等间距的值
    real_values = np.linspace(zmin.real, zmax.real, w)
    imag_values = np.linspace(zmin.imag, zmax.imag, h)
    
    for x in range(w):
        for y in range(h):
            real_value = real_values[x]
            imag_value = imag_values[y]
            z = complex(real_value, imag_value)
            if is_in_Julia_new(z = z, c = c, max_iter = max_iter):
                pix[x, y] = (0, 0, 0)
    bitmap.save(figname)
    bitmap.show()


if __name__ == '__main__':
    is_in_Mandelbrot(c = 0.251)

    is_in_Mandelbrot(c = 0.251, max_iter = 100)

    is_in_Julia(z = 0.25 + 0.25j, c = 0.25)
    plot_mandelbrot(zmin=-0.7440+0.1305j,
                    zmax=-0.7425+0.1320j,
                    pixel_size=5e-4,
                    max_iter=200,figname="Mandelbrot_tentacle.png")
    plot_julia(c=-0.8 + 0.156j,
                zmin=-2-1j,
                zmax=2+1j,
                pixel_size=5e-4,
                max_iter=100,
                figname="Julia_-0.8+0.156j.png")