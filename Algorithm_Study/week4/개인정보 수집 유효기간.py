
#입출력 예
# today = "2022.05.19"
# terms = ["A 6", "B 12", "C 3"]
# privacies = ["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"]
# result = [1, 3]

def convert_date(date):
    YY, MM, DD = date.split('.')
    return int(YY) * 28 * 12 + int(MM) * 28 + int(DD)

def solution(today, terms, privacies):
    terms_dict = dict()
    for term in terms:
        typ, duration = term.split(' ')
        terms_dict[typ] = int(duration)

        today = convert_date(today)
        answer = []
        for i, privacy in enumerate(privacies):
            date, typ = privacy.split(' ')
            date = convert_date(date)
            if date + terms_dict[typ] * 28 <= today:
                answer.append(i + 1)


        return answer