package main

import (
	"fmt"
	"io"
	"os"
	"regexp"
	"strconv"
)

// Problem: https://adventofcode.com/2024/day/3


func main() {
	filePath := os.Args[1]
	fp, err := os.Open(filePath)
	if err != nil {
		panic("File not found!")
	}
	defer fp.Close()
	input := parseInput(fp)
	pairs := processInput(string(input))
	fmt.Println(pairs.TMul())
	pairs2 := getPairs2(string(input))
	fmt.Println(pairs2.TMul())
}

func parseInput(r io.Reader) []byte {
	text := make([]byte, 1024*20) // size of input is 19k
	_, err := r.Read(text)
	if err != nil {
		panic(err)
	}
	return text
}

func getIndexes(text string, re *regexp.Regexp) []int {
	dos := re.FindAllStringIndex(text, -1)
	var indexes []int
	for i := range dos {
		indexes = append(indexes, dos[i][0])
	}
	return indexes
}

func getPairs2(text string) Pairs {
	pairs := processInput(text)

	reDos := regexp.MustCompile(`do\(\)`)
	dos := getIndexes(text, reDos)

	reDonts := regexp.MustCompile(`don't\(\)`)
	donts := getIndexes(text, reDonts)

	return helper(pairs, dos, donts)
}

func helper(matches Pairs, dos, donts []int) Pairs {
	dosDonts := mergeSortedArrays(dos, donts)
	var pairs Pairs

	for i := 0; i < len(matches); i++ {
		if matches[i].index < dosDonts[0] {
			pairs = append(pairs, matches[i])
		}
	}

	for i, idx := range dosDonts {
		var valid bool
		if contains(donts, idx) {
			valid = false
		} else {
			valid = true
		}

		start := idx
		end := matches[len(matches)-1].index
		if i+1 < len(dosDonts) {
			end = dosDonts[i+1]
		}

		if valid {
			for j := 0; j < len(matches); j++ {
				if matches[j].index > end {
					break
				}
				if matches[j].index > start {
					pairs = append(pairs, matches[j])
				}
			}
		}
	}

	return pairs
}

func processInput(text string) Pairs {
	reMul := regexp.MustCompile(`mul\((\d+),(\d+)\)`)

	matches := reMul.FindAllStringSubmatchIndex(text, -1)
	var pairs []Pair
	for _, match := range matches {
		pairs = append(
			pairs,
			Pair{mustAtoi(text[match[2]:match[3]]), mustAtoi(text[match[4]:match[5]]), match[0]},
		)
	}
	return pairs
}

func mustAtoi(x string) int {
	y, err := strconv.Atoi(x)
	if err != nil {
		panic(err)
	}
	return y
}

type Pair struct {
	a     int
	b     int
	index int
}

func (p Pair) Mul() int {
	return p.a * p.b
}

type Pairs []Pair

func (p Pairs) TMul() int {
	var sum int
	for _, pair := range p {
		sum += pair.Mul()
	}
	return sum
}

func mergeSortedArrays(arr1, arr2 []int) []int {
	result := make([]int, 0, len(arr1)+len(arr2))
	i, j := 0, 0

	for i < len(arr1) && j < len(arr2) {
		if arr1[i] < arr2[j] {
			result = append(result, arr1[i])
			i++
		} else {
			result = append(result, arr2[j])
			j++
		}
	}

	for i < len(arr1) {
		result = append(result, arr1[i])
		i++
	}
	for j < len(arr2) {
		result = append(result, arr2[j])
		j++
	}

	return result
}

func contains(arr []int, x int) bool {
	for _, y := range arr {
		if x == y {
			return true
		}
	}
	return false
}
