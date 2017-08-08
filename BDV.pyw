from __future__ import division
import sys
import inspect
from GUI import *
from Charts import *
from About import *
from Table import *
from Predict import *
#from sklearn import linear_model

import pandas as pd

class aboutDialog(QtGui.QDialog, Ui_aboutDialog):
	def __init__(self, parent=None):
		QtGui.QDialog.__init__(self, parent)
		flags = QtCore.Qt.Drawer | QtCore.Qt.WindowStaysOnTopHint
		self.setWindowFlags(flags)
		self.setupUi(self)

class tableDialog(QtGui.QDialog, Ui_tableDialog):
	def __init__(self, parent=None):
		QtGui.QDialog.__init__(self, parent)
		flags = QtCore.Qt.Drawer | QtCore.Qt.WindowStaysOnTopHint
		self.setWindowFlags(flags)
		self.setupUi(self)

		self.addTableData()

	def addTableData(self):
		Par = dataset.columns.values
		row = 0
		col = 0
		for item in Par:
			anitem = QtGui.QTableWidgetItem(item)
			self.tableWidget.setItem(row, col, anitem)
			col+=1

		row = 1
		col = 0
		for nitem in Par:
			for i in dataset[str(nitem)]:
				anitem = QtGui.QTableWidgetItem(str(i))
				self.tableWidget.setItem(row, col, anitem)
				row+=1
			row=1
			col+=1

class predictDialog(QtGui.QDialog, Ui_predictDialog):
	def __init__(self, parent=None):
		QtGui.QDialog.__init__(self, parent)
		flags = QtCore.Qt.Drawer | QtCore.Qt.WindowStaysOnTopHint
		self.setWindowFlags(flags)
		self.setupUi(self)

		self.sqfeet = [150, 200, 250, 300, 350, 400, 600, 750, 950, 1300]
		self.price = [6450, 7450, 8450, 9450, 11450, 15450, 18450, 21350, 25650, 31960]

		row=0
		col=0
		for i1, i2 in zip(self.sqfeet, self.price):
			item1 = QtGui.QTableWidgetItem(str(i1))
			item2 = QtGui.QTableWidgetItem(str(i2))
			self.tableWidget_1.setItem(row, col, item1)
			self.tableWidget_1.setItem(row, col+1, item2)
			row+=1
		'''
		regr = linear_model.LinearRegression()
		regr.fit(self.sqfeet, self.price)

		QtCore.QObject.connect(self.ui.predictButton_1, QtCore.SIGNAL('clicked()'), self.showResult)

		QtCore.QObject.connect(self.ui.linearModelButton, QtCore.SIGNAL('clicked()'), self.plotModel)

		def showResult(self):
				value = self.ui.lineEdit_1.text()
				self.ui.predictResultLabel.setText(regr.predict(value))

		def plotModel(self):
			plt.scatter(self.sqfeet, self.price, color='Blue')
			plt.plot(self.sqfeet, regr.predict(self.price), color='Red', linewidth=4)
			plt.show()
		'''

