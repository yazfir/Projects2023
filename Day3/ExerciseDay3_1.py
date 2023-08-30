import pandas as pd

data = pd.read_csv('olympics.csv', skiprows=4)

"""
print(data.head())

print(data.Medal)

print(data['Medal'])

print(data[['Medal','Sport','Athlete']])

print(data.shape)


print(data.head(10))

print(data.tail(10))

print(data.info())

print(data['City'].unique())

print(data.Edition.value_counts()) #Cuenta las diferentes ediciones que hay. Value_Count cuenta veces del valor.

print(data.City.sort_values())

print(data.sort_values(by=['Edition','Medal']))

print(data[ (data.Medal == 'Gold') & (data.Gender == 'Men') ])

print( data[ data.Sport == 'Tennis' ] )

print( data[ data.Athlete.str.contains('Pedro') ] )

print( data[ data.NOC.str.contains('MEX') ] )

"""
print( data['Medal'].values[0] )
print( data['Medal'].values[1] )



print( data.values[10][0] )
print( data.values[10][1] )

