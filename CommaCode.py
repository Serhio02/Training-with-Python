spam = ['apples', 'bananas', 'tofu', 'cats', 'cars']

def comma(items):
    for i in range(len(items) -2):
        print(items[i], end=", ")# minor adjustment from one beginner to another: to make it cleaner, simply move the ', ' to equal 'end'. the print statement should finish like this --> end=', '
    print(items[-2] + ' and ' + items[-1]) 

comma(spam)
