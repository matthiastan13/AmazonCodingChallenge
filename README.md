# Solution to Amazon coding challenge - 2D Pathfinding

Author - Matthias Tan

Email - firstname.lastname13@gmail.com

## Problem

Given a 2-D grid, a starting point, a destination, and obstacles scattered accross the 2-D grid, find a path to navigate a robot from the starting point to the destination. The robot can move 1 square in each direction, including diagonally. If the destination cannot be reached, find the minimum number of obstacles that need to be removed to get there, and provide the path.

## Comments

This implementation is more general than the one requested in the solution specification.

- It allows rectangular grids of any size instead of a fixed 10x10 square
- It allows the start and end squares to be anywhere, as opposed to being on opposite corners
- It finds the shortest path as measured by squared euclidean distance, not just any path
- It completes the bonus section, where the fewest number of obstacles needed to be removed (if necessary) are found, and the path found is still the shortest.

## Data Structure

Every square in the grid is represented by a named-tuple called a **Tile** with the following fields

- x: x coordinate
- y: y coordinate
- path_from_start: a list of co-ordinate tuples containing a path from the starting square to the present tile (when the function is complete, it will contain the shortest path)
- obstacles_removed: a list of co-ordinate tuples containing the obstacles removed (if any) that are necessary in order to reach this tile, it will also include the coordinates of this tile if itself is an obstacle.

## Algorithm

1. Initialise a "visited" empty dictionary and an "updated" queue. Put the starting tile into the updated queue. The tile will contain its x and y coordinates, path_from start will be a list containing a tuple of its co-ordinates, obstacles_removed will be an empty list.
2. While the updated queue is not empty:
   - dequeue a tile.
   - if the tile has not been visited before:
     - add it to the visited dictionary (the key will be the tuple of its co-ordinates)
     - add all its neighbours tiles to the updated queue. The neighhbour tile will have its x and y coordinates, path_from start will be path_from_start of the dequeued tile with its own tuple of coordinates appended. obstacles_removed will be obstacles_removed from the dequeued tile with its own tuple of coordinates appended if it is an obstacle
   - if the tile has been visited before
     - if obstacles_removed of the tile from the visited dictionary has more obstacles than our newly found path or if they have the same number of obstacles but the path_from_start to the tile is longer than our newly found path by measure of squared euclidean distance, then we will replace the entry for this tile in the visited dictionary with this entry containing either a shorter obstacles_removed or an equal obstacles_removed but shorter path_from_start.

## Instructions

Execute `path_find(obstacle_list,random_obs,size_x,size_y,start,end)` to run the program.

- obstacle_list is a list of tuples containing the coordinates of obstacles you wish to set
- random obs is an integer, which will generate an additional number of random obstacles not on the start square, end square or obstacle_list
- size_x is the length of the grid
- size_y is the height of the grid
- start is the starting coordinate
- end is the ending coordinate

## Description of graphical output

The program will first print the initial layout. Then it will print the path and the layout with the path from the start to the destination. If there is no valid path, it will print out the fewest number of obstacles to be removed and their coordinates and it will print out the path and the layout with the path and obstacle(s) removed

Legend:

- **S** starting square
- **E** ending square
- **\_** floor tile
- **O** obstacle
- **P** path
- **R** obstacle which has been removed

## Sample output

### Phase 1

Corresponds to calling the `path_find` with these parameters `path_find([(9,7),(8,7),(7,7),(7,8)],0,10,10,(0,0),(9,9))`.

The output is the following.

