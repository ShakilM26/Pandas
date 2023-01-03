```python
import pandas as pd
```


```python
df = pd.read_csv('world population.csv')
df.head(5)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Rank</th>
      <th>Country(or dependency)</th>
      <th>Population(2020)</th>
      <th>Yearly_Change</th>
      <th>Net_Change</th>
      <th>Density(P/Km²)</th>
      <th>Land_Area(Km²)</th>
      <th>Migrants(net)</th>
      <th>Fertility_Rate</th>
      <th>Median_Age</th>
      <th>Urban _Pop %</th>
      <th>World_Share</th>
      <th>Continent</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>China</td>
      <td>1,439,323,776</td>
      <td>0.39 %</td>
      <td>5,540,090</td>
      <td>153</td>
      <td>9,388,211</td>
      <td>-348,399</td>
      <td>1.7</td>
      <td>38</td>
      <td>61 %</td>
      <td>18.47 %</td>
      <td>Asia</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>India</td>
      <td>1,380,004,385</td>
      <td>0.99 %</td>
      <td>13,586,631</td>
      <td>464</td>
      <td>2,973,190</td>
      <td>-532,687</td>
      <td>2.2</td>
      <td>28</td>
      <td>35 %</td>
      <td>17.70 %</td>
      <td>Asia</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>United States</td>
      <td>331,002,651</td>
      <td>0.59 %</td>
      <td>1,937,734</td>
      <td>36</td>
      <td>9,147,420</td>
      <td>954,806</td>
      <td>1.8</td>
      <td>38</td>
      <td>83 %</td>
      <td>4.25 %</td>
      <td>North America</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4</td>
      <td>Indonesia</td>
      <td>273,523,615</td>
      <td>1.07 %</td>
      <td>2,898,047</td>
      <td>151</td>
      <td>1,811,570</td>
      <td>-98,955</td>
      <td>2.3</td>
      <td>30</td>
      <td>56 %</td>
      <td>3.51 %</td>
      <td>Asia</td>
    </tr>
    <tr>
      <th>4</th>
      <td>5</td>
      <td>Pakistan</td>
      <td>220,892,340</td>
      <td>2.00 %</td>
      <td>4,327,022</td>
      <td>287</td>
      <td>770,880</td>
      <td>-233,379</td>
      <td>3.6</td>
      <td>23</td>
      <td>35 %</td>
      <td>2.83 %</td>
      <td>Asia</td>
    </tr>
  </tbody>
</table>
</div>




```python
df.isnull().sum().any()
```




    True



There is some null values and punctuations. so we have to clean it

### preprocessing

* drop unnecessary column
* fill null values
* remove punctuation
* proper column data-type 


```python
# actually we don't need this col so drop it 

df = df.drop('Rank', axis=1)
```


```python
# fill all null values with 0 

df = df.fillna(0)
```


```python
# remove punctuations

df.replace(',','', regex=True, inplace=True)
```


```python
df.head(1)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Country(or dependency)</th>
      <th>Population(2020)</th>
      <th>Yearly_Change</th>
      <th>Net_Change</th>
      <th>Density(P/Km²)</th>
      <th>Land_Area(Km²)</th>
      <th>Migrants(net)</th>
      <th>Fertility_Rate</th>
      <th>Median_Age</th>
      <th>Urban _Pop %</th>
      <th>World_Share</th>
      <th>Continent</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>China</td>
      <td>1439323776</td>
      <td>0.39 %</td>
      <td>5540090</td>
      <td>153</td>
      <td>9388211</td>
      <td>-348399</td>
      <td>1.7</td>
      <td>38</td>
      <td>61 %</td>
      <td>18.47 %</td>
      <td>Asia</td>
    </tr>
  </tbody>
</table>
</div>




```python

```

### Our dataset contains percentages and dollar signs. If we wanted, we could have removed these in the previous simple rules [ replace() ] . But we will apply different rules here.



```python
# in our datasets their are some percentage, we have to remove them. and we are gonna using rstrip().
# well, basically rstrip() returns a copy of the string with trailing characters removed (based on the string argument passed)

df['Yearly_Change'] = df['Yearly_Change'].str.rstrip('%').astype('float64')
df['Urban _Pop %'] = df['Urban _Pop %'].str.rstrip('%')
df['World_Share'] = df['World_Share'].str.rstrip('%')
```


```python
# but still our 'Urban_Pop % and Median_Age' is not free to go. this cols contain some non-numeric value. 
# we have clean it and make it numeric

df['Urban _Pop %'] = pd.to_numeric(df['Urban _Pop %'], errors='coerce')
df['Median_Age'] = pd.to_numeric(df['Median_Age'], errors='coerce')
df['Fertility_Rate'] = pd.to_numeric(df['Fertility_Rate'], errors='coerce')
```


```python
# now fill this nan values with zero

import numpy as np

df['Urban _Pop %'] = df['Urban _Pop %'].replace(np.nan, 0)
df['Median_Age'] = df['Median_Age'].replace(np.nan, 0)
df['Fertility_Rate'] = df['Fertility_Rate'].replace(np.nan, 0)
```


```python

```


```python
# remove dollar '$' sign

df['Density(P/Km²)'] = [x.strip('$') for x in df['Density(P/Km²)']]
```


```python

```


