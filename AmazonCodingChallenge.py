#Amazon 2D pathfinding coding challenge solution
#Author - Matthias Tan

from collections import namedtuple
import random
Tile = namedtuple('Tile', 'x y path_from_start obstacles_removed')
    
#Helper functions
def get_neighbours(x,y,size_x,size_y):
    neigh=[]
    for i in range(-1,2):
        for j in range(-1,2):
            if i==0 and j==0:
                continue
            if 0<=x+i<size_x and 0<=y+j<size_y:
                neigh.append((x+i,y+j))
    return neigh


def gen_ran_obs(random_obs,obstacle_list,size_x,size_y,start,end):
    coords=[(x,y) for x in range(0,size_x) for y in range (0,size_y)]
    coords =[coord for coord in coords if coord not in (obstacle_list+[start,end])]
    return random.sample(coords,random_obs)

def print_layout(layout):
    for row in layout:
        print(row)
        
def compute_sqdistance(points):
    sqdist=0
    for i in range(len(points)-1):
        sqdist+= ((points[i][0]-points[i+1][0])**2+(points[i][1]-points[i+1][1])**2)
    return sqdist

#Function to solve the path_finding problem
def path_find(obstacle_list,random_obs,size_x,size_y, start,end):
    #Initialise the map, create obstacles and print it
    layout=[['_'for j in range(size_x)] for i in range(size_y)]
    obstacles=gen_ran_obs(random_obs,obstacle_list,size_x,size_y,start,end)+obstacle_list
    layout[start[1]][start[0]]="S"
    layout[end[1]][end[0]]="E"
    #print("Obstacles at", obstacles)
    for obs in obstacles:
        layout[obs[1]][obs[0]]='O'
    print("Layout:")
    print_layout(layout)
    #start pathfinding from the starting location, add the starting tile to the updated queue
    visited={}
    updated=[Tile(start[0],start[1],[start],[])]
    while len(updated)!=0:
        t=updated.pop(0)
        #if this tile has been visited before compare the previous path with the current path.
        if ((t.x,t.y) in visited):
            prev=visited[(t.x,t.y)]
            #we do not want to keep the current path if either it has to remove more obstacles, or it takes longer or the same number of steps to reach it
            if len(t.obstacles_removed)>len(prev.obstacles_removed):
                continue
            elif len(t.obstacles_removed)==len(prev.obstacles_removed) and compute_sqdistance(t.path_from_start)>=compute_sqdistance(prev.path_from_start):
                continue
        #if the tile has not been visited before or we have found a better path to it, we keep it, and add all its neighbours.
        visited[(t.x,t.y)]=t
        neighbours=get_neighbours(t.x,t.y,size_x,size_y)
        for neighbour in neighbours:
            x,y=neighbour[0],neighbour[1]
            neighbour_tile=Tile(x,y,t.path_from_start+[(x,y)], t.obstacles_removed+[(x,y)] if (x,y) in obstacles else t.obstacles_removed)
            updated.append(neighbour_tile)
    
    #print the path to the goal.
    destination=visited[(end[0],end[1])]
    if len(destination.obstacles_removed)>0:
        print("Unable to reach delivery point. Fewest obstacles to remove is ", len(destination.obstacles_removed), "at ", destination.obstacles_removed)

    for point in destination.path_from_start:
        if (point[0],point[1])==start or (point[0],point[1])==end:
            continue
        elif point in destination.obstacles_removed:
            layout[point[1]][point[0]]="R"
        else:
            layout[point[1]][point[0]]="P"

    print("Shortest path to goal:", destination.path_from_start)
    print_layout(layout)

    #Commands to print out paths to all squares.
    #print("Number of checked tiles= ",len(visited), "Should equal ", size_x*size_y)
    #print("Shortest paths to all other squares")
    #for k in visited:
    #print (visited[k])

if(__name__=="__main__"):
    print("Output from phase 1")
    path_find([(9,7),(8,7),(7,7),(7,8)],0,10,10,(0,0),(9,9))
    print("Output from phase 2")
    path_find([(9,7),(8,7),(7,7),(7,8)],20,10,10,(0,0),(9,9))
    print("Output from extra test case. 12x14 rectangle, 50 random obstacles, start at (1,6), end at (9,4)")
    path_find([],50,12,14,(1,3),(9,10))
    print("Output from extra test case. 9x9 rectangle, 50 random obstacles, start at (0,4), end at (7,2)")
    path_find([],50,9,9,(0,4),(7,2))
    