class MyForm(QtGui.QDialog):
	def __init__(self, parent=None):
		QtGui.QWidget.__init__(self, parent)
		self.ui = Ui_Dialog()
		self.ui.setupUi(self)

		self.listWidCon = []
		self.listWidPar = []

		self.addcontent()
		#self.addcontentPar()

		self.addcontent_2()
		self.addcontentPar_2()

		QtCore.QObject.connect(self.ui.aboutButton, QtCore.SIGNAL('clicked()'), self.aboutTriggered)
		self.popAboutDialog = aboutDialog()

		QtCore.QObject.connect(self.ui.databaseButton, QtCore.SIGNAL('clicked()'), self.tableTriggered)
		self.popTableDialog = tableDialog()

		QtCore.QObject.connect(self.ui.predictButon, QtCore.SIGNAL('clicked()'), self.predictTriggered)
		self.poppredictDialog = predictDialog()

		QtCore.QObject.connect(self.ui.radioButtonEnergy, QtCore.SIGNAL('clicked()'), self.addcontentParEnergy)
		QtCore.QObject.connect(self.ui.radioButtonHealth, QtCore.SIGNAL('clicked()'), self.addcontentParHealth)
		QtCore.QObject.connect(self.ui.radioButtonPop, QtCore.SIGNAL('clicked()'), self.addcontentParPop)

		QtCore.QObject.connect(self.ui.addButton, QtCore.SIGNAL('clicked()'), self.additem)
		QtCore.QObject.connect(self.ui.deleteButton, QtCore.SIGNAL('clicked()'), self.delitem)
		QtCore.QObject.connect(self.ui.clearAllButton, QtCore.SIGNAL('clicked()'), self.clearallitem)
		QtCore.QObject.connect(self.ui.showGraphButton, QtCore.SIGNAL('clicked()'), self.plotGraph)

		QtCore.QObject.connect(self.ui.addButton_2, QtCore.SIGNAL('clicked()'), self.additem_2)
		QtCore.QObject.connect(self.ui.deleteButton_2, QtCore.SIGNAL('clicked()'), self.delitem_2)
		QtCore.QObject.connect(self.ui.clearAllButton_2, QtCore.SIGNAL('clicked()'), self.clearallitem_2)
		QtCore.QObject.connect(self.ui.showGraphButton_2, QtCore.SIGNAL('clicked()'), self.plotGraph_2)

	def aboutTriggered(self):
		self.popAboutDialog.show()

	def tableTriggered(self):
		self.popTableDialog.show()

	def predictTriggered(self):
		self.poppredictDialog.show()

	def addcontent(self):
		self.ui.comboCountry.addItem('--Select--')
		for i in Countries:
			self.ui.comboCountry.addItem(i)

	def addcontentParEnergy(self):
		self.ui.comboParameterHealth.clear()
		self.ui.comboParameterPop.clear()
		self.ui.comboParameter.addItem('--Select--')
		for i in ParametersDict.keys():
			self.ui.comboParameter.addItem(i)

	def addcontentParHealth(self):
		self.ui.comboParameter.clear()
		self.ui.comboParameterPop.clear()
		self.ui.comboParameterHealth.addItem('--Select--')
		for i in ParametersDictHealth.keys():
			self.ui.comboParameterHealth.addItem(i)

	def addcontentParPop(self):
		self.ui.comboParameterHealth.clear()
		self.ui.comboParameter.clear()
		self.ui.comboParameterPop.addItem('--Select--')
		for i in ParametersDictPop.keys():
			self.ui.comboParameterPop.addItem(i)

	def addcontent_2(self):
		self.ui.comboCountry_2.addItem('--Select--')
		for i in Countries:
			self.ui.comboCountry_2.addItem(i)

	def addcontentPar_2(self):
		self.ui.comboParameter_2.addItem('--Select--')
		for i in Parameters:
			self.ui.comboParameter_2.addItem(i)

	def additem(self):
		if self.ui.comboCountry.currentIndex() == 0:
			pass
		else:
			choosenCon = self.ui.comboCountry.itemText(self.ui.comboCountry.currentIndex())
			self.ui.listWidget.addItem(choosenCon)
			self.listWidCon.append(choosenCon)

	def additem_2(self):
		if self.ui.comboParameter_2.currentIndex() == 0:
			pass
		else:
			choosenCon = self.ui.comboParameter_2.itemText(self.ui.comboParameter_2.currentIndex())
			self.ui.listWidget_2.addItem(choosenCon)
			self.listWidPar.append(choosenCon)

	def delitem(self):
		del self.listWidCon[self.ui.listWidget.currentRow()]
		self.ui.listWidget.takeItem(self.ui.listWidget.currentRow())

	def delitem_2(self):
		del self.listWidPar[self.ui.listWidget_2.currentRow()]
		self.ui.listWidget_2.takeItem(self.ui.listWidget_2.currentRow())

	def clearallitem(self):
		self.ui.listWidget.clear()
		self.listWidCon = []

	def clearallitem_2(self):
		self.ui.listWidget_2.clear()
		self.listWidPar = []

	def plotGraph(self):
		if self.ui.radioButtonEnergy.isChecked():
			countryIndex = self.ui.comboParameter.currentIndex()
			if countryIndex == 0:
				pass
			else:
				parName = str(self.ui.comboParameter.itemText(self.ui.comboParameter.currentIndex()))
				barChartComp(ParametersDict, parName, Countries, self.listWidCon)
				self.clearallitem()
		elif self.ui.radioButtonHealth.isChecked():
			countryIndex = self.ui.comboParameterHealth.currentIndex()
			if countryIndex == 0:
				pass
			else:
				parName = str(self.ui.comboParameterHealth.itemText(self.ui.comboParameterHealth.currentIndex()))
				barChartComp(ParametersDictHealth, parName, Countries, self.listWidCon)
				self.clearallitem()
		elif self.ui.radioButtonPop.isChecked():
			countryIndex = self.ui.comboParameterPop.currentIndex()
			if countryIndex == 0:
				pass
			else:
				parName = str(self.ui.comboParameterPop.itemText(self.ui.comboParameterPop.currentIndex()))
				barChartComp(ParametersDictPop, parName, Countries, self.listWidCon)
				self.clearallitem()
		
	def plotGraph_2(self):
		countryName = self.ui.comboCountry_2.itemText(self.ui.comboCountry_2.currentIndex())
		countryIndex = self.ui.comboCountry_2.currentIndex()
		if countryIndex == 0:
			pass
		elif self.ui.radioButtonBar.isChecked():
			countryIndex = countryIndex-1
			indices = range(len(self.listWidPar))
			dlist = []
			for item in self.listWidPar:
				item = str(item)
				dlist.append(dataset[item][countryIndex])
			ticklist = []
			for par in self.listWidPar:
				ticklist.append(par[:15])
			Title = 'Parameters Comparison of '+countryName
			Xlabel = 'Parameters'
			Ylabel = 'Values'
			barChart(indices, dlist, ticklist, Xlabel, Ylabel, Title)
			self.clearallitem_2()
		elif self.ui.radioButtonPie.isChecked():
			countryIndex = countryIndex-1
			explode = [0.0 for i in range(len(self.listWidPar))]
			dlist = []
			for item in self.listWidPar:
				item = str(item)
				dlist.append(dataset[item][countryIndex])
			pieChart(dlist, explode, self.listWidPar, countryName)
			self.clearallitem_2()

