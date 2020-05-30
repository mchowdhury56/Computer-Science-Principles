import sys
database = "musicrecplus.txt"

def main():
    '''Main function, initiates the program and menu'''
    usermap = loadUsers(database)
    publicmap = filtermap(usermap)
    username = input("Enter your name (put a $ symbol after your name if you wish your preferences to remain private):\n")
    if username == '':
        while username == '':
            print('You cannot enter a blank username. Please enter a username.')
            username = input("Enter your name (put a $ symbol after your name if you wish your preferences to remain private):\n")
    if username not in usermap:
        enter_preferences(usermap, username)
    while True:
        print("Enter a letter to choose an option:")
        print("e - Enter preferences")
        print("r - Get recommendations")
        print("p - Show most popular artists")
        print("h - How popular is the most popular")
        print("m - Which user has the most likes")
        print("q - Save and quit")
        choice = input()
        if choice == 'e':
            enter_preferences(usermap, username)
        if choice == 'r':
            recs = getRecommendations(username,usermap[username],filtermap(usermap))
            printrecs(recs,username)
        if choice == 'p':
            bestArtists(filtermap(usermap))
        if choice == 'h':
            number_of_likes(filtermap(usermap))
        if choice == 'm':
            bestUser(filtermap(usermap))
        if choice == 'q':
            save_and_quit(usermap,database,username,usermap[username])
            break
        if choice == '':
            continue

def loadUsers(filename):
    '''loads users from a file and creates a file if it doesnt exist'''
    try: file = open(filename, 'r')
    except FileNotFoundError:
        open(filename, 'w')
    file = open(filename, 'r')
    usermap = {}
    for line in file:
        [user, artists] = line.strip().split(':')
        artistList = artists.split(",")
        artistList.sort()
        usermap[user] = artistList
    file.close()
    return usermap

def filtermap(dictionary):
    ''' returns a new dictionary with public users only'''
    newdict = {}
    for key, value in dictionary.items():
        if key[-1] != '$':
            newdict[key] = value
    return newdict

def enter_preferences(dictionary, name):
    '''allows users to enter their preferrences and updates if necessary'''
    artistlist = []
    preference = input("Enter an artist that you like (Enter to finish):\n")
    if preference == '':
        while preference == '':
            print('You must enter at least 1 artist before you can proceed')
            preference = input("Enter an artist that you like (Enter to finish):\n")
    while preference != '':
        artistlist.append(preference)
        preference = input("Enter an artist that you like (Enter to finish):\n")
        dictionary[name] = list(set(artistlist))
    
def save_and_quit(dictionary,filename,user,preferences):
    '''saves preferences and ends the program if option q is chosen'''
    dictionary[user] = preferences
    file = open(filename, 'w')
    for user in dictionary:
        newline = str(user)+":"+",".join(dictionary[user])+ \
                  "\n"
        file.write(newline)
    file.close()

def printrecs(recs, username):
    '''prints the reccomended artists in the program'''
    if recs == []:
        print("No recommendations available at this time")
    else:
        for artists in recs:
            print(artists)
            
def getRecommendations(currentuser,prefs,usermap):
    '''returns the user's recommended artists '''
    bestUser = findBestUser(currentuser,prefs,usermap)
    if bestUser == None:
        return []
    recomendations = drop(prefs,usermap[bestUser])
    return recomendations

def findBestUser(currentuser,prefs,usermap):
    '''find the user with the most similar preferences'''
    users = usermap.keys()
    bestUser = None
    bestScore = -1
    for user in users:
        score = number_of_matches(prefs,usermap[user])
        if score > bestScore and currentuser != user and prefs != usermap[user]:
            bestScore = score
            bestUser = user
    if bestScore == 0:
        bestUser = None
    return bestUser

def number_of_matches(list1,list2):
    '''finds the number of matches that two users have'''
    list1.sort()
    list2.sort()
    matches = i = j = 0
    while i<len(list1) and j<len(list2):
        if list1[i] == list2[j]:
            matches += 1
            i += 1
            j += 1
        elif list1[i] < list2[j]:
            i += 1
        else:
            j += 1
    return matches

def drop(list1,list2):
    '''generates the list of recommendations based on sorted lists'''
    list1.sort()
    list2.sort()
    result = []
    i = j = 0
    while i < len(list1) and j < len(list2):
        if list1[i] == list2[j]:
            i += 1
            j+= 1
        elif list1[i] < list2[j]:
            i += 1
        else:
            result.append(list2[j])
            j += 1
    return result


def bestArtists(usermap):
    '''returns the most popular artists'''
    userlist = usermap.keys()
    likes = {}
    mostPopular = []
    maxLikes = 0
    for user in userlist:
        for artist in usermap[user]:
            if artist in likes:
                likes[artist] += 1
            else:
                likes[artist] = 1
    for artists in likes:
        if likes[artists] > maxLikes:
            maxLikes = likes[artists]
    for artists in likes:
        if likes[artists] == maxLikes:
            mostPopular.append(artists)
    if mostPopular == []:
        print("Sorry, no artists found")
    else:
        for artist in mostPopular:
            print(artist)

def number_of_likes(usermap):
    '''returns the number of likes that the most popular artist has'''
    userlist = list(usermap.keys())
    if userlist == []:
        print("Sorry, no artists found")
    else:
        likes = {}
        mostPopular = []
        maxLikes = 0
        for user in userlist:
            for artist in usermap[user]:
                if artist in likes:
                    likes[artist] += 1
                else:
                    likes[artist] = 1
        for artists in likes:
            if likes[artists] > maxLikes:
                maxLikes = likes[artists]
        for artists in likes:
            if likes[artists] == maxLikes:
                mostPopular.append(artists)
        print(maxLikes)

def bestUser(usermap):
    '''returns the user with the most likes'''
    users = list(usermap.keys())
    if users == []:
        print("Sorry, no user found")
    else:
        maximum = 0
        bestUser = []
        for x in range(len(users)):
            if len(usermap[users[x]]) >= maximum:
                maximum = len(usermap[users[x]])
                bestUser.append(users[x])
        for x in range(len(bestUser)):
            print(bestUser[x])

    
if __name__ == "__main__": main()
