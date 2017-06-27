# Name: Dustin Burnham
# CSE 160
# Homework 4

import networkx as nx
import matplotlib.pyplot as plt
from operator import itemgetter

###
### Problem 1a
###

practice_graph = nx.Graph()

practice_graph.add_edge('A', 'B')
practice_graph.add_edge('A', 'C')
practice_graph.add_edge('B', 'C')
practice_graph.add_edge('B', 'D')
practice_graph.add_edge('C', 'D')
practice_graph.add_edge('C', 'F')
practice_graph.add_edge('D', 'F')
practice_graph.add_edge('D', 'E')

assert len(practice_graph.nodes()) == 6
assert len(practice_graph.edges()) == 8

# Test shape of practice graph
assert set(practice_graph.neighbors("A")) == set(["B", "C"])
assert set(practice_graph.neighbors("B")) == set(["A", "D", "C"])
assert set(practice_graph.neighbors("C")) == set(["A", "B", "D", "F"])
assert set(practice_graph.neighbors("D")) == set(["B", "C", "E", "F"])
assert set(practice_graph.neighbors("E")) == set(["D"])
assert set(practice_graph.neighbors("F")) == set(["C", "D"])

def draw_practice_graph():
    """Draw practice_graph to the screen.
    """
    nx.draw_networkx(practice_graph)
    plt.show()

# Comment out this line after you have visually verified your practice graph.
# Otherwise, the picture will pop up every time that you run your program.
# draw_practice_graph()


###
### Problem 1b
###

rj = nx.Graph()

rj.add_edge('Nurse', 'Juliet')
rj.add_edge('Juliet', 'Tybalt')
rj.add_edge('Juliet', 'Friar Laurence',)
rj.add_edge('Juliet', 'Romeo')
rj.add_edge('Juliet', 'Capulet')
rj.add_edge('Tybalt', 'Capulet')
rj.add_edge('Romeo', 'Friar Laurence')
rj.add_edge('Romeo', 'Benvolio')
rj.add_edge('Romeo', 'Montague')
rj.add_edge('Romeo', 'Mercutio')
rj.add_edge('Montague', 'Benvolio')
rj.add_edge('Montague', 'Escalus')
rj.add_edge('Escalus', 'Mercutio')
rj.add_edge('Paris', 'Mercutio')
rj.add_edge('Escalus', 'Paris')
rj.add_edge('Escalus', 'Capulet')
rj.add_edge('Paris', 'Capulet')

assert len(rj.nodes()) == 11
assert len(rj.edges()) == 17

# Test shape of Romeo-and-Juliet graph
assert set(rj.neighbors("Nurse")) == set(["Juliet"])
assert set(rj.neighbors("Friar Laurence")) == set(["Juliet", "Romeo"])
assert set(rj.neighbors("Tybalt")) == set(["Juliet", "Capulet"])
assert set(rj.neighbors("Benvolio")) == set(["Romeo", "Montague"])
assert set(rj.neighbors("Paris")) == set(["Escalus", "Capulet", "Mercutio"])
assert set(rj.neighbors("Mercutio")) == set(["Paris", "Escalus", "Romeo"])
assert set(rj.neighbors("Montague")) == set(["Escalus", "Romeo", "Benvolio"])
assert set(rj.neighbors("Capulet")) == \
set(["Juliet", "Tybalt", "Paris", "Escalus"])
assert set(rj.neighbors("Escalus")) == \
set(["Paris", "Mercutio", "Montague", "Capulet"])
assert set(rj.neighbors("Juliet")) == \
set(["Nurse", "Tybalt", "Capulet", "Friar Laurence", "Romeo"])
assert set(rj.neighbors("Romeo")) == \
set(["Juliet", "Friar Laurence", "Benvolio", "Montague", "Mercutio"])

def draw_rj():
    """Draw the rj graph to the screen and to a file.
    """
    nx.draw_networkx(rj)
    plt.savefig("romeo-and-juliet.pdf")
    plt.show()

# Comment out this line after you have visually verified your rj graph and
# created your PDF file.
# Otherwise, the picture will pop up every time that you run your program.
# draw_rj()