dataset = pd.read_csv('food_csv.csv')

for item in dataset.columns.values:
    exec("%s = []" % (item.split(' ')[0]))
    for val in dataset[item]:
        exec("%s.append(val)" % (item.split(' ')[0]))

Parameters = dataset.columns.values[3:]

ParametersDict = {'EnergyTotal':{'Energy':Energy},
				'Protein Fats and Carbs':{'Protein':Protein, 'Fats':Fats, 'Carbohydrates':Carbohydrates},
				'AnimalProducts':{'AnimalProducts':AnimalProducts},
				'AnimalProducts Milk':{'MilkNoButter':MilkNoButter, 'MilkWhole':MilkWhole, 'ButterGhee':ButterGhee, 'Cheese':Cheese},
				'AnimalProducts Meat':{'Meat':Meat, 'BovineMeat':BovineMeat, 'MuttonGoatMeat':MuttonGoatMeat, 'Pigmeat':Pigmeat, 'PoultryMeat':PoultryMeat, 'OffalsEdible':OffalsEdible},
				'AnimalProducts Fish':{'FishSeafood':FishSeafood, 'FreshwaterFish':FreshwaterFish, 'PelagicFish':PelagicFish},
				'AnimalProducts Others':{'Eggs':Eggs, 'Honey':Honey, 'AnimalFats':AnimalFats, 'FatsAnimalsRaw':FatsAnimalsRaw},
				'VegetableProducts':{'VegetableProducts':VegetableProducts},
				'VegetableProducts Vegetables':{'Potatoes':Potatoes, 'Vegetables':Vegetables},
				'VegetableProducts Oils':{'VegetableOils':VegetableOils, 'SoyabeanOil':SoyabeanOil, 'OliveOil':OliveOil, 'PalmOil':PalmOil, 'CoconutOil':CoconutOil},
				'VegetableProducts SugarItems':{'SugarRaw':SugarRaw, 'SugarRawEquivalent':SugarRawEquivalent, 'SugarRefinedEquiv':SugarRefinedEquiv, 'SugarSweeteners':SugarSweeteners},
				'VegetableProducts Fruits':{'Apples':Apples, 'Bananas':Bananas, 'FruitsExcludingWine':FruitsExcludingWine},
				'VegetableProducts Alcoholic Items':{'AlcoholicBeverages':AlcoholicBeverages, 'Wine':Wine},
				'VegetableProducts Cereals Items':{'CerealsExcludingBeer':CerealsExcludingBeer, 'RiceMilledEquivalent':RiceMilledEquivalent, 'RicePaddyEquivalent':RicePaddyEquivalent, 'Wheat':Wheat, 'Pulses':Pulses},
				'VegetableProducts Roots Items':{'StarchyRoots':StarchyRoots, 'RootsTuberDryEquiv':RootsTuberDryEquiv},
				'VegetableProducts Others':{'Beans':Beans, 'Nuts':Nuts, 'Coffee':Coffee}}

