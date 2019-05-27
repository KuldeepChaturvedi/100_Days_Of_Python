import numpy as np

# pip install lightfm
# for installing lightfm Microsoft Visual C++ 14.0 is required so please install before installing lightfm
from lightfm.datasets import fetch_movielens
from lightfm import LightFM


# fetch data and format it  
data = fetch_movielens(min_rating=4.0)

# print training and testing data
print(repr(data['train']))
print(repr(data['test']))

# create model
model = LightFM(loss='warp')

# train model
model.fit(data['train'],epochs=30,num_threads=2)

def sample_recomendation(model, data, user_ids):
    # number of users and movies in train data
    n_user, n_items = data['train'].shape

    # generate recommendation for each user we input
    for user_id in user_ids:

        # movies they already like
        known_positives = data['item_labels'][data['train'].tocsr()[user_id].indices]

        # movies our model pridicts they will like
        scores = model.predict(user_id,np.arange(n_items))

        # rank them order of most liked to least
        top_items = data['item_labels'][np.argsort(-scores)]

        # print out the results
        print("Users %s" % user_id)
        print("        Known Positives:")

        for x in known_positives[:3]:
            print("         %s" % x)
        
        print("        Recommended:")

        for x in top_items[:3]:
            print("         %s" % x)
        
sample_recomendation(model,data,[100,200,400])