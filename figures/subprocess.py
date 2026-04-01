from multiprocessing import Process, Queue

def subprocess(
  queue: Queue()
):
  
  while True:
    # waits until data available in queue
    data = queue.get()
    
    # process data
    process(data)

def main():
    # message passing queue
    queue = Queue()

    subprocess = Process(
      target=subprocess, 
      args=(queue,)
    )
    subprocess.start()

    # trigger subprocess
    data = analyze()
    queue.put(data)
   

    
