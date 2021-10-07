## 💻 Exercises: Day 5

### Exercises: Level 2

# 1. The following is a list of 10 students ages:

'''sh
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
'''
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
# - Sort the list and find the min and max age
ages.sort() 
print(ages)
min_ = ages[0]
max_ = ages[len(ages)-1]
print(f'Min age : {min_} and Max age : {max_}\n')
# - Add the min age and the max age again to the list
ages.append(min_)
ages.append(max_)
print(f'Add the min age and the max age again to the list {ages}\n')
# - Find the median age (one middle item or two middle items divided by two)
#ages.sort() 
middle = (len(ages)-1)//2
if (len(ages)%2 == 0) : # pair
    median = (ages[middle] + ages[middle+1]) / 2
else :
    median = ages[middle] 
print(f'Median age : {median}\n')    
# - Find the average age (sum of all items divided by their number )
""" sum = 0
for i in range(len(ages)) : 
    sum += ages[i] """
average = sum(ages)/len(ages)
print(f'Average age : {average}\n')
# - Find the range of the ages (max minus min)
""" ages.sort()
min = ages[0]
print(f'ages sort ascending: {ages}')
ages.sort(reverse=True)
max = ages[0]
print(f'ages sort descending : {ages}') """
min_ = min(ages)
max_ = max(ages)
range = max(ages) - min(ages)
print(f'Find the range of the ages (max minus min) : {range} \n')

# - Compare the value of (min - average) and (max - average), use _abs()_ method
min_abs = abs(min_ - average)
max_abs = abs(max_ - average)
print(f'Compare the value of (min - average) {min_abs} and (max - average) {max_abs} \n')

# 1. Find the middle country(ies) in the [countries list](https://github.com/Asabeneh/30-Days-Of-Python/tree/master/data/countries.py)
countries = [
  'Afghanistan',
  'Albania',
  'Algeria',
  'Andorra',
  'Angola',
  'Antigua and Barbuda',
  'Argentina',
  'Armenia',
  'Australia',
  'Austria',
  'Azerbaijan',
  'Bahamas',
  'Bahrain',
  'Bangladesh',
  'Barbados',
  'Belarus',
  'Belgium',
  'Belize',
  'Benin',
  'Bhutan',
  'Bolivia',
  'Bosnia and Herzegovina',
  'Botswana',
  'Brazil',
  'Brunei',
  'Bulgaria',
  'Burkina Faso',
  'Burundi',
  'Cambodia',
  'Cameroon',
  'Canada',
  'Cape Verde',
  'Central African Republic',
  'Chad',
  'Chile',
  'China',
  'Colombi',
  'Comoros',
  'Congo (Brazzaville)',
  'Congo',
  'Costa Rica',
  "Cote d'Ivoire",
  'Croatia',
  'Cuba',
  'Cyprus',
  'Czech Republic',
  'Denmark',
  'Djibouti',
  'Dominica',
  'Dominican Republic',
  'East Timor (Timor Timur)',
  'Ecuador',
  'Egypt',
  'El Salvador',
  'Equatorial Guinea',
  'Eritrea',
  'Estonia',
  'Ethiopia',
  'Fiji',
  'Finland',
  'France',
  'Gabon',
  'Gambia, The',
  'Georgia',
  'Germany',
  'Ghana',
  'Greece',
  'Grenada',
  'Guatemala',
  'Guinea',
  'Guinea-Bissau',
  'Guyana',
  'Haiti',
  'Honduras',
  'Hungary',
  'Iceland',
  'India',
  'Indonesia',
  'Iran',
  'Iraq',
  'Ireland',
  'Israel',
  'Italy',
  'Jamaica',
  'Japan',
  'Jordan',
  'Kazakhstan',
  'Kenya',
  'Kiribati',
  'Korea, North',
  'Korea, South',
  'Kuwait',
  'Kyrgyzstan',
  'Laos',
  'Latvia',
  'Lebanon',
  'Lesotho',
  'Liberia',
  'Libya',
  'Liechtenstein',
  'Lithuania',
  'Luxembourg',
  'Macedonia',
  'Madagascar',
  'Malawi',
  'Malaysia',
  'Maldives',
  'Mali',
  'Malta',
  'Marshall Islands',
  'Mauritania',
  'Mauritius',
  'Mexico',
  'Micronesia',
  'Moldova',
  'Monaco',
  'Mongolia',
  'Morocco',
  'Mozambique',
  'Myanmar',
  'Namibia',
  'Nauru',
  'Nepal',
  'Netherlands',
  'New Zealand',
  'Nicaragua',
  'Niger',
  'Nigeria',
  'Norway',
  'Oman',
  'Pakistan',
  'Palau',
  'Panama',
  'Papua New Guinea',
  'Paraguay',
  'Peru',
  'Philippines',
  'Poland',
  'Portugal',
  'Qatar',
  'Romania',
  'Russia',
  'Rwanda',
  'Saint Kitts and Nevis',
  'Saint Lucia',
  'Saint Vincent',
  'Samoa',
  'San Marino',
  'Sao Tome and Principe',
  'Saudi Arabia',
  'Senegal',
  'Serbia and Montenegro',
  'Seychelles',
  'Sierra Leone',
  'Singapore',
  'Slovakia',
  'Slovenia',
  'Solomon Islands',
  'Somalia',
  'South Africa',
  'Spain',
  'Sri Lanka',
  'Sudan',
  'Suriname',
  'Swaziland',
  'Sweden',
  'Switzerland',
  'Syria',
  'Taiwan',
  'Tajikistan',
  'Tanzania',
  'Thailand',
  'Togo',
  'Tonga',
  'Trinidad and Tobago',
  'Tunisia',
  'Turkey',
  'Turkmenistan',
  'Tuvalu',
  'Uganda',
  'Ukraine',
  'United Arab Emirates',
  'United Kingdom',
  'United States',
  'Uruguay',
  'Uzbekistan',
  'Vanuatu',
  'Vatican City',
  'Venezuela',
  'Vietnam',
  'Yemen',
  'Zambia',
  'Zimbabwe',  
]
print(len(countries))
medium = (len(countries)-1)//2

if (len(countries)%2 != 0) :
    print(f'Find the middle country : {countries[medium]}\n') 
else :
    print(f'Find the middle countries : {countries[medium:medium+2]}\n')

# 1. Divide the countries list into two equal lists if it is even if not one more country for the first half.
lst1 = countries[:medium]
lst2 = countries[medium:]
print(f'First list of length {len(lst1)} : {lst1} \n')
print(f'Second list of length {len(lst2)} : {lst2} \n')

# 1. ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']. 
# Unpack the first three countries and the rest as scandic countries.
superpower = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
c, r, u, *valhalla = superpower
print(f'Countries superpower : {superpower}')
print(f'China : {c}')
print(f'Rusia : {r}')
print(f'USA : {u}')
print(f'Countries scandic : {valhalla}')
