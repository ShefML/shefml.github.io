Title: The k-Nearest Neighbours Classifier
Authors: Paul Brabban
Date: 2018-01-16 22:00
Category: meetup
Summary: SheffieldML #2: a k-nearest neighbour classifier workshop

January's SheffieldML meetup took place earlier today, with a hands-on workshop looking at the
k-nearest neighbour classifier.
Around ten people came along, including some faces I recognise from the first meetup last November - which is great!

We followed guidance that focused first on how we might implement our own kNN classifier from scratch in Python,
then suggested options to explore further.
A couple of specific datasets were suggested for the exercise, one small, one large enough to show the need for efficiency.
If you're interested in having a go yourself, the material is available in our [dojo-knn repository](https://github.com/ShefML/dojo-knn).
Forks, issues and pull requests very welcome!

There were a number of questions during the session - initially caused by a mistake I'd made in preparing the material above!
A directory in the wrong place, meaning that the beginner's template didn't work!
Of all the things to mess up :facepalm:
Fixed with a quick commit and push, and the attendees affected just took it in their stride.

Some interesting questions I hadn't anticipated came up, including:

* is it necessary to normalize the features in the data?
* is the square root part of the distance calculation actually redundant?
* is there a faster way of getting the "nearest k" neighbours than sorting *all* the distances?
* is the kNN classifier a clustering algorithm?

Those are great questions - what do you think?

After a couple of hours, we went around the group, with everyone talking briefly about what they'd found interesting.
A couple of people had skipped the implementation itself and instead used a scikit-learn's classifier to explore the datasets instead.
Another attendee suggested that they'd have preferred to do something like that.

That's useful feedback - I'd not really considered that some people might not be interested in implementing the classifier themselves.
We should think about how to accommodate both perspectives in sessions like this going forward!

Everyone attending gave really nice feedback too, with a few people saying they'll be back in February.
I guess we'd best crack on with sorting out a February session!
