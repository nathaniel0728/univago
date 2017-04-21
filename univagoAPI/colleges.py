from michigan import michiganUpdate
from brown import brownUpdate
from worcester import worcesterUpdate
from harvard import harvardUpdate
from northwestern import northwesternUpdate
from uva import uvaUpdate
from cornell import cornellUpdate
from cmu import cmuUpdate

#yes, this is ugly, but it works... I'll fix it later
def updateCollege():
	colleges = []
	colleges.append(michiganUpdate())
	colleges.append(brownUpdate())
	colleges.append(worcesterUpdate())
	colleges.append(harvardUpdate())
	colleges.append(northwesternUpdate())
	colleges.append(uvaUpdate())
	colleges.append(cmuUpdate())
	colleges.append(cornellUpdate())
	return colleges
