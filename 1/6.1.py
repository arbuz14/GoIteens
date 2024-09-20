west_hemisphere_continents = ["Північна Америка", "Південна Америка"]

east_hemisphere_continents = ["Євразія (частина Європи та Азії)", "Африка", "Австралія", "Антарктида"]

all_continents = west_hemisphere_continents + east_hemisphere_continents

sorted_continents = sorted(all_continents)

for continent in sorted_continents:
    print(continent)
