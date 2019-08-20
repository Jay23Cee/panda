#pandas Dataframe
import pandas as pd

#df = pd.DataFrame()
#print(df)


## create DataFramr from list
#data = [1,2,3,4,5]
#df = pd.DataFrame(data)
#print(df)

			#example 2  List
#data = [['Alex',10 ], ['Bob',12] , ['Clarke',13]]
#df = pd.DataFrame( data, columns = [ 'Name' , 'Age'])	#DataFrame()
#print(df)

##Example 3
#data = [['Alex',10 ], ['Bob',12] , ['Clarke',13]]
#df = pd.DataFrame( data, columns = [ 'Name' , 'Age'], dtype = float )	#DataFrame() dtype =float
#print(df)


###########################
############################


#CREATE A DATAFRAME FROM DICT
#of ndarrays /list
#data = { 'Name': ['Tom', 'Jack', 'Steve', 'Ricky'], 'Age': [28,34,29,42]}

#df = pd.DataFrame(data, index=['rank1', 'rank2', 'rank3', 'rank4'])
#print(df)


#Example2
#data ={'Name':['Tom', 'Jack', 'Steve', 'Ricky'], 'Age': [28,34,29,42]}
#df = pd.DataFrame(data, index= ['rank1', 'rank2', 'rank3', 'rank4'])
#print(df)

##############################
##############################

#Create a DataFrame from List of Dicts
#Example 1
        ##The following  example showshowto createa DataFrame by passing a list of dictionaries
#data = [{'a': 1, 'b': 2}, {'a':5 , 'b': 10, 'c':20}]
#df = pd.DataFrame(data)
#print(df)


#example 2
#data = [{'a':1, 'b':2}, {'a': 5, 'b':10 , 'c':20}]
#df = pd.DataFrame(data, index = ['first', 'second'])
#print(df)


#example 3
#data = [{'a': 1, 'b':2}, {'a':5, 'b':10, 'c': 20}]

            #with2 ccolumn indices, values same as dictionary keys 
#df1 = pd.DataFrame(data, index= ['first', 'second'], columns= ['a', 'b'])
            #with 2 column indices with one index with other 
#df2 = pd.DataFrame(data, index = ['first','second'], columns=['a', 'b1'])

#print(df1)
#print("\n")
#print(df2)


##create a DataFrame from Dict of Series





