import pandas as pd

def changeDistricts(name):
    df = pd.read_csv(name)

    df['PdDistrict'] = df['PdDistrict'].replace({'SOUTHERN': 'DAGORETTI'})
    df['PdDistrict'] = df['PdDistrict'].replace({'NORTHERN': 'EMBAKASI'})
    df['PdDistrict'] = df['PdDistrict'].replace({'BAYVIEW': 'KAMUKUNJI'})
    df['PdDistrict'] = df['PdDistrict'].replace({'TENDERLOIN': 'KIBRA'})
    df['PdDistrict'] = df['PdDistrict'].replace({'PARK': 'LANGATA'})
    df['PdDistrict'] = df['PdDistrict'].replace({'MISSION': 'MAKADARA'})
    df['PdDistrict'] = df['PdDistrict'].replace({'INGLESIDE': 'MATHARE'})
    df['PdDistrict'] = df['PdDistrict'].replace({'TARAVAL': 'ROYSAMBU'})
    df['PdDistrict'] = df['PdDistrict'].replace({'RICHMOND': 'STAREHE'})
    df['PdDistrict'] = df['PdDistrict'].replace({'CENTRAL': 'WESTLANDS'})
    df.to_csv(name)
    print(df['PdDistrict'])

def changeCoordinates(name):
    df = pd.read_csv(name)
    for i in range (len(df)):
        if df.values[i][6] == 'LANGATA':
            x_val = df.values[i][9]
            y_val = df.values[i][10]
            df['X'] = df['X'].replace({x_val: '36.80488586425781'})
            df['Y'] = df['Y'].replace({y_val: '-1.3511930983018765'})

        if df.values[i][6] == 'EMBAKASI':
            x_val = df.values[i][9]
            y_val = df.values[i][10]
            df['X'] = df['X'].replace({x_val: '36.9305419921875'})
            df['Y'] = df['Y'].replace({y_val: '-1.2983355281519586'})

        if df.values[i][6] == 'DAGORETTI':
            x_val = df.values[i][9]
            y_val = df.values[i][10]
            df['X'] = df['X'].replace({x_val: '36.82170867919922'})
            df['Y'] = df['Y'].replace({y_val: '-1.2787710799462924'})

        if df.values[i][6] == 'KAMUKUNJI':
            x_val = df.values[i][9]
            y_val = df.values[i][10]
            df['X'] = df['X'].replace({x_val: '36.85466766357422'})
            df['Y'] = df['Y'].replace({y_val: '-1.2753387051710048'})

        if df.values[i][6] == 'KIBRA':
            x_val = df.values[i][9]
            y_val = df.values[i][10]
            df['X'] = df['X'].replace({x_val: '36.79286956787109'})
            df['Y'] = df['Y'].replace({y_val: '-1.3093190118076432'})

        if df.values[i][6] == 'MAKADARA':
            x_val = df.values[i][9]
            y_val = df.values[i][10]
            df['X'] = df['X'].replace({x_val: '36.872520446777344'})
            df['Y'] = df['Y'].replace({y_val: '-1.2973058241064253'})

        if df.values[i][6] == 'MATHARE':
            x_val = df.values[i][9]
            y_val = df.values[i][10]
            df['X'] = df['X'].replace({x_val: '36.86187744140625'})
            df['Y'] = df['Y'].replace({y_val: '-1.2571470427327895'})

        if df.values[i][6] == 'ROYSAMBU':
            x_val = df.values[i][9]
            y_val = df.values[i][10]
            df['X'] = df['X'].replace({x_val: '36.864967346191406'})
            df['Y'] = df['Y'].replace({y_val: '-1.222822807617807'})

        if df.values[i][6] == 'STAREHE':
            x_val = df.values[i][9]
            y_val = df.values[i][10]
            df['X'] = df['X'].replace({x_val: '36.70463562011719'})
            df['Y'] = df['Y'].replace({y_val: '-1.2828899236168285'})

        if df.values[i][6] == 'WESTLANDS':
            x_val = df.values[i][9]
            y_val = df.values[i][10]
            df['X'] = df['X'].replace({x_val: '36.784629821777344'})
            df['Y'] = df['Y'].replace({y_val: '-1.2399849808106485'})

        print(i)
    df.to_csv(name)



# changeDistricts('nairobi_crimes16.csv')
# changeDistricts('nairobi_crimes17.csv')
changeCoordinates('nairobi_crimes17.csv')
#changeCoordinates('nairobi_crimes17.csv')

