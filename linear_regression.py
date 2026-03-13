import csv
import matplotlib.pyplot  as plt
class LinearRegression:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def fit(self):
        def addList(lst):
            s=0
            for xitem in lst:
                s+=xitem
            return s
        def mean(lst):
            m=addList(lst)
            return m/len(lst)
        def slope(x,y):
            xm=mean(x)
            ym=mean(y)
            d=n=0
            for i in range(len(x)):
                d+=(x[i]-xm) ** 2
                n+=(x[i]-xm)*(y[i]-ym)
            return n/d
        def intercept(x,y):
            b=mean(y) - (slope(x,y)*mean(x))
            return b
        self.slope=slope(self.x,self.y)
        self.intercept=intercept(self.x,self.y)
    def predict(self, new_x):
        new_y=[]
        for i in range(len(new_x)):
            new_y.append((self.slope*new_x[i]) + self.intercept)
        return new_y
    def calculate_mse(self):
        new_y=self.predict(self.x)
        mse=0
        for i in range(len(self.x)):
            mse+=(self.y[i] - new_y[i]) ** 2
        mse=mse/len(self.x)
        return mse

def load_dataset(file_path):
    x_values=[]
    y_values=[]
    with open(file_path,'r') as file:
        csv_reader=csv.reader(file)
        next(csv_reader)
        for row in csv_reader:
            x=float(row[0])
            y=float(row[1])
            x_values.append(x)
            y_values.append(y)
    return x_values, y_values
x_data, y_data = load_dataset('startup_marketing.csv')
l1= LinearRegression(x_data,y_data)
l1.fit()
print("The MSE is: "+str(l1.calculate_mse()))
print("Predicted revenue for $4000 ad spend: " + str(l1.predict([4000])))
predicted_y_data=l1.predict(x_data)
plt.figure(figsize=(10,6))
plt.scatter(x_data,y_data, color="blue", label="Actual Revenue (Historical Data)")
plt.plot(x_data, predicted_y_data, color="red", linewidth=2, label="AI Prediction (Line of Best Fit)")
plt.title('Startup Marketing Trend vs Revenue Forecast')
plt.xlabel('Marketing Spend($)')
plt.ylabel('Revenue($)')
plt.legend()
plt.grid(True)
plt.show()