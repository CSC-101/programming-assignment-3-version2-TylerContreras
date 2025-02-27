from typing import List
from data import CountyDemographics

def population_total(counties: List[CountyDemographics]) -> int:
    return sum(county.population.get('2014 Population') for county in counties)

def filter_by_state(counties: List[CountyDemographics], state_abbr: str) -> List[CountyDemographics]:
    if not counties or not isinstance(state_abbr, str) or len(state_abbr) != 2:
        return []

    filtered_counties = [county for county in counties if county.state.upper() == state_abbr.upper()]

    return filtered_counties

def population_by_education(counties: List[CountyDemographics], education_key: str) -> float:
    total = 0.0
    for county in counties:
        population_2014 = county.population.get("2014 Population", 0)
        percentage = county.education.get(education_key, 0)
        computed_value = (population_2014 * (percentage / 100))
        total += computed_value
    return total

def population_by_ethnicity(counties: List[CountyDemographics], ethnicity_key: str) -> float:
    total = 0.0
    for county in counties:
            population_2014 = county.population.get("2014 Population", 0)
            percentage = county.ethnicities.get(ethnicity_key, 0)
            total += (population_2014 * (percentage / 100))
    return total

def population_below_poverty_level(counties: List[CountyDemographics]) -> float:
        total = 0.0
        for county in counties:
            population_2014 = county.population.get("2014 Population", 0)
            percentage = county.income.get("Persons Below Poverty Level", 0)
            total += (population_2014 * (percentage / 100))
        return total


def percent_by_education(counties: List[CountyDemographics], education_key: str) -> float:
    total_population = population_total(counties)
    if total_population == 0:
        return 0.0
    return (population_by_education(counties, education_key) / total_population) * 100


def percent_by_ethnicity(counties: List[CountyDemographics], ethnicity_key: str) -> float:
    total_population = population_total(counties)
    if total_population == 0:
        return 0.0
    return (population_by_ethnicity(counties, ethnicity_key) / total_population) * 100


def percent_below_poverty_level(counties: List[CountyDemographics]) -> float:
    total_population = population_total(counties)
    if total_population == 0:
        return 0.0
    return (population_below_poverty_level(counties) / total_population) * 100


def education_greater_than(counties: List[CountyDemographics], education_key: str, threshold: float) -> List[
    CountyDemographics]:
    return [county for county in counties if county.education.get(education_key, 0) > threshold]


def education_less_than(counties: List[CountyDemographics], education_key: str, threshold: float) -> List[
    CountyDemographics]:
    return [county for county in counties if county.education.get(education_key, 0) < threshold]


def ethnicity_greater_than(counties: List[CountyDemographics], ethnicity_key: str, threshold: float) -> List[
    CountyDemographics]:
    return [county for county in counties if county.ethnicities.get(ethnicity_key, 0) > threshold]


def ethnicity_less_than(counties: List[CountyDemographics], ethnicity_key: str, threshold: float) -> List[
    CountyDemographics]:
    return [county for county in counties if county.ethnicities.get(ethnicity_key, 0) < threshold]


def below_poverty_level_greater_than(counties: List[CountyDemographics], threshold: float) -> List[CountyDemographics]:
    return [county for county in counties if county.income.get("Persons Below Poverty Level", 0) > threshold]


def below_poverty_level_less_than(counties: List[CountyDemographics], threshold: float) -> List[CountyDemographics]:
    return [county for county in counties if county.income.get("Persons Below Poverty Level", 0) < threshold]