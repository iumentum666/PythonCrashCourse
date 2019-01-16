# Her importerer vi en standard klasse fra python biblioteket
# Denne oppfører seg omtrent som en dictionary, men den holder rede på rekkefølgen 
# ting blir lagt inn i

from collections import OrderedDict

favorite_languages = OrderedDict()

favorite_languages['jen'] = 'python'
favorite_languages['sarah'] = 'c'
favorite_languages['edward'] = 'ruby'
favorite_languages['phil'] = 'python'

for name, language in favorite_languages.items():
    print(name.title() + "'s favorite language is " + language.title() + ".")