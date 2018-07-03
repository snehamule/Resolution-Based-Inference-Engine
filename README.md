# Resolutution Based Inference Engine
This project  is implementation a propositional logic resolution-based inference engine
This is implementation a propositional logic resolution-based inference engine
This Program has 3 functions : 

1. tell () Function : Two-Statement Resolution
2. resolve() Function: Resolution Inference Engine
3. ask() Function:  Conjunctive normal form (CNF) Conversion

## Technology / libraries used: <br />
Python

## Setup required:<br />
python version: 3 or greater<br />

## Install python <br />
If python is not installed then need to install python:<br />
<br />
**For  osx operating system (mac)**<br />
	python get-pip.py 

**For windows operating system**<br />
	refer steps from [windows python installation steps](https://docs.python.org/3/using/windows.html).
	

## Check python version:
python -version

## Output Format 

| Input  					 		| Output 		|
| --------------------------------------------------------------| --------------------- |
| resolve (["or", "a", "b", "c"], ["not", "b"])  		| ['or', 'a', 'c'] 	|
| resolve (["or", "a", "b", "c"], ["or", "b", ["not", "c"]])    | ['or', 'a', 'b']  	|
| resolve (["or", ["not", "raining"], "wet ground"], "raining") | wet ground 	        |
| resolve ("a", ["not", "a"])					| ['or', 'a', 'b']  	|
| tell (["or", ["not", "a"], "b"])
tell (["or", ["not", "b"], "c"])
tell ("a")
print(ask("d")) | wet ground 	        |
| resolve ("a", ["not", "a"])					| ['or', 'a', 'b']  	|



tell (["or", ["not", "a"], "b"])
tell (["or", ["not", "b"], "c"])
tell ("a")
print(ask("d"))
OutPut :   False


tell (["or", ["not", "a"], "b"])
tell (["or", ["not", "b"], "c"])
tell ("a")
print (ask("c"))  
Output : True

## Run program : <br />
1. Download code from git  using  git clone .
2. For test Testcases run command
```
	python test.py
```	

