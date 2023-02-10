feedback = input("будь ласка залишне свій відгук для 'Морська Зірка': ")

discount = 0

if "menu" in feedback.lower():
    discount += 5
if "gym" in feedback.lower() or "sportzal" in feedback.lower():
    discount += 5
if "service" in feedback.lower() or "obsluzhuvannya" in feedback.lower():
    discount += 5

if len(feedback) > 60:
    discount += 15

print("ваша знижка наступного разу складає : " + str(discount) + "%")
