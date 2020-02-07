class MappingAdapter:
    def __init__(self, adaptee):
        self.adaptee = adaptee

    def get_objects_grid(self, desc, grid):
        res= []
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == desc:
                    res.append((j, i))
        return res

    def lighten(self, grid):
        dim = (len(grid[0]), len(grid))
        self.adaptee.set_dim(dim)
        lights = self.get_objects_grid(1, grid)
        obstacles = self.get_objects_grid(-1, grid)
        self.adaptee.set_lights(lights)
        self.adaptee.set_obstacles(obstacles)
        return self.adaptee.generate_lights()
