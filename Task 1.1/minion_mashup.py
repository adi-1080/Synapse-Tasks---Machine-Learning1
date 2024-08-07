Kevin = {"Halsey","Taylor Swift", "Mitski", "Joji", "Shawn Mendes", "Sabrina Carpenter", "Nicky Minaj", "Conan Gray", "One Direction", "Justin Bieber"}
Stuart = {"Kendrick Lamar", "Steve Lacy", "Tyler the Creator", "Joji", "TheWeeknd", "Coldplay", "Kanye West", "Travis Scott", "Frank Ocean", "Brent Faiyaz"}
Bob = {"Conan Gray", "Joji", "Dove Cameron", "Mitski", "Arctic Monkeys", "Steve Lacy", "Kendrick Lamar", "Isabel LaRosa", "Shawn Mendes", "Coldplay"}
Edith = {"Metallica", "Billie Eilish", "TheWeeknd", "Mitski", "NF", "Conan Gray", "Kendrick Lamar", "Nicky Minaj", "Kanye West", "Coldplay"}
djs = {
    "Kevin" : Kevin,
    "Stuart" : Stuart,
    "Bob" : Bob,
    "Edith" : Edith,
}
#Finding pairs
dj_list = list(djs.keys())  # =>  #djs = {'Kevin','Stuart','Bob','Edith'}
pairs = []
#print(dj_list)
for i in range(len(dj_list)):
    for j in range(len(dj_list)):
        if(i==j):
            continue
        pairs.append((dj_list[i],dj_list[j]))
#print((pairs[0][1]))


#Finding common artists in two djs
def findCommonArtists(dj1, dj2):
    s1 = djs[dj1]
    s2 = djs[dj2]
    common = s1.intersection(s2)
    percentage_overlap = (len(common)/len(s1)) * 100 #since both have 10 artists each
    return percentage_overlap

#Finding possible dj pairs
possible_dj_pairs = []
for each_pair in pairs:
    #print(each_pair)
    percentage_overlap = findCommonArtists(each_pair[0],each_pair[1])
    if(percentage_overlap >= 30):
        possible_dj_pairs.append((each_pair[0],each_pair[1],percentage_overlap))

unique_pairs = set()
final = []
for each_pair in possible_dj_pairs:
    sorted_pair = tuple(sorted(each_pair[:2]))
    if sorted_pair not in unique_pairs:
        unique_pairs.add(sorted_pair)
        final.append(each_pair)
print(final)

final_sorted = sorted(final, key=lambda x: (-x[2], sorted(x[:2])))

for i in final_sorted:
    print(i)
















   
# check=findCommonArtists(pairs[0][0],pairs[0][1])
# print(check)

# for i in range(1,6):
#     for j in range(1,6):
#         pairs.append((dj[i],dj[j]))
# print(pairs)

# print(type(Kevin))
# print(Kevin)

# print(type(djs))
# print(djs)
# print(djs["Kevin"])
# print(list(djs.keys()))

# for i in range(len(djs)):
#     for j in range(len(djs)):
#         for items in djs:
#             print(items)
            
# def findIntersection(dj1, dj2):
#     common = dj1.intersection(dj2)
#     print(common)

# findIntersection(kevinSet,bobSet)