from docxtpl import DocxTemplate
import random


def get_different_numbers(n):
    x = list(range(64, 128))
    random.shuffle(x)
    return x[0:n]


doc = DocxTemplate("template.docx")

dec_to_bin = get_different_numbers(3)
dec_to_oct = get_different_numbers(3)

bin_to_dec = get_different_numbers(3)
oct_to_dec = get_different_numbers(3)


context = {'dec_to_bin_1': dec_to_bin[0],
           'dec_to_bin_2': dec_to_bin[1],
           'dec_to_bin_3': dec_to_bin[2],
           'dec_to_oct_1': dec_to_oct[0],
           'dec_to_oct_2': dec_to_oct[1],
           'dec_to_oct_3': dec_to_oct[2],
           'bin_to_dec_1': bin(bin_to_dec[0])[2:],
           'bin_to_dec_2': bin(bin_to_dec[1])[2:],
           'bin_to_dec_3': bin(bin_to_dec[2])[2:],
           'oct_to_dec_1': oct(oct_to_dec[0])[2:],
           'oct_to_dec_2': oct(oct_to_dec[1])[2:],
           'oct_to_dec_3': oct(oct_to_dec[2])[2:],
           }
doc.render(context)
doc.save("template-final.docx")
