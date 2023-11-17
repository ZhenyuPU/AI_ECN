USAGE
=====

Mandelbrot_Julia_Plot is a Python project for generating Mandelbrot and Julia set images.

Features
--------

- Generate Mandelbrot set images.
- Generate Julia set images.
- Customize image details, including complex value ranges, pixel size, and maximum iteration count.
- Support custom image generation using command-line parameters.

Installation
------------

You can easily install the Mandelbrot_Julia_Plot project using the following command:

.. code-block:: bash

   $ cd chemin/des/sources
   $ pip install .

Usage Examples
--------------

If you want to use this module, you can input the following command:

.. code-block:: bash

   $ python -m Mandelbrot_Julia_Plot MandelbrotPlot -o mandelbrot.png

If you don't want to input ``python -m Mandelbrot_Julia_Plot`` every time, you can use this command:

.. code-block:: bash

   $ source load_aliases.sh

Then you can easily use ``MandelbrotPlot`` and ``MandelbrotPlot`` as aliases.

Following are certain examples:

Generate a default Mandelbrot set image:

.. code-block:: bash

   $ MandelbrotPlot -o mandelbrot.png

Generate a default Julia set image:

.. code-block:: bash

   $ JuliaPlot -c=-0.8j\
               --pixel_size=1e-3\
               --max-iter=50\
               -o "thunder-julia.png" 


.. image:: https://cdn.statically.io/gh/ZhenyuPU/picx-images-hosting@master/20231027/thunder-julia.68tydezpz8w0.webp
   :width: 300
   :height: 300
   :scale: 50 %
   :align: center
   :alt: Your Image Alt Text


Customize image generation, for example, a Mandelbrot set:

.. code-block:: bash

   $ MandelbrotPlot --zmin=-0.7440+0.1305j\
                   --zmax=-0.7425+0.1320j \
                   --pixel_size=5e-7\
                   --max-iter=50\
                   -o "Mandelbrot_tentacle_lowiter.png"

.. image:: https://cdn.statically.io/gh/ZhenyuPU/picx-images-hosting@master/20231027/Mandelbrot_tentacle_lowiter.6c9q2d9u5t80.png
   :width: 300
   :height: 300
   :scale: 50 %
   :align: center
   :alt: Your Image Alt Text

Documentation
-------------

Detailed project documentation can be found in the project documentation.

Issues and Feedback
-------------------

If you encounter any issues while using the project or need assistance, please feel free to raise an issue, and we will be happy to help.

License
-------

This project is licensed under the MIT License. For details, please refer to the License file.

Thank you for choosing the Mandelbrot_Julia_Plot project! We hope it proves helpful for your work.