###
### Problem 2
###

def friends(graph, user):
    """Returns a set of the friends of the given user, in the given graph.
    """
    # This function has already been implemented for you.
    # You do not need to add any more code to this (short!) function.
    return set(graph.neighbors(user))

assert friends(rj, "Mercutio") == set(['Romeo', 'Escalus', 'Paris'])

def friends_of_friends(graph, user):
    """Returns a set of friends of friends of the given user, in the given
    graph. The result does not include the given user nor any of that user's
    friends.
    """
    possible_friends = set()
    for Name in friends(graph,user):
        possible_friends = possible_friends | set(graph.neighbors(Name))
    possible_friends = possible_friends - friends(graph,user) - set([user])
    return possible_friends

assert friends_of_friends(rj, "Mercutio") == \
    set(['Benvolio', 'Capulet', 'Friar Laurence', 'Juliet', 'Montague'])


def common_friends(graph, user1, user2):
    """Returns the set of friends that user1 and user2 have in common.
    """
    friends1 = set(graph.neighbors(user1))
    friends2 = set(graph.neighbors(user2))
    friends_in_common = friends1 & friends2
    return friends_in_common


assert common_friends(practice_graph,"A", "B") == set(['C'])
assert common_friends(practice_graph,"A", "D") == set(['B', 'C'])
assert common_friends(practice_graph,"A", "E") == set([])
assert common_friends(practice_graph,"A", "F") == set(['C'])
assert common_friends(rj, "Mercutio", "Nurse") == set()
assert common_friends(rj, "Mercutio", "Romeo") == set()
assert common_friends(rj, "Mercutio", "Juliet") == set(["Romeo"])
assert common_friends(rj, "Mercutio", "Capulet") == set(["Escalus", "Paris"])


def number_of_common_friends_map(graph, user):
    """Returns a map (a dictionary), mapping from each user U to the number
    of friends U has in common with the given user. The map keys are the
    users who have at least one friend in common with the given user,
    and are neither the given user nor one of the given user's friends.
    Example: a graph called my_graph and user "A"
    (Note: This is NOT the practice_graph used in the assignment writeup.)
    Here is what is relevant about my_graph:
    - "A" and "B" have two friends in common
    - "A" and "C" have one friend in common
    - "A" and "D" have one friend in common
    - "A" and "E" have no friends in common
    - "A" is friends with "D" (but not with "B" or "C")
    Here is what should be returned:
    number_of_common_friends_map(my_graph, "A")  =>   { 'B':2, 'C':1 }
    """
    common_friends_map = {}
    for Name in friends_of_friends(graph, user):
        common = common_friends(graph, user, Name)
        common_friends_map[Name] = len(common)
    return common_friends_map

assert number_of_common_friends_map(practice_graph, "A") == {'D': 2, 'F': 1}
assert number_of_common_friends_map(rj, "Mercutio") == \
    { 'Benvolio': 1, 'Capulet': 2, 'Friar Laurence': 1, 
      'Juliet': 1, 'Montague': 2 }


def number_map_to_sorted_list(map_with_number_vals):
    """Given map_with_number_vals, a dictionary whose values are numbers,
    return a list of the keys in the dictionary.
    The keys are sorted by the number value they map to, from greatest
    number down to smallest number.
    When two keys map to the same number value, the keys are sorted by their
    natural sort order for whatever type the key is, from least to greatest.
    """

    final_list = list()
    sorted_by_name = sorted(map_with_number_vals.items(), key=itemgetter(0))
    sorted_by_score = sorted(sorted_by_name, key=itemgetter(1),reverse=True)
    for index in range(len(sorted_by_score)):
        final_list.append(sorted_by_score[index][0])
    return final_list
    
assert number_map_to_sorted_list({"a":5, "b":2, "c":7, "d":5, "e":5}) == \
['c', 'a', 'd', 'e', 'b']


