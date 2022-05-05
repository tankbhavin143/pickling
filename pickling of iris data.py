import requests
import pickle

url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"
response = requests.get(url)
data = response.text
listt = data.split("\n")
l1 = [item.split(",") for item in listt if len(item) != 0]
	
#with open("myfile.pkl","wb") as f:
	#pickle.dump(l1,f)
		
with open("myfile.pkl","rb") as f:
	read = pickle.load(f)
	print(read)