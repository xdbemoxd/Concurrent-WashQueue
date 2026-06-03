import threading
import time
import numpy as np
from scipy.stats import poisson, norm, expon, uniform

lock_1 = threading.Semaphore(1);
lock_2 = threading.Semaphore(1);
lock_3 = threading.Semaphore(1);

def car_wahs(id_car):

    lock_1.acquire();
    
    t_a = norm.rvs( loc = 10, scale = 2 );
    print( f"the car {id_car} is in the lock_1 with on time {t_a}" );
    time.sleep( t_a );
    
    lock_1.release();

    lock_2.acquire();
        
    t_b = expon.rvs( scale = 12 );
    print( f"the car {id_car} is in the lock_2 with on time {t_b}" );
    time.sleep( t_b );

    lock_2.release();
    
    lock_3.acquire();
    
    t_c = uniform.rvs( loc = 8, scale = 4 );
    print( f"the car {id_car} is in the lock_3 with on time {t_c}" );
    time.sleep( t_c );

    lock_3.release();

def num_cars( current_hour ):

    lambda_poisson = 10;

    arrivals = poisson.rvs( mu = lambda_poisson ); 

    print( "amount of cars at the current hour ", arrivals )

    threads = []

    for i in range( arrivals ):
        car_id = f"H{current_hour}-C{i+1}"
        threads.append( threading.Thread( target=car_wahs, args=(car_id,) ) );
        threads[-1].start();
    
    for t in threads:
        t.join();

def main():
    hours_count = 8;
    current_hour = 0

    while hours_count > current_hour:

        num_cars(current_hour);
    
        current_hour+=1;

    
init = time.perf_counter();

main();

final = time.perf_counter();

print( final - init );
print( threading.active_count() );
print( threading.enumerate() )