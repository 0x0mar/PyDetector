from networkx import *

z=[5,3,3,3,3,2,2,2,1,1,1]
print is_valid_degree_sequence(z)

print("Configuration model")
G=configuration_model(z)  # configuration model
degree_sequence=list(degree(G).values()) # degree sequence
print("Degree sequence %s" % degree_sequence)
print("Degree histogram")
hist={}
for d in degree_sequence:
    if d in hist:
        hist[d]+=1
    else:
        hist[d]=1
print("degree #nodes")
for d in hist:
    print('%d %d' % (d,hist[d]))