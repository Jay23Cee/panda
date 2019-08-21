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

#d = { 'one ':  pd.Series([1,2,3], index = [ 'a', 'b', 'c']),
  #    'two ': pd.Series ([1,2,3,4], index = ['a', 'b', 'c', 'd'])}

#df = pd.DataFrame(d)
#print(df)

                #// Column Selection
#d = { 'one':  pd.Series([1,2,3], index = [ 'a', 'b', 'c']),
 #     'two': pd.Series ([1,2,3,4], index = ['a', 'b', 'c', 'd'])}
#df = pd.DataFrame(d)

#print(df['one'])



            #// Column Addition
#d = { 'one':  pd.Series([1,2,3], index = [ 'a', 'b', 'c']),
      #'two': pd.Series ([1,2,3,4], index = ['a', 'b', 'c', 'd'])}

#df = pd.DataFrame(d)

#adding a new column to an existing Datafraame object with column label passing

#print("Adding a new column by passing as as Series : ")
#df['three'] = pd.Series([10, 20, 30], index = ['a', 'b', 'c'])
#print(df)


#print('Adding a new Column')
#df['four'] = df['one'] + df['three']

#print(df)




                #Column Deletion
# Using the previous DataFrame, we will delete a column
#using del function

import pandas as pd

d = {'one' : pd.Series([1,2,3], index = ['a', 'b', 'c']),
     'two' : pd.Series([1,2,3,4], index = ['a', 'b', 'c', 'd'])
  #  'three' : pd.Series([10,20,30], index = ['a', 'b', 'c'])
        }

#df = pd.DataFrame(d)

#print("Our dataframe is:")
#print(df)


#using del function
#print("Deleting the first column using DEL function:")
#del df['one']
#print(df)


# using pop fucntion
#print("Deleting another  using pop fucntion")
#df.pop('two')
#rint(df)

#SELECTING BY LABEL ! ! 
#print(df.loc['b'])


#sELECTIon by integer location
#print(df.iloc[2])


#Slice Rows
#print(df[2:4])


#Addition of Rows
print('addition')
df= pd.DataFrame([[1,2] , [3,4]], columns = ['a' ,'b'])

df2 = pd.DataFrame([[5,6], [7,3]], columns= ['a', 'b'])

df = df.append(df2)
print(df)


#ROW  Deletion 
print('Deletion')
print(df.drop(0))