```{text}
Layout:
['S', '_', '_', '_', '_', '_', '_', '_', '_', '_']
['_', '_', '_', '_', '_', '_', '_', '_', '_', '_']
['_', '_', '_', '_', '_', '_', '_', '_', '_', '_']
['_', '_', '_', '_', '_', '_', '_', '_', '_', '_']
['_', '_', '_', '_', '_', '_', '_', '_', '_', '_']
['_', '_', '_', '_', '_', '_', '_', '_', '_', '_']
['_', '_', '_', '_', '_', '_', '_', '_', '_', '_']
['_', '_', '_', '_', '_', '_', '_', 'O', 'O', 'O']
['_', '_', '_', '_', '_', '_', '_', 'O', '_', '_']
['_', '_', '_', '_', '_', '_', '_', '_', '_', 'E']
Shortest path to goal: [(0, 0), (0, 1), (0, 2), (1, 3), (2, 4), (3, 5), (4, 6), (5, 7), (6, 8), (7, 9), (8, 9), (9, 9)]
['S', '_', '_', '_', '_', '_', '_', '_', '_', '_']
['P', '_', '_', '_', '_', '_', '_', '_', '_', '_']
['P', '_', '_', '_', '_', '_', '_', '_', '_', '_']
['_', 'P', '_', '_', '_', '_', '_', '_', '_', '_']
['_', '_', 'P', '_', '_', '_', '_', '_', '_', '_']
['_', '_', '_', 'P', '_', '_', '_', '_', '_', '_']
['_', '_', '_', '_', 'P', '_', '_', '_', '_', '_']
['_', '_', '_', '_', '_', 'P', '_', 'O', 'O', 'O']
['_', '_', '_', '_', '_', '_', 'P', 'O', '_', '_']
['_', '_', '_', '_', '_', '_', '_', 'P', 'P', 'E']
```

### Phase 2

Corresponds to calling the `path_find` with these parameters `path_find([(9,7),(8,7),(7,7),(7,8)],20,10,10,(0,0),(9,9))`.

Some randomly generated outputs.

```{text}

Layout:
['S', '_', '_', '_', '_', 'O', 'O', '_', '_', '_']
['_', '_', '_', '_', '_', '_', 'O', '_', '_', '_']
['_', '_', 'O', '_', '_', '_', '_', '_', '_', 'O']
['_', '_', '_', '_', '_', 'O', '_', '_', '_', '_']
['O', '_', '_', '_', '_', '_', '_', '_', 'O', '_']
['_', '_', '_', '_', 'O', '_', '_', '_', '_', 'O']
['_', '_', '_', 'O', '_', 'O', '_', 'O', '_', '_']
['_', '_', '_', '_', 'O', '_', 'O', 'O', 'O', 'O']
['_', '_', '_', '_', 'O', 'O', 'O', 'O', '_', '_']
['_', '_', '_', 'O', '_', '_', '_', 'O', '_', 'E']
Unable to reach delivery point. Fewest obstacles to remove is 1 at [(7, 7)]
Shortest path to goal: [(0, 0), (0, 1), (1, 2), (2, 3), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9)]
['S', '_', '_', '_', '_', 'O', 'O', '_', '_', '_']
['P', '_', '_', '_', '_', '_', 'O', '_', '_', '_']
['_', 'P', 'O', '_', '_', '_', '_', '_', '_', 'O']
['_', '_', 'P', 'P', '_', 'O', '_', '_', '_', '_']
['O', '_', '_', '_', 'P', '_', '_', '_', 'O', '_']
['_', '_', '_', '_', 'O', 'P', '_', '_', '_', 'O']
['_', '_', '_', 'O', '_', 'O', 'P', 'O', '_', '_']
['_', '_', '_', '_', 'O', '_', 'O', 'R', 'O', 'O']
['_', '_', '_', '_', 'O', 'O', 'O', 'O', 'P', '_']
['_', '_', '_', 'O', '_', '_', '_', 'O', '_', 'E']
```

Another example output

