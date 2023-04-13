import matplotlib.pyplot as plt 
import pandas as pd
import plotly.express as px
from sklearn.decomposition import PCA
from gensim.models import Word2Vec

model = Word2Vec.load("word2vec.model")

target_words =["endowment", "gospel", "faith", "ordinance", "baptism", "atonement", "priesthood", "bible", "mormon", "agency", "proxy", "bishop", "prophet", "celestial", "heaven", "hell", "satan", "cross", "godhead", "gratitude", "christmas", "humble", "miracle", "peace", "polygamy", "sacrament", "spirit", "commandments", "tithing", "authority", "blessing", "christian", "church", "calling", "doctrine", "creation", "mortality", "charity", "faith", "hope", "repentance", "conversion", "mission", "missionary", "doctrine", "disciple", "easter", "endure", "fall", "jesus", "joy", "happiness", "knowledge", "language", "light", "love", "mercy", "mortality", "patience", "prayer", "pride", "prompting", "restoration", "vision", "redemption", "resurrection", "sabbath", "sunday", "sacrifice", "scriptures", "sealing", "sin", "talent", "temple", "testimony"]

# Makes the vectors 2D
x = model.wv[target_words]
pca = PCA(n_components=2)
result = pca.fit_transform(x)

df = pd.DataFrame(result, columns=list('XY'))
df['target_words'] = target_words
df['target_words'] = df['target_words'].str.title()

# scatter plot and display
fig = px.scatter(df, x="X", y="Y", text="target_words", log_x=True, size_max=60)
fig.update_traces(textposition='top center')
fig.update_layout(
    height=600,
    title_text='Word embedding chart'
)
fig.show()

