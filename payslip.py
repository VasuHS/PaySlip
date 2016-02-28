# -*- coding: utf-8 -*-
"""


Created on Fri Feb 26 23:18:17 2016

@author: Vasu
"""


from __future__ import division
import sys
import time

"""
class to calculate the payslip details

In 2.7 version of python importing division is
 required to convert the operation value to decimal value

Used time function to get the current month details(month of payslip generation)
"""
class PaySlip:
    def __init__(self,basic,grade):
            
        if ( basic.isdigit() and int(basic) == 0 ):
            self.basic=0
        else:
            if (basic.isdigit()):
                self.basic=int(basic)
                #print "here"
            else:
                self.basic=float(basic)
        self.grade=grade
    """
        Function to remove .0 resulted from the calculation and inclustion of
        from __future__ import division
    """
    def dotZeroRemove(self,passNum):
        passNumTemp=passNum
        passNumTemp=str(passNumTemp)
        if(passNumTemp.endswith(".0")):
            passNum=int(float(passNumTemp))
        return passNum
    def EarnDeduct(self):
        pFund=(12*(self.basic))/100
        pFund=self.dotZeroRemove(pFund)     
        #pFunTemp=pFund
        #pFunTemp=str(pFunTemp)
        #if (pFunTemp.endswith(".0")):
        #    pFund=int(float(pFunTemp))
        
        HRA=(30*self.basic)/100
        HRA=self.dotZeroRemove(HRA)
        
        
        profeTax=200
        FuelAllow=1000
        
        if (self.grade=="G1"):
            Grade=(50*self.basic)/100
        else:
            Grade=(70*self.basic)/100
        Grade=self.dotZeroRemove(Grade)
        
            
        if (self.basic <= 0):
            TotalEarn=0
            IncomTax=0
        else:
            TotalEarn=(self.basic+HRA+FuelAllow+Grade)    
            IncomTax=(30*(TotalEarn-(profeTax+pFund)))/100
        
        TotalEarn=self.dotZeroRemove(TotalEarn)        
        IncomTax=self.dotZeroRemove(IncomTax)                
       
        if (self.basic<=0):
            TotalDeduct=0
        else:
            TotalDeduct=pFund+profeTax+IncomTax
        TotalDeduct=self.dotZeroRemove(TotalDeduct)    
        
        
        if (self.basic <= 0):
            Net=0
        else:
            Net=TotalEarn-TotalDeduct
        Net=self.dotZeroRemove(Net)
       
        
        print ("BASIC\t\t%s\tPF\t\t%s" % (str(self.basic),str(pFund)))
        print ("HRA\t\t%s\tProfession Tax\t%s" % (str(HRA),profeTax))
        print ("Fuel Alloance\t%d\tIncome Tax\t\t%s" % (FuelAllow,str(IncomTax)))
        print ("Grade Allowance\t%s\t                       " % str(Grade))
        print ("Total Earnings\t%s\tTotal Deductions\t%s" %(str(TotalEarn),str(TotalDeduct)))
        print ("Net Income:\t%s" % str(Net))
    



def MonthlyPay():
    Basic=sys.argv[1]
    Grade=sys.argv[2]
    if (Basic.startswith("-")):
        Basic="0"
    pay1=PaySlip(Basic,Grade)
    Month=time.strftime("%b")
    Year=time.strftime("%Y")
    name="ABC"
    print ("PaySlip For %s %s\n" % (Month,Year))  
    print ("Employee: %s  Grade: %s\n"% (name,Grade))
    print ("Earnings\t\t\tDeductions\t\t")
    pay1.EarnDeduct()
    
MonthlyPay()
