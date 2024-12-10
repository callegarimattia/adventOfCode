package utils

import (
	"strconv"
)

func Contains[T comparable](l []T, x T) bool {
	for _, v := range l {
		if v == x {
			return true
		}
	}
	return false
}

func Abs(x int) int {
	if x < 0 {
		return -x
	}
	return x
}

func MustAtoi(s string) int {
	x, err := strconv.Atoi(s)
	if err != nil {
		panic(err)
	}
	return x
}

func Reversed[T any](a []T) []T {
	for left, right := 0, len(a)-1; left < right; left, right = left+1, right-1 {
		a[left], a[right] = a[right], a[left]
	}
	return a
}

func Reverse[T any](a []T) {
	for left, right := 0, len(a)-1; left < right; left, right = left+1, right-1 {
		a[left], a[right] = a[right], a[left]
	}
}

func Add2map(m map[int][]int, first, second int) {
	v, ok := m[first]
	if !ok {
		m[first] = []int{second}
	} else {
		m[first] = append(v, second)
	}
}

func ToInts(ss []string) []int {
	ints := []int{}
	for _, s := range ss {
		ints = append(ints, MustAtoi(s))
	}
	return ints
}

func Pop[T comparable](l *[]T, i int) (T, bool) {
	n := len(*l)
	if i < 0 || i > n {
		return *new(T), false
	}
	x := (*l)[i]
	for i < n-1 {
		(*l)[i] = (*l)[i+1]
		i++
	}
	*l = (*l)[:n-1]
	return x, true
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

// Returns
func (h *IntHeap) Pop() any {
	old := *h
	n := len(old)
	x := old[n-1]
	*h = old[0 : n-1]
	return x
}

// LinkedList implementation
type LinkedList[T any] struct {
	Head *Node[T]
}

type Node[T any] struct {
	Val  T
	Next *Node[T]
}

// Inserts a node in the idx-th position.
// If idx is out of range, it creates a new node at the end of the linked list.
func (ll *LinkedList[T]) Insert(idx int, val T) {
	newNode := &Node[T]{Val: val}
	if ll.Head == nil {
		ll.Head = newNode
		return
	}

	if idx <= 0 {
		newNode.Next = ll.Head
		ll.Head = newNode
	}

	curr := ll.Head
	for curr.Next != nil || idx == 0 {
		idx--
		curr = curr.Next
	}
	curr.Next = newNode
}

// Deletes the idx-th node. Returns the value stored in the node and true.
// If the idx provided is out of range, returns the zero-value of type [T] and false.
func (ll *LinkedList[T]) Pop(idx int) (T, bool) {
	if ll.Head == nil || idx < 0 {
		return *new(T), false
	}
	curr := ll.Head
	prev := (*Node[T])(nil)
	for i := 0; curr != nil; i++ {
		if i == idx {
			if prev == nil {
				ll.Head = curr.Next
				return curr.Val, true
			}
			prev.Next = curr.Next
			return curr.Val, true
		}
		prev = curr
		curr = curr.Next
	}
	return *new(T), false
}
