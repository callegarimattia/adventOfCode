package main

import (
	"bufio"
	"fmt"
	"os"
)

func main() {
	filePath := os.Args[1]
	fp, err := os.Open(filePath)
	if err != nil {
		panic(err)
	}
	input := processInput(fp)
	grid1 := deepCopy(input.Grid)
	count := walk(grid1, input.Pos, Dir{0, -1}, make(map[Pos]struct{}))
	fmt.Println(count)
	grid2 := deepCopy(input.Grid)
	obs := make(map[Pos]struct{})
	walk2(grid2, input.Pos, Dir{0, -1}, obs)
	fmt.Println(len(obs))
}

func processInput(fp *os.File) Input {
	input := Input{
		Pos:  Pos{},
		Grid: Grid{},
	}
	scanner := bufio.NewScanner(fp)
	row := 0
	for scanner.Scan() {
		line := []rune(scanner.Text())
		for col, ch := range line {
			if ch == '^' {
				input.Pos.x = col
				input.Pos.y = row
			}
		}
		input.Grid = append(input.Grid, line)
		row++
	}
	return input
}

func walk(g Grid, c Pos, d Dir, seen map[Pos]struct{}) int {
	if !g.isValid(c) {
		return 0
	}

	if g.isObstacle(c.step(d)) {
		d = turnRight(d)
	}

	return walk(g, c.step(d), d, seen) + c.isNew(seen)
}

func walk2(g Grid, c Pos, d Dir, obs map[Pos]struct{}) {
	if !g.isValid(c) || !g.isValid(c.step(d)) {
		return
	}

	ahead := c.step(d)

	if g.isObstacle(ahead) {
		d = turnRight(d)
		walk2(g, c.step(d), d, obs)
		return
	}

	g.addObstacle(ahead)
	if detectLoop(g, c, turnRight(d)) {
		obs[c] = struct{}{}
	}
	g.removeObstacle(ahead)

	walk2(g, ahead, d, obs)
}

func detectLoop(g Grid, c Pos, d Dir) bool {
	states := make(map[State]struct{})
	s := State{c, d}
	for !in(states, s) {
		states[s] = struct{}{}
		if !g.isValid(c) {
			return false
		}
		if g.isObstacle(c.step(d)) {
			d = turnRight(d)
		}
		c = c.step(d)
		s = State{c, d}
	}
	return true
}

func in[T comparable](m map[T]struct{}, s T) bool {
	_, ok := m[s]
	return ok
}

func deepCopy(src Grid) Grid {
	dst := make(Grid, len(src))
	for i := range src {
		dst[i] = make([]rune, len(src[i]))
		copy(dst[i], src[i])
	}
	return dst
}

type State struct {
	Pos
	Dir
}

type Input struct {
	Pos
	Grid
}

type Pos struct {
	x, y int
}

type Grid [][]rune

func (g Grid) isObstacle(p Pos) bool {
	if !g.isValid(p) {
		return false
	}
	return g[p.y][p.x] == '#' ||
		g[p.y][p.x] == 'O'
}

func (g Grid) addObstacle(p Pos) {
	g[p.y][p.x] = 'O'
}

func (g Grid) removeObstacle(p Pos) {
	g[p.y][p.x] = '.'
}

func (p Pos) step(d Dir) Pos {
	return Pos{p.x + d.dx, p.y + d.dy}
}

func (p Pos) isNew(seen map[Pos]struct{}) int {
	if _, ok := seen[p]; !ok {
		seen[p] = struct{}{}
		return 1
	}
	return 0
}

func (g Grid) isValid(c Pos) bool {
	return c.x < len(g[0]) && c.x >= 0 &&
		c.y < len(g) && c.y >= 0
}

type Dir struct {
	dx, dy int
}

func turnRight(d Dir) Dir {
	return Dir{-d.dy, d.dx}
}

func (g Grid) print() {
	fmt.Println("----------------")
	for i := range g {
		fmt.Println(string(g[i]))
	}
}
