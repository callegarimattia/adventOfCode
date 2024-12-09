package utils_test

import (
	"testing"

	"github.com/callegarimattia/adventOfcode/2024/utils"
	"github.com/stretchr/testify/assert"
	"github.com/stretchr/testify/require"
)

func TestInsert(t *testing.T) {
	ll := &utils.LinkedList[int]{}
	assert.Nil(t, ll.Head)

	ll.Insert(0, 10)

	require.NotNil(t, ll.Head)
	assert.Equal(t, 10, ll.Head.Val)
	assert.Nil(t, ll.Head.Next)

	ll.Insert(1, 20)

	assert.Equal(t, 10, ll.Head.Val)
	assert.Equal(t, 20, ll.Head.Next.Val)

	ll.Insert(0, 30)

	assert.Equal(t, 30, ll.Head.Val)
	assert.Equal(t, 10, ll.Head.Next.Val)
	assert.Equal(t, 20, ll.Head.Next.Next.Val)
}

func TestPop(t *testing.T) {
	ll := &utils.LinkedList[int]{
		&utils.Node[int]{10, &utils.Node[int]{20, nil}},
	}

	val, ok := ll.Pop(1)

	assert.True(t, ok)
	assert.Equal(t, 20, val)
	assert.Equal(t, 10, ll.Head.Val)
	assert.Nil(t, ll.Head.Next)

	val, ok = ll.Pop(0)
	assert.True(t, ok)
	assert.Equal(t, 10, val)
	assert.Nil(t, ll.Head)

	_, ok = ll.Pop(0)
	assert.False(t, ok)
}
