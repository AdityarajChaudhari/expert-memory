
import pickle

x = pickle.load(open('ModelSave/model.pkl','rb'))
print(x.predict([[4.15,5200,1,1,1,0]]))