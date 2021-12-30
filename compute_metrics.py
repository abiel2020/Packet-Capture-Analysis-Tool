import re


def compute() :
	print('\ncalled compute function in compute_metrics.py\n')

f = "Node1_filtered.txt"
req = 8
rep = 0
L=[] #Computing actual metrics
L2 = [] #Computing actual metrics
L3= [] #Computing actual metrics
L4 = [] #Computing actual metrics
L5 = [] #Storing new metrics
L6 = [] #Storing new metrics
L7 = [] #Storing new metrics
L8 = [] #Storing new metrics
frame = []
record=[]
newData = []


def read_data(filename,list) :
   

   with open(filename) as file:
      for line in file:
         split_line = line.strip().split()
         line = (split_line[0])
         time = (split_line[1]) #Time
         sIP = (split_line[2]) #Source IP
         dIP = (split_line[3]) #Destination IP
         icmp = (split_line[4])
         length = int(split_line[5]) #Length
         echo = (split_line[6])
         ping = (split_line[7])
         type = (split_line[8]) #req or reply
         id = (split_line[9])
         seq = (split_line[10]) #Sequence Number
         ttl = (split_line[11]) #TTL
         
         
         frame=[line,time,sIP,dIP,icmp,length,echo,ping,type,id,seq,ttl] #Create a frame
         list.append(frame) #Put it in a list
         
         
     
def data_size_metrics(list,sIP,newList):
   requestSent = 0
   requestRecieved = 0
   repliesSent = 0
   repliesRecieved = 0
   requestBytesSent = 0
   requestBytesRecieved = 0
   requestDataSent = 0
   requestDataRecieved = 0
   totalTime = 0
   a = 0
   b = 0
   c = 0
   d = 0
   e = 0
   rtt = 0
   requestThroughput = 0
   requestGoodput = 0
   replyDelay = 0
   differenceTime = 0
   nodeTimeDifference = 0
   currentHops = 0
   ttl = 0
   hops = 0
   oghop = 129
   count = 0
   averageHops = 0
   timeDelay = 0

   
   for data in list :
      
      
      if data[8] == "request" : #type is a request
         if data[2] == sIP : #if Source IP == sourceIP
            requestSent += 1 
            requestBytesSent += (data[5]) 
            requestDataSent += (data[5]) - 42 #14(ETHERNET II frame size) + 20(Header length) + 8(echo request header) = 42 

         if data[3] == sIP : #Otherwise, if destination is source IP
            requestRecieved += 1 
            requestBytesRecieved += (data[5]) 
            requestDataRecieved += (data[5]) - 42 #14(ETHERNET II frame size) + 20(Header length) + 8(echo request header) = 42 
         

      if data[8] == "reply" : #Type is a reply
         if data[2] == sIP : #If source is sending out 
            repliesSent += 1 
	
         if data[3] == sIP : #If source is the destination IP
            repliesRecieved += 1 




   print("Request sent: " , requestSent)
   print("Request recieved: " , requestRecieved)
   print("Replies sent: ",repliesSent)
   print("Replies recieved: ",repliesRecieved) 
   print("Request bytes sent: ",requestBytesSent)
   print("Request bytes recieved: ", requestBytesRecieved)
   print("Request data sent: ",requestDataSent)
   print("Request data recieved:" ,requestDataRecieved)

   
   #RTT
   for i in range(0, len(list)):
      
      if list[i][2] == sIP and list[i][8] == "request": #If the index in the sourceIP == sourceIP and the index in the type is 8:
      #if list[i][10] == list[i+1][10]:
         totalTime = totalTime + (float(list[i + 1][1]) - float(list[i][1])) #Subtract times
         #print(totalTime)
         a += 1
         #print(a)
         rtt = ((totalTime / a) * 1000)
   print("Average RTT (ms): ",round(rtt,2))
   
   #THROUGHPUT
   for i in range(0, len(list)):
      
      if list[i][2] == sIP and list[i][8] == "request": #If the index in the sourceIP == sourceIP and the index in the type is 8:
         b = (requestBytesSent / totalTime)
         requestThroughput = b / 1000
   print("Request throughput: ",round(requestThroughput,1))
   
   
   #GOODPUT
   for i in range(0, len(list)):
      if list[i][2] == sIP and list[i][8] == "request":
         c = requestDataSent / totalTime
         requestGoodput = c / 1000
   print("Request goodput: ",round(requestGoodput,1))
   
   #TIME DELAY
   for i in range(0, len(list)):
        if list[i][3] == sIP and list[i][8] == "request":
            differenceTime = differenceTime + (float(list[i + 1][1]) - float(list[i][1]))
            d += 1
            nodeTimeDifference = (differenceTime/d)
            timeDelay = nodeTimeDifference*1000000
   print("Average reply delay: ",round(timeDelay,2))
   
  
   
   #AVERAGE HOPS
   for i in range(0, len(list)):
      if list[i][8] == "reply" and list[i][3] == sIP :       
         ttl = int(re.search(r'\d+', list[i][11]).group()) #Turn String into integer
         e = oghop - ttl
         hops = hops + e
         
         averageHops = hops / requestSent
   print("Average request hop count: ",round(averageHops,2))
 
   newData = [requestSent,requestRecieved,repliesSent,repliesRecieved,requestBytesSent,requestDataSent,requestBytesRecieved,requestDataRecieved,round(rtt,2),round(requestThroughput,1),round(requestGoodput,1),round(timeDelay,2),round(averageHops,2)]
   newList.append(newData)


