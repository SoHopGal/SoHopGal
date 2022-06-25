#################################################################################
# Queue session.                                               Date: 25/06/2022 #
# This algorithm is open source.                                                #
# In this file there is example question for using queue data stracture.        #
# Written by Gal Argov Sofer for 9th Grade (KITA TET) exam in Handasaim School. #
#################################################################################


import queue

# Ex 1 - Sort elements from q1 in q2 (lower to upper)
q1 = queue.Queue()
q2 = queue.Queue()
  
q1.put(11)
q1.put(5)
q1.put(3)
q1.put(2)
q1.put(9)

print("Queue 1:", end = " ")

while (q1.empty() == False):
    print(q1.queue[0], end = " ")
    q2.put(q1.get())
    
n = q2.qsize()

for i in range(n):
    x = q2.get()
    for j in range(n - 1):
        y = q2.get()
        if x > y:
            q2.put(y)
        else:
            q2.put(x)
            x = y
    q2.put(x)

print()
print("Queue 2:", end = " ")

while (q2.empty() == False):
    print(q2.queue[0], end = " ")
    q2.get()


# EOF