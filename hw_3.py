from typing import List
from data import CountyDemographics

def population_total(counties: List[CountyDemographics]) -> int:
    #Returns the total 2014 population.
    return sum(county.population.get('2014 Population', 0) for county in counties)

def filter_by_state(counties: List[CountyDemographics], state_abbr: str) -> List[CountyDemographics]:
   #Filters and returns a list of counties that belong to the state abbreviation given.
    if not counties or not isinstance(state_abbr, str) or len(state_abbr) != 2:
        return []
    return [county for county in counties if county.state.upper() == state_abbr.upper()]

def population_by_education(counties: List[CountyDemographics], education_key: str) -> float:
    #Calculates the total sub-population with the given education level across all counties.
    total = 0.0
    for county in counties:
        population_2014 = county.population.get("2014 Population", 0)
        percentage = county.education.get(education_key, 0)
        total += (population_2014 * (percentage / 100))
    return total

def population_by_ethnicity(counties: List[CountyDemographics], ethnicity_key: str) -> float:
    #Calculates the total sub-population for the given ethnicity across all counties.
    total = 0.0
    for county in counties:
        population_2014 = county.population.get("2014 Population", 0)
        percentage = county.ethnicities.get(ethnicity_key, 0)
        total += (population_2014 * (percentage / 100))
    return total

def population_below_poverty_level(counties: List[CountyDemographics]) -> float:
    #Calculates the total sub-population below the poverty level across all counties.
    total = 0.0
    for county in counties:
        population_2014 = county.population.get("2014 Population", 0)
        percentage = county.income.get("Persons Below Poverty Level", 0)
        total += (population_2014 * (percentage / 100))
    return total

def percent_by_education(counties: List[CountyDemographics], education_key: str) -> float:
    #Returns the percentage of the total population that has the given education level.
    total_population = population_total(counties)
    if total_population == 0:
        return 0.0
    return (population_by_education(counties, education_key) / total_population) * 100

def percent_by_ethnicity(counties: List[CountyDemographics], ethnicity_key: str) -> float:
    #Returns the percentage of the total population that belongs to the given ethnicity.
    total_population = population_total(counties)
    if total_population == 0:
        return 0.0
    return (population_by_ethnicity(counties, ethnicity_key) / total_population) * 100

def percent_below_poverty_level(counties: List[CountyDemographics]) -> float:
    #Returns the percentage of the total population that is below the poverty level.
    total_population = population_total(counties)
    if total_population == 0:
        return 0.0
    return (population_below_poverty_level(counties) / total_population) * 100

def education_greater_than(counties: List[CountyDemographics], education_key: str, threshold: float) -> List[CountyDemographics]:
    #Returns a list of counties where the given education level is greater than the given threshold.
    return [county for county in counties if county.education.get(education_key, 0) > threshold]

def education_less_than(counties: List[CountyDemographics], education_key: str, threshold: float) -> List[CountyDemographics]:
    #Returns a list of counties where the given education level is less than the given threshold.
    return [county for county in counties if county.education.get(education_key, 0) < threshold]

def ethnicity_greater_than(counties: List[CountyDemographics], ethnicity_key: str, threshold: float) -> List[CountyDemographics]:
    #Returns a list of counties where the given ethnicity percentage is greater than the given threshold.
    return [county for county in counties if county.ethnicities.get(ethnicity_key, 0) > threshold]

def ethnicity_less_than(counties: List[CountyDemographics], ethnicity_key: str, threshold: float) -> List[CountyDemographics]:
    #Returns a list of counties where the given ethnicity percentage is less than the given threshold.
    return [county for county in counties if county.ethnicities.get(ethnicity_key, 0) < threshold]

def below_poverty_level_greater_than(counties: List[CountyDemographics], threshold: float) -> List[CountyDemographics]:
    #Returns a list of counties where the percentage of people below poverty level is greater than the threshold.
    return [county for county in counties if county.income.get("Persons Below Poverty Level", 0) > threshold]

def below_poverty_level_less_than(counties: List[CountyDemographics], threshold: float) -> List[CountyDemographics]:
    #Returns a list of counties where the percentage of people below poverty level is less than the threshold.
    return [county for county in counties if county.income.get("Persons Below Poverty Level", 0) < threshold]