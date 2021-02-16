import math


def impact_factor(citations, plan_to_publish):
    return math.ceil(citations / plan_to_publish)


plan_to_publish, impact_factor_required = list(map(int, input().split()))

citations = 0
while impact_factor(citations, plan_to_publish) < impact_factor_required:
    citations += 1

print(citations)
