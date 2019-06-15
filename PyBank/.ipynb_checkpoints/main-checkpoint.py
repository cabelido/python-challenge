{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [],
   "source": [
    "import os\n",
    "import csv\n",
    "\n",
    "datecount=0\n",
    "sumpl=0\n",
    "varlist=[]\n",
    "datelist=[]\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [],
   "source": [
    "budgetpath = os.path.join('C:\\\\Users\\\\cabel\\\\python-challenge\\\\Resources\\\\budget_data.csv')\n",
    "with open(budgetpath, 'r') as csvfile:\n",
    "    budgetreader = csv.reader(csvfile, delimiter=',')\n",
    "    budgetheader = next(budgetreader)\n",
    "    \n",
    "    for row in budgetreader:\n",
    "        \n",
    "        date = row[0]\n",
    "        pl = int(row[1])\n",
    "        datelist.append(date)\n",
    "        sumpl+=pl\n",
    "                    \n",
    "        if len(datelist)>1:\n",
    "            varpl=pl-prevpl\n",
    "            varlist.append(varpl)\n",
    "        prevpl=pl\n",
    "         \n",
    "datecount=len(datelist)\n",
    "varcount=datecount-1\n",
    "    \n",
    "sumvarpl=sum(varlist)\n",
    "avevarpl=sumvarpl/varcount\n",
    "minvar=min(varlist)\n",
    "maxvar=max(varlist)\n",
    "    \n",
    "minindex=varlist.index(minvar)+1\n",
    "maxindex=varlist.index(maxvar)+1\n",
    "mindate=datelist[minindex]\n",
    "maxdate=datelist[maxindex]   \n",
    "        "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Financial Analysis\n",
      "----------------------------------------\n",
      "Total Months: 86\n",
      "Total: $38382578\n",
      "Average Revenue Change: $-2315.12\n",
      "Greatest Increase in Revenue: Feb-2012 ($1926159)\n",
      "Greatest Decrease in Revenue: Sep-2013 ($-2196167)\n"
     ]
    }
   ],
   "source": [
    "# print summary to user\n",
    "\n",
    "print(\"Financial Analysis\")\n",
    "print(\"----------------------------------------\")\n",
    "print(f\"Total Months: {datecount}\")\n",
    "print(f\"Total: ${sumpl}\")\n",
    "print(f\"Average Revenue Change: ${round(avevarpl,2)}\")\n",
    "print(f\"Greatest Increase in Revenue: {maxdate} (${maxvar})\")\n",
    "print(f\"Greatest Decrease in Revenue: {mindate} (${minvar})\")   \n",
    "    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {},
   "outputs": [],
   "source": [
    "Output = (\n",
    "f\"Financial Analysis \\n\"\n",
    "f\"---------------------------------------- \\n\"\n",
    "f\"Total Months: {datecount} \\n\"\n",
    "f\"Total: ${sumpl} \\n\"\n",
    "f\"Average Revenue Change: ${round(avevarpl,2)} \\n\"\n",
    "f\"Greatest Increase in Revenue: {maxdate} (${maxvar}) \\n\"\n",
    "f\"Greatest Decrease in Revenue: {mindate} (${minvar}) \\n\")  \n",
    "    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {},
   "outputs": [],
   "source": [
    "saveFile=open('Results.txt','w')\n",
    "saveFile.write(Output)\n",
    "saveFile.close()\n"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