```{text}

Layout:
['S', 'O', '_', 'O', '_', '_', '_', '_', '_', '_']
['_', 'O', '_', 'O', '_', '_', '_', '_', 'O', '_']
['O', 'O', '_', 'O', '_', '_', '_', '_', '_', '_']
['_', '_', 'O', 'O', 'O', '_', '_', '_', '_', '_']
['_', '_', '_', '_', '_', '_', 'O', '_', '_', '_']
['_', 'O', '_', '_', '_', '_', '_', '_', 'O', '_']
['O', '_', '_', '_', '_', '_', '_', '_', '_', '_']
['_', '_', 'O', '_', '_', '_', '_', 'O', 'O', 'O']
['_', '_', '_', '_', '_', 'O', '_', 'O', 'O', '_']
['O', '_', '_', '_', '_', '_', 'O', '_', '_', 'E']
Unable to reach delivery point. Fewest obstacles to remove is  1 at  [(0, 2)]
Shortest path to goal: [(0, 0), (0, 1), (0, 2), (1, 3), (2, 4), (3, 5), (4, 6), (5, 7), (6, 8), (7, 9), (8, 9), (9, 9)]
['S', 'O', '_', 'O', '_', '_', '_', '_', '_', '_']
['P', 'O', '_', 'O', '_', '_', '_', '_', 'O', '_']
['R', 'O', '_', 'O', '_', '_', '_', '_', '_', '_']
['_', 'P', 'O', 'O', 'O', '_', '_', '_', '_', '_']
['_', '_', 'P', '_', '_', '_', 'O', '_', '_', '_']
['_', 'O', '_', 'P', '_', '_', '_', '_', 'O', '_']
['O', '_', '_', '_', 'P', '_', '_', '_', '_', '_']
['_', '_', 'O', '_', '_', 'P', '_', 'O', 'O', 'O']
['_', '_', '_', '_', '_', 'O', 'P', 'O', 'O', '_']
['O', '_', '_', '_', '_', '_', 'O', 'P', 'P', 'E']
```

Yet another example

```{text}

Layout:
['S', '_', '_', 'O', '_', '_', '_', '_', '_', 'O']
['_', '_', '_', '_', '_', '_', '_', '_', '_', '_']
['_', '_', 'O', '_', '_', '_', '_', 'O', '_', '_']
['_', '_', 'O', 'O', '_', '_', '_', '_', '_', '_']
['_', '_', '_', '_', '_', '_', '_', '_', '_', '_']
['O', 'O', 'O', '_', '_', '_', '_', '_', '_', 'O']
['O', '_', '_', '_', '_', 'O', 'O', '_', '_', 'O']
['_', '_', '_', 'O', '_', 'O', '_', 'O', 'O', 'O']
['_', '_', '_', 'O', '_', '_', 'O', 'O', '_', 'O']
['_', '_', 'O', '_', '_', '_', '_', '_', '_', 'E']
Shortest path to goal: [(0, 0), (0, 1), (0, 2), (1, 3), (2, 4), (3, 5), (3, 6), (4, 7), (5, 8), (6, 9), (7, 9), (8, 9), (9, 9)]
['S', '_', '_', 'O', '_', '_', '_', '_', '_', 'O']
['P', '_', '_', '_', '_', '_', '_', '_', '_', '_']
['P', '_', 'O', '_', '_', '_', '_', 'O', '_', '_']
['_', 'P', 'O', 'O', '_', '_', '_', '_', '_', '_']
['_', '_', 'P', '_', '_', '_', '_', '_', '_', '_']
['O', 'O', 'O', 'P', '_', '_', '_', '_', '_', 'O']
['O', '_', '_', 'P', '_', 'O', 'O', '_', '_', 'O']
['_', '_', '_', 'O', 'P', 'O', '_', 'O', 'O', 'O']
['_', '_', '_', 'O', '_', 'P', 'O', 'O', '_', 'O']
['_', '_', 'O', '_', '_', '_', 'P', 'P', 'P', 'E']
```

### Extra test cases with different sized grids and different number of obstacles

12x14 rectangle, 50 random obstacles, start at (2,13), end at (11,0)

`path_find([],50,12,14,(2,13),(11,0))`

