import re

text='''Horia Chiornita <horia.chiornita@ericsson.com>; Mihai Cornea <mihai.cornea@ericsson.com>; Florin Marius Ghimie <florin.marius.ghimie@ericsson.com>; Adrian Gurbina <adrian.gurbina@ericsson.com>; Ionut Bojinca <ionut.bojinca@ericsson.com>; Eduard-Andrei Garoafa <eduard-andrei.garoafa@ericsson.com>; Dixit Sharma <dixit.sharma@ericsson.com>'''

occ = re.sub(r"([\w.-]*)@([\w.-]*\.\w{2,3})",r"\1 at \2",text)
print(occ)
