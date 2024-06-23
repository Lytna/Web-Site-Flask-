import random

def soru_uret(min_operand, max_operand, operatorler):
    sol = random.randint(min_operand, max_operand)
    sag = random.randint(min_operand, max_operand)
    operator = random.choice(operatorler)

    ifade = str(sol) + " " + operator + " " + str(sag)
    cevap = eval(ifade)
    return ifade, cevap

def matematik_oyunu(min_operand, max_operand, toplam_soru, operatorler):
    sorular = []
    for _ in range(toplam_soru):
        ifade, cevap = soru_uret(min_operand, max_operand, operatorler)
        sorular.append((ifade, cevap))
    return sorular
