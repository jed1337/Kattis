b_age, b_retire_age, b_yearly_savings, a_age, a_yearly_savings = list(map(int, input().rstrip().split()))

b_total_savings = b_yearly_savings * (b_retire_age-b_age)

a_total_savings = 0
a_retire_age = a_age
while a_total_savings <= b_total_savings:
    a_total_savings += a_yearly_savings
    a_retire_age +=1

print(a_retire_age)