from collections import Counter

users = [
{"id":0,"name":"Hero"},
{"id":1,"name":"Dunn"},
{"id":2,"name":"Sue"},
{"id":3,"name":"Chi"},
{"id":4,"name":"Thor"},
{"id":5,"name":"Clive"},
{"id":6,"name":"Hicks"},
{"id":7,"name":"Devin"},
{"id":8,"name":"Kate"},
{"id":9,"name":"Klein"}
]
friendship = [
(0,1),(0,2),(1,2),(1,3),(2,3),(3,4),(4,5),(5,6),(5,7),(6,8),(7,8),(8,9)
]

for user in users:
    user["friends"] = []

for i,j in friendship:
    users[i]["friends"].append(users[j])
    users[j]["friends"].append(users[i])

def number_of_friends(user):
    return len(user["friends"])

total_connections = sum(number_of_friends(user) for user in users)


num_users = len(users)
avg_connections = total_connections / num_users

num_friends_by_id = [(user["id"], number_of_friends(user)) for user in users]

# sorted(number_of_friends, key=lambda (user_id, num_friends): num_friends, reverse=True)

def friends_of_friend_ibs_bad(user):
    return[foaf["id"]
        for friend in user["friends"]
        for foaf in friend["friends"]]

print [friend["id"] for friend in users[0]["friends"]]
print [friend["id"] for friend in users[1]["friends"]]
print [friend["id"] for friend in users[2]["friends"]]

def not_the_same(user, other_user):
    return user["id"] != other_user["id"]

def not_friend(user, other_user):
    return all(not_the_same(friend, other_user)for friend in user["friends"])

def friends_of_friend_ibs(user):
    return Counter(foaf["id"] for frisnd in user["friends"]
    for foaf in friend["friends"]
    if not_the_same(user, foaf)
    and not_friend(user,foaf))

print(friends_of_friend_ibs(users[3]))
