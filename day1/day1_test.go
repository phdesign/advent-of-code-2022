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
