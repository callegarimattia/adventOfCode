package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"

	"github.com/callegarimattia/adventOfcode/2024/utils"
)

func main() {
	filePath := os.Args[1]
	fp, err := os.Open(filePath)
	if err != nil {
		panic("file not found")
	}
	defer fp.Close()
	input := processInput(fp)
	fmt.Println(part1(input))
	fmt.Println(part2(input))
}

func part1(input Input) int {
	sum := 0
	for _, u := range input.updates {
		if checkUpdate(input.orderings, u) {
			sum += u[len(u)/2]
		}
	}
	return sum
}

func part2(input Input) int {
	sum := 0
	for _, u := range input.updates {
		if checkUpdate(input.orderings, u) {
			continue
		}
		for !checkUpdate(input.orderings, u) {
			u = order(input.orderings, u)
		}
		sum += u[len(u)/2]
	}
	return sum
}

func order(o map[int][]int, u []int) []int {
	for i := len(u) - 1; i >= 0; i-- {
		for j := 0; j < i; j++ {
			if utils.Contains(o[u[i]], u[j]) {
				wrong, _ := utils.Pop(&u, j)
				u = append(u, wrong)
			}
		}
	}
	return u
}

func checkUpdate(o map[int][]int, u []int) bool {
	for i := len(u) - 1; i >= 0; i-- {
		for j := 0; j < i; j++ {
			if utils.Contains(o[u[i]], u[j]) {
				return false
			}
		}
	}
	return true
}

type Input struct {
	orderings map[int][]int
	updates   [][]int
}

func processInput(fp *os.File) Input {
	scanner := bufio.NewScanner(fp)
	// orderings
	orderings := map[int][]int{}
	for scanner.Scan() {
		line := scanner.Text()
		rawPair := strings.Split(line, "|")
		if len(rawPair) < 2 {
			break
		}
		pair := utils.ToInts(rawPair)
		utils.Add2map(orderings, pair[0], pair[1])
	}

	// updates
	updates := [][]int{}
	for scanner.Scan() {
		line := scanner.Text()
		update := utils.ToInts(strings.Split(line, ","))
		updates = append(updates, update)
	}
	return Input{orderings, updates}
}
