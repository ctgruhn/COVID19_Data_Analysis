from flask_table import Table, Col

class ItemTable(Table):
    # Classes for styling, uses bootstrap
    classes = ['table', 'table-hover', 'table-bordered', 'table-condensed']
    #Header names
    name = Col('Field Name')
    description = Col('Description')

class Item(object):
    def __init__(self, name, description):
        self.name = name
        self.description = description

# From https://covidtracking.com/about-data/data-definitions
SCHEMA = [
    dict(name='positive', 
    description='Total number of people with confirmed OR probable cases of COVID-19 reported by the state or territory (per the expanded CSTE case definition of April 5th, 2020 approved by the CDC).' +
                '\nA confirmed case is a person who has a positive test result from an FDA approved diagnostic molecular test.\nA probable case is a person who has presentable symptoms WITH epidemiological ' +
                'evidence or has BOTH a positive presumptive laboratory test AND also EITHER presentable symptoms OR epidemiological evidence, or who has been issued a death certificate listing COVID-19 as a ' +
                'cause of death or significant contributing cause of death with no confirmatory testing. Epidemiological evidence refers either to close proximity contact with a known case or travel history ' +
                'to an area with high disease incidence. According to the guidelines, FDA approved antibody and antigen tests are considered presumptive laboratory evidence and therefore only one potential part ' +
                'of the evidence required to classify a case as probable.'),

    dict(name='negative', 
    description='Total number of unique people with a completed PCR test that returns negative. For states / territories that do not report this number directly, we compute it using one of several methods, ' +
                'depending on which data points the state provides. Due to complex reporting procedures, this number might be mixing units and therefore, at best, it should only be considered an estimate of ' +
                'the number of people with a completed PCR test that return negative.'),

    dict(name='pending', 
    description='Total number of viral tests that have not been completed as reported by the state or territory.'),
    
    dict(name='hospitalizedCurrently', 
    description='Individuals who are currently hospitalized with COVID-19. Definitions vary by state / territory. Where possible, we report hospitalizations with confirmed or probable COVID-19 cases per the ' +
                'expanded CSTE case definition of April 5th, 2020 approved by the CDC.'),

    dict(name='hospitalized', 
    description='Same as hospitalizedCurrently'),

    dict(name='inIcuCurrently', 
    description='Individuals who are currently hospitalized in the Intensive Care Unit with COVID-19. Definitions vary by state / territory. Where possible, we report patients in the ICU with confirmed or ' +
                'probable COVID-19 cases per the expanded CSTE case definition of April 5th, 2020 approved by the CDC.'),
    
    dict(name='onVentilatorCurrently', 
    description='Individuals who are currently hospitalized under advanced ventilation with COVID-19. Definitions vary by state / territory. Where possible, we report patients on ventilation with confirmed ' +
                'or probable COVID-19 cases per the expanded CSTE case definition of April 5th, 2020 approved by the CDC.'),
    
    dict(name='recovered', 
    description='Total number of people that are identified as recovered from COVID-19. States provide very disparate definitions on what constitutes a “recovered” COVID-19 case. Types of “recovered” cases ' +
                'include those who are discharged from hospitals, released from isolation after meeting CDC guidance on symptoms cessation, or those who have not been identified as fatalities after a number ' +
                'of days (30 or more) post disease onset. Specifics vary for each state or territory.'),

    dict(name='totalTestsViral', 
    description='Total number of PCR tests (or specimens tested) as reported by the state or territory. The count for this metric is incremented up each time a specimen is tested and the result is reported. If we ' +
                'discover that a jurisdiction is including antigen tests in this metric, we will annotate that state or territory’s data accordingly.'),

    dict(name='positiveTestsViral', 
    description='Total number of unique people tested at least once via PCR testing, as reported by the state or territory. The count for this metric is incremented up only the first time an individual person is ' +
                'tested and their result is reported. Future tests of the same person will not be added to this count.\nFor states with ambiguous annotations, we have assigned their total tests to this category. ' +
                'In the case where the state only provides negative cases, this field is calculated as the summation of people who tested positive (\“Positive Cases (People\”) and the number of people who tested ' +
                'negative (“Negative (People or Cases)”). If we discover that a jurisdiction is including antigen tests in this metric, we will annotate that state or territory’s data accordingly.'),

    dict(name='negativeTestsViral', 
    description='Total number of completed PCR tests (or specimens tested) that return negative as reported by the state or territory. For states/territories that do not report this number directly, we compute it ' +
                'using one of several methods, depending on which data points the state provides. If we discover that a jurisdiction is including antigen tests in this metric, we will annotate that state or territory’s data accordingly.'),

    dict(name='positiveCasesViral', 
    description='Total number of unique people with a completed PCR test that returns positive as reported by the state or territory. This is equivalent to a confirmed case as per the expanded CSTE case definition of April 5th, 2020 approved by the CDC.'),

    dict(name='deathConfirmed', 
    description='Total fatalities with confirmed COVID-19 case diagnosis (per the expanded CSTE case definition of April 5th, 2020 approved by the CDC). In states where the information is available, it only tracks ' +
                'fatalities with confirmed COVID-19 case diagnosis where on the death certificate, COVID-19 is listed as an underlying cause of death according to WHO guidelines.'),

    dict(name='deathProbable', 
    description='Total fatalities with probable COVID-19 case diagnosis (per the expanded CSTE case definition of April 5th, 2020 approved by the CDC). In states where the information is available, it only tracks ' +
                'fatalities with probable COVID-19 case diagnosis where on the death certificate, COVID-19 is listed as an underlying cause of death according to WHO guidelines.'),

    dict(name='death', 
    description='Total fatalities with confirmed OR probable COVID-19 case diagnosis (per the expanded CSTE case definition of April 5th, 2020 approved by the CDC). In states where the information is available, ' +
                'it only tracks fatalities with confirmed OR probable COVID-19 case diagnosis where on the death certificate, COVID-19 is listed as an underlying cause of death according to WHO guidelines.')
]

# Create Table
table = ItemTable(SCHEMA)