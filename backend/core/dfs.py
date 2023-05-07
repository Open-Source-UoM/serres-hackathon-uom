from shape import Shape
import networkx as nx
class Dfs():
    def __init__(self, shapes: List[Shape], holes: List[Tuple[int, int]], dimensions: Tuple[int, int]):
        self.shapes: List[Shape] = shapes
        self.holes: List[Tuple[int, int]] = holes
        self.dimensions: Tuple[int, int] = dimensions
        self.tree: nx.Graph = nx.Graph()

class Node:
    shapes_that_must_be_used = ["W", "T", "Y", "U", "P", "F", "L", "Z", "X", "V", "N"]

    def init(self, parent, canvas):
        # List[Node]

        self.parent = parent
        if (parent == None):
            self.canvas = canvas
        else:
            self.canvas = parent.canvas

        self.children = []

    def generate_children(self) -> Tuple[Shape, Tuple[int, int]]:
        # get random shape
        available_shapes = copy.deepcopy(self.shapes_that_must_be_used)
        shape_letter = random.choice(self.shapes_that_must_be_used)
        shape = Shape(shape_letter)

        print(self.shapes_that_must_be_used)

        # get random position from available ones
        possible_coords = self.canvas.get_available_positions_for_shape(shape)
        # selected_coords = random.choice(possible_coords)
        # if there isn't one available i will change the shape till i find one that can fit
        # if i cant find i gotta switch the coords i choose
        #  return the first shape that fits somewhere

        #         the available positions already considers that the shape can be placed in these
        available_shapes.remove(shape)
        while len(possible_coords) == 0:
            shape_letter = random.choice(available_shapes)
            shape = Shape(shape_letter)
            available_shapes.remove(shape)
            possible_coords = self.canvas.get_available_positions_for_shape(shape)

        selected_coords = random.choice(possible_coords)
        self.shapes_that_must_be_used.remove(shape)

        return shape, selected_coords

        pass


def is_solution(current):
    pass

def run():
    x, y = 15, 15
    root = Node(None, Canvas(15, 15, []))
    frontier = [root]
    solutions = []
    while len(frontier) > 0:
        current = frontier.pop()
        if(is_solution(current)):
             solutions.append(current)
        shape_to_place,position = current.generate_children()
        current.canvas.place_shape_checked(shape_to_place,position)
        frontier.push(Node(current))
    pass
run()