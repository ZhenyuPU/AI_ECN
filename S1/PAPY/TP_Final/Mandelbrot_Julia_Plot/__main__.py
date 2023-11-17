#!/usr/bin/env python
import argparse
from .TP import plot_mandelbrot, plot_julia #Importer le module ou la fonction à tester

def main():
    parser = argparse.ArgumentParser(description='Generate Mandelbrot and Julia Set Image')   
    parser.add_argument('name', type = str, default = None, help = 'Generate Mandelbrot ou Julia')
    parser.add_argument('-c', '--c_de_Julia', type = complex, default = -0.8 + 0.156j, help = 'Julia parameter')
    parser.add_argument('--zmin', type = complex, default = -2-2j, help = 'Minimum complex value')
    parser.add_argument('--zmax', type = complex, default = 2+2j, help = 'Maximum complex value')
    parser.add_argument('--pixel_size', type = float, default = 5e-4, help = 'Pixel size')
    parser.add_argument('--max_iter', type = int, default = 50, help = 'Maximum iteration')
    parser.add_argument('-o', '--output', default = 'output.png', help='Output file name')
    
    args = parser.parse_args()
    
    name = args.name

    if name == None:
        name = input("Please input the chosen module name (MandelbrotPlot or JuliaPlot): ")

    if name == 'MandelbrotPlot':
        plot_mandelbrot(zmin = args.zmin, zmax = args.zmax, pixel_size = args.pixel_size, max_iter = args.max_iter, figname = args.output)
    elif name == 'JuliaPlot':
        plot_julia(c = args.c_de_Julia, zmin = args.zmin, zmax = args.zmax, pixel_size = args.pixel_size, max_iter = args.max_iter, figname = args.output)
    else:
        print("Invalid module name. Please choose MandelbrotPlot or JuliaPlot.")
    
        
if __name__ == '__main__':
    main()
