import csv

# open dataset 
f = open("climate_change_dataset.csv", "r", encoding="utf-8")   
data = csv.DictReader(f)
rows = list(data)

print("Total rows:", len(rows))
print("Headers:", data.fieldnames)

# Q1: Temperature change first vs last year
years = [int(r["Year"]) for r in rows if r["Year"] != ""]
first = min(years)
last = max(years)
first_temps = [float(r["Avg Temperature (°C)"]) for r in rows if r["Year"] != "" and int(r["Year"]) == first and r["Avg Temperature (°C)"] != ""]
last_temps = [float(r["Avg Temperature (°C)"]) for r in rows if r["Year"] != "" and int(r["Year"]) == last and r["Avg Temperature (°C)"] != ""]
print("\nQ1:", first, "->", last, "Temp:", round(sum(first_temps)/len(first_temps),2), "to", round(sum(last_temps)/len(last_temps),2))

# Q2: Top CO2 emitters
co2 = {}
for r in rows:
    if r["Country"] != "" and r["CO2 Emissions (Tons/Capita)"] != "":
        co2.setdefault(r["Country"], []).append(float(r["CO2 Emissions (Tons/Capita)"]))
avg_co2 = {c: sum(co2[c])/len(co2[c]) for c in co2}
print("\nQ2: Top CO2 emitters:", sorted(avg_co2.items(), key=lambda x: x[1], reverse=True)[:5])

# Q3: Renewable vs CO2
x=[]; y=[]
for r in rows:
    if r["Renewable Energy (%)"]!="" and r["CO2 Emissions (Tons/Capita)"]!="":
        x.append(float(r["Renewable Energy (%)"])); y.append(float(r["CO2 Emissions (Tons/Capita)"]))
if x and y:
    print("\nQ3: Renewable vs CO2 sample:", list(zip(x[:5], y[:5])))

# Q4: Forest vs CO2
forest={}
for r in rows:
    if r["Country"]!="" and r["Forest Area (%)"]!="":
        forest.setdefault(r["Country"], []).append(float(r["Forest Area (%)"]))
sample=[(c, round(sum(forest[c])/len(forest[c]),2), round(sum(co2[c])/len(co2[c]),2) if c in co2 else None) for c in list(forest.keys())[:5]]
print("\nQ4: Forest vs CO2 sample:", sample)

# Q5: Population vs CO2
top_emitters=sorted(avg_co2.items(), key=lambda x: x[1], reverse=True)[:5]
for c,_ in top_emitters:
    pops=[float(r["Population"]) for r in rows if r["Country"]==c and r["Population"]!=""]
    co2vals=[float(r["CO2 Emissions (Tons/Capita)"]) for r in rows if r["Country"]==c and r["CO2 Emissions (Tons/Capita)"]!=""]
    if pops and co2vals:
        print("\nQ5:", c, "pop:", pops[0], "->", pops[-1], "CO2:", co2vals[0], "->", co2vals[-1])

# Q6: Rainfall vs Extreme Events
rain=[]; ext=[]
for r in rows:
    if r["Rainfall (mm)"]!="" and r["Extreme Weather Events"]!="":
        rain.append(float(r["Rainfall (mm)"])); ext.append(float(r["Extreme Weather Events"]))
if rain and ext:
    print("\nQ6: Rainfall vs Extreme Events sample:", list(zip(rain[:5], ext[:5])))

# Q7: Triple challenge
triple=[]
for c in co2:
    ren=[float(r["Renewable Energy (%)"]) for r in rows if r["Country"]==c and r["Renewable Energy (%)"]!=""]
    fo=[float(r["Forest Area (%)"]) for r in rows if r["Country"]==c and r["Forest Area (%)"]!=""]
    if ren and fo:
        if (avg_co2[c] > 50) and (sum(ren)/len(ren) < 20) and (sum(fo)/len(fo) < 30):
            triple.append(c)
print("\nQ7: Triple challenge countries:", triple[:5])

# Q8: Climate leaders
leaders=[]
for c in co2:
    ren=[float(r["Renewable Energy (%)"]) for r in rows if r["Country"]==c and r["Renewable Energy (%)"]!=""]
    fo=[float(r["Forest Area (%)"]) for r in rows if r["Country"]==c and r["Forest Area (%)"]!=""]
    if ren and fo:
        if (avg_co2[c] < 20) and (sum(ren)/len(ren) > 40) and (sum(fo)/len(fo) > 40):
            leaders.append(c)
print("\nQ8: Climate leaders:", leaders[:5])

# Q9: CO2 vs Temp
x=[float(r["CO2 Emissions (Tons/Capita)"]) for r in rows if r["CO2 Emissions (Tons/Capita)"]!="" and r["Avg Temperature (°C)"]!=""]
y=[float(r["Avg Temperature (°C)"]) for r in rows if r["CO2 Emissions (Tons/Capita)"]!="" and r["Avg Temperature (°C)"]!=""]
print("\nQ9: Sample CO2 vs Temp:", list(zip(x[:5], y[:5])))

# Q10: Developed vs Developing
top_names=[t[0] for t in top_emitters]
top_ren=[float(r["Renewable Energy (%)"]) for r in rows if r["Country"] in top_names and r["Renewable Energy (%)"]!=""]
rest_ren=[float(r["Renewable Energy (%)"]) for r in rows if r["Country"] not in top_names and r["Renewable Energy (%)"]!=""]
print("\nQ10: Avg renewable - top emitters:", round(sum(top_ren)/len(top_ren),2), "rest:", round(sum(rest_ren)/len(rest_ren),2))

# Q11: Renewable improvement
growth={}
for r in rows:
    if r["Year"]!="" and r["Renewable Energy (%)"]!="" and r["Country"]!="":
        y=int(r["Year"]); c=r["Country"]; v=float(r["Renewable Energy (%)"])
        if y==first: growth.setdefault(c,[0,0])[0]=v
        if y==last: growth.setdefault(c,[0,0])[1]=v
diffs=[(c,growth[c][1]-growth[c][0]) for c in growth if growth[c][0] and growth[c][1]]
print("\nQ11: Top renewable improvers:", sorted(diffs,key=lambda x:x[1],reverse=True)[:5])

# Q12: Best vs Worst overall
score={}
for c in co2:
    ren=[float(r["Renewable Energy (%)"]) for r in rows if r["Country"]==c and r["Renewable Energy (%)"]!=""]
    fo=[float(r["Forest Area (%)"]) for r in rows if r["Country"]==c and r["Forest Area (%)"]!=""]
    if ren and fo:
        score[c] = -avg_co2[c] + (sum(ren)/len(ren)) + (sum(fo)/len(fo))
sorted_score=sorted(score.items(), key=lambda x: x[1], reverse=True)
print("\nQ12: Best countries:", sorted_score[:5])
print("Q12: Worst countries:", sorted_score[-5:])