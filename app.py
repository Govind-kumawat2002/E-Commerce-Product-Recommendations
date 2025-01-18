from flask import Flask ,render_template ,request ,url_for
import joblib
import pandas as pd 
import numpy as np 
name = list(pd.read_csv('maindata/clean_electronic.csv'))
main=Flask(__name__)


popular=pd.read_csv('maindata/clean_electronic.csv')
@main.route('/')
def index():
    return render_template('index.html')
@main.route('/bookName')
def show_book_name():
    name = list(pd.read_csv('maindata/clean_electronic.csv')['name'].values)
    return render_template("bookname.html",list_fo_item_name = name)
# to get the popularity based recommandation system


@main.route('/recommend1')
def recommend1():
    return render_template('popularity.html',
                           itmename = list(popular['name'].values),
                           image=list(popular['image'].values),
                           image_link=list(popular['link'].values),
                           rating=list(popular['ratings'].values),
                           discount_price=list(popular['discount_price'].values),
                           actual_price=list(popular['actual_price'].values),
                           search_terms=list(popular['search_terms'].values),
                           image_id=list(popular['image_id'].values),
                           link_id=list(popular['link_id'].values),
                           ratings_cleaned=list(popular['ratings_cleaned'].values),
                           num_ratings_cleaned=list(popular['num_ratings_cleaned'].values)
                        
                           
                           )




@main.route('/recommend2')
def recommend2():
    return render_template('recomandation.html')

# # to get the recommandation by the recommandation-2
@main.route('/recommend_books',methods=['post'])
def recommend():
    try:
        user_input = request.form.get('user_input')
        index = np.where(name.index == user_input)[0][0]
        similar_items = sorted(list(enumerate(name[index])), key=lambda x: x[1], reverse=True)[1:9]
    except:
        return render_template("errorrr.html")
    else:
        data = []
        for i in similar_items:
            item = []
            temp_df = name[name['Book-Title'] == name.index[i[0]]]
            item.extend(list(temp_df.drop_duplicates('name')['name'].values))
            item.extend(list(temp_df.drop_duplicates('name')['image'].values))
            item.extend(list(temp_df.drop_duplicates('name')['link'].values))
            item.extend(list(temp_df.drop_duplicates('name')['ratings'].values))
            item.extend(list(temp_df.drop_duplicates('name')['discount_price'].values))
            item.extend(list(temp_df.drop_duplicates('name')['search_terms'].values))
            item.extend(list(temp_df.drop_duplicates('name')['image_id'].values))
            item.extend(list(temp_df.drop_duplicates('name')['link_id'].values))
            item.extend(list(temp_df.drop_duplicates('name')['ratings_cleaned'].values))
            item.extend(list(temp_df.drop_duplicates('name')['num_ratings_cleaned'].values))




            data.append(item)
        print(item)
        # print(data)
        return render_template('recomandation.html',data=data)


if __name__=="__main__":
    main.run(debug= True)
