package main

import (
	"crypto/sha1"
	"fmt"
	"os"
	"strconv"
)

func main() {
	fo, err := os.Create("rainbow_table.txt")
	if err != nil {
		panic(err)
	}
	defer func() {
		if err := fo.Close(); err != nil {
			panic(err)
		}
	}()

	for i := 10000000; i < 20000000; i++ {
		sha := strconv.Itoa(i) + "salt_for_you"
		for i := 0; i < 500; i++ {
			sha = fmt.Sprintf("%x", sha1.Sum([]byte(sha)))
		}
		_, err2 := fmt.Fprintf(fo, "%s\n", sha)
		if err2 != nil {
			return
		}
	}
}
