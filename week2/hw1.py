import numpy as np, numpy
import time
import sys
# import matplotlib.pyplot as plt

if (len(sys.argv) != 2):
    print("usage: python %s N" % sys.argv[0])
    quit()

### 行列積
n = int(sys.argv[1])
a = np.array([[n,n,n],[n,n,n],[n,n,n]])
b = np.array([[n,n,n],[n,n,n],[n,n,n]])

begin = time.time()       # 実行時間の測定開始
c = np.dot(a,b)
end = time.time()         # 実行時間の測定終了
print(c)

time = end - begin
print("time: %.6f sec" % time)

