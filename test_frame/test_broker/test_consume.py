import time
import random
from function_scheduling_distributed_framework import task_deco,BrokerEnum

@task_deco('test_queue66',broker_kind=BrokerEnum.REDIS,qps=3,log_level=10,is_print_detail_exception=False,is_show_message_get_from_broker=False,
           is_using_distributed_frequency_control=True)
def f(x,y):
    # time.sleep(10)
    print(f''' {x} + {y} = {x + y}''')
    return x + y


if __name__ == '__main__':
    # f.consume()
    f.multi_process_consume(2)





















