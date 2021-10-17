from docxtpl import DocxTemplate
import random


def get_variant_number(numbers):
    alpha = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ+_'
    return ''.join([alpha[i] for i in list(map(lambda x: x - 64, numbers))])


def get_different_numbers(n):
    x = list(range(64, 128))
    random.shuffle(x)
    return x[0:n]


def make_numbered_docx(template, outputdir):
    doc = DocxTemplate(template)

    dec_to_bin = get_different_numbers(3)
    dec_to_oct = get_different_numbers(3)

    bin_to_dec = get_different_numbers(3)
    oct_to_dec = get_different_numbers(3)

    questions = [dec_to_bin,
                 dec_to_oct,
                 list(map(lambda x: bin(x)[2:], bin_to_dec)),
                 list(map(lambda x: oct(x)[2:], oct_to_dec)),
                 ]
    print(questions)
    answers = [list(map(lambda x: bin(x)[2:], dec_to_bin)),
               list(map(lambda x: oct(x)[2:], dec_to_oct)),
               bin_to_dec,
               oct_to_dec,
               ]

    variant = get_variant_number(dec_to_bin + dec_to_oct + bin_to_dec + oct_to_dec)
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
               'variant': variant,
               }
    doc.render(context)
    doc.save(f"{outputdir}/{variant}.docx")

    f = open(f'{outputdir}/{variant}.txt', 'w')
    msg = ''
    for answ in answers:
        msg += str(' '.join(list(map(str, answ))))+'\n'
    f.write(msg)
    f.close()

    return ()


for _ in range(20):
    make_numbered_docx('template.docx', 'output')
