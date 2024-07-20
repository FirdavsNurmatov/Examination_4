def find_numbers(text):
    lst = []
    n = len(text)
    m = 0
    while m < n:
        if 47 < ord(text[m]) < 58:
            if 47 < ord(text[m+1]) < 58:
                temp = text[m] + text[m+1]
                lst.append(int(temp))
                m+=1
            else:
                lst.append(int(text[m]))
        m+=1
    if sorted(lst) == lst:
        return True
    return False

text = "Maktabimizda 4-'a' sinfdagi 17 tadan ortiq o'quvchilar imtixondan 86 balldan yuqori ball oldi."
text2 = "Najot ta'limdagi Foundation 81 gurugidagi 90 %' o'quvchilar  imtixondan 85 balldan yuqori vall oldi."
text3 = "Nafot ta'limdagi 81 guruhdagi 11 ta o'quvchidan 11 ta tasi imtixonlarni a'lo topshirdi."
print(find_numbers(text))