from PIL import Image
from random import choice
from inputimeout import inputimeout

original_photo = Image.new(('RGB'), (801, 1216), (255, 255, 255))
original_photo.paste((30, 31, 37), (0, 0, 801, 1216))
original_photo.paste((28, 29, 35), (5, 5, 796, 1211))
original_photo.paste((26, 27, 33), (10, 10, 791, 1206))
original_photo.paste((25, 26, 32), (15, 15, 786, 1201))
original_photo.paste((26, 27, 33), (55, 55, 746, 1161))
original_photo.paste((27, 28, 34), (60, 60, 741, 1156))
original_photo.paste((30, 31, 37), (65, 65, 736, 1151))
original_photo.paste((35, 36, 42), (70, 70, 731, 1146))
original_photo.paste((30, 31, 37), (150, 70, 153, 1146))
original_photo.paste((30, 31, 37), (233, 70, 236, 1146))
original_photo.paste((30, 31, 37), (316, 70, 319, 1146))
original_photo.paste((30, 31, 37), (399, 70, 402, 1146))
original_photo.paste((30, 31, 37), (482, 70, 485, 1146))
original_photo.paste((30, 31, 37), (565, 70, 568, 1146))
original_photo.paste((30, 31, 37), (648, 70, 651, 1146))
original_photo.paste((30, 31, 37), (70, 150, 731, 153))
original_photo.paste((30, 31, 37), (70, 233, 731, 236))
original_photo.paste((30, 31, 37), (70, 316, 731, 319))
original_photo.paste((30, 31, 37), (70, 399, 731, 402))
original_photo.paste((30, 31, 37), (70, 482, 731, 485))
original_photo.paste((30, 31, 37), (70, 565, 731, 568))
original_photo.paste((30, 31, 37), (70, 648, 731, 651))
original_photo.paste((30, 31, 37), (70, 731, 731, 734))
original_photo.paste((30, 31, 37), (70, 814, 731, 817))
original_photo.paste((30, 31, 37), (70, 897, 731, 900))
original_photo.paste((30, 31, 37), (70, 980, 731, 983))
original_photo.paste((30, 31, 37), (70, 1063, 731, 1066))

the_starting_point = True
score = 0