```python
# now change data type

df['Population(2020)'] = df['Population(2020)'].astype('int64')
df['Net_Change'] = df['Net_Change'].astype('int64')
df['Yearly_Change'] = df['Yearly_Change'].astype('float64')
df['Density(P/Km²)'] = df['Yearly_Change'].astype('float64')
df['Land_Area(Km²)'] = df['Land_Area(Km²)'].astype('int64')
df['Migrants(net)'] = df['Migrants(net)'].astype('int64')
df['Fertility_Rate'] = df['Fertility_Rate'].astype('float64')
df['Median_Age'] = df['Median_Age'].astype('int64')
df['Urban _Pop %'] = df['Urban _Pop %'].astype('int64')
df['World_Share'] = df['World_Share'].astype('float64')
```


```python

```


```python
## Our Desired Dataset is now crystal clear
```


```python
df.head(10)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Country(or dependency)</th>
      <th>Population(2020)</th>
      <th>Yearly_Change</th>
      <th>Net_Change</th>
      <th>Density(P/Km²)</th>
      <th>Land_Area(Km²)</th>
      <th>Migrants(net)</th>
      <th>Fertility_Rate</th>
      <th>Median_Age</th>
      <th>Urban _Pop %</th>
      <th>World_Share</th>
      <th>Continent</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>China</td>
      <td>1439323776</td>
      <td>0.39</td>
      <td>5540090</td>
      <td>0.39</td>
      <td>9388211</td>
      <td>-348399</td>
      <td>1.7</td>
      <td>38</td>
      <td>61</td>
      <td>18.47</td>
      <td>Asia</td>
    </tr>
    <tr>
      <th>1</th>
      <td>India</td>
      <td>1380004385</td>
      <td>0.99</td>
      <td>13586631</td>
      <td>0.99</td>
      <td>2973190</td>
      <td>-532687</td>
      <td>2.2</td>
      <td>28</td>
      <td>35</td>
      <td>17.70</td>
      <td>Asia</td>
    </tr>
    <tr>
      <th>2</th>
      <td>United States</td>
      <td>331002651</td>
      <td>0.59</td>
      <td>1937734</td>
      <td>0.59</td>
      <td>9147420</td>
      <td>954806</td>
      <td>1.8</td>
      <td>38</td>
      <td>83</td>
      <td>4.25</td>
      <td>North America</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Indonesia</td>
      <td>273523615</td>
      <td>1.07</td>
      <td>2898047</td>
      <td>1.07</td>
      <td>1811570</td>
      <td>-98955</td>
      <td>2.3</td>
      <td>30</td>
      <td>56</td>
      <td>3.51</td>
      <td>Asia</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Pakistan</td>
      <td>220892340</td>
      <td>2.00</td>
      <td>4327022</td>
      <td>2.00</td>
      <td>770880</td>
      <td>-233379</td>
      <td>3.6</td>
      <td>23</td>
      <td>35</td>
      <td>2.83</td>
      <td>Asia</td>
    </tr>
    <tr>
      <th>5</th>
      <td>Brazil</td>
      <td>212559417</td>
      <td>0.72</td>
      <td>1509890</td>
      <td>0.72</td>
      <td>8358140</td>
      <td>21200</td>
      <td>1.7</td>
      <td>33</td>
      <td>88</td>
      <td>2.73</td>
      <td>South America</td>
    </tr>
    <tr>
      <th>6</th>
      <td>Nigeria</td>
      <td>206139589</td>
      <td>2.58</td>
      <td>5175990</td>
      <td>2.58</td>
      <td>910770</td>
      <td>-60000</td>
      <td>5.4</td>
      <td>18</td>
      <td>52</td>
      <td>2.64</td>
      <td>Africa</td>
    </tr>
    <tr>
      <th>7</th>
      <td>Bangladesh</td>
      <td>164689383</td>
      <td>1.01</td>
      <td>1643222</td>
      <td>1.01</td>
      <td>130170</td>
      <td>-369501</td>
      <td>2.1</td>
      <td>28</td>
      <td>39</td>
      <td>2.11</td>
      <td>Asia</td>
    </tr>
    <tr>
      <th>8</th>
      <td>Russia</td>
      <td>145934462</td>
      <td>0.04</td>
      <td>62206</td>
      <td>0.04</td>
      <td>16376870</td>
      <td>182456</td>
      <td>1.8</td>
      <td>40</td>
      <td>74</td>
      <td>1.87</td>
      <td>Europe</td>
    </tr>
    <tr>
      <th>9</th>
      <td>Mexico</td>
      <td>128932753</td>
      <td>1.06</td>
      <td>1357224</td>
      <td>1.06</td>
      <td>1943950</td>
      <td>-60000</td>
      <td>2.1</td>
      <td>29</td>
      <td>84</td>
      <td>1.65</td>
      <td>North America</td>
    </tr>
  </tbody>
</table>
</div>




```python

```

#### Here are several ways to remove the dollar sign


```python
#1. df['Density(P/Km²)'] = df['Density(P/Km²)'].apply(lambda x: float(x.split()[0].replace('$', '')))

#2. df['Density(P/Km²)'] = df['Density(P/Km²)'].apply(lambda x: x.strip('$'))

#3. df['Density(P/Km²)'] = df['Density(P/Km²)'].apply(lambda x: x.replace('$',''))

#4. df['Density(P/Km²)'] = [x.strip('$') for x in df['Density(P/Km²)']]

#5. df['Density(P/Km²)'] = [x.strip('$') for x in df['Density(P/Km²)']]

#6. df['Density(P/Km²)'] = [x[1:] for x in df['Density(P/Km²)']]
```


```python

```