#Writing to output file. Takes newList as a parameter   
def output(node1,node2,node3,node4):

   for data in node1:
   
      f = open("output.csv","w")
      f.write("Node1\n\n")    
      f.write("Echo Requests Sent" + "," + "Echo Requests Recieved" + "," + "Echo Replies Sent" + "," + "Echo Replies Recieved\n")
      f.write(str(data[0]) + ","+str(data[1]) + ","+str(data[2]) + ","+str(data[3]) + "\n")
      f.write("Echo Request Bytes sent (bytes)" + "," + "Echo Request Data Sent (bytes)\n")
      f.write(str(data[4])+","+str(data[5]) + "\n")
      f.write("Echo Request Bytes Recieved (bytes)" + "," + "Echo Request Data Recieved (bytes)\n")
      f.write(str(data[6]) + "," + str(data[7]))
      f.write("\n\n")
      f.write("Average RTT (miliseconds)" + "," + str(data[8]) + "\n")
      f.write("Echo Request Throughput (kB/sec)" + "," + str(data[9]) + "\n")
      f.write("Echo Request Goodput (kB/sec)" + "," + str(data[10]) + "\n")
      f.write("Average Reply Delay (microseconds)" + "," + str(data[11]) + "\n")
      f.write("Average Echo Request Hop Count" + "," + str(data[12]) + "\n\n")
      
   for data in node2:
      
      f.write("Node2\n\n")    
      f.write("Echo Requests Sent" + "," + "Echo Requests Recieved" + "," + "Echo Replies Sent" + "," + "Echo Replies Recieved\n")
      f.write(str(data[0]) + ","+str(data[1]) + ","+str(data[2]) + ","+str(data[3]) + "\n")
      f.write("Echo Request Bytes sent (bytes)" + "," + "Echo Request Data Sent (bytes)\n")
      f.write(str(data[4])+","+str(data[5]) + "\n")
      f.write("Echo Request Bytes Recieved (bytes)" + "," + "Echo Request Data Recieved (bytes)\n")
      f.write(str(data[6]) + "," + str(data[7]))
      f.write("\n\n")
      f.write("Average RTT (miliseconds)" + "," + str(data[8]) + "\n")
      f.write("Echo Request Throughput (kB/sec)" + "," + str(data[9]) + "\n")
      f.write("Echo Request Goodput (kB/sec)" + "," + str(data[10]) + "\n")
      f.write("Average Reply Delay (microseconds)" + "," + str(data[11]) + "\n")
      f.write("Average Echo Request Hop Count" + "," + str(data[12]) + "\n")
   
   for data in node3:
      
      f.write("\nNode3\n\n")    
      f.write("Echo Requests Sent" + "," + "Echo Requests Recieved" + "," + "Echo Replies Sent" + "," + "Echo Replies Recieved\n")
      f.write(str(data[0]) + ","+str(data[1]) + ","+str(data[2]) + ","+str(data[3]) + "\n")
      f.write("Echo Request Bytes sent (bytes)" + "," + "Echo Request Data Sent (bytes)\n")
      f.write(str(data[4])+","+str(data[5]) + "\n")
      f.write("Echo Request Bytes Recieved (bytes)" + "," + "Echo Request Data Recieved (bytes)\n")
      f.write(str(data[6]) + "," + str(data[7]))
      f.write("\n\n")
      f.write("Average RTT (miliseconds)" + "," + str(data[8]) + "\n")
      f.write("Echo Request Throughput (kB/sec)" + "," + str(data[9]) + "\n")
      f.write("Echo Request Goodput (kB/sec)" + "," + str(data[10]) + "\n")
      f.write("Average Reply Delay (microseconds)" + "," + str(data[11]) + "\n")
      f.write("Average Echo Request Hop Count" + "," + str(data[12]) + "\n")
      
   for data in node4:
      
      f.write("\nNode4\n\n")    
      f.write("Echo Requests Sent" + "," + "Echo Requests Recieved" + "," + "Echo Replies Sent" + "," + "Echo Replies Recieved\n")
      f.write(str(data[0]) + ","+str(data[1]) + ","+str(data[2]) + ","+str(data[3]) + "\n")
      f.write("Echo Request Bytes sent (bytes)" + "," + "Echo Request Data Sent (bytes)\n")
      f.write(str(data[4])+","+str(data[5]) + "\n")
      f.write("Echo Request Bytes Recieved (bytes)" + "," + "Echo Request Data Recieved (bytes)\n")
      f.write(str(data[6]) + "," + str(data[7]))
      f.write("\n\n")
      f.write("Average RTT (miliseconds)" + "," + str(data[8]) + "\n")
      f.write("Echo Request Throughput (kB/sec)" + "," + str(data[9]) + "\n")
      f.write("Echo Request Goodput (kB/sec)" + "," + str(data[10]) + "\n")
      f.write("Average Reply Delay (microseconds)" + "," + str(data[11]) + "\n")
      f.write("Average Echo Request Hop Count" + "," + str(data[12]) + "\n")

         
