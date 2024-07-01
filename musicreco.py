import pandas as pd
from bs4 import BeautifulSoup

metadata =pd.read_csv("./sss1.csv")

from sklearn.feature_extraction.text import TfidfVectorizer

def get_recommendations(title):

    metadata['overview'] = metadata['Tweet'].apply(lambda x: BeautifulSoup(x, "lxml").text)

    metadata['overview'] =metadata['overview']+metadata['Artist']+metadata['song']+metadata['Album']+metadata['Sentiment'];


    #Define a TF-IDF Vectorizer Object. Remove all english stop words such as 'the', 'a'
    tfidf = TfidfVectorizer(stop_words='english')

    #Replace NaN with an empty string
    metadata['overview'] = metadata['overview'].fillna('')

    #Construct the required TF-IDF matrix by fitting and transforming the data
    tfidf_matrix = tfidf.fit_transform(metadata['overview'])

    #Output the shape of tfidf_matrix
    print(tfidf_matrix.shape)

    from sklearn.metrics.pairwise import linear_kernel

    # Compute the cosine similarity matrix
    cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)

    indices = pd.Series(metadata.index, index=metadata['song']).drop_duplicates()


    # Get the index of the song that matches the title
    idx = indices[title]

    # Get the pairwsie similarity scores of all songs with that song
    sim_scores = list(enumerate(cosine_sim[idx]))
#    print(sim_scores)

    # Sort the songs based on the similarity scores
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)

    # Get the scores of the 10 most similar song
    sim_scores = sim_scores[1:11]

    # Get the song indices
    movie_indices = [i[0] for i in sim_scores]

    # Return the top 10 most similar song
    return metadata['song'].iloc[movie_indices]




def getTitle(rec):
    asd = metadata[metadata['Genre'] == rec[0]]
    ret = (asd.sample(n=1))


    return  ret



def getRecommendations(rec):
   
    asd = metadata[metadata['Genre'] == rec[0]]
    
    ret = (asd.sample(n=1))
    s1 = ret.loc[:, 'song']
    
    rest = get_recommendations(s1.values[0])
    return rest

#song = getRecommendations(['Pop'])
# print(song)
