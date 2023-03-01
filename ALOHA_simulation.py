
import random 
import matplotlib.pyplot as  plt 

def send_time (transmistions,b,fail):
  
    transmistion_time =[]
    
    for i in range (transmistions-fail):
        transmistion_time.append(random.randint(0, b))
        
    for i in range (fail):# fail will wait random time unit before retransmitting 
        transmistion_time.append(random.randint(0, b)+ random.randint(0, 5))
    return transmistion_time


def check_collision (transmistion_list):
    counts = []
    for i in range (len(transmistion_list)):
        counts.append(transmistion_list.count(transmistion_list[i])) 
    success = counts.count(1)
    fail = len(counts)- success
    return success , fail 


def check_active_nodes (total_nodes,fail,lembda):#return number of active nodes
    maximum = total_nodes - fail # maximum number of nodes that can be active 
    active = 1
    for i in range (maximum):
        if round(random.random(),2) <=  round(lembda,2) :
            active += 1

    return active
    
def simulate (N,lembda ,num_time_slots):

    total_transmitions = 0 
    maximum_sending_time = round( N /4)
    
    
    active_nodes = check_active_nodes (N,0,lembda)
    transmistion_time = send_time (active_nodes,maximum_sending_time,0) 
    success , fail   = check_collision (transmistion_time)
    
    total_transmitions += success + fail 
    total_success = success
        
    
    
  
   
    for i in range (num_time_slots):
        
        print("Time slot check ",i+1,"\n")
        print(transmistion_time)
        print("\n#success = ",success ," , #fail = ", fail  )
        
        active_nodes = check_active_nodes (N,fail,lembda)
        print(active_nodes ," New nodes want to send ")
        transmistion_time = send_time (active_nodes + fail ,maximum_sending_time,fail)
        success , fail   = check_collision (transmistion_time)
        total_transmitions += success + fail 
        total_success += success
        print("-"*50)
        
        
        
      
        
    print("Total transmistions :",total_transmitions)
    print("Total success : ",total_success)
    print("Probability of success: ",round( total_success/total_transmitions,3))
   

if __name__ == '__main__':
    
    N = 50
    lembda = 0.2
    num_time_slots = 50
    simulate (N,lembda ,num_time_slots)
        
    