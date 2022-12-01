package main

import (
	"flag"
	"fmt"
	"io/ioutil"
	"strconv"
	"strings"
)

func maxOfInts(ints []int) (int, int) {
	max := ints[0]
	maxPos := 0
	for i, val := range ints {
		if val > max {
			max = val
			maxPos = i
		}
	}
	return max, maxPos
}

func sumInts(ints []int) int {
	sum := 0
	for _, i := range ints {
		sum += i
	}
	return sum
}

func stringsToInts(strings []string) []int {
	var result = []int{}

	for _, s := range strings {
		j, err := strconv.Atoi(s)
		if err == nil {
			result = append(result, j)
		}
	}
	return result
}

func parseInput(input string) [][]int {
	var result = [][]int{}
	groups := strings.Split(input, "\n\n")
	fmt.Printf("Found %d groups\n", len(groups))
	for _, group := range groups {
		lines := strings.Split(group, "\n")
		fmt.Printf("Found %d lines\n", len(lines))
		result = append(result, stringsToInts(lines))
	}
	return result
}

func readInput(filename string) string {
	data, err := ioutil.ReadFile(filename)
	if err != nil {
		panic(err)
	}
	return string(data)
}

func sumItems(groups [][]int) []int {
	var result = []int{}
	for _, group := range groups {
		result = append(result, sumInts(group))
	}
	return result
}

func main() {
	flag.Parse()
	filename := flag.Arg(0)
	fmt.Printf("Reading input from %s\n", filename)
	input := readInput(filename)
	fmt.Printf("Read input %s\n", input[:10])
	itemsByElf := parseInput(input)
	caloriesPerElf := sumItems(itemsByElf)
	maxCalories, maxElfID := maxOfInts(caloriesPerElf)
	fmt.Printf("Elf %d has the most calories: %d\n", maxElfID, maxCalories)
}