def recommend_by_number_of_common_friends(graph, user):
    """Return a list of friend recommendations for the given user.
        The friend recommendation list consists of names/IDs of people in
    the graph who are not yet a friend of the given user.  The order
    of the list is determined by the number of common friends (people
    with the most common friends are listed first).  In the
    case of a tie in number of common friends, the names/IDs are
    sorted by their natural sort order, from least to greatest.
    """

    common_friends = number_of_common_friends_map(graph, user)
    Recommendation = number_map_to_sorted_list(common_friends)
    return Recommendation

assert recommend_by_number_of_common_friends(practice_graph,"A") == ['D', 'F']
assert recommend_by_number_of_common_friends(rj, "Mercutio") == \
['Capulet', 'Montague', 'Benvolio', 'Friar Laurence', 'Juliet']


###
### Problem 3
###

def influence_map(graph, user):
    """Returns a map (a dictionary) mapping from each person P to their
    influence score, with respect to the given user. The map only
    contains people who have at least one friend in common with the given
    user and are neither the user nor one of the users's friends.
    See the assignment for the definition of influence scores.
    """
    
    influence = {}
    potential_friends = friends_of_friends(graph, user)
    for people in potential_friends:
        friends_in_common = common_friends(graph,people,user)
        influence_fraction = 0
    
    # Calculate the total influence of a person. Sum of 1/(# of freinds)
        for Name in friends_in_common:
            influence_fraction += (1.0 / len(friends(graph,Name)))
        influence[people] = influence_fraction
    return influence


assert influence_map(rj, "Mercutio") == \
    { 'Benvolio': 0.2, 'Capulet': 0.5833333333333333,
    'Friar Laurence': 0.2, 'Juliet': 0.2, 'Montague': 0.45 }
    

def recommend_by_influence(graph, user):
    """Return a list of friend recommendations for the given user.
        The friend recommendation list consists of names/IDs of people in
    the graph who are not yet a friend of the given user.  The order
    of the list is determined by the influence score (people
    with the biggest influence score are listed first).  In the
    case of a tie in influence score, the names/IDs are sorted
    by their natural sort order, from least to greatest.
    """
    influence_dict = influence_map(graph, user) 
    final_list = list()
    sorted_by_name = sorted(influence_dict.items(), key=itemgetter(0))
    sorted_by_score = sorted(sorted_by_name, key=itemgetter(1),reverse=True)
    for index in range(len(sorted_by_score)):
        final_list.append(sorted_by_score[index][0])
    return final_list

assert recommend_by_influence(rj, "Mercutio") == \
    ['Capulet', 'Montague', 'Benvolio', 'Friar Laurence', 'Juliet']


###
### Problem 4
###

def unchanged_recommendations(graph, data):
    """This function uses a list of names (data) and a graph
    and compares the two lists of friend recommendations (influence and common
    friends),and saves the names of the people with unchanged recommendations
    to a sorted list.
    """

    no_diff = list()
    for person in data:
        influence_method = recommend_by_influence(graph, person)
        common_method = recommend_by_number_of_common_friends(graph, person)
        if influence_method == common_method:
            no_diff.append(person)

    return sorted(no_diff)

def changed_recommendations(graph, data):
    """This function uses a list of names (data) and a graph
    and compares the two lists of friend recommendations (influence and common
    friends), and saves the names of the people with changed recommendations
    to a sorted list.
    """

    diff = list()
    for person in data:
        influence_method = recommend_by_influence(graph, person)
        common_method = recommend_by_number_of_common_friends(graph, person)
        if influence_method != common_method:
            diff.append(person)
    return sorted(diff)
    
rj_people = ["Nurse", "Juliet", "Tybalt", "Capulet", "Friar Laurence",
            "Romeo", "Benvolio", "Montague", "Mercutio", "Escalus", "Paris"]

print "Unchanged Recommendations:", unchanged_recommendations(rj, rj_people)
print "Changed Recommendations:", changed_recommendations(rj, rj_people)


###
### Problem 5
###

# (Your Problem 5 code goes here.)

assert len(facebook.nodes()) == 63731
assert len(facebook.edges()) == 817090


###
### Problem 6
###

# (Your Problem 6 code goes here.)

###
### Problem 7
###

# (Your Problem 7 code goes here.)

###
### Problem 8
###

# (Your Problem 8 code goes here.)

###
### Collaboration
###

# No Collaboration