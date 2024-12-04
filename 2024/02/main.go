package main

import (
	"bufio"
	"fmt"
	"io"
	"os"
	"strconv"
	"strings"
)

// Problem: https://adventofcode.com/2024/day/2

func main() {
	filePath := os.Args[1]
	fp, err := os.Open(filePath)
	if err != nil {
		panic("File not found!")
	}
	defer fp.Close()
	input := parseInput(fp)
	fmt.Println(getNumSafeReports(input.Reports, isSafe))
	fmt.Println(getNumSafeReports(input.Reports, isSafe2))
}

type (
	Input   struct{ Reports }
	Reports []Report
	Report  []int
)

func (r Report) Len() int {
	return len(r)
}

func (r *Report) Pop(i int) int {
	old := *r
	x := old[i]
	*r = append(old[:i], old[i+1:]...)
	return x
}

func isSafe(r Report) bool {
	var diff int
	for i, j := 0, 1; j < r.Len(); i, j = i+1, j+1 {
		currDiff := r[j] - r[i]
		if currDiff*diff < 0 { // if the diffs have different signs, return false
			return false
		}
		if abs(currDiff) < 1 || abs(currDiff) > 3 {
			return false
		}
		diff = currDiff
	}
	return true
}

func isSafe2(r Report) bool {
	if isSafe(r) {  // if it's already safe, no need to check subarrays
		return true
	}
	for i := range r {
		clone := make(Report, r.Len())
		copy(clone, r)
		fmt.Println(clone.Pop(i))
		if isSafe(clone) {
			return true
		}
	}
	return false
}

func getNumSafeReports(r Reports, f func(r Report) bool) int {
	count := 0
	for i := range r {
		if f(r[i]) {
			fmt.Println(r[i])
			count++
		}
	}
	return count
}

func parseInput(r io.Reader) Input {
	scanner := bufio.NewScanner(r)
	reports := Reports{}
	for scanner.Scan() {
		line := scanner.Text()
		reports = append(reports, extractReportFromLine(line))
	}
	return Input{reports}
}

func extractReportFromLine(line string) Report {
	nums := strings.Split(line, " ")
	var report Report
	for i := range nums {
		curr := mustAtoi(nums[i])
		report = append(report, curr)
	}
	return report
}

func mustAtoi(x string) int {
	n, err := strconv.Atoi(x)
	if err != nil {
		panic(err)
	}
	return n
}

func abs(x int) int {
	if x > 0 {
		return x
	} else {
		return -x
	}
}
