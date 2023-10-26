
import unittest
import os
from PIL import Image
from TP_final import plot_mandelbrot, plot_julia # 导入要测试的模块或函数

class TestHelloWorld(unittest.TestCase):
    def test_plot(self):
        generate_iamge = Image.open('TP_final/Mandelbrot.png')
        expected_image = Image.open('TP_origine_img/text')
        assert generate_iamge == expected_image
        os.remove('TP_final/Mandelbrot.png')
if __name__ == '__main__':
    unittest.main()
