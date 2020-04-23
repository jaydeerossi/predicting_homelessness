from util import load_dbmi
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import BernoulliNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix, f1_score
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import plot_confusion_matrix


filename = r'data/smokers_surrogate_train_all_version2.xml'
notes, smoking = load_dbmi(filename, mode = 'smoking')
smoking = [ 0 if (smok == 'NON-SMOKER' or smok == 'UNKNOWN') else 1 for smok in smoking]
print(set(smoking))

bow = CountVectorizer()
tfidf = TfidfTransformer()

print('Building featurizer...')
X_train_bow = bow.fit_transform(notes)
# X_train_tfidf = tfidf.fit_transform(X_train_bow)

print('Splitting train and dev data...')
X_train, X_dev, y_train, y_dev = train_test_split(X_train_bow, smoking, test_size=0.3, random_state=42)

model = BernoulliNB().fit(X_train, y_train)
y_hat = model.predict(X_dev)

print('Accuracy = {}'.format(np.mean(y_hat == y_dev)))

confmat = confusion_matrix(["SMOKER" if y == 1 else "NON-SMOKER" for y in y_dev],\
 ["SMOKER" if y == 1 else "NON-SMOKER" for y in y_hat])

disp = plot_confusion_matrix(model, X_dev, y_dev,
                                cmap='Blues', display_labels=['NON-smoker','smoker'])

disp.ax_.set_title('Confusion Matrix. F1 = {}'.format(f1_score(y_dev, y_hat)))

# print(disp.confusion_matrix)
plt.savefig('confmat.png')
