import heapq
from point import Point


def manhattan_distance(x1, y1, x2, y2):
    """Calculate Manhattan distance between two points."""
    return abs(x1 - x2) + abs(y1 - y2)


def find_target_position(components, target):
    """Find the position of the target symbol on the board."""
    board = components.board
    for y in range(len(board)):
        for x in range(len(board[y])):
            if board[y][x] == target:
                return (x, y)
    return None


def a_star(components, target, safe):
    you_x = components.head['x']
    you_y = components.head['y']
    
    target_pos = find_target_position(components, target)
    if target_pos is None:
        return []
    
    target_x, target_y = target_pos
    
    start_point = Point(components, you_x, you_y, safe, 
                       g_score=0, 
                       h_score=manhattan_distance(you_x, you_y, target_x, target_y))
    
    _open = [start_point]
    heapq.heapify(_open)
    closed = set()
    
    open_dict = {(you_x, you_y): start_point}

    while _open:
        current = heapq.heappop(_open)
        current_pos = (current.x, current.y)
        
        if current_pos in open_dict:
            del open_dict[current_pos]
        
        if current.get_symbol() == target:
            return current.get_move()
        
        closed.add(current_pos)
        
        neighbours = current.get_neighbours(target_x, target_y)
        for neighbour in neighbours:
            neighbour_pos = (neighbour.x, neighbour.y)
            
            if neighbour_pos in closed:
                continue
            
            if neighbour_pos in open_dict:
                existing = open_dict[neighbour_pos]
                if neighbour.g_score < existing.g_score:
                    _open.remove(existing)
                    heapq.heapify(_open)
                    heapq.heappush(_open, neighbour)
                    open_dict[neighbour_pos] = neighbour
            else:
                heapq.heappush(_open, neighbour)
                open_dict[neighbour_pos] = neighbour
    
    return []


def get_food(components, safe=['F', '.', 'T', 't']):
    print("GET FOOD")
    return a_star(components, 'F', safe)


def chase_tail(components, safe=['F', '.', 'T']):
    print("CHASE TAIL")
    return a_star(components, 'T', safe)
