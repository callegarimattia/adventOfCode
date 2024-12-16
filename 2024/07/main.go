package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"

	"github.com/callegarimattia/adventOfcode/2024/utils"
)

func main() {
	filePath := os.Args[1]
	fp, err := os.Open(filePath)
	if err != nil {
		panic(err)
	}
	defer fp.Close()

	input := parseInput(fp)
	fmt.Println(getSum(input.eqs))
	fmt.Println(getSum2(input.eqs))
}

type Input struct {
	eqs []Equation
}

type Equation struct {
	Total    int
	Operands []int
}

func (e Equation) isValid(h func(int, int, int, []int) bool) bool {
	return h(e.Operands[0], 0, e.Total, e.Operands)
}

func help(curr, i, target int, operands []int) bool {
	if i == len(operands)-1 {
		if curr == target {
			return true
		}
		return false
	}

	if curr > target { // early stopping when going over the target
		return false
	}

	i++

	return help(curr+operands[i], i, target, operands) ||
		help(curr*operands[i], i, target, operands)
}

func help2(curr, i, target int, operands []int) bool {
	if i == len(operands)-1 {
		if curr == target {
			return true
		}
		return false
	}

	if curr > target { // early stopping when going over the target
		return false
	}

	i++

	return help2(curr+operands[i], i, target, operands) ||
		help2(curr*operands[i], i, target, operands) ||
		help2(utils.MustAtoi(strconv.Itoa(curr)+strconv.Itoa(operands[i])), i, target, operands)
}

func parseInput(fp *os.File) Input {
	eqs := []Equation{}
	scanner := bufio.NewScanner(fp)
	for scanner.Scan() {
		eq := Equation{}
		line := scanner.Text()
		total, operands, ok := strings.Cut(line, ":")
		if !ok {
			print(line)
			continue
		}
		eq.Total = utils.MustAtoi(total)
		eq.Operands = utils.ToInts(strings.Split(operands, " ")[1:])
		eqs = append(eqs, eq)

	}
	return Input{eqs}
}

func getSum(es []Equation) int {
	res := 0
	for i := range es {
		if es[i].isValid(help) {
			res += es[i].Total
		}
	}
	return res
}

func getSum2(es []Equation) int {
	res := 0
	for i := range es {
		if es[i].isValid(help2) {
			res += es[i].Total
		}
	}
	return res
}
