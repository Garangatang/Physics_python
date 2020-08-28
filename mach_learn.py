import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt
from sklearn import datasets, svm, metrics
from sklearn.model_selection import train_test_split
import numpy as np


digits = datasets.load_digits()
# from skleanr tutorial page
images_and_labels = list(zip(digits.images, digits.target))
n_samples = len(digits.images)
data = digits.images.reshape((n_samples, -1))

# ben mucked w/this
_, axes = plt.subplots(4, 4)
plt.subplots_adjust(hspace=0.5)
for ax, (image,label) in zip(axes[:2,:].flatten()[:], images_and_labels[:8]):
    ax.set_axis_off()
    ax.imshow(image, cmap=plt.cm.gray_r, interpolation='nearest')
    ax.set_title('Training: %i' % label)

# choose your classifier
classifier = svm.SVC(gamma=0.001)

# split into training and test sets
X_train, X_test, y_train, y_test = train_test_split(data, digits.target, test_size=0.5, shuffle=False)

# do it!
classifier.fit(X_train, y_train)
predicted = classifier.predict(X_test)

print('number in test set:',len(y_test))
right=np.sum(y_test==predicted)
print('number corretly classified:',right)

msk = y_test!=predicted
X_fails,y_fails,predfails = X_test[msk],y_test[msk],predicted[msk]

plot_the_failures=False
if plot_the_failures:
    print('plotting the bad predictions')
    digims = digits.images[n_samples // 2:]
    digimfails = digims[msk]
    im_and_pred = list(zip(digimfails, predfails))
    for ax, (image,pred) in zip(axes[2:, :].flatten()[:], im_and_pred[:8]):
        ax.set_axis_off()
        ax.imshow(image, cmap=plt.cm.gray_r, interpolation='nearest')
        ax.set_title('Bad Predict: %i' % pred)

else:
    images_and_predictions = list(zip(digits.images[n_samples // 2:], predicted))
    for ax, (image,pred) in zip(axes[2:, :].flatten()[:], images_and_predictions[:8]):
        ax.set_axis_off()
        ax.imshow(image, cmap=plt.cm.gray_r, interpolation='nearest')
        ax.set_title('Prediction: %i' % pred)

ofil='tmp.png'
print('saving to file',ofil)
plt.savefig(ofil)
import os
os.system('convert '+ofil+' ~/public_html/tmp.jpg')
