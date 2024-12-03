package main

import (
	"bufio"
	"container/heap"
	"fmt"
	"io"
	"os"
	"regexp"
	"strconv"
)

// Problem: https://adventofcode.com/2024/day/1

func main() {
	inputFilePath := os.Args[1]
	fp, err := os.Open(inputFilePath)
	if err != nil {
		panic(fmt.Sprintf("File %v not found!", inputFilePath))
	}
	defer fp.Close()

	input := parseInput(fp)

	totalDist := calcTotalDistance(input.heapA, input.heapB)
	fmt.Println(totalDist)

	totalSimil := calcTotalSimilarityScore(input.freqA, input.freqB)
	fmt.Println(totalSimil)
}

// Input contains tha processed input.
// Stores the original lists of numbers, the min-heaps associated and the freqency maps.
type Input struct {
	a     []int
	b     []int
	heapA *IntHeap
	heapB *IntHeap
	freqA FreqMap
	freqB FreqMap
}

func parseInput(fp io.Reader) Input {
	var arrA, arrB []int
	heapA := &IntHeap{}
	heapB := &IntHeap{}
	freqA, freqB := FreqMap{}, FreqMap{}

	scanner := bufio.NewScanner(fp)
	for scanner.Scan() { // Scan line by line.
		a, b := extractNumsFromLine(scanner.Text())
		arrA = append(arrA, a)
		arrB = append(arrB, b)
		freqA.Add(a)
		freqB.Add(b)
		heap.Push(heapA, a)
		heap.Push(heapB, b)
	}
	return Input{arrA, arrB, heapA, heapB, freqA, freqB}
}

func extractNumsFromLine(line string) (int, int) {
	re := regexp.MustCompile(`(\d+)\s+(\d+)`)
	matches := re.FindStringSubmatch(line)
	if len(matches) != 3 {
		panic("Failed to extract nums")
	}
	return mustAtoi(matches[1]), mustAtoi(matches[2])
}

func calcTotalDistance(a, b *IntHeap) int {
	dist := 0
	for a.Len() > 0 && b.Len() > 0 {
		n1 := heap.Pop(a).(int)
		n2 := heap.Pop(b).(int)
		diff := n1 - n2
		if diff < 0 {
			dist += -diff
		} else {
			dist += diff
		}
	}

	return dist
}

// Calculates a total similarity score by
// adding up each number in the first list
// after multiplying it by the number of times
// that number appears in the second list.
func calcTotalSimilarityScore(a, b FreqMap) int {
	score := 0
	for key := range a {
		score += key * b[key] * a[key]
	}
	return score
}

// Panics if [strconv.Atoi](x) returns a non-nil error.
func mustAtoi(x string) int {
	y, err := strconv.Atoi(x)
	if err != nil {
		panic(err)
	}
	return y
}

// FreqMap stores the frequency of each number in a list.
// Keys are the numbers in the list.
// Values are the number of occurence of the key in the list
type FreqMap map[int]int

func (f FreqMap) Add(x int) {
	f[x]++
}

// IntHeap implementation
// Source: https://pkg.go.dev/container/heap
type IntHeap []int

// Sort interface
func (h IntHeap) Len() int           { return len(h) }
func (h IntHeap) Less(i, j int) bool { return h[i] < h[j] }
func (h IntHeap) Swap(i, j int)      { h[i], h[j] = h[j], h[i] }

func (h *IntHeap) Push(x any) {
	*h = append(*h, x.(int))
}

func (h *IntHeap) Pop() any {
	old := *h
	n := len(old)
	x := old[n-1]
	*h = old[0 : n-1]
	return x
}
