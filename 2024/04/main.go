package main

import (
	"bufio"
	"fmt"
	"io"
	"os"
)

// Problem: https://adventofcode.com/2024/day/4

func main() {
	filePath := os.Args[1]
	fp, err := os.Open(filePath)
	if err != nil {
		panic("File not found!")
	}
	defer fp.Close()
	grid := parseInput(fp)
	fmt.Println(countXMAS(grid))
	fmt.Println(countXMAS2(grid))
}

type Grid [][]rune

func parseInput(fp io.Reader) Grid {
	scanner := bufio.NewScanner(fp)
	grid := Grid{}
	for scanner.Scan() {
		grid = append(grid, []rune(scanner.Text()))
	}
	return grid
}

var xmas = []rune("XMAS")

var dirs = map[string][]int{
	// dir : {dy, dx}
	"ul": {-1, -1},
	"uu": {-1, 0},
	"ur": {-1, +1},
	"ll": {0, -1},
	"rr": {0, +1},
	"dl": {+1, -1},
	"dd": {+1, 0},
	"dr": {+1, +1},
}

func dfs(grid Grid, x, y int, dir []int, i int) int {
	lenX := len(grid[0])
	lenY := len(grid)
	if x < 0 || x >= lenX || y < 0 || y >= lenY {
		return 0
	}
	if grid[y][x] != xmas[i] {
		return 0
	}

	if i == len(xmas)-1 {
		return 1
	}
	return dfs(grid, x+dir[1], y+dir[0], dir, i+1)
}

func countXMAS(grid Grid) int {
	count := 0
	for y := 0; y < len(grid); y++ {
		for x := 0; x < len(grid[0]); x++ {
			for key := range dirs {
				count += dfs(grid, x, y, dirs[key], 0)
			}
		}
	}
	return count
}

func out3x3(grid Grid) {
	for y := range grid[:3] {
		fmt.Println(string(grid[y][:3]))
	}
	fmt.Println()
}

func countXMAS2(grid Grid) int {
	count := 0
	for y := 0; y < len(grid)-2; y += 1 {
		for x := 0; x < len(grid[0])-2; x += 1 {
			subBlock := get3x3(grid, x, y)
			if validBlock(subBlock) {
				count++
			}
		}
	}
	return count
}

func get3x3(grid Grid, x, y int) Grid {
	subGrid := make(Grid, 3)
	for i := 0; i < 3; i++ {
		subGrid[i] = make([]rune, 3)
		for j := 0; j < 3; j++ {
			subGrid[i][j] = grid[y+i][x+j]
		}
	}
	return subGrid
}

func validBlock(grid Grid) bool {
	return (dfs(grid, 0, 0, dirs["dr"], 1) +
		dfs(grid, 2, 0, dirs["dl"], 1) +
		dfs(grid, 2, 2, dirs["ul"], 1) +
		dfs(grid, 0, 2, dirs["ur"], 1)) == 2
}
