from covid import Covid  # pip install covid

covid = Covid()
cases = covid.get_status_by_country_name("Bangladesh")
print(cases)
for x in cases:
    print(x, ":", cases[x])
