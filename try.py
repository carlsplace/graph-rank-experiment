# coding:utf-8

output = [['increment', 'quantil', 1.0, 0.0, 0.0, 1501.8020277777268], 
          ['estim', 'quantil', 1.0, 0.891659080982, 0.0, 1254.121972541718], 
          ['estim', 'massiv', 1.0, 0.0, 0.0, 1092.1359180938769], 
          ['massiv', 'track', 1.0, 0.0, 0.0, 1443.5186982349112]]

import csv

with open('./test_csv.csv', 'w') as file:
    table = csv.writer(file)
    table.writerows(output)