while the_starting_point == True:

    print(score)
    List_of_shapes = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11 , 12, 13]
    random_shape = choice(List_of_shapes)
    sub_photo = None
    width = 0
    length = 0
    revolutions = 0
    doop_determinant = 4

    if random_shape == 1:

        while original_photo.getpixel((361 + width, 71 + length)) == (35, 36, 42):

            sub_photo = original_photo.copy()
            sub_photo.paste((0, 200, 0), (319 + width, 70 + length, 399 + width, 150 + length))
            sub_photo.paste((30, 31, 37), (150, 70, 153, 1146))
            sub_photo.paste((30, 31, 37), (233, 70, 236, 1146))
            sub_photo.paste((30, 31, 37), (316, 70, 319, 1146))
            sub_photo.paste((30, 31, 37), (399, 70, 402, 1146))
            sub_photo.paste((30, 31, 37), (482, 70, 485, 1146))
            sub_photo.paste((30, 31, 37), (565, 70, 568, 1146))
            sub_photo.paste((30, 31, 37), (648, 70, 651, 1146))
            sub_photo.paste((30, 31, 37), (70, 150, 731, 153))
            sub_photo.paste((30, 31, 37), (70, 233, 731, 236))
            sub_photo.paste((30, 31, 37), (70, 316, 731, 319))
            sub_photo.paste((30, 31, 37), (70, 399, 731, 402))
            sub_photo.paste((30, 31, 37), (70, 482, 731, 485))
            sub_photo.paste((30, 31, 37), (70, 565, 731, 568))
            sub_photo.paste((30, 31, 37), (70, 648, 731, 651))
            sub_photo.paste((30, 31, 37), (70, 731, 731, 734))
            sub_photo.paste((30, 31, 37), (70, 814, 731, 817))
            sub_photo.paste((30, 31, 37), (70, 897, 731, 900))
            sub_photo.paste((30, 31, 37), (70, 980, 731, 983))
            sub_photo.paste((30, 31, 37), (70, 1063, 731, 1066))
            length += 83
            sub_photo.show()

            try:

                answer = inputimeout(timeout=1.4)
                for i in range(len(answer)):

                    if answer[i] == 'd':

                        if original_photo.getpixel((444 + width, 71 + length)) == (35, 36, 42):

                            width += 83

                    elif answer[i] == 'a':

                        if original_photo.getpixel((278 + width, 71 + length)) == (35, 36, 42):

                            width += -83

            except Exception:
                pass

        original_photo = sub_photo.copy()
        sub_photo = None
        width = 0
        length = 0
        revolutions = 0

    if random_shape == 2:

        while original_photo.getpixel((361 + width, 71 + length)) == (35, 36, 42) and \
        revolutions != 100:

            try:

                while original_photo.getpixel((361 + width, 71 + length)) == (35, 36, 42) and \
                original_photo.getpixel((444 + width, 71 + length)) == (35, 36, 42) and \
                doop_determinant % 2 == 0:

                    sub_photo = original_photo.copy()
                    sub_photo.paste((255, 180, 50), (319 + width, 70 + length, 482 + width, 150 + length))
                    sub_photo.paste((30, 31, 37), (150, 70, 153, 1146))
                    sub_photo.paste((30, 31, 37), (233, 70, 236, 1146))
                    sub_photo.paste((30, 31, 37), (316, 70, 319, 1146))
                    sub_photo.paste((30, 31, 37), (399, 70, 402, 1146))
                    sub_photo.paste((30, 31, 37), (482, 70, 485, 1146))
                    sub_photo.paste((30, 31, 37), (565, 70, 568, 1146))
                    sub_photo.paste((30, 31, 37), (648, 70, 651, 1146))
                    sub_photo.paste((30, 31, 37), (70, 150, 731, 153))
                    sub_photo.paste((30, 31, 37), (70, 233, 731, 236))
                    sub_photo.paste((30, 31, 37), (70, 316, 731, 319))
                    sub_photo.paste((30, 31, 37), (70, 399, 731, 402))
                    sub_photo.paste((30, 31, 37), (70, 482, 731, 485))
                    sub_photo.paste((30, 31, 37), (70, 565, 731, 568))
                    sub_photo.paste((30, 31, 37), (70, 648, 731, 651))
                    sub_photo.paste((30, 31, 37), (70, 731, 731, 734))
                    sub_photo.paste((30, 31, 37), (70, 814, 731, 817))
                    sub_photo.paste((30, 31, 37), (70, 897, 731, 900))
                    sub_photo.paste((30, 31, 37), (70, 980, 731, 983))
                    sub_photo.paste((30, 31, 37), (70, 1063, 731, 1066))
                    length += 83
                    sub_photo.show()

                    try:

                        answer = inputimeout(timeout=1.4)
                        for i in range(len(answer)):

                            if answer[i] == 'd':

                                if doop_determinant % 2 == 0:

                                    if original_photo.getpixel((527 + width, 71 + length)) == (35, 36, 42) and \
                                    original_photo.getpixel((444 + width, 71 + length)) == (35, 36, 42):

                                        width += 83

                                elif doop_determinant % 2 == 1:

                                    if original_photo.getpixel((444 + width, 71 + length)) == (35, 36, 42) and \
                                    original_photo.getpixel((444 + width, 154 + length)) == (35, 36, 42):

                                        width += 83

                            elif answer[i] == 'a':

                                if doop_determinant % 2 == 0:

                                    if original_photo.getpixel((278 + width, 71 + length)) == (35, 36, 42) and \
                                    original_photo.getpixel((361 + width, 71 + length)) == (35, 36, 42):

                                        width += -83

                                elif doop_determinant % 2 == 1:

                                    if original_photo.getpixel((278 + width, 71 + length)) == (35, 36, 42) and \
                                    original_photo.getpixel((278 + width, 154 + length)) == (35, 36, 42):

                                        width += -83

                            elif answer[i] in ['s','w']:

                                if doop_determinant % 2 == 0:

                                    if original_photo.getpixel((361 + width, 71 + length)) == (35, 36, 42) and \
                                    original_photo.getpixel((361 + width, 154 + length)) == (35, 36, 42):

                                        length += -83
                                        doop_determinant += 1

                                elif doop_determinant % 2 == 1:

                                    if original_photo.getpixel((361 + width, 71 + length)) == (35, 36, 42) and \
                                    original_photo.getpixel((444 + width, 71 + length)) == (35, 36, 42):

                                        length += 83
                                        doop_determinant += 1

                    except Exception:
                        pass

                while original_photo.getpixel((361 + width, 154 + length)) == (35, 36, 42) and \
                doop_determinant % 2 == 1:

                    sub_photo = original_photo.copy()
                    sub_photo.paste((255, 180, 50), (319 + width, 70 + length, 399 + width, 233 + length))
                    sub_photo.paste((30, 31, 37), (150, 70, 153, 1146))
                    sub_photo.paste((30, 31, 37), (233, 70, 236, 1146))
                    sub_photo.paste((30, 31, 37), (316, 70, 319, 1146))
                    sub_photo.paste((30, 31, 37), (399, 70, 402, 1146))
                    sub_photo.paste((30, 31, 37), (482, 70, 485, 1146))
                    sub_photo.paste((30, 31, 37), (565, 70, 568, 1146))
                    sub_photo.paste((30, 31, 37), (648, 70, 651, 1146))
                    sub_photo.paste((30, 31, 37), (70, 150, 731, 153))
                    sub_photo.paste((30, 31, 37), (70, 233, 731, 236))
                    sub_photo.paste((30, 31, 37), (70, 316, 731, 319))
                    sub_photo.paste((30, 31, 37), (70, 399, 731, 402))
                    sub_photo.paste((30, 31, 37), (70, 482, 731, 485))
                    sub_photo.paste((30, 31, 37), (70, 565, 731, 568))
                    sub_photo.paste((30, 31, 37), (70, 648, 731, 651))
                    sub_photo.paste((30, 31, 37), (70, 731, 731, 734))
                    sub_photo.paste((30, 31, 37), (70, 814, 731, 817))
                    sub_photo.paste((30, 31, 37), (70, 897, 731, 900))
                    sub_photo.paste((30, 31, 37), (70, 980, 731, 983))
                    sub_photo.paste((30, 31, 37), (70, 1063, 731, 1066))
                    length += 83
                    sub_photo.show()

                    try:

                        answer = inputimeout(timeout=1.4)
                        for i in range(len(answer)):

                            if answer[i] == 'd':

                                if doop_determinant % 2 == 1:

                                    if original_photo.getpixel((444 + width, 71 + length)) == (35, 36, 42) and \
                                    original_photo.getpixel((444 + width, 154 + length)) == (35, 36, 42):

                                        width += 83

                                elif doop_determinant % 2 == 0:

                                    if original_photo.getpixel((527 + width, 71 + length)) == (35, 36, 42) and \
                                    original_photo.getpixel((444 + width, 71 + length)) == (35, 36, 42):

                                        width += 83

                            elif answer[i] == 'a':

                                if doop_determinant % 2 == 1:

                                    if original_photo.getpixel((278 + width, 71 + length)) == (35, 36, 42) and \
                                    original_photo.getpixel((278 + width, 154 + length)) == (35, 36, 42):

                                        width += -83

                                elif doop_determinant % 2 == 0:

                                    if original_photo.getpixel((278 + width, 71 + length)) == (35, 36, 42) and \
                                    original_photo.getpixel((361 + width, 71 + length)) == (35, 36, 42):

                                        width += -83

                            elif answer[i] in ['s','w']:

                                if doop_determinant % 2 == 1:

                                    if original_photo.getpixel((361 + width, 71 + length)) == (35, 36, 42) and \
                                    original_photo.getpixel((444 + width, 71 + length)) == (35, 36, 42):

                                        doop_determinant += 1

                                    elif original_photo.getpixel((278 + width, 71 + length)) == (35, 36, 42) and \
                                    original_photo.getpixel((361 + width, 71 + length)) == (35, 36, 42):

                                        doop_determinant += 1
                                        width += -83

                                elif doop_determinant % 2 == 0:

                                    if original_photo.getpixel((361 + width, 71 + length)) == (35, 36, 42) and \
                                    original_photo.getpixel((361 + width, 154 + length)) == (35, 36, 42):

                                        doop_determinant += 1

                    except Exception:
                        pass
                revolutions += 1

            except Exception:
                pass

        w = 0
        width = 0
        length = 0
        original_photo = sub_photo.copy()
        sub_photo = None
        revolutions = 0
        doop_determinant = 4

    if random_shape == 3:

        while original_photo.getpixel((361 + width, 71 + length)) == (35, 36, 42) and \
        revolutions != 100:

            try:

                while original_photo.getpixel((361 + width, 71 + length)) == (35, 36, 42) and \
                 original_photo.getpixel((444 + width, 71 + length)) == (35, 36, 42) and \
                original_photo.getpixel((527 + width, 71 + length)) == (35, 36, 42) and \
                doop_determinant % 2 == 0:

                    sub_photo = original_photo.copy()
                    sub_photo.paste((0, 180, 255), (319 + width, 70 + length, 565 + width, 150 + length))
                    sub_photo.paste((30, 31, 37), (150, 70, 153, 1146))
                    sub_photo.paste((30, 31, 37), (233, 70, 236, 1146))
                    sub_photo.paste((30, 31, 37), (316, 70, 319, 1146))
                    sub_photo.paste((30, 31, 37), (399, 70, 402, 1146))
                    sub_photo.paste((30, 31, 37), (482, 70, 485, 1146))
                    sub_photo.paste((30, 31, 37), (565, 70, 568, 1146))
                    sub_photo.paste((30, 31, 37), (648, 70, 651, 1146))
                    sub_photo.paste((30, 31, 37), (70, 150, 731, 153))
                    sub_photo.paste((30, 31, 37), (70, 233, 731, 236))
                    sub_photo.paste((30, 31, 37), (70, 316, 731, 319))
                    sub_photo.paste((30, 31, 37), (70, 399, 731, 402))
                    sub_photo.paste((30, 31, 37), (70, 482, 731, 485))
                    sub_photo.paste((30, 31, 37), (70, 565, 731, 568))
                    sub_photo.paste((30, 31, 37), (70, 648, 731, 651))
                    sub_photo.paste((30, 31, 37), (70, 731, 731, 734))
                    sub_photo.paste((30, 31, 37), (70, 814, 731, 817))
                    sub_photo.paste((30, 31, 37), (70, 897, 731, 900))
                    sub_photo.paste((30, 31, 37), (70, 980, 731, 983))
                    sub_photo.paste((30, 31, 37), (70, 1063, 731, 1066))
                    length += 83
                    w += 1
                    sub_photo.show()

                    try:

                        answer = inputimeout(timeout=1.4)
                        for i in range(len(answer)):

                            if answer[i] == 'd':

                                if doop_determinant % 2 == 0:

                                    if original_photo.getpixel((444 + width, 71 + length)) == (35, 36, 42) and \
                                    original_photo.getpixel((527 + width, 71 + length)) == (35, 36, 42) and \
                                    original_photo.getpixel((610 + width, 71 + length)) == (35, 36, 42):

                                        width += 83

                                elif doop_determinant % 2 == 1:

                                    if original_photo.getpixel((444 + width, 71 + length)) == (35, 36, 42) and \
                                    original_photo.getpixel((444 + width, 154 + length)) == (35, 36, 42) and \
                                    original_photo.getpixel((444 + width, 237 + length)) == (35, 36, 42):

                                        width += 83

                            elif answer[i] == 'a':

                                if doop_determinant % 2 == 0:

                                    if original_photo.getpixel((278 + width, 71 + length)) == (35, 36, 42) and \
                                    original_photo.getpixel((361 + width, 71 + length)) == (35, 36, 42) and \
                                    original_photo.getpixel((444 + width, 71 + length)) == (35, 36, 42):

                                        width += -83

                                elif doop_determinant % 2 == 1:

                                    if original_photo.getpixel((278 + width, 71 + length)) == (35, 36, 42) and \
                                    original_photo.getpixel((278 + width, 154 + length)) == (35, 36, 42) and \
                                    original_photo.getpixel((278 + width, 237 + length)) == (35, 36, 42):

                                        width += -83

                            elif answer[i] in ['s', 'w']:

                                if doop_determinant % 2 == 0:

                                    if original_photo.getpixel((444 + width, 71 + length)) == (35, 36, 42) and \
                                    original_photo.getpixel((444 + width, -12 + length)) == (35, 36, 42) and \
                                    original_photo.getpixel((444 + width, -95 + length)) == (35, 36, 42):

                                        length += -166
                                        width += 83
                                        doop_determinant += 1

                                elif doop_determinant % 2 == 1:

                                    if original_photo.getpixel((278 + width, 71 + length)) == (35, 36, 42) and \
                                    original_photo.getpixel((361 + width, 71 + length)) == (35, 36, 42) and \
                                    original_photo.getpixel((444 + width, 71 + length)) == (35, 36, 42):

                                        length += 166
                                        width += -83
                                        doop_determinant += 1

                    except Exception:
                        pass

                while original_photo.getpixel((361 + width, 237 + length)) == (35, 36, 42) and \
                doop_determinant % 2 == 1:

                    sub_photo = original_photo.copy()
                    sub_photo.paste((0, 180, 255), (319 + width, 70 + length, 399 + width, 316 + length))
                    sub_photo.paste((30, 31, 37), (150, 70, 153, 1146))
                    sub_photo.paste((30, 31, 37), (233, 70, 236, 1146))
                    sub_photo.paste((30, 31, 37), (316, 70, 319, 1146))
                    sub_photo.paste((30, 31, 37), (399, 70, 402, 1146))
                    sub_photo.paste((30, 31, 37), (482, 70, 485, 1146))
                    sub_photo.paste((30, 31, 37), (565, 70, 568, 1146))
                    sub_photo.paste((30, 31, 37), (648, 70, 651, 1146))
                    sub_photo.paste((30, 31, 37), (70, 150, 731, 153))
                    sub_photo.paste((30, 31, 37), (70, 233, 731, 236))
                    sub_photo.paste((30, 31, 37), (70, 316, 731, 319))
                    sub_photo.paste((30, 31, 37), (70, 399, 731, 402))
                    sub_photo.paste((30, 31, 37), (70, 482, 731, 485))
                    sub_photo.paste((30, 31, 37), (70, 565, 731, 568))
                    sub_photo.paste((30, 31, 37), (70, 648, 731, 651))
                    sub_photo.paste((30, 31, 37), (70, 731, 731, 734))
                    sub_photo.paste((30, 31, 37), (70, 814, 731, 817))
                    sub_photo.paste((30, 31, 37), (70, 897, 731, 900))
                    sub_photo.paste((30, 31, 37), (70, 980, 731, 983))
                    sub_photo.paste((30, 31, 37), (70, 1063, 731, 1066))
                    length += 83
                    sub_photo.show()

                    try:

                        answer = inputimeout(timeout=1.4)
                        for i in range(len(answer)):

                            if answer[i] == 'd':

                                if doop_determinant % 2 == 1:

                                    if original_photo.getpixel((444 + width, 71 + length)) == (35, 36, 42) and \
                                    original_photo.getpixel((444 + width, 154 + length)) == (35, 36, 42) and \
                                    original_photo.getpixel((444 + width, 237 + length)) == (35, 36, 42):

                                        width += 83

                                elif doop_determinant % 2 == 0:

                                    if original_photo.getpixel((444 + width, 71 + length)) == (35, 36, 42) and \
                                    original_photo.getpixel((527 + width, 71 + length)) == (35, 36, 42) and \
                                    original_photo.getpixel((610 + width, 71 + length)) == (35, 36, 42):

                                        width += 83

                            elif answer[i] == 'a':

                                if doop_determinant % 2 == 1:

                                    if original_photo.getpixel((278 + width, 71 + length)) == (35, 36, 42) and\
                                    original_photo.getpixel((278 + width, 154 + length)) == (35, 36, 42) and \
                                    original_photo.getpixel((278 + width, 237 + length)) == (35, 36, 42):

                                        width += -83

                                elif doop_determinant % 2 == 0:

                                    if original_photo.getpixel((278 + width, 71 + length)) == (35, 36, 42) and \
                                    original_photo.getpixel((361 + width, 71 + length)) == (35, 36, 42) and \
                                    original_photo.getpixel((444 + width, 71 + length)) == (35, 36, 42):

                                        width += -83

                            elif answer[i] in ['s', 'w']:

                                if doop_determinant % 2 == 1:

                                    if original_photo.getpixel((278 + width, 154 + length)) == (35, 36, 42) and \
                                    original_photo.getpixel((361 + width, 154 + length)) == (35, 36, 42) and \
                                    original_photo.getpixel((444 + width, 154 + length)) == (35, 36, 42):

                                        length += 83
                                        width += -83
                                        doop_determinant += 1

                                    elif original_photo.getpixel((195 + width, 154 + length)) == (35, 36, 42) and \
                                    original_photo.getpixel((278 + width, 154 + length)) == (35, 36, 42) and \
                                    original_photo.getpixel((361 + width, 154 + length)) == (35, 36, 42):

                                        length += 83
                                        width += -166
                                        doop_determinant += 1

                                    elif original_photo.getpixel((361 + width, 154 + length)) == (35, 36, 42) and \
                                    original_photo.getpixel((444 + width, 154 + length)) == (35, 36, 42) and \
                                    original_photo.getpixel((527 + width, 154 + length)) == (35, 36, 42):

                                        length += 83
                                        doop_determinant += 1

                                elif doop_determinant % 2 == 0:

                                    if original_photo.getpixel((278 + width, 154 + length)) == (35, 36, 42) and \
                                    original_photo.getpixel((361 + width, 154 + length)) == (35, 36, 42) and \
                                    original_photo.getpixel((444 + width, 154 + length)) == (35, 36, 42):

                                        length += -83
                                        width += 83
                                        doop_determinant += 1

                    except Exception:
                        pass

                revolutions += 1

            except Exception:
                pass

        w = 0
        width = 0
        length = 0
        original_photo = sub_photo.copy()
        sub_photo = None
        revolutions = 0
        doop_determinant = 4

    if random_shape == 4:

        while original_photo.getpixel((320 + width, 71 + length)) == (35, 36, 42) and \
        revolutions != 100:

            try:

                while original_photo.getpixel((278 + width, 71 + length)) == (35, 36, 42) and \
                original_photo.getpixel((361 + width, 71 + length)) == (35, 36, 42) and \
                original_photo.getpixel((444 + width, 71 + length)) == (35, 36, 42) and \
                original_photo.getpixel((527 + width, 71 + length)) == (35, 36, 42) and \
                doop_determinant % 2 == 0:

                    sub_photo = original_photo.copy()
                    sub_photo.paste((255, 223, 0), (236 + width, 70 + length, 565 + width, 150 + length))
                    sub_photo.paste((30, 31, 37), (150, 70, 153, 1146))
                    sub_photo.paste((30, 31, 37), (233, 70, 236, 1146))
                    sub_photo.paste((30, 31, 37), (316, 70, 319, 1146))
                    sub_photo.paste((30, 31, 37), (399, 70, 402, 1146))
                    sub_photo.paste((30, 31, 37), (482, 70, 485, 1146))
                    sub_photo.paste((30, 31, 37), (565, 70, 568, 1146))
                    sub_photo.paste((30, 31, 37), (648, 70, 651, 1146))
                    sub_photo.paste((30, 31, 37), (70, 150, 731, 153))
                    sub_photo.paste((30, 31, 37), (70, 233, 731, 236))
                    sub_photo.paste((30, 31, 37), (70, 316, 731, 319))
                    sub_photo.paste((30, 31, 37), (70, 399, 731, 402))
                    sub_photo.paste((30, 31, 37), (70, 482, 731, 485))
                    sub_photo.paste((30, 31, 37), (70, 565, 731, 568))
                    sub_photo.paste((30, 31, 37), (70, 648, 731, 651))
                    sub_photo.paste((30, 31, 37), (70, 731, 731, 734))
                    sub_photo.paste((30, 31, 37), (70, 814, 731, 817))
                    sub_photo.paste((30, 31, 37), (70, 897, 731, 900))
                    sub_photo.paste((30, 31, 37), (70, 980, 731, 983))
                    sub_photo.paste((30, 31, 37), (70, 1063, 731, 1066))
                    length += 83
                    sub_photo.show()

                    try:

                        answer = inputimeout(timeout=1.4)
                        for i in range(len(answer)):

                            if answer[i] == 'd':

                                if doop_determinant % 2 == 0:

                                    if original_photo.getpixel((361 + width, 71 + length)) == (35, 36, 42) and \
                                    original_photo.getpixel((444 + width, 71 + length)) == (35, 36, 42) and \
                                    original_photo.getpixel((527 + width, 71 + length)) == (35, 36, 42) and \
                                    original_photo.getpixel((610 + width, 71 + length)) == (35, 36, 42):

                                        width += 83

                                elif doop_determinant % 2 == 1:

                                    if original_photo.getpixel((444 + width, 71 + length)) == (35, 36, 42) and \
                                    original_photo.getpixel((444 + width, 154 + length)) == (35, 36, 42) and \
                                    original_photo.getpixel((444 + width, 237 + length)) == (35, 36, 42) and \
                                    original_photo.getpixel((444 + width, 320 + length)) == (35, 36, 42):

                                        width += 83

                            elif answer[i] == 'a':

                                if doop_determinant % 2 == 0:

                                    if original_photo.getpixel((195 + width, 71 + length)) == (35, 36, 42) and \
                                    original_photo.getpixel((278 + width, 71 + length)) == (35, 36, 42) and \
                                    original_photo.getpixel((361 + width, 71 + length)) == (35, 36, 42) and \
                                    original_photo.getpixel((444 + width, 71 + length)) == (35, 36, 42):

                                        width += -83

                                elif doop_determinant % 2 == 1:

                                    if original_photo.getpixel((278 + width, 71 + length)) == (35, 36, 42) and \
                                    original_photo.getpixel((278 + width, 154 + length)) == (35, 36, 42) and \
                                    original_photo.getpixel((278 + width, 237 + length)) == (35, 36, 42) and \
                                    original_photo.getpixel((278 + width, 320 + length)) == (35, 36, 42):

                                        width += -83

                            elif answer[i] in ['s', 'w']:

                                if doop_determinant % 2 == 0:

                                    if original_photo.getpixel((444 + width, -178 + length)) == (35, 36, 42) and \
                                    original_photo.getpixel((444 + width, -95 + length)) == (35, 36, 42) and \
                                    original_photo.getpixel((444 + width, -12 + length)) == (35, 36, 42) and \
                                    original_photo.getpixel((444 + width, 71 + length)) == (35, 36, 42):

                                        doop_determinant += 1
                                        length += -249

                                elif doop_determinant % 2 == 1:

                                    if original_photo.getpixel((278 + width, 237 + length)) == (35, 36, 42) and \
                                    original_photo.getpixel((361 + width, 237 + length)) == (35, 36, 42) and \
                                    original_photo.getpixel((444 + width, 237 + length)) == (35, 36, 42) and \
                                    original_photo.getpixel((527 + width, 237 + length)) == (35, 36, 42):

                                        length += 166
                                        doop_determinant += 1

                                    elif original_photo.getpixel((361 + width, 237 + length)) == (35, 36, 42) and \
                                    original_photo.getpixel((444 + width, 237 + length)) == (35, 36, 42) and \
                                    original_photo.getpixel((527 + width, 237 + length)) == (35, 36, 42) and \
                                    original_photo.getpixel((610 + width, 237 + length)) == (35, 36, 42):

                                        width += 83
                                        length += 166
                                        doop_determinant += 1

                                    elif original_photo.getpixel((195 + width, 237 + length)) == (35, 36, 42) and \
                                    original_photo.getpixel((278 + width, 237 + length)) == (35, 36, 42) and \
                                    original_photo.getpixel((361 + width, 237 + length)) == (35, 36, 42) and \
                                    original_photo.getpixel((444 + width, 237 + length)) == (35, 36, 42):

                                        length += 166
                                        width += -83
                                        doop_determinant += 1

                                    elif original_photo.getpixel((112 + width, 237 + length)) == (35, 36, 42) and \
                                    original_photo.getpixel((195 + width, 237 + length)) == (35, 36, 42) and \
                                    original_photo.getpixel((278 + width, 237 + length)) == (35, 36, 42) and \
                                    original_photo.getpixel((361 + width, 237 + length)) == (35, 36, 42):

                                        length += 166
                                        width += -166
                                        doop_determinant += 1

                    except Exception:
                        pass

                while original_photo.getpixel((320 + width, 320 + length)) == (35, 36, 42) and \
                doop_determinant % 2 == 1:

                    sub_photo = original_photo.copy()
                    sub_photo.paste((255, 223, 0), (319 + width, 70 + length, 399 + width, 399 + length))
                    sub_photo.paste((30, 31, 37), (150, 70, 153, 1146))
                    sub_photo.paste((30, 31, 37), (233, 70, 236, 1146))
                    sub_photo.paste((30, 31, 37), (316, 70, 319, 1146))
                    sub_photo.paste((30, 31, 37), (399, 70, 402, 1146))
                    sub_photo.paste((30, 31, 37), (482, 70, 485, 1146))
                    sub_photo.paste((30, 31, 37), (565, 70, 568, 1146))
                    sub_photo.paste((30, 31, 37), (648, 70, 651, 1146))
                    sub_photo.paste((30, 31, 37), (70, 150, 731, 153))
                    sub_photo.paste((30, 31, 37), (70, 233, 731, 236))
                    sub_photo.paste((30, 31, 37), (70, 316, 731, 319))
                    sub_photo.paste((30, 31, 37), (70, 399, 731, 402))
                    sub_photo.paste((30, 31, 37), (70, 482, 731, 485))
                    sub_photo.paste((30, 31, 37), (70, 565, 731, 568))
                    sub_photo.paste((30, 31, 37), (70, 648, 731, 651))
                    sub_photo.paste((30, 31, 37), (70, 731, 731, 734))
                    sub_photo.paste((30, 31, 37), (70, 814, 731, 817))
                    sub_photo.paste((30, 31, 37), (70, 897, 731, 900))
                    sub_photo.paste((30, 31, 37), (70, 980, 731, 983))
                    sub_photo.paste((30, 31, 37), (70, 1063, 731, 1066))
                    length += 83
                    sub_photo.show()

                    try:

                        answer = inputimeout(timeout=1.4)
                        for i in range(len(answer)):

                            if answer[i] == 'd':

                                if doop_determinant % 2 == 1:

                                    if original_photo.getpixel((444 + width, 71 + length)) == (35, 36, 42) and \
                                    original_photo.getpixel((444 + width, 154 + length)) == (35, 36, 42) and \
                                    original_photo.getpixel((444 + width, 237 + length)) == (35, 36, 42) and \
                                    original_photo.getpixel((444 + width, 320 + length)) == (35, 36, 42):

                                        width += 83

                                if doop_determinant % 2 == 0:

                                    if original_photo.getpixel((444 + width, 71 + length)) == (35, 36, 42) and \
                                    original_photo.getpixel((527 + width, 71 + length)) == (35, 36, 42) and \
                                    original_photo.getpixel((610 + width, 71 + length)) == (35, 36, 42) and \
                                    original_photo.getpixel((793 + width, 71 + length)) == (35, 36, 42):

                                        width += 83

                            elif answer[i] == 'a':

                                if doop_determinant % 2 == 1:

                                    if original_photo.getpixel((278 + width, 71 + length)) == (35, 36, 42) and \
                                    original_photo.getpixel((278 + width, 154 + length)) == (35, 36, 42) and \
                                    original_photo.getpixel((278 + width, 237 + length)) == (35, 36, 42) and \
                                    original_photo.getpixel((278 + width, 320 + length)) == (35, 36, 42):

                                        width += -83
                                elif doop_determinant % 2 == 0:

                                    if original_photo.getpixel((195 + width, 71 + length)) == (35, 36, 42) and \
                                    original_photo.getpixel((278 + width, 71 + length)) == (35, 36, 42) and \
                                    original_photo.getpixel((361 + width, 71 + length)) == (35, 36, 42) and \
                                    original_photo.getpixel((444 + width, 71 + length)) == (35, 36, 42):

                                        width += -83

                            elif answer[i] in ['s', 'w']:

                                if doop_determinant % 2 == 1:

                                    if original_photo.getpixel((278 + width, 237 + length)) == (35, 36, 42) and \
                                    original_photo.getpixel((361 + width, 237 + length)) == (35, 36, 42) and \
                                    original_photo.getpixel((444 + width, 237 + length)) == (35, 36, 42) and \
                                    original_photo.getpixel((527 + width, 237 + length)) == (35, 36, 42):

                                        length += 166
                                        doop_determinant += 1

                                    elif original_photo.getpixel((361 + width, 237 + length)) == (35, 36, 42) and \
                                    original_photo.getpixel((444 + width, 237 + length)) == (35, 36, 42) and \
                                    original_photo.getpixel((527 + width, 237 + length)) == (35, 36, 42) and \
                                    original_photo.getpixel((610 + width, 237 + length)) == (35, 36, 42):

                                        width += 83
                                        length += 166
                                        doop_determinant += 1

                                    elif original_photo.getpixel((195 + width, 237 + length)) == (35, 36, 42) and \
                                    original_photo.getpixel((278 + width, 237 + length)) == (35, 36, 42) and \
                                    original_photo.getpixel((361 + width, 237 + length)) == (35, 36, 42) and \
                                    original_photo.getpixel((444 + width, 237 + length)) == (35, 36, 42):

                                        length += 166
                                        width += -83
                                        doop_determinant += 1

                                    elif original_photo.getpixel((112 + width, 237 + length)) == (35, 36, 42) and \
                                    original_photo.getpixel((195 + width, 237 + length)) == (35, 36, 42) and \
                                    original_photo.getpixel((278 + width, 237 + length)) == (35, 36, 42) and \
                                    original_photo.getpixel((361 + width, 237 + length)) == (35, 36, 42):

                                        length += 166
                                        width += -166
                                        doop_determinant += 1

                                elif doop_determinant % 2 == 0:

                                    if original_photo.getpixel((444 + width, -178 + length)) == (35, 36, 42) and \
                                    original_photo.getpixel((444 + width, -95 + length)) == (35, 36, 42) and \
                                    original_photo.getpixel((444 + width, -12 + length)) == (35, 36, 42) and \
                                    original_photo.getpixel((444 + width, 71 + length)) == (35, 36, 42):

                                        doop_determinant += 1
                                        length += -249

                    except Exception:
                        pass

                revolutions += 1

            except Exception:
                pass

        width = 0
        length = 0
        original_photo = sub_photo.copy()
        revolutions = 0
        doop_determinant = 4

    if random_shape == 5:

        while original_photo.getpixel((361 + width, 71 + length)) == (35, 36, 42) and \
        original_photo.getpixel((444 + width, 71 + length)) == (35, 36, 42) and \
        original_photo.getpixel((361 + width, 154 + length)) == (35, 36, 42) and \
        original_photo.getpixel((444 + width, 154 + length)) == (35, 36, 42):

            sub_photo = original_photo.copy()
            sub_photo.paste((64, 224, 208), (319 + width, 70 + length, 482 + width, 233 + length))
            sub_photo.paste((30, 31, 37), (150, 70, 153, 1146))
            sub_photo.paste((30, 31, 37), (233, 70, 236, 1146))
            sub_photo.paste((30, 31, 37), (316, 70, 319, 1146))
            sub_photo.paste((30, 31, 37), (399, 70, 402, 1146))
            sub_photo.paste((30, 31, 37), (482, 70, 485, 1146))
            sub_photo.paste((30, 31, 37), (565, 70, 568, 1146))
            sub_photo.paste((30, 31, 37), (648, 70, 651, 1146))
            sub_photo.paste((30, 31, 37), (70, 150, 731, 153))
            sub_photo.paste((30, 31, 37), (70, 233, 731, 236))
            sub_photo.paste((30, 31, 37), (70, 316, 731, 319))
            sub_photo.paste((30, 31, 37), (70, 399, 731, 402))
            sub_photo.paste((30, 31, 37), (70, 482, 731, 485))
            sub_photo.paste((30, 31, 37), (70, 565, 731, 568))
            sub_photo.paste((30, 31, 37), (70, 648, 731, 651))
            sub_photo.paste((30, 31, 37), (70, 731, 731, 734))
            sub_photo.paste((30, 31, 37), (70, 814, 731, 817))
            sub_photo.paste((30, 31, 37), (70, 897, 731, 900))
            sub_photo.paste((30, 31, 37), (70, 980, 731, 983))
            sub_photo.paste((30, 31, 37), (70, 1063, 731, 1066))
            length += 83
            sub_photo.show()

            try:

                answer = inputimeout(timeout=1.4)
                for i in range(len(answer)):

                    if answer[i] == 'd':

                        if original_photo.getpixel((444 + width, 71 + length)) == (35, 36, 42) and \
                        original_photo.getpixel((527 + width, 71 + length)) == (35, 36, 42) and \
                        original_photo.getpixel((444 + width, 154 + length)) == (35, 36, 42) and \
                        original_photo.getpixel((527 + width, 154 + length)) == (35, 36, 42):

                            width += 83

                    elif answer[i] == 'a':

                        if original_photo.getpixel((278 + width, 71 + length)) == (35, 36, 42) and \
                        original_photo.getpixel((361 + width, 71 + length)) == (35, 36, 42) and \
                        original_photo.getpixel((278 + width, 154 + length)) == (35, 36, 42) and \
                        original_photo.getpixel((361 + width, 154 + length)) == (35, 36, 42):

                            width += -83

            except Exception:
                pass

        width = 0
        length = 0
        original_photo = sub_photo.copy()
        revolutions = 0

    if random_shape == 6:

        while original_photo.getpixel((444 + width, 71 + length)) == (35, 36, 42) and \
        original_photo.getpixel((361 + width, 154 + length)) == (35, 36, 42) and \
        original_photo.getpixel((444 + width, 154 + length)) == (35, 36, 42) and \
        doop_determinant % 4 == 0:

            sub_photo = original_photo.copy()
            sub_photo.paste((186, 85, 211), (319 + width, 70 + length, 482 + width, 233 + length))
            sub_photo.paste((35, 36, 42), (319 + width, 70 + length, 399 + width, 150 + length))
            sub_photo.paste((30, 31, 37), (150, 70, 153, 1146))
            sub_photo.paste((30, 31, 37), (233, 70, 236, 1146))
            sub_photo.paste((30, 31, 37), (316, 70, 319, 1146))
            sub_photo.paste((30, 31, 37), (399, 70, 402, 1146))
            sub_photo.paste((30, 31, 37), (482, 70, 485, 1146))
            sub_photo.paste((30, 31, 37), (565, 70, 568, 1146))
            sub_photo.paste((30, 31, 37), (648, 70, 651, 1146))
            sub_photo.paste((30, 31, 37), (70, 150, 731, 153))
            sub_photo.paste((30, 31, 37), (70, 233, 731, 236))
            sub_photo.paste((30, 31, 37), (70, 316, 731, 319))
            sub_photo.paste((30, 31, 37), (70, 399, 731, 402))
            sub_photo.paste((30, 31, 37), (70, 482, 731, 485))
            sub_photo.paste((30, 31, 37), (70, 565, 731, 568))
            sub_photo.paste((30, 31, 37), (70, 648, 731, 651))
            sub_photo.paste((30, 31, 37), (70, 731, 731, 734))
            sub_photo.paste((30, 31, 37), (70, 814, 731, 817))
            sub_photo.paste((30, 31, 37), (70, 897, 731, 900))
            sub_photo.paste((30, 31, 37), (70, 980, 731, 983))
            sub_photo.paste((30, 31, 37), (70, 1063, 731, 1066))
            length += 83
            sub_photo.show()

            try:

                answer = inputimeout(timeout=1.4)
                for i in range(len(answer)):

                    if answer[i] == 'd':

                        if doop_determinant % 4 == 0:

                            if original_photo.getpixel((527 + width, 71 + length)) == (35, 36, 42) and \
                            original_photo.getpixel((444 + width, 154 + length)) == (35, 36, 42) and \
                            original_photo.getpixel((527 + width, 154 + length)) == (35, 36, 42):

                                width += 83

                        elif doop_determinant % 4 == 1:

                            if original_photo.getpixel((444 + width, 71 + length)) == (35, 36, 42) and \
                            original_photo.getpixel((444 + width, 154 + length)) == (35, 36, 42) and \
                            original_photo.getpixel((527 + width, 154 + length)) == (35, 36, 42):

                                width += 83

                        elif doop_determinant % 4 == 2:

                            if original_photo.getpixel((444 + width, 71 + length)) == (35, 36, 42) and \
                            original_photo.getpixel((527 + width, 71 + length)) == (35, 36, 42) and \
                            original_photo.getpixel((444 + width, 154 + length)) == (35, 36, 42):

                                width += 83

                        elif doop_determinant % 4 == 3:

                            if original_photo.getpixel((444 + width, 71 + length)) == (35, 36, 42) and \
                            original_photo.getpixel((527 + width, 71 + length)) == (35, 36, 42) and \
                            original_photo.getpixel((527 + width, 154 + length)) == (35, 36, 42):

                                width += 83

                    elif answer[i] == 'a':

                        if doop_determinant % 4 == 0:

                            if original_photo.getpixel((361 + width, 71 + length)) == (35, 36, 42) and \
                            original_photo.getpixel((278 + width, 154 + length)) == (35, 36, 42) and \
                            original_photo.getpixel((361 + width, 154 + length)) == (35, 36, 42):

                                width += -83

                        elif doop_determinant % 4 == 1:

                            if original_photo.getpixel((278 + width, 71 + length)) == (35, 36, 42) and \
                            original_photo.getpixel((278 + width, 154 + length)) == (35, 36, 42) and \
                            original_photo.getpixel((361 + width, 154 + length)) == (35, 36, 42):

                                width += -83

                        elif doop_determinant % 4 == 2:

                            if original_photo.getpixel((278 + width, 71 + length)) == (35, 36, 42) and \
                            original_photo.getpixel((361 + width, 154 + length)) == (35, 36, 42) and \
                            original_photo.getpixel((278 + width, 154 + length)) == (35, 36, 42):

                                width += -83

                        elif doop_determinant % 4 == 3:

                            if original_photo.getpixel((278 + width, 71 + length)) == (35, 36, 42) and \
                            original_photo.getpixel((361 + width, 154 + length)) == (35, 36, 42) and \
                            original_photo.getpixel((361 + width, 154 + length)) == (35, 36, 42):

                                width += -83

                    elif answer[i] == 's':

                        if doop_determinant % 4 == 0:

                            if original_photo.getpixel((361 + width, 71 + length)) == (35, 36, 42) and \
                            original_photo.getpixel((444 + width, 154 + length)) == (35, 36, 42) and \
                            original_photo.getpixel((444 + width, 154 + length)) == (35, 36, 42):

                                doop_determinant += -3

                        elif doop_determinant % 4 == 1:

                            if original_photo.getpixel((444 + width, 71 + length)) == (35, 36, 42) and \
                            original_photo.getpixel((361 + width, 154 + length)) == (35, 36, 42) and \
                            original_photo.getpixel((444 + width, 154 + length)) == (35, 36, 42):

                                doop_determinant += -3

                        elif doop_determinant % 4 == 2:

                            if original_photo.getpixel((361 + width, 71 + length)) == (35, 36, 42) and \
                            original_photo.getpixel((361 + width, 154 + length)) == (35, 36, 42) and \
                            original_photo.getpixel((444 + width, 154 + length)) == (35, 36, 42):

                                doop_determinant += -3

                        elif doop_determinant % 4 == 3:

                            if original_photo.getpixel((361 + width, 71 + length)) == (35, 36, 42) and \
                            original_photo.getpixel((444 + width, 154 + length)) == (35, 36, 42) and \
                            original_photo.getpixel((361 + width, 154 + length)) == (35, 36, 42):

                                doop_determinant += -3

                    elif answer[i] == 'w':

                        if doop_determinant % 4 == 0:

                            if original_photo.getpixel((361 + width, 71 + length)) == (35, 36, 42) and \
                            original_photo.getpixel((361 + width, 154 + length)) == (35, 36, 42) and \
                            original_photo.getpixel((444 + width, 154 + length)) == (35, 36, 42):

                                doop_determinant += 1

                        elif doop_determinant % 4 == 1:

                            if original_photo.getpixel((361 + width, 71 + length)) == (35, 36, 42) and \
                            original_photo.getpixel((444 + width, 154 + length)) == (35, 36, 42) and \
                            original_photo.getpixel((361 + width, 154 + length)) == (35, 36, 42):

                                doop_determinant += 1

                        elif doop_determinant % 4 == 2:

                            if original_photo.getpixel((361 + width, 71 + length)) == (35, 36, 42) and \
                            original_photo.getpixel((444 + width, 154 + length)) == (35, 36, 42) and \
                            original_photo.getpixel((444 + width, 154 + length)) == (35, 36, 42):

                                doop_determinant += 1

                        elif doop_determinant % 4 == 3:

                            if original_photo.getpixel((444 + width, 71 + length)) == (35, 36, 42) and \
                            original_photo.getpixel((361 + width, 154 + length)) == (35, 36, 42) and \
                            original_photo.getpixel((444 + width, 154 + length)) == (35, 36, 42):

                                doop_determinant += 1

            except Exception:
                pass

    while revolutions != 120:

        if original_photo.getpixel((70, 1066 - 0)) != (35, 36, 42) and original_photo.getpixel((153, 1066 - 0)) != (35, 36, 42)\
        and original_photo.getpixel((236, 1066 - 0)) != (35, 36, 42) and original_photo.getpixel((319, 1066 - 0)) != (35, 36, 42)\
        and original_photo.getpixel((402, 1066 - 0)) != (35, 36, 42) and original_photo.getpixel((485, 1066 - 0)) != (35, 36, 42)\
        and original_photo.getpixel((568, 1066 - 0)) != (35, 36, 42) and original_photo.getpixel((651, 1066 - 0)) != (35, 36, 42):

            A = original_photo.crop((65, 67, 734, 1063 - 0))
            original_photo.paste((30, 31, 37), (0, 0, 801, 1216))
            original_photo.paste((28, 29, 35), (5, 5, 796, 1211))
            original_photo.paste((26, 27, 33), (10, 10, 791, 1206))
            original_photo.paste((25, 26, 32), (15, 15, 786, 1201))
            original_photo.paste((26, 27, 33), (55, 55, 746, 1161))
            original_photo.paste((27, 28, 34), (60, 60, 741, 1156))
            original_photo.paste((30, 31, 37), (65, 65, 736, 1151))
            original_photo.paste((35, 36, 42), (70, 70, 731, 1146))
            original_photo.paste((30, 31, 37), (150, 70, 153, 1146))
            original_photo.paste((30, 31, 37), (233, 70, 236, 1146))
            original_photo.paste((30, 31, 37), (316, 70, 319, 1146))
            original_photo.paste((30, 31, 37), (399, 70, 402, 1146))
            original_photo.paste((30, 31, 37), (482, 70, 485, 1146))
            original_photo.paste((30, 31, 37), (565, 70, 568, 1146))
            original_photo.paste((30, 31, 37), (648, 70, 651, 1146))
            original_photo.paste((30, 31, 37), (70, 150, 731, 153))
            original_photo.paste((30, 31, 37), (70, 233, 731, 236))
            original_photo.paste((30, 31, 37), (70, 316, 731, 319))
            original_photo.paste((30, 31, 37), (70, 399, 731, 402))
            original_photo.paste((30, 31, 37), (70, 482, 731, 485))
            original_photo.paste((30, 31, 37), (70, 565, 731, 568))
            original_photo.paste((30, 31, 37), (70, 648, 731, 651))
            original_photo.paste((30, 31, 37), (70, 731, 731, 734))
            original_photo.paste((30, 31, 37), (70, 814, 731, 817))
            original_photo.paste((30, 31, 37), (70, 897, 731, 900))
            original_photo.paste((30, 31, 37), (70, 980, 731, 983))
            original_photo.paste((30, 31, 37), (70, 1063, 731, 1066))
            original_photo.paste((A), (65, 150))
            score += 100

        if original_photo.getpixel((70, 1066 - 83)) != (35, 36, 42) and original_photo.getpixel((153, 1066 - 83)) != (35, 36, 42)\
        and original_photo.getpixel((236, 1066 - 83)) != (35, 36, 42) and original_photo.getpixel((319, 1066 - 83)) != (35, 36, 42)\
        and original_photo.getpixel((402, 1066 - 83)) != (35, 36, 42) and original_photo.getpixel((485, 1066 - 83)) != (35, 36, 42)\
        and original_photo.getpixel((568, 1066 - 83)) != (35, 36, 42) and original_photo.getpixel((651, 1066 - 83)) != (35, 36, 42):

            A = original_photo.crop((65, 67, 734, 1063 - 83))
            B = original_photo.crop((65, 1066, 736, 1151))
            original_photo.paste((30, 31, 37), (0, 0, 801, 1216))
            original_photo.paste((28, 29, 35), (5, 5, 796, 1211))
            original_photo.paste((26, 27, 33), (10, 10, 791, 1206))
            original_photo.paste((25, 26, 32), (15, 15, 786, 1201))
            original_photo.paste((26, 27, 33), (55, 55, 746, 1161))
            original_photo.paste((27, 28, 34), (60, 60, 741, 1156))
            original_photo.paste((30, 31, 37), (65, 65, 736, 1151))
            original_photo.paste((35, 36, 42), (70, 70, 731, 1146))
            original_photo.paste((30, 31, 37), (150, 70, 153, 1146))
            original_photo.paste((30, 31, 37), (233, 70, 236, 1146))
            original_photo.paste((30, 31, 37), (316, 70, 319, 1146))
            original_photo.paste((30, 31, 37), (399, 70, 402, 1146))
            original_photo.paste((30, 31, 37), (482, 70, 485, 1146))
            original_photo.paste((30, 31, 37), (565, 70, 568, 1146))
            original_photo.paste((30, 31, 37), (648, 70, 651, 1146))
            original_photo.paste((30, 31, 37), (70, 150, 731, 153))
            original_photo.paste((30, 31, 37), (70, 233, 731, 236))
            original_photo.paste((30, 31, 37), (70, 316, 731, 319))
            original_photo.paste((30, 31, 37), (70, 399, 731, 402))
            original_photo.paste((30, 31, 37), (70, 482, 731, 485))
            original_photo.paste((30, 31, 37), (70, 565, 731, 568))
            original_photo.paste((30, 31, 37), (70, 648, 731, 651))
            original_photo.paste((30, 31, 37), (70, 731, 731, 734))
            original_photo.paste((30, 31, 37), (70, 814, 731, 817))
            original_photo.paste((30, 31, 37), (70, 897, 731, 900))
            original_photo.paste((30, 31, 37), (70, 980, 731, 983))
            original_photo.paste((30, 31, 37), (70, 1063, 731, 1066))
            original_photo.paste((A), (65, 150))
            original_photo.paste((B), (65, 1066))
            score += 100

        if original_photo.getpixel((70, 1066 - 166)) != (35, 36, 42) and original_photo.getpixel((153, 1066 - 166)) != (35, 36, 42)\
        and original_photo.getpixel((236, 1066 - 166)) != (35, 36, 42) and original_photo.getpixel((319, 1066 - 166)) != (35, 36, 42)\
        and original_photo.getpixel((402, 1066 - 166)) != (35, 36, 42) and original_photo.getpixel((485, 1066 - 166)) != (35, 36, 42)\
        and original_photo.getpixel((568, 1066 - 166)) != (35, 36, 42) and original_photo.getpixel((651, 1066 - 166)) != (35, 36, 42):

            A = original_photo.crop((65, 67, 734, 1063 - 166))
            B = original_photo.crop((65, 1066 - 83, 736, 1151))
            original_photo.paste((30, 31, 37), (0, 0, 801, 1216))
            original_photo.paste((28, 29, 35), (5, 5, 796, 1211))
            original_photo.paste((26, 27, 33), (10, 10, 791, 1206))
            original_photo.paste((25, 26, 32), (15, 15, 786, 1201))
            original_photo.paste((26, 27, 33), (55, 55, 746, 1161))
            original_photo.paste((27, 28, 34), (60, 60, 741, 1156))
            original_photo.paste((30, 31, 37), (65, 65, 736, 1151))
            original_photo.paste((35, 36, 42), (70, 70, 731, 1146))
            original_photo.paste((30, 31, 37), (150, 70, 153, 1146))
            original_photo.paste((30, 31, 37), (233, 70, 236, 1146))
            original_photo.paste((30, 31, 37), (316, 70, 319, 1146))
            original_photo.paste((30, 31, 37), (399, 70, 402, 1146))
            original_photo.paste((30, 31, 37), (482, 70, 485, 1146))
            original_photo.paste((30, 31, 37), (565, 70, 568, 1146))
            original_photo.paste((30, 31, 37), (648, 70, 651, 1146))
            original_photo.paste((30, 31, 37), (70, 150, 731, 153))
            original_photo.paste((30, 31, 37), (70, 233, 731, 236))
            original_photo.paste((30, 31, 37), (70, 316, 731, 319))
            original_photo.paste((30, 31, 37), (70, 399, 731, 402))
            original_photo.paste((30, 31, 37), (70, 482, 731, 485))
            original_photo.paste((30, 31, 37), (70, 565, 731, 568))
            original_photo.paste((30, 31, 37), (70, 648, 731, 651))
            original_photo.paste((30, 31, 37), (70, 731, 731, 734))
            original_photo.paste((30, 31, 37), (70, 814, 731, 817))
            original_photo.paste((30, 31, 37), (70, 897, 731, 900))
            original_photo.paste((30, 31, 37), (70, 980, 731, 983))
            original_photo.paste((30, 31, 37), (70, 1063, 731, 1066))
            original_photo.paste((A), (65, 150))
            original_photo.paste((B), (65, 1066 - 83))
            score += 100

        if original_photo.getpixel((70, 1066 - 249)) != (35, 36, 42) and original_photo.getpixel((153, 1066 - 249)) != (35, 36, 42)\
        and original_photo.getpixel((236, 1066 - 249)) != (35, 36, 42) and original_photo.getpixel((319, 1066 - 249)) != (35, 36, 42)\
        and original_photo.getpixel((402, 1066 - 249)) != (35, 36, 42) and original_photo.getpixel((485, 1066 - 249)) != (35, 36, 42)\
        and original_photo.getpixel((568, 1066 - 249)) != (35, 36, 42) and original_photo.getpixel((651, 1066 - 249)) != (35, 36, 42):

            A = original_photo.crop((65, 67, 734, 1063 - 249))
            B = original_photo.crop((65, 1066 - 166, 736, 1151))
            original_photo.paste((30, 31, 37), (0, 0, 801, 1216))
            original_photo.paste((28, 29, 35), (5, 5, 796, 1211))
            original_photo.paste((26, 27, 33), (10, 10, 791, 1206))
            original_photo.paste((25, 26, 32), (15, 15, 786, 1201))
            original_photo.paste((26, 27, 33), (55, 55, 746, 1161))
            original_photo.paste((27, 28, 34), (60, 60, 741, 1156))
            original_photo.paste((30, 31, 37), (65, 65, 736, 1151))
            original_photo.paste((35, 36, 42), (70, 70, 731, 1146))
            original_photo.paste((30, 31, 37), (150, 70, 153, 1146))
            original_photo.paste((30, 31, 37), (233, 70, 236, 1146))
            original_photo.paste((30, 31, 37), (316, 70, 319, 1146))
            original_photo.paste((30, 31, 37), (399, 70, 402, 1146))
            original_photo.paste((30, 31, 37), (482, 70, 485, 1146))
            original_photo.paste((30, 31, 37), (565, 70, 568, 1146))
            original_photo.paste((30, 31, 37), (648, 70, 651, 1146))
            original_photo.paste((30, 31, 37), (70, 150, 731, 153))
            original_photo.paste((30, 31, 37), (70, 233, 731, 236))
            original_photo.paste((30, 31, 37), (70, 316, 731, 319))
            original_photo.paste((30, 31, 37), (70, 399, 731, 402))
            original_photo.paste((30, 31, 37), (70, 482, 731, 485))
            original_photo.paste((30, 31, 37), (70, 565, 731, 568))
            original_photo.paste((30, 31, 37), (70, 648, 731, 651))
            original_photo.paste((30, 31, 37), (70, 731, 731, 734))
            original_photo.paste((30, 31, 37), (70, 814, 731, 817))
            original_photo.paste((30, 31, 37), (70, 897, 731, 900))
            original_photo.paste((30, 31, 37), (70, 980, 731, 983))
            original_photo.paste((30, 31, 37), (70, 1063, 731, 1066))
            original_photo.paste((A), (65, 150))
            B.paste((B), (65, 1066 - 166))
            score += 100

        if original_photo.getpixel((70, 1066 - 332)) != (35, 36, 42) and original_photo.getpixel((153, 1066 - 332)) != (35, 36, 42)\
        and original_photo.getpixel((236, 1066 - 332)) != (35, 36, 42) and original_photo.getpixel((319, 1066 - 332)) != (35, 36, 42)\
        and original_photo.getpixel((402, 1066 - 332)) != (35, 36, 42) and original_photo.getpixel((485, 1066 - 332)) != (35, 36, 42)\
        and original_photo.getpixel((568, 1066 - 332)) != (35, 36, 42) and original_photo.getpixel((651, 1066 - 332)) != (35, 36, 42):

            A = original_photo.crop((65, 67, 734, 1063 - 332))
            B = original_photo.crop((65, 1066 - 249, 736, 1151))
            original_photo.paste((30, 31, 37), (0, 0, 801, 1216))
            original_photo.paste((28, 29, 35), (5, 5, 796, 1211))
            original_photo.paste((26, 27, 33), (10, 10, 791, 1206))
            original_photo.paste((25, 26, 32), (15, 15, 786, 1201))
            original_photo.paste((26, 27, 33), (55, 55, 746, 1161))
            original_photo.paste((27, 28, 34), (60, 60, 741, 1156))
            original_photo.paste((30, 31, 37), (65, 65, 736, 1151))
            original_photo.paste((35, 36, 42), (70, 70, 731, 1146))
            original_photo.paste((30, 31, 37), (150, 70, 153, 1146))
            original_photo.paste((30, 31, 37), (233, 70, 236, 1146))
            original_photo.paste((30, 31, 37), (316, 70, 319, 1146))
            original_photo.paste((30, 31, 37), (399, 70, 402, 1146))
            original_photo.paste((30, 31, 37), (482, 70, 485, 1146))
            original_photo.paste((30, 31, 37), (565, 70, 568, 1146))
            original_photo.paste((30, 31, 37), (648, 70, 651, 1146))
            original_photo.paste((30, 31, 37), (70, 150, 731, 153))
            original_photo.paste((30, 31, 37), (70, 233, 731, 236))
            original_photo.paste((30, 31, 37), (70, 316, 731, 319))
            original_photo.paste((30, 31, 37), (70, 399, 731, 402))
            original_photo.paste((30, 31, 37), (70, 482, 731, 485))
            original_photo.paste((30, 31, 37), (70, 565, 731, 568))
            original_photo.paste((30, 31, 37), (70, 648, 731, 651))
            original_photo.paste((30, 31, 37), (70, 731, 731, 734))
            original_photo.paste((30, 31, 37), (70, 814, 731, 817))
            original_photo.paste((30, 31, 37), (70, 897, 731, 900))
            original_photo.paste((30, 31, 37), (70, 980, 731, 983))
            original_photo.paste((30, 31, 37), (70, 1063, 731, 1066))
            original_photo.paste((A), (65, 150))
            original_photo.paste((B), (65, 1066 - 249))
            score += 100

        if original_photo.getpixel((70, 1066 - 415)) != (35, 36, 42) and original_photo.getpixel((153, 1066 - 415)) != (35, 36, 42)\
        and original_photo.getpixel((236, 1066 - 415)) != (35, 36, 42) and original_photo.getpixel((319, 1066 - 415)) != (35, 36, 42)\
        and original_photo.getpixel((402, 1066 - 415)) != (35, 36, 42) and original_photo.getpixel((485, 1066 - 415)) != (35, 36, 42)\
        and original_photo.getpixel((568, 1066 - 415)) != (35, 36, 42) and original_photo.getpixel((651, 1066 - 415)) != (35, 36, 42):

            A = original_photo.crop((65, 67, 734, 1063 - 415))
            B = original_photo.crop((65, 1066 - 332, 736, 1151))
            original_photo.paste((30, 31, 37), (0, 0, 801, 1216))
            original_photo.paste((28, 29, 35), (5, 5, 796, 1211))
            original_photo.paste((26, 27, 33), (10, 10, 791, 1206))
            original_photo.paste((25, 26, 32), (15, 15, 786, 1201))
            original_photo.paste((26, 27, 33), (55, 55, 746, 1161))
            original_photo.paste((27, 28, 34), (60, 60, 741, 1156))
            original_photo.paste((30, 31, 37), (65, 65, 736, 1151))
            original_photo.paste((35, 36, 42), (70, 70, 731, 1146))
            original_photo.paste((30, 31, 37), (150, 70, 153, 1146))
            original_photo.paste((30, 31, 37), (233, 70, 236, 1146))
            original_photo.paste((30, 31, 37), (316, 70, 319, 1146))
            original_photo.paste((30, 31, 37), (399, 70, 402, 1146))
            original_photo.paste((30, 31, 37), (482, 70, 485, 1146))
            original_photo.paste((30, 31, 37), (565, 70, 568, 1146))
            original_photo.paste((30, 31, 37), (648, 70, 651, 1146))
            original_photo.paste((30, 31, 37), (70, 150, 731, 153))
            original_photo.paste((30, 31, 37), (70, 233, 731, 236))
            original_photo.paste((30, 31, 37), (70, 316, 731, 319))
            original_photo.paste((30, 31, 37), (70, 399, 731, 402))
            original_photo.paste((30, 31, 37), (70, 482, 731, 485))
            original_photo.paste((30, 31, 37), (70, 565, 731, 568))
            original_photo.paste((30, 31, 37), (70, 648, 731, 651))
            original_photo.paste((30, 31, 37), (70, 731, 731, 734))
            original_photo.paste((30, 31, 37), (70, 814, 731, 817))
            original_photo.paste((30, 31, 37), (70, 897, 731, 900))
            original_photo.paste((30, 31, 37), (70, 980, 731, 983))
            original_photo.paste((30, 31, 37), (70, 1063, 731, 1066))
            original_photo.paste((A), (65, 150))
            original_photo.paste((B), (65, 1066 - 332))
            score += 100

        if original_photo.getpixel((70, 1066 - 498)) != (35, 36, 42) and original_photo.getpixel((153, 1066 - 498)) != (35, 36, 42)\
        and original_photo.getpixel((236, 1066 - 498)) != (35, 36, 42) and original_photo.getpixel((319, 1066 - 498)) != (35, 36, 42)\
        and original_photo.getpixel((402, 1066 - 498)) != (35, 36, 42) and original_photo.getpixel((485, 1066 - 498)) != (35, 36, 42)\
        and original_photo.getpixel((568, 1066 - 498)) != (35, 36, 42) and original_photo.getpixel((651, 1066 - 498)) != (35, 36, 42):

            A = original_photo.crop((65, 67, 734, 1063 - 498))
            B = original_photo.crop((65, 1066 - 415, 736, 1151))
            original_photo.paste((30, 31, 37), (0, 0, 801, 1216))
            original_photo.paste((28, 29, 35), (5, 5, 796, 1211))
            original_photo.paste((26, 27, 33), (10, 10, 791, 1206))
            original_photo.paste((25, 26, 32), (15, 15, 786, 1201))
            original_photo.paste((26, 27, 33), (55, 55, 746, 1161))
            original_photo.paste((27, 28, 34), (60, 60, 741, 1156))
            original_photo.paste((30, 31, 37), (65, 65, 736, 1151))
            original_photo.paste((35, 36, 42), (70, 70, 731, 1146))
            original_photo.paste((30, 31, 37), (150, 70, 153, 1146))
            original_photo.paste((30, 31, 37), (233, 70, 236, 1146))
            original_photo.paste((30, 31, 37), (316, 70, 319, 1146))
            original_photo.paste((30, 31, 37), (399, 70, 402, 1146))
            original_photo.paste((30, 31, 37), (482, 70, 485, 1146))
            original_photo.paste((30, 31, 37), (565, 70, 568, 1146))
            original_photo.paste((30, 31, 37), (648, 70, 651, 1146))
            original_photo.paste((30, 31, 37), (70, 150, 731, 153))
            original_photo.paste((30, 31, 37), (70, 233, 731, 236))
            original_photo.paste((30, 31, 37), (70, 316, 731, 319))
            original_photo.paste((30, 31, 37), (70, 399, 731, 402))
            original_photo.paste((30, 31, 37), (70, 482, 731, 485))
            original_photo.paste((30, 31, 37), (70, 565, 731, 568))
            original_photo.paste((30, 31, 37), (70, 648, 731, 651))
            original_photo.paste((30, 31, 37), (70, 731, 731, 734))
            original_photo.paste((30, 31, 37), (70, 814, 731, 817))
            original_photo.paste((30, 31, 37), (70, 897, 731, 900))
            original_photo.paste((30, 31, 37), (70, 980, 731, 983))
            original_photo.paste((30, 31, 37), (70, 1063, 731, 1066))
            original_photo.paste((A), (65, 150))
            original_photo.paste((B), (65, 1066 - 415))
            score += 100

        if original_photo.getpixel((70, 1066 - 581)) != (35, 36, 42) and original_photo.getpixel((153, 1066 - 581)) != (35, 36, 42)\
        and original_photo.getpixel((236, 1066 - 581)) != (35, 36, 42) and original_photo.getpixel((319, 1066 - 581)) != (35, 36, 42)\
        and original_photo.getpixel((402, 1066 - 581)) != (35, 36, 42) and original_photo.getpixel((485, 1066 - 581)) != (35, 36, 42)\
        and original_photo.getpixel((568, 1066 - 581)) != (35, 36, 42) and original_photo.getpixel((651, 1066 - 581)) != (35, 36, 42):

            A = original_photo.crop((65, 67, 734, 1063 - 581))
            B = original_photo.crop((65, 1066 - 498, 736, 1151))
            original_photo.paste((30, 31, 37), (0, 0, 801, 1216))
            original_photo.paste((28, 29, 35), (5, 5, 796, 1211))
            original_photo.paste((26, 27, 33), (10, 10, 791, 1206))
            original_photo.paste((25, 26, 32), (15, 15, 786, 1201))
            original_photo.paste((26, 27, 33), (55, 55, 746, 1161))
            original_photo.paste((27, 28, 34), (60, 60, 741, 1156))
            original_photo.paste((30, 31, 37), (65, 65, 736, 1151))
            original_photo.paste((35, 36, 42), (70, 70, 731, 1146))
            original_photo.paste((30, 31, 37), (150, 70, 153, 1146))
            original_photo.paste((30, 31, 37), (233, 70, 236, 1146))
            original_photo.paste((30, 31, 37), (316, 70, 319, 1146))
            original_photo.paste((30, 31, 37), (399, 70, 402, 1146))
            original_photo.paste((30, 31, 37), (482, 70, 485, 1146))
            original_photo.paste((30, 31, 37), (565, 70, 568, 1146))
            original_photo.paste((30, 31, 37), (648, 70, 651, 1146))
            original_photo.paste((30, 31, 37), (70, 150, 731, 153))
            original_photo.paste((30, 31, 37), (70, 233, 731, 236))
            original_photo.paste((30, 31, 37), (70, 316, 731, 319))
            original_photo.paste((30, 31, 37), (70, 399, 731, 402))
            original_photo.paste((30, 31, 37), (70, 482, 731, 485))
            original_photo.paste((30, 31, 37), (70, 565, 731, 568))
            original_photo.paste((30, 31, 37), (70, 648, 731, 651))
            original_photo.paste((30, 31, 37), (70, 731, 731, 734))
            original_photo.paste((30, 31, 37), (70, 814, 731, 817))
            original_photo.paste((30, 31, 37), (70, 897, 731, 900))
            original_photo.paste((30, 31, 37), (70, 980, 731, 983))
            original_photo.paste((30, 31, 37), (70, 1063, 731, 1066))
            original_photo.paste((A), (65, 150))
            original_photo.paste((B), (65, 1066 - 498))
            score += 100

        if original_photo.getpixel((70, 1066 - 664)) != (35, 36, 42) and original_photo.getpixel((153, 1066 - 664)) != (35, 36, 42)\
        and original_photo.getpixel((236, 1066 - 664)) != (35, 36, 42) and original_photo.getpixel((319, 1066 - 664)) != (35, 36, 42)\
        and original_photo.getpixel((402, 1066 - 664)) != (35, 36, 42) and original_photo.getpixel((485, 1066 - 664)) != (35, 36, 42)\
        and original_photo.getpixel((568, 1066 - 664)) != (35, 36, 42) and original_photo.getpixel((651, 1066 - 664)) != (35, 36, 42):

            A = original_photo.crop((65, 67, 734, 1063 - 664))
            B = original_photo.crop((65, 1066 - 581, 736, 1151))
            original_photo.paste((30, 31, 37), (0, 0, 801, 1216))
            original_photo.paste((28, 29, 35), (5, 5, 796, 1211))
            original_photo.paste((26, 27, 33), (10, 10, 791, 1206))
            original_photo.paste((25, 26, 32), (15, 15, 786, 1201))
            original_photo.paste((26, 27, 33), (55, 55, 746, 1161))
            original_photo.paste((27, 28, 34), (60, 60, 741, 1156))
            original_photo.paste((30, 31, 37), (65, 65, 736, 1151))
            original_photo.paste((35, 36, 42), (70, 70, 731, 1146))
            original_photo.paste((30, 31, 37), (150, 70, 153, 1146))
            original_photo.paste((30, 31, 37), (233, 70, 236, 1146))
            original_photo.paste((30, 31, 37), (316, 70, 319, 1146))
            original_photo.paste((30, 31, 37), (399, 70, 402, 1146))
            original_photo.paste((30, 31, 37), (482, 70, 485, 1146))
            original_photo.paste((30, 31, 37), (565, 70, 568, 1146))
            original_photo.paste((30, 31, 37), (648, 70, 651, 1146))
            original_photo.paste((30, 31, 37), (70, 150, 731, 153))
            original_photo.paste((30, 31, 37), (70, 233, 731, 236))
            original_photo.paste((30, 31, 37), (70, 316, 731, 319))
            original_photo.paste((30, 31, 37), (70, 399, 731, 402))
            original_photo.paste((30, 31, 37), (70, 482, 731, 485))
            original_photo.paste((30, 31, 37), (70, 565, 731, 568))
            original_photo.paste((30, 31, 37), (70, 648, 731, 651))
            original_photo.paste((30, 31, 37), (70, 731, 731, 734))
            original_photo.paste((30, 31, 37), (70, 814, 731, 817))
            original_photo.paste((30, 31, 37), (70, 897, 731, 900))
            original_photo.paste((30, 31, 37), (70, 980, 731, 983))
            original_photo.paste((30, 31, 37), (70, 1063, 731, 1066))
            original_photo.paste((A), (65, 150))
            original_photo.paste((B), (65, 1066 - 581))
            score += 100

        if original_photo.getpixel((70, 1066 - 747)) != (35, 36, 42) and original_photo.getpixel((153, 1066 - 747)) != (35, 36, 42)\
        and original_photo.getpixel((236, 1066 - 747)) != (35, 36, 42) and original_photo.getpixel((319, 1066 - 747)) != (35, 36, 42)\
        and original_photo.getpixel((402, 1066 - 747)) != (35, 36, 42) and original_photo.getpixel((485, 1066 - 747)) != (35, 36, 42)\
        and original_photo.getpixel((568, 1066 - 747)) != (35, 36, 42) and original_photo.getpixel((651, 1066 - 747)) != (35, 36, 42):

            A = original_photo.crop((65, 67, 734, 1063 - 747))
            B = original_photo.crop((65, 1066 - 664, 736, 1151))
            original_photo.paste((30, 31, 37), (0, 0, 801, 1216))
            original_photo.paste((28, 29, 35), (5, 5, 796, 1211))
            original_photo.paste((26, 27, 33), (10, 10, 791, 1206))
            original_photo.paste((25, 26, 32), (15, 15, 786, 1201))
            original_photo.paste((26, 27, 33), (55, 55, 746, 1161))
            original_photo.paste((27, 28, 34), (60, 60, 741, 1156))
            original_photo.paste((30, 31, 37), (65, 65, 736, 1151))
            original_photo.paste((35, 36, 42), (70, 70, 731, 1146))
            original_photo.paste((30, 31, 37), (150, 70, 153, 1146))
            original_photo.paste((30, 31, 37), (233, 70, 236, 1146))
            original_photo.paste((30, 31, 37), (316, 70, 319, 1146))
            original_photo.paste((30, 31, 37), (399, 70, 402, 1146))
            original_photo.paste((30, 31, 37), (482, 70, 485, 1146))
            original_photo.paste((30, 31, 37), (565, 70, 568, 1146))
            original_photo.paste((30, 31, 37), (648, 70, 651, 1146))
            original_photo.paste((30, 31, 37), (70, 150, 731, 153))
            original_photo.paste((30, 31, 37), (70, 233, 731, 236))
            original_photo.paste((30, 31, 37), (70, 316, 731, 319))
            original_photo.paste((30, 31, 37), (70, 399, 731, 402))
            original_photo.paste((30, 31, 37), (70, 482, 731, 485))
            original_photo.paste((30, 31, 37), (70, 565, 731, 568))
            original_photo.paste((30, 31, 37), (70, 648, 731, 651))
            original_photo.paste((30, 31, 37), (70, 731, 731, 734))
            original_photo.paste((30, 31, 37), (70, 814, 731, 817))
            original_photo.paste((30, 31, 37), (70, 897, 731, 900))
            original_photo.paste((30, 31, 37), (70, 980, 731, 983))
            original_photo.paste((30, 31, 37), (70, 1063, 731, 1066))
            original_photo.paste((A), (65, 150))
            original_photo.paste((B), (65, 1066 - 664))
            score += 100

        if original_photo.getpixel((70, 1066 - 830)) != (35, 36, 42) and original_photo.getpixel((153, 1066 - 830)) != (35, 36, 42)\
        and original_photo.getpixel((236, 1066 - 830)) != (35, 36, 42) and original_photo.getpixel((319, 1066 - 830)) != (35, 36, 42)\
        and original_photo.getpixel((402, 1066 - 830)) != (35, 36, 42) and original_photo.getpixel((485, 1066 - 830)) != (35, 36, 42)\
        and original_photo.getpixel((568, 1066 - 830)) != (35, 36, 42) and original_photo.getpixel((651, 1066 - 830)) != (35, 36, 42):

            A = original_photo.crop((65, 67, 734, 1063 - 830))
            B = original_photo.crop((65, 106 - 7476, 736, 1151))
            original_photo.paste((30, 31, 37), (0, 0, 801, 1216))
            original_photo.paste((28, 29, 35), (5, 5, 796, 1211))
            original_photo.paste((26, 27, 33), (10, 10, 791, 1206))
            original_photo.paste((25, 26, 32), (15, 15, 786, 1201))
            original_photo.paste((26, 27, 33), (55, 55, 746, 1161))
            original_photo.paste((27, 28, 34), (60, 60, 741, 1156))
            original_photo.paste((30, 31, 37), (65, 65, 736, 1151))
            original_photo.paste((35, 36, 42), (70, 70, 731, 1146))
            original_photo.paste((30, 31, 37), (150, 70, 153, 1146))
            original_photo.paste((30, 31, 37), (233, 70, 236, 1146))
            original_photo.paste((30, 31, 37), (316, 70, 319, 1146))
            original_photo.paste((30, 31, 37), (399, 70, 402, 1146))
            original_photo.paste((30, 31, 37), (482, 70, 485, 1146))
            original_photo.paste((30, 31, 37), (565, 70, 568, 1146))
            original_photo.paste((30, 31, 37), (648, 70, 651, 1146))
            original_photo.paste((30, 31, 37), (70, 150, 731, 153))
            original_photo.paste((30, 31, 37), (70, 233, 731, 236))
            original_photo.paste((30, 31, 37), (70, 316, 731, 319))
            original_photo.paste((30, 31, 37), (70, 399, 731, 402))
            original_photo.paste((30, 31, 37), (70, 482, 731, 485))
            original_photo.paste((30, 31, 37), (70, 565, 731, 568))
            original_photo.paste((30, 31, 37), (70, 648, 731, 651))
            original_photo.paste((30, 31, 37), (70, 731, 731, 734))
            original_photo.paste((30, 31, 37), (70, 814, 731, 817))
            original_photo.paste((30, 31, 37), (70, 897, 731, 900))
            original_photo.paste((30, 31, 37), (70, 980, 731, 983))
            original_photo.paste((30, 31, 37), (70, 1063, 731, 1066))
            original_photo.paste((A), (65, 150))
            original_photo.paste((B), (65, 1066 - 747))
            score += 100

        if original_photo.getpixel((70, 1066 - 913)) != (35, 36, 42) and original_photo.getpixel((153, 1066 - 913)) != (35, 36, 42)\
        and original_photo.getpixel((236, 1066 - 913)) != (35, 36, 42) and original_photo.getpixel((319, 1066 - 913)) != (35, 36, 42)\
        and original_photo.getpixel((402, 1066 - 913)) != (35, 36, 42) and original_photo.getpixel((485, 1066 - 913)) != (35, 36, 42)\
        and original_photo.getpixel((568, 1066 - 913)) != (35, 36, 42) and original_photo.getpixel((651, 1066 - 913)) != (35, 36, 42):

            A = original_photo.crop((65, 67, 734, 1063 - 913))
            B = original_photo.crop((65, 1066 - 830, 736, 1151))
            original_photo.paste((30, 31, 37), (0, 0, 801, 1216))
            original_photo.paste((28, 29, 35), (5, 5, 796, 1211))
            original_photo.paste((26, 27, 33), (10, 10, 791, 1206))
            original_photo.paste((25, 26, 32), (15, 15, 786, 1201))
            original_photo.paste((26, 27, 33), (55, 55, 746, 1161))
            original_photo.paste((27, 28, 34), (60, 60, 741, 1156))
            original_photo.paste((30, 31, 37), (65, 65, 736, 1151))
            original_photo.paste((35, 36, 42), (70, 70, 731, 1146))
            original_photo.paste((30, 31, 37), (150, 70, 153, 1146))
            original_photo.paste((30, 31, 37), (233, 70, 236, 1146))
            original_photo.paste((30, 31, 37), (316, 70, 319, 1146))
            original_photo.paste((30, 31, 37), (399, 70, 402, 1146))
            original_photo.paste((30, 31, 37), (482, 70, 485, 1146))
            original_photo.paste((30, 31, 37), (565, 70, 568, 1146))
            original_photo.paste((30, 31, 37), (648, 70, 651, 1146))
            original_photo.paste((30, 31, 37), (70, 150, 731, 153))
            original_photo.paste((30, 31, 37), (70, 233, 731, 236))
            original_photo.paste((30, 31, 37), (70, 316, 731, 319))
            original_photo.paste((30, 31, 37), (70, 399, 731, 402))
            original_photo.paste((30, 31, 37), (70, 482, 731, 485))
            original_photo.paste((30, 31, 37), (70, 565, 731, 568))
            original_photo.paste((30, 31, 37), (70, 648, 731, 651))
            original_photo.paste((30, 31, 37), (70, 731, 731, 734))
            original_photo.paste((30, 31, 37), (70, 814, 731, 817))
            original_photo.paste((30, 31, 37), (70, 897, 731, 900))
            original_photo.paste((30, 31, 37), (70, 980, 731, 983))
            original_photo.paste((30, 31, 37), (70, 1063, 731, 1066))
            original_photo.paste((A), (65, 150))
            original_photo.paste((B), (65, 1066 - 830))
            score += 100

        if original_photo.getpixel((70, 1066 - 996)) != (35, 36, 42) and original_photo.getpixel((153, 1066 - 996)) != (35, 36, 42)\
        and original_photo.getpixel((236, 1066 - 996)) != (35, 36, 42) and original_photo.getpixel((319, 1066 - 996)) != (35, 36, 42)\
        and original_photo.getpixel((402, 1066 - 996)) != (35, 36, 42) and original_photo.getpixel((485, 1066 - 996)) != (35, 36, 42)\
        and original_photo.getpixel((568, 1066 - 996)) != (35, 36, 42) and original_photo.getpixel((651, 1066 - 996)) != (35, 36, 42):

            A = original_photo.crop((65, 67, 734, 1063 - 996))
            B = original_photo.crop((65, 1066 - 913, 736, 1151))
            original_photo.paste((30, 31, 37), (0, 0, 801, 1216))
            original_photo.paste((28, 29, 35), (5, 5, 796, 1211))
            original_photo.paste((26, 27, 33), (10, 10, 791, 1206))
            original_photo.paste((25, 26, 32), (15, 15, 786, 1201))
            original_photo.paste((26, 27, 33), (55, 55, 746, 1161))
            original_photo.paste((27, 28, 34), (60, 60, 741, 1156))
            original_photo.paste((30, 31, 37), (65, 65, 736, 1151))
            original_photo.paste((35, 36, 42), (70, 70, 731, 1146))
            original_photo.paste((30, 31, 37), (150, 70, 153, 1146))
            original_photo.paste((30, 31, 37), (233, 70, 236, 1146))
            original_photo.paste((30, 31, 37), (316, 70, 319, 1146))
            original_photo.paste((30, 31, 37), (399, 70, 402, 1146))
            original_photo.paste((30, 31, 37), (482, 70, 485, 1146))
            original_photo.paste((30, 31, 37), (565, 70, 568, 1146))
            original_photo.paste((30, 31, 37), (648, 70, 651, 1146))
            original_photo.paste((30, 31, 37), (70, 150, 731, 153))
            original_photo.paste((30, 31, 37), (70, 233, 731, 236))
            original_photo.paste((30, 31, 37), (70, 316, 731, 319))
            original_photo.paste((30, 31, 37), (70, 399, 731, 402))
            original_photo.paste((30, 31, 37), (70, 482, 731, 485))
            original_photo.paste((30, 31, 37), (70, 565, 731, 568))
            original_photo.paste((30, 31, 37), (70, 648, 731, 651))
            original_photo.paste((30, 31, 37), (70, 731, 731, 734))
            original_photo.paste((30, 31, 37), (70, 814, 731, 817))
            original_photo.paste((30, 31, 37), (70, 897, 731, 900))
            original_photo.paste((30, 31, 37), (70, 980, 731, 983))
            original_photo.paste((30, 31, 37), (70, 1063, 731, 1066))
            original_photo.paste((A), (65, 150))
            original_photo.paste((B), (65, 1066 - 913))
            score += 100

        revolutions += 1