def main():
   compute()
   
   print()
   read_data(f,L)
   data_size_metrics(L,"192.168.100.1",L5)
   
   read_data("Node2_filtered.txt",L2)
   data_size_metrics(L2,"192.168.100.2",L6)
   
   read_data("Node3_filtered.txt",L3)
   data_size_metrics(L3,"192.168.200.1",L7)
   
   read_data("Node4_filtered.txt",L4)
   data_size_metrics(L4,"192.168.200.2",L8)    
   
   output(L5,L6,L7,L8)
   
   
   compute()
   print("computing: Node1")
   read_data(f,L)
   data_size_metrics(L,"192.168.100.1",L5)
   print("-----------------------------------------------------")
   print("computing: Node2")
   read_data("Node2_filtered.txt",L2)
   data_size_metrics(L2,"192.168.100.2",L6)
   print("-----------------------------------------------------")
   print("computing: Node3")
   read_data("Node3_filtered.txt",L7)
   data_size_metrics(L3,"192.168.200.1",L7)
   print("-----------------------------------------------------")
   print("computing: Node4")
   read_data("Node4_filtered.txt",L8)
   data_size_metrics(L4,"192.168.200.2",L8)


output(L5,L6,L7,L8)

#UNCOMMENT TO MAKE IT WORK

#main()
