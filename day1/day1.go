package main

import (
	"flag"
	"fmt"
	"io/ioutil"
	"strconv"
	"strings"
)

type elf struct {
	totalCalories int
	food          []int
}

func newElf(food []int) *elf {
	return &elf{totalCalories: maxInts(food), food: food}
}

func maxInts(ints []int) int {
	max := ints[0]
	for _, i := range ints {
		if i > max {
			max = i
		}
	}
	return max
}

func stringsToInts(strings []string) []int {
	var result = []int{}

	for _, s := range strings {
		j, err := strconv.Atoi(s)
		if err != nil {
			panic(err)
		}
		result = append(result, j)
	}
	return result
}

func parseInput(input string) [][]int {
	var result = [][]int{}
	groups := strings.Split(input, "\n\n")
	for _, group := range groups {
		result = append(result, stringsToInts(strings.Split(group, "\n")))
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

func getElves(groups [][]int) []*elf {
	var elves = []*elf{}
	for _, group := range groups {
		elves = append(elves, newElf(group))
	}
	return elves
}

func main() {
	input := readInput(flag.Arg(0))
	groups := parseInput(input)
	getElves(groups)
	//maxCalories := maxInts(elves)
	fmt.Println("done")
}
