# PassGen

PassGen is a simple random password generator tool.

## Installation

Use the package manager pip to install requirements or dependencies. 

```bash
>> pip3 install -r requirements.txt
```
Then to run the tool
```python
>> python Password.py -h
```
Output:


![](images/HelpOutput.png)


## Usage
--------Low Strength---------
```
>> python Password.py 8 l
```
Output:


![](images/low.png)


------Medium Strength-------
```
>> python Password.py 8 m
```
Output:


![](images/Medium.png)


----------High Strength-------
```
>> python Password.py 8 s
```
Output:


![](images/Strongpass.png)


## Error Output
1. Input of length less than 8
```python
>> python Password.py 7 l
```
Output:


![](images/less8.png)


2. Not giving Available Strength Options
```python
python Password.py 8 k
```
Output:


![](images/lms.png)
