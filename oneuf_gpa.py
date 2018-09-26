import argparse
import json
import decimal
from decimal import ROUND_DOWN

parser = argparse.ArgumentParser()
parser.add_argument('-i', help='Input JSON file')
args = parser.parse_args()

major_prefixes = {'MAC', 'MAD', 'STA', 'MAS',
                  'CIS', 'CEN', 'CNT', 'CDA', 'CAP', 'COP', 'COT',
                  'EEL', 'EGS', 'ENC'}

grade_point_map = {'A': 4.0,
                   'A-': 3.67,
                   'B+': 3.33,
                   'B': 3.0,
                   'B-': 2.67,
                   'C+': 2.33,
                   'C': 2.0,
                   'C-': 1.67,
                   'D+': 1.33,
                   'D': 1.0,
                   'D-': 0.67,
                   'S': 0}

with open(args.i) as f:
    records = json.load(f)

overall_hours_carried = 0
overall_points_earned = 0
major_hours_carried = 0
major_points_earned = 0

for term in records['undergraduate']['terms']:
    print term['termDescription']
    if len(term['creditSources'][0]['sessions']) > 1:
        raise Exception()

    for source in term['creditSources']:
        if source['sourceDescription'] != 'University of Florida':
            print 'skipping non-UF source: {}'.format(source['sourceDescription'])
            continue
        for course in source['sessions'][0]['courses']:
            if course['grade'] == '':
                print 'skipping ungraded course: {} {}'.format(course['subject'], course['catalogNumber'])
                continue
            overall_hours_carried += float(course['credits'])
            overall_points_earned += float(course['hoursEarned']) * grade_point_map[course['grade']]
            if course['subject'] in major_prefixes:
                major_hours_carried += float(course['credits'])
                major_points_earned += float(course['hoursEarned']) * grade_point_map[course['grade']]
                print '{} {}\t[MAJOR]'.format(course['subject'], course['catalogNumber'])
            else:
                print '{} {}'.format(course['subject'], course['catalogNumber'])

    print

overall_gpa = decimal.Decimal(overall_points_earned / overall_hours_carried)
major_gpa = decimal.Decimal(major_points_earned / major_hours_carried)

decimal.getcontext().prec = 4
decimal.getcontext().rounding = ROUND_DOWN

print 'Overall GPA: {:.2f}'.format(overall_gpa)
print 'Major GPA: {:.2f}'.format(major_gpa)
