from flask import Flask ,render_template ,request ,url_for
import joblib
import pandas as pd 
import numpy as np 
main=Flask(__name__)
@main.route('/')
def index():
    return render_template('index.html')
@main.route('/bookName')
def show_book_name():
    book_name = list(pd.read_csv('maindata/clean_electronic.csv')['name'].values)
    return render_template("bookname.html",list_fo_book_name = book_name)
# to get the popularity based recommandation system


if __name__=="__main__":
    main.run(debug= True)
