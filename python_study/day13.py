from random import randint
from time import time, sleep
from multiprocessing import Process
from threading import Thread, Lock
from os import getpid

def download_task(filename):
    print('start process which pid is [%d].' % getpid())
    print('downloading %s ...' % filename)
    use_time = randint(5, 10)
    sleep(use_time)
    print('%s downloads which spent %s seconds' % (filename, use_time))

class DownloadTask(Thread):
    def __init__(self, filename):
        super().__init__()
        self._filename = filename
    def run(self):
        print('start process ...')
        print('downloading %s...' % self._filename)
        use_time = randint(5, 10)
        sleep(use_time)
        print('%s downloads which spent %s seconds' % (self._filename, use_time))

class Account(object):
    def __init__(self, balance=0):
        self._balance = balance
        self._lock = Lock()
    def deposit(self, money):
        self._lock.acquire()  # 获取锁
        try:
            new_balance = self._balance + money
            sleep(0.01)
            self._balance = new_balance  # 一共有两个元操作
        finally:
            self._lock.release()  # 解锁
    @property
    def balance(self):
        return self._balance

class AddMoneyThread(Thread):
    def __init__(self, account, money):  # account是一个对象
        super().__init__()
        self._account = account
        self._money = money
    def run(self):
        self._account.deposit(self._money)


def main():
    """
    start = time()
    p1 = Process(target=download_task, args=('file1', ))  #args里填函数需要的参数
    p1.start()
    p2 = Process(target=download_task, args=('file2', ))
    p2.start()
    p1.join()
    p2.join()
    end = time()
    print('it cost %.2f seconds.' % (end - start))

    start_thread = time()
    t1 = DownloadTask('Thread_file_one')
    t1.start()
    t2 = DownloadTask('Thread_file_sec')
    t2.start()
    t1.join()
    t2.join()
    end_thread = time()
    print('it cost %.2f seconds.' % (end_thread - start_thread))
    """
    account = Account()
    threads = []
    for _ in range(100):
        t = AddMoneyThread(account, 1)
        threads.append(t)
        t.start()
    for t in threads:
        t.join()
    print('the balance of the account is %d yuan.' % account.balance)

if __name__ == '__main__':
    main()
