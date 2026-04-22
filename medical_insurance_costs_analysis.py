#import
import csv
with open('insurance.csv', newline='') as insurance_csv:
    data = insurance_csv.readlines()

#group results by gender/generation/kids
u50_w_nk = {}
o50_w_nk = {}
u50_w_k = {}
o50_w_k = {}
men = {}
for row in data[1:]:
    values = row.strip().split(",")
    person = {
        "age": int(values[0]),
        "sex": values[1],
        "bmi": float(values[2]),
        "children": int(values[3]),
        "smoker": values[4],
        "region": values[5],
        "charges": float(values[6])
    }
    if person['age'] < 50 and person['sex'] == 'female' and person['children'] == 0:
        u50_w_nk.update({len(u50_w_nk): person})
    elif person['age'] >= 50 and person['sex'] == 'female' and person['children'] == 0:
        o50_w_nk.update({len(o50_w_nk): person})
    elif person['age'] < 50 and person['sex'] == 'female' and person['children'] != 0:
        u50_w_k.update({len(u50_w_k): person})
    elif person['age'] >= 50 and person['sex'] == 'female' and person['children'] != 0:
        o50_w_k.update({len(o50_w_k): person})
    else:
        men.update({len(men): person})
#check group coding
#for person in u50_w_k.values():
    #if not (person['age'] < 50 and person['sex'] == 'female' and person['children'] != 0):
        #print("Error found:", person)
#for person in o50_w_k.values():
    #if not (person['age'] >= 50 and person['sex'] == 'female' and person['children'] != 0):
        #print("Error found:", person)
#for person in men.values():
    #if not person['sex'] == 'male':
        #print("Error found:", person)
#for person in u50_w_nk.values():
    #if not (person['age'] < 50 and person['sex'] == 'female' and person['children'] == 0):
        #print("Error found:", person)
#for person in o50_w_nk.values():
    #if not (person['age'] >= 50 and person['sex'] == 'female' and person['children'] == 0):
        #print("Error found:", person)

#further subdivide u50_w_nk
#smoker/non-smoker
smoker = {}
non_smoker = {}
for person in u50_w_nk.values():
    if person['smoker'] == 'yes':
        smoker.update(({len(smoker): person}))
    else:
        non_smoker.update(({len(non_smoker): person}))
#for person in non_smoker.values():
    #if not person['smoker'] == 'no':
        #print("Error found:", person)
#BMI
under_or_normal = {}
overweight = {}
obese = {}
for person in u50_w_nk.values():
    if person['bmi'] < 25:
        under_or_normal.update(({len(under_or_normal): person}))
    elif person['bmi'] >= 30:
        obese.update(({len(obese): person}))
    else:
        overweight.update(({len(overweight): person}))
#for person in under_or_normal.values():
    #if person['bmi'] > 25:
        #print("Error found:", person)
#for person in obese.values():
    #if person['bmi'] < 30:
        #print("Error found:", person)
#Region
northwest = {}
southwest = {}
northeast = {}
southeast = {}
for person in u50_w_nk.values():
    if person['region'] == 'northwest':
        northwest.update(({len(northwest): person}))
    elif person['region'] == 'southwest':
        southwest.update(({len(southwest): person}))
    elif person['region'] == 'northeast':
        northeast.update(({len(northeast): person}))
    else:
        southeast.update(({len(southeast): person}))
#print(len(northwest) + len(northeast) + len(southwest) + len(southeast) == len(u50_w_nk))

#define averaging function
def avg_cost_plus_size(group):
    count = len(group)
    if count == 0:
        return 0, 0
    total = 0
    for person in group.values():
        total += person['charges']
    return round(total / count, 2), count
#group average
#avg, n = avg_cost_plus_size(u50_w_nk)
#print("Women under 50, no kids average insurance cost: ", avg, "Sample size: ", n)

#average by smoking
#avg, n = avg_cost_plus_size(smoker)
#print("Smokers average insurance cost: ", avg, "Sample size: ", n)
#avg, n = avg_cost_plus_size(non_smoker)
#print("Non-smokers average insurance cost: ", avg, "Sample size: ", n)

#average by BMI
#avg, n = avg_cost_plus_size(under_or_normal)
#print("Under or normal weight average insurance cost: ", avg, "Sample size: ", n)
#avg, n = avg_cost_plus_size(overweight)
#print("Overweight average insurance cost: ", avg, "Sample size: ", n)
#avg, n = avg_cost_plus_size(obese)
#print("Obese average insurance cost: ", avg, "Sample size: ", n)

#average by region
#avg, n = avg_cost_plus_size(northwest)
#print("Northwest average insurance cost: ", avg, "Sample size: ", n)
#avg, n = avg_cost_plus_size(southwest)
#print("Southwest average insurance cost: ", avg, "Sample size: ", n)
#avg, n = avg_cost_plus_size(northeast)
#print("Northeast average insurance cost: ", avg, "Sample size: ", n)
#avg, n = avg_cost_plus_size(southeast)
#print("Southeast average insurance cost: ", avg, "Sample size: ", n)

#calculate impacts
# Smoking impact
smoker_avg, smoker_n = avg_cost_plus_size(smoker)
non_smoker_avg, non_smoker_n = avg_cost_plus_size(non_smoker)

smoking_diff = round(smoker_avg - non_smoker_avg, 2)
smoking_pct = round((smoking_diff / non_smoker_avg) * 100, 2)

# BMI impact
overweight_avg, _ = avg_cost_plus_size(overweight)
obese_avg, _ = avg_cost_plus_size(obese)

bmi_diff = round(obese_avg - overweight_avg, 2)
bmi_pct = round((bmi_diff / overweight_avg) * 100, 2)

#print results
table = {}

table['Women <50 no kids'] = avg_cost_plus_size(u50_w_nk)

table['Smokers'] = avg_cost_plus_size(smoker)
table['Non-Smokers'] = avg_cost_plus_size(non_smoker)

table['Under/Normal BMI'] = avg_cost_plus_size(under_or_normal)
table['Overweight'] = avg_cost_plus_size(overweight)
table['Obese'] = avg_cost_plus_size(obese)

table['Northeast'] = avg_cost_plus_size(northeast)
table['Northwest'] = avg_cost_plus_size(northwest)
table['Southeast'] = avg_cost_plus_size(southeast)
table['Southwest'] = avg_cost_plus_size(southwest)

print(f"{'Group':<20}{'Avg Cost':<15}{'Sample Size'}")
for group, (avg, size) in table.items():
    print(f"{group:<20}{avg:<15.2f}{size}")

print("\n--- Key Impacts ---")
print(f"{'Comparison':<25}{'Cost Diff':>15}{'% Diff':>10}")
print(f"{'Smoking (Yes vs No)':<25}{smoking_diff:>15.2f}{f'{smoking_pct:.2f}%':>10}")
print(f"{'Obese vs Overweight':<25}{bmi_diff:>15.2f}{f'{bmi_pct:.2f}%':>10}")
