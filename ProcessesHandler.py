## Defining my Processes header file
## easy to use Processes.methods

## Credits: elProfesor

import psutil

## return a list of all processes with:
## PID, name and started_time
## each object in this list is Process.object
## has his own methods .name(), .info() etc

def get_all_running_processes_linux():
    all_processes = []
    for proc in psutil.process_iter():
        all_processes.append(proc)
    return all_processes


## input process_name to search (string)
## input list of all processes
## return Process.object if True
## return False if the process specified is not Running

def search_for_a_process(search_ps_by_name, all_processes):
    for proc in all_processes:
        if search_ps_by_name == proc.name():
            return proc
    return False


## input a list with process_names to search
## input list with all_processes running
## if true returns a list with process found
## if return an empty list it means that none of processes found
## can iterate through return result and use methods of the class

def search_for_multi_processes(process_name_list, all_processes):
    found_procs = []
    for proc in all_processes:
        for proc_test in process_name_list:
            if proc_test == proc.name():
                found_procs.append(proc)
    return found_procs


## kill(terminate) the entire process
## input the process u want to kill

def kill_a_process(proc):
    proc.kill()

## just terminate the processe
## input the process u want to termiante

def terminate_a_process(proc):
    proc.terminate()
