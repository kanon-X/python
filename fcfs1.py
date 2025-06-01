def fcfs():
    N_process = int(input("Enter number of processes: "))
    brust_time= [] * N_process
    turnArroundTime = [0] * N_process
    WaitingTime = [0] * N_process
    
    for i in range(0,N_process):
        bt = int(input(f"Enter the process {i+1} : "))
        brust_time.append(bt)
    # calculating waiting time :
    for i in range(1,N_process):
        WaitingTime[i] = WaitingTime[i-1] + brust_time[i-1]
    # calculating turnArround Time:
    for i in range(0,N_process):
        turnArroundTime[i] = WaitingTime[i] + brust_time[i]
        avg_waiting_Time = sum(WaitingTime)/N_process
        avg_Time_arround_time = sum(turnArroundTime)/N_process 
        
    # calculating grantt chart:
    print(f" N.Proc. | B.T. | W.T. | T.A.T. |")
    print("----------------------------------")
    for i in range(0,N_process):
        print(f"{i+1} | {brust_time[i]} | {WaitingTime[i]} | {turnArroundTime[i]} |")
        print("------------------------------")
    print(f"avg waiting time : {avg_waiting_Time:.2f}")
    print(f"avg turn arround time : {avg_Time_arround_time:.2f}")
# output/function calling:
fcfs()