```{text
}

Layout:
['_', '_', '_', 'O', '_', '_', '_', '_', '_', 'O', '_', 'E']
['_', 'O', 'O', '_', '_', '_', 'O', '_', '_', '_', 'O', '_']
['O', '_', 'O', 'O', '_', '_', '_', '_', '_', '_', 'O', '_']
['_', '_', 'O', '_', '_', '_', 'O', 'O', 'O', 'O', '_', '_']
['_', '_', '_', '_', '_', '_', 'O', 'O', 'O', '_', 'O', 'O']
['_', 'O', '_', '_', 'O', '_', '_', 'O', 'O', '_', '_', 'O']
['_', '_', '_', '_', '_', 'O', '_', 'O', 'O', '_', '_', '_']
['_', '_', '_', '_', '_', '_', 'O', '_', 'O', 'O', '_', '_']
['_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_']
['_', '_', 'O', '_', 'O', '_', '_', '_', '_', '_', '_', 'O']
['O', 'O', '_', '_', '_', 'O', '_', '_', '_', '_', '_', 'O']
['_', 'O', '_', '_', 'O', 'O', '_', '_', 'O', 'O', '_', '_']
['_', 'O', '_', '_', 'O', '_', '_', '_', '_', '_', '_', 'O']
['_', '_', 'S', '_', '_', '_', '_', 'O', '_', 'O', 'O', 'O']
Shortest path to goal: [(2, 13), (2, 12), (2, 11), (2, 10), (3, 9), (3, 8), (3, 7), (3, 6), (3, 5), (4, 4), (5, 3), (6, 2), (7, 1), (8, 1), (9, 1), (10, 0), (11, 0)]
['_', '_', '_', 'O', '_', '_', '_', '_', '_', 'O', 'P', 'E']
['_', 'O', 'O', '_', '_', '_', 'O', 'P', 'P', 'P', 'O', '_']
['O', '_', 'O', 'O', '_', '_', 'P', '_', '_', '_', 'O', '_']
['_', '_', 'O', '_', '_', 'P', 'O', 'O', 'O', 'O', '_', '_']
['_', '_', '_', '_', 'P', '_', 'O', 'O', 'O', '_', 'O', 'O']
['_', 'O', '_', 'P', 'O', '_', '_', 'O', 'O', '_', '_', 'O']
['_', '_', '_', 'P', '_', 'O', '_', 'O', 'O', '_', '_', '_']
['_', '_', '_', 'P', '_', '_', 'O', '_', 'O', 'O', '_', '_']
['_', '_', '_', 'P', '_', '_', '_', '_', '_', '_', '_', '_']
['_', '_', 'O', 'P', 'O', '_', '_', '_', '_', '_', '_', 'O']
['O', 'O', 'P', '_', '_', 'O', '_', '_', '_', '_', '_', 'O']
['_', 'O', 'P', '_', 'O', 'O', '_', '_', 'O', 'O', '_', '_']
['_', 'O', 'P', '_', 'O', '_', '_', '_', '_', '_', '_', 'O']
['_', '_', 'S', '_', '_', '_', '_', 'O', '_', 'O', 'O', 'O']
```

9x9 rectangle, 50 random obstacles, start at (0,4), end at (7,2)

`path_find([],50,9,9,(0,4),(7,2))`

```{text}

Layout:
['O', 'O', 'O', '_', '_', 'O', 'O', 'O', 'O']
['_', 'O', '_', 'O', '_', 'O', 'O', 'O', 'O']
['_', 'O', 'O', '_', 'O', 'O', 'O', 'E', '_']
['_', '_', '_', 'O', 'O', 'O', 'O', '_', 'O']
['S', '_', 'O', 'O', '_', '_', 'O', '_', 'O']
['_', 'O', 'O', '_', '_', 'O', 'O', 'O', 'O']
['O', 'O', 'O', 'O', 'O', '_', 'O', '_', 'O']
['O', 'O', 'O', 'O', '_', '_', 'O', '_', 'O']
['O', '_', '_', 'O', '_', 'O', 'O', '_', '_']
Unable to reach delivery point. Fewest obstacles to remove is  2 at  [(5, 1), (6, 1)]
Shortest path to goal: [(0, 4), (1, 3), (2, 3), (3, 2), (4, 1), (5, 1), (6, 1), (7, 2)]
['O', 'O', 'O', '_', '_', 'O', 'O', 'O', 'O']
['_', 'O', '_', 'O', 'P', 'R', 'R', 'O', 'O']
['_', 'O', 'O', 'P', 'O', 'O', 'O', 'E', '_']
['_', 'P', 'P', 'O', 'O', 'O', 'O', '_', 'O']
['S', '_', 'O', 'O', '_', '_', 'O', '_', 'O']
['_', 'O', 'O', '_', '_', 'O', 'O', 'O', 'O']
['O', 'O', 'O', 'O', 'O', '_', 'O', '_', 'O']
['O', 'O', 'O', 'O', '_', '_', 'O', '_', 'O']
['O', '_', '_', 'O', '_', 'O', 'O', '_', '_']
```
