from filter_packets import *
from packet_parser import *
from compute_metrics import *


L1 = []
L2 = []
L3 = []
L4 = []


#used for computing data
L5 = []
L6 = []
L7 = [] 
L8 = []
L9 = []
L10 = []
L11 = []
L12 = []



#calls the filter function from file_analyzer
filter("Node1.txt",1)
filter("Node2.txt",2)
filter("Node3.txt",3)
filter("Node4.txt",4)

#calls the packet parser
parse("Node1_filtered.txt", L1)
parse("Node2_filtered.txt", L2)
parse("Node3_filtered.txt", L3)
parse("Node4_filtered.txt", L4)


compute()
print("computing: Node1")
read_data(f,L5)
data_size_metrics(L5,"192.168.100.1",L9)
print("-----------------------------------------------------")
print("computing: Node2")
read_data("Node2_filtered.txt",L6)
data_size_metrics(L6,"192.168.100.2",L10)
print("-----------------------------------------------------")
print("computing: Node3")
read_data("Node3_filtered.txt",L7)
data_size_metrics(L7,"192.168.200.1",L11)
print("-----------------------------------------------------")
print("computing: Node4")
read_data("Node4_filtered.txt",L8)
data_size_metrics(L8,"192.168.200.2",L12)


print("\nWriting everything to output.csv")
output(L9,L10,L11,L12)
