from canvas import Canvas
from node import Node
from shape import Shape
from typing import Tuple, List, Callable, Any
import time
import copy

def measure_time(func: Callable[..., Any], *args: Tuple[Any], **kwargs: Any) -> Tuple[ any, float]:
    start_time = time.time()
    result = func(*args, **kwargs)
    end_time = time.time()
    running_time = end_time - start_time
    return result, running_time

def main():
                    #  Y X
    my_canvas = Canvas(6,6, [])

    s1 = Shape('Y')
    s1.rotate_shape(5)
    s2 = Shape('T')
    my_canvas.place_shape(s1,(0,1))
    my_canvas.place_shape(s2,(2,0))
    print(my_canvas.calculate_parimeter_of_shapes([s1, s2]))
    print(my_canvas.get_matrix())
    #print(s1.get_coords_list())
    #print(my_canvas.calculate_parameter_of_shape(s1))
    #print(my_canvas.count_filled_cells())
    #print(my_canvas.get_all_available_positions())

    #print(s1==s2)

    #s1.rotate_shape(1)
    # print(my_canvas.get_all_non_available_positions(s1))
    # my_canvas.place_shape(s1,(1,0))
    # print(my_canvas.get_matrix())
    #res, time = measure_time(my_canvas.get_all_available_positions, s1)
    #print(time)
    # # man = manipullator()
    # # result1 = my_canvas.count_filled_cells()
    # # #print("Filled Cells" ,result1)
    # # result2 = my_canvas.count_empty_cells()
    # # #print("Empty Cells",result2)
    # # result3 = my_canvas.count_holes()
    # # #print("Hole Cells",result3)
    #s1 = Shape('F')
    # s2 = Shape('N')
    # # s3 = Shape('T')
    #
    #
    # #rotate s1 with manipulator
    # #man.rotate_shape(s1,0)
    # #print cords of s1
    # #print(s1.get_coords_list())
    #pos1 = (6,6)
    # pos2 = (2,2)
    # #Shape.change_cords_by_a_position(s1,pos)
    # #print(s1.get_coords_list())
    #
    # print(my_canvas.check_for_out_of_bounds_when_placed_in(s1,pos1))                                    # Y X
    # my_canvas.place_shape(s1,pos1)
    # # my_canvas.place_shape(s2, pos2)
    # print(my_canvas.get_matrix())
    # n = Node((1,2),"F")
    # print(n.get_coords())
    # n.set_coords((3,4))
    # print(n.get_coords())
    # s1 = Shape('F')
    # print(s1.get_coords_list())
    # s1.change_cords_by_a_position((1,1))
    # print(s1.get_coords_list())



main()