# python Clustering.py numberOfClusters file.txt\
import sys
import time

def main():
    start_time = time.time()
    # file input -> read the 2d points
    points = list()
#    with(sys.argv[1]) as file:
#        for line in file:
#            line = line.sp
#            lit(' ')
#            x = line[0]
#            y = line[1]
#            points.append(Point(x, y))
            # display graph -> verify read correctly

            # cluster until optimal
            # cluster forms k groups, each of which
            # display clustered graph
            # when the results don't change, it is done
    print ("End")
    print ("Time taken: " + str(time.time() - start_time) + ' s')

main()


def Point(x,y):
    Point.x = x
    Point.y = y
