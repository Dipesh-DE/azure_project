# importing the multiprocessing module
import multiprocessing

def process_record(data):
    # processing
    processed_chunk = [record * 2 for record in data]
    print(processed_chunk)

if __name__ == "__main__":
    record_list = list(range(1,1000000))
    
    # creating process
    p1 = multiprocessing.Process(target=process_record, args=(record_list, ))

    # starting process
    p1.start()

    # wait until process is finished
    p1.join()
    
    # process finished
    print("Finished!")