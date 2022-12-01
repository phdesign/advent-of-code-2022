package main

import (
	"testing"

	"github.com/stretchr/testify/require"
)

func TestParseInput(t *testing.T) {
	t.Run("should return one group given no blank lines", func(t *testing.T) {
		input := `1
2
3
4`
		expected := [][]int{{1, 2, 3, 4}}
		actual := parseInput(input)
		require.Equal(t, expected, actual)
	})

	t.Run("should return multiple groups given ints split by blank lines", func(t *testing.T) {
		input := `1
2

3
4

5`
		expected := [][]int{{1, 2}, {3, 4}, {5}}
		actual := parseInput(input)
		require.Equal(t, expected, actual)
	})
}

func TestSumItems(t *testing.T) {
	t.Run("should return the sum of the items in each group", func(t *testing.T) {
		input := [][]int{{1, 2}, {3, 4}, {5}}
		expected := []int{3, 7, 5}
		actual := sumItems(input)
		require.Equal(t, expected, actual)
	})
}

func TestMaxOfInts(t *testing.T) {
	t.Run("should return the max and its position", func(t *testing.T) {
		input := []int{1, 2, 3, 4}
		expectedMax := 4
		expectedPos := 3
		actualMax, actualPos := maxOfInts(input)
		require.Equal(t, expectedMax, actualMax)
		require.Equal(t, expectedPos, actualPos)
	})
}

func TestMaxesOfInts(t *testing.T) {
	t.Run("should return the maxes of the ints", func(t *testing.T) {
		input := []int{1, 2, 3, 4}
		expected := []int{4, 3}
		actual := maxesOfInts(input, 2)
		require.Equal(t, expected, actual)
	})
}