ParametersDictHealth = {'Healthy Life Expectancy':{'HaleF':HaleF, 'HaleM':HaleM, 'HaleFM':HaleFM},
						'Life Lost Communicable and NC Disease':{'LifeLostCD':LifeLostCD, 'LifeLostNCD':LifeLostNCD},
						'Mortality Rate Under 5 Year (live Birth)':{'U5MR_F':U5MR_F, 'U5MR_M':U5MR_M, 'U5MR_FM':U5MR_FM},
						'Tuberculosis Prevalence and Incidence':{'PrevalenceOfTuberculosis':PrevalenceOfTuberculosis, 'IncidenceTuberculosis':IncidenceTuberculosis},
						'Neonatal Mortality Rate':{'NeonatalMortalityRate':NeonatalMortalityRate},
						'Maternal Mortality Rate':{'MaternalMortalityRatio':MaternalMortalityRatio},
						'Diabetes Crude Prevalence':{'Diabetes':Diabetes},
						'Life Expectancy At Birth':{'LifeExpectancyAtBirthF':LifeExpectancyAtBirthF, 'LifeExpectancyAtBirthM':LifeExpectancyAtBirthM, 'LifeExpectancyAtBirthFM':LifeExpectancyAtBirthFM},
						'Infant Mortality Rate':{'IMR_F':IMR_F, 'IMR_M':IMR_M, 'IMR_FM':IMR_FM},
						'Age Standarized Mortality Rate':{'NCDisease':NCDisease, 'Cancer':Cancer, 'Injuries':Injuries, 'Cardio':Cardio},
						'Adult Mortality Rate':{'AdultMortalityRateF':AdultMortalityRateF, 'AdultMortalityRateM':AdultMortalityRateM, 'AdultMortalityRateFM':AdultMortalityRateFM},
						'Obesity Prevalence':{'ObesityPrevalenceM':ObesityPrevalenceM, 'ObesityPrevalenceF':ObesityPrevalenceF},
						'Systolic Blood Pressure':{'SBPM':SBPM, 'SBPF':SBPF},
						'Total Cholestrol':{'CholesterolMen':CholesterolMen, 'CholesterolFemale':CholesterolFemale},
						'Tobacco Prevalence':{'TobaccoGT15M':TobaccoGT15M, 'TobaccoGT15F':TobaccoGT15F, 'TobaccoGT15MF':TobaccoGT15MF}}

ParametersDictPop = {'Total Income Per Capita':{'NationalIncome':NationalIncome},
					'Population Annual Growth':{'PopulationAnnualGrowthRate':PopulationAnnualGrowthRate},
					'Population in Urban Areas':{'PopulationUrban':PopulationUrban},
					'Population Median Age':{'PopulationMedianAge':PopulationMedianAge},
					'Population Proportion':{'PopulationProportionUnder15':PopulationProportionUnder15, 'PopulationProportionOver60':PopulationProportionOver60},
					'Fertility Rate':{'TotalFertilityRate':TotalFertilityRate},
					'Alcohol Consumption':{'AlcoholGT15':AlcoholGT15},
					'Population Sustainable Access Water Sources':{'WaterTotal':WaterTotal, 'WaterUrban':WaterUrban, 'WaterRural':WaterRural},
					'Population Improved Sanitation Access':{'SanitationTotal':SanitationTotal, 'SanitationUrban':SanitationUrban, 'SanitationRural':SanitationRural}}

'''
def retrieve_name(var):
    callers_local_vars = inspect.currentframe().f_back.f_globals.items()
    name = [var_name for var_name, var_val in callers_local_vars if var_val is var]
    return name[0]
'''

if __name__ == '__main__':
	app = QtGui.QApplication(sys.argv)
	myapp = MyForm()
	myapp.show()
	sys.exit(app.exec_())