from __future__ import annotations
from dataclasses import dataclass, field
from heapq import heappush, heappop
from typing import List, Tuple, Dict, Optional, Set
import math


@dataclass(order=True)
class PriorityNode:
    priority: float
    node: "Node" = field(compare=False)


@dataclass(frozen=True)
class Node:
    x: int
    y: int


class AStar:
    def __init__(self, grid: List[List[int]], allow_diagonal: bool = True):
        """
        grid:
            0 = walkable
            1 = obstacle
        """
        self.grid = grid
        self.rows = len(grid)
        self.cols = len(grid[0])
        self.allow_diagonal = allow_diagonal

    def heuristic(self, a: Node, b: Node) -> float:
        return math.sqrt((a.x - b.x) ** 2 + (a.y - b.y) ** 2)

    def in_bounds(self, node: Node) -> bool:
        return 0 <= node.x < self.rows and 0 <= node.y < self.cols

    def is_walkable(self, node: Node) -> bool:
        return self.grid[node.x][node.y] == 0

    def get_neighbors(self, node: Node) -> List[Tuple[Node, float]]:
        directions = [
            (-1, 0), (1, 0), (0, -1), (0, 1)
        ]

        if self.allow_diagonal:
            directions += [
                (-1, -1), (-1, 1),
                (1, -1), (1, 1)
            ]

        neighbors = []

        for dx, dy in directions:
            nxt = Node(node.x + dx, node.y + dy)

            if not self.in_bounds(nxt):
                continue

            if not self.is_walkable(nxt):
                continue

            cost = math.sqrt(2) if dx != 0 and dy != 0 else 1
            neighbors.append((nxt, cost))

        return neighbors

    def reconstruct_path(
        self,
        came_from: Dict[Node, Node],
        current: Node
    ) -> List[Node]:
        path = [current]

        while current in came_from:
            current = came_from[current]
            path.append(current)

        return path[::-1]

    def search(
        self,
        start: Tuple[int, int],
        goal: Tuple[int, int]
    ) -> Optional[List[Node]]:

        start_node = Node(*start)
        goal_node = Node(*goal)

        open_set = []
        heappush(
            open_set,
            PriorityNode(
                self.heuristic(start_node, goal_node),
                start_node
            )
        )

        came_from: Dict[Node, Node] = {}

        g_score: Dict[Node, float] = {
            start_node: 0
        }

        f_score: Dict[Node, float] = {
            start_node: self.heuristic(start_node, goal_node)
        }

        closed_set: Set[Node] = set()

        while open_set:
            current = heappop(open_set).node

            if current == goal_node:
                return self.reconstruct_path(came_from, current)

            closed_set.add(current)

            for neighbor, movement_cost in self.get_neighbors(current):

                if neighbor in closed_set:
                    continue

                tentative_g = (
                    g_score[current] + movement_cost
                )

                if (
                    neighbor not in g_score
                    or tentative_g < g_score[neighbor]
                ):
                    came_from[neighbor] = current
                    g_score[neighbor] = tentative_g

                    f = tentative_g + self.heuristic(
                        neighbor,
                        goal_node
                    )

                    f_score[neighbor] = f

                    heappush(
                        open_set,
                        PriorityNode(f, neighbor)
                    )

        return None


def visualize(
    grid: List[List[int]],
    path: Optional[List[Node]]
):
    display = [
        ["#" if cell else "." for cell in row]
        for row in grid
    ]

    if path:
        for node in path:
            display[node.x][node.y] = "*"

        display[path[0].x][path[0].y] = "S"
        display[path[-1].x][path[-1].y] = "G"

    print("\n".join(" ".join(row) for row in display))


if __name__ == "__main__":

    grid = [
        [0,0,0,0,0,0,0,0],
        [0,1,1,1,0,1,1,0],
        [0,0,0,1,0,0,1,0],
        [1,1,0,1,0,0,1,0],
        [0,0,0,0,0,1,0,0],
        [0,1,1,1,0,0,0,1],
        [0,0,0,0,0,1,0,0],
        [0,1,0,1,0,0,0,0]
    ]

    astar = AStar(grid, allow_diagonal=True)

    path = astar.search(
        start=(0, 0),
        goal=(7, 7)
    )

    if path:
        print("Path found!")
        print(path)
        visualize(grid, path)
    else:
        print("No path found.")