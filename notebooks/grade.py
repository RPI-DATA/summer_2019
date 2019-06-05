from bs4 import BeautifulSoup
import pandas as pd
import os


def grade(student, ok):
#Grade Results
    results= {q[:-3]:ok.grade(q[:-3]) for q in os.listdir("tests") if q.startswith('q')}

    #If running locally with lots of notebooks load the grades.
    df = pd.DataFrame()
    row=df.shape[0]
    df.loc[row,'student']=name  #This is set in the last.
    #df.loc[row,'rcsid']=rcsid   #This is set in the last.
    total_grade=0
    #This loops through the results
    for key, val in results.items():
        df.loc[row,key]=val.grade
        results_key=str(key)+"-failed"
        df.loc[row,key]=val.grade*points_per_test
        #We use beautiful soup to parse the tests.
        soup = BeautifulSoup(str(val.failed_tests), "lxml")
        #There are multiple components, but the expected data seems most valuable.
        got = soup.get_text().split('\\n')[16:20]
        df.loc[row,results_key]=str(got)
        total_grade+=df.loc[row,key]  #total grade
    df.loc[row,'total_grade']=total_grade
    df.loc[row,'comments']=comments

    if not os.path.isfile('grades.csv'):
       df.to_csv('grades.csv', index=False)
    else: # else it exists so append without writing the header
       df.to_csv('grades.csv', mode='a', header=False,index=False)
    return df
