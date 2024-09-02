# def average_salary(music):
#     annual_salary = sum(music)
#     monthly_salary = len(music)
#     average = annual_salary / monthly_salary
#     return average
# music = [100,200,300,15023,2102]
# print("Musician average salary: ",average_salary(music))
#
# def average_salary(footballer):
#     annual_salary = sum(footballer)
#     monthly_salary = len(footballer)
#     average = annual_salary / monthly_salary
#     return average
# footballer = [100,200,300,15023,2102]
# print("footballer avearage salary: ",average_salary(footballer))

def average_salary(footballer , musician):
    annual_salary = sum(footballer , musician)
    monthly_salary = len(footballer , musician)
    average_salary = annual_salary / monthly_salary
    return