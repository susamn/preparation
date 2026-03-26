package main

import (
	"fmt"
	"time"
)

func main() {
	// ============================================================================
	// 1. MAPS - Size and Capacity
	// ============================================================================
	// Exercise 1.1: Create a map of string keys to int values and add elements
	// Then print the size



	// Exercise 1.2: Create a map with initial capacity and add elements
	// Maps don't have capacity, but you can declare them - practice the syntax



	// Exercise 1.3: Create a nested map (map of string to map of string to int)
	// and populate it with data



	// Exercise 1.4: Delete elements from a map and check the size



	// Exercise 1.5: Check if a key exists in a map using the comma ok idiom



	// ============================================================================
	// 2. SLICES - Create and Manipulate
	// ============================================================================
	// Exercise 2.1: Create a slice of integers with length and capacity



	// Exercise 2.2: Create a slice and append elements to it



	// Exercise 2.3: Create a slice and use make() with length and capacity



	// Exercise 2.4: Slice a slice (reslice) and demonstrate the effect



	// Exercise 2.5: Copy elements from one slice to another using copy()



	// ============================================================================
	// 3. VARIABLES AND DATA TYPES
	// ============================================================================
	// Exercise 3.1: Define a variable of int64 type



	// Exercise 3.2: Define multiple variables of different integer types (int8, int16, int32, int64)



	// Exercise 3.3: Define a variable with type inference and demonstrate the type



	// Exercise 3.4: Define constants of different numeric types



	// Exercise 3.5: Define a string variable and manipulate it (concat, length, substring)



	// Exercise 3.6: Define a boolean variable and use it in conditional statements



	// Exercise 3.7: Define float variables and perform arithmetic operations



	// ============================================================================
	// 4. CHANNELS - Basic Send and Receive
	// ============================================================================
	// Exercise 4.1: Create a channel of type int and use it to send and receive messages



	// Exercise 4.2: Create a buffered channel with capacity 3



	// Exercise 4.3: Use channels with goroutines to send data



	// Exercise 4.4: Use select statement to handle multiple channels



	// Exercise 4.5: Close a channel and handle the closed channel detection



	// ============================================================================
	// 5. GOROUTINES AND CONCURRENCY
	// ============================================================================
	// Exercise 5.1: Create and run multiple goroutines



	// Exercise 5.2: Use sync.WaitGroup to wait for goroutines to complete



	// Exercise 5.3: Create goroutines that communicate via channels



	// Exercise 5.4: Implement a worker pool pattern with goroutines and channels



	// ============================================================================
	// 6. FAN-IN PATTERN
	// ============================================================================
	// Exercise 6.1: Show usage of fan-in - merge multiple channels into one



	// Exercise 6.2: Fan-in with goroutines sending on separate channels



	// Exercise 6.3: Fan-in with select statement



	// ============================================================================
	// 7. FAN-OUT PATTERN
	// ============================================================================
	// Exercise 7.1: Show usage of fan-out - distribute work across multiple goroutines



	// Exercise 7.2: Fan-out with a for loop creating workers



	// Exercise 7.3: Fan-out with result collection



	// ============================================================================
	// 8. STRUCTS
	// ============================================================================
	// Exercise 8.1: Define a struct with multiple fields



	// Exercise 8.2: Create a struct with methods



	// Exercise 8.3: Embed structs (composition)



	// Exercise 8.4: Create methods with pointer receivers



	// ============================================================================
	// 9. INTERFACES
	// ============================================================================
	// Exercise 9.1: Define an interface and implement it



	// Exercise 9.2: Use an interface with multiple implementations



	// Exercise 9.3: Create a function that accepts an interface parameter



	// Exercise 9.4: Use type assertion with interfaces



	// ============================================================================
	// 10. FUNCTIONS
	// ============================================================================
	// Exercise 10.1: Create a function that returns multiple values



	// Exercise 10.2: Create a variadic function (accepts variable number of arguments)



	// Exercise 10.3: Create a function that returns a function (higher-order function)



	// Exercise 10.4: Create a function with named return values



	// ============================================================================
	// 11. ERROR HANDLING
	// ============================================================================
	// Exercise 11.1: Create and return a custom error



	// Exercise 11.2: Implement the error interface



	// Exercise 11.3: Use defer, panic, and recover



	// ============================================================================
	// 12. LOOPS AND CONDITIONALS
	// ============================================================================
	// Exercise 12.1: Create a for loop with range over a slice



	// Exercise 12.2: Create a for loop iterating over a map



	// Exercise 12.3: Create a switch statement with multiple cases



	// Exercise 12.4: Use if-else if-else statement



	// ============================================================================
	// 13. POINTERS
	// ============================================================================
	// Exercise 13.1: Create a pointer to a variable and dereference it



	// Exercise 13.2: Pass pointers to functions to modify values



	// Exercise 13.3: Create a pointer to a struct and modify its fields



	// Exercise 13.4: Use pointer receivers in methods



	// ============================================================================
	// 14. PACKAGE MANAGEMENT AND IMPORTS
	// ============================================================================
	// Exercise 14.1: Use multiple packages (already using fmt and time)



	// Exercise 14.2: Use package alias



	// Exercise 14.3: Use blank import (for side effects)



	// ============================================================================
	// 15. TESTING AND BENCHMARKING CONCEPTS (show usage, not actual tests)
	// ============================================================================
	// Exercise 15.1: Create a function suitable for unit testing



	// Exercise 15.2: Create a function suitable for benchmarking



	// ============================================================================
	// 16. CONCURRENCY PATTERNS - ADVANCED
	// ============================================================================
	// Exercise 16.1: Pipeline pattern - chain multiple goroutines



	// Exercise 16.2: Timeout with channels



	// Exercise 16.3: Rate limiting with channels



	// ============================================================================
	// 17. TYPE CONVERSION AND CASTING
	// ============================================================================
	// Exercise 17.1: Convert between different numeric types



	// Exercise 17.2: Convert string to int and handle errors



	// Exercise 17.3: Convert int to string



	// ============================================================================
	// 18. SLICING OPERATIONS
	// ============================================================================
	// Exercise 18.1: Create a slice from an array



	// Exercise 18.2: Use slice operations (append, copy, len, cap)



	// Exercise 18.3: Demonstrate slice header and underlying array



	// ============================================================================
	// 19. REFLECTION (Basic)
	// ============================================================================
	// Exercise 19.1: Use reflect package to get type of a variable



	// Exercise 19.2: Use reflect to iterate over struct fields



	// ============================================================================
	// 20. CONTEXT AND CANCELLATION
	// ============================================================================
	// Exercise 20.1: Use context.Context for cancellation



	// Exercise 20.2: Use context with timeout



	// Exercise 20.3: Pass context through goroutines



	// ============================================================================
	// TEMPLATE SOLUTIONS SECTION (for reference, comment these out if desired)
	// ============================================================================
	// Uncomment below to see example patterns:
	// exampleMapUsage()
	// exampleChannelUsage()
	// exampleFanIn()
	// exampleFanOut()
}

// ============================================================================
// HELPER FUNCTIONS (Templates for reference)
// ============================================================================

// Example: Basic map usage
func exampleMapUsage() {
	fmt.Println("\n--- Example: Map Usage ---")
	// Create a map
	ages := make(map[string]int)
	ages["Alice"] = 30
	ages["Bob"] = 25
	fmt.Println("Map size:", len(ages))
	fmt.Println("Alice's age:", ages["Alice"])
}

// Example: Basic channel usage
func exampleChannelUsage() {
	fmt.Println("\n--- Example: Channel Usage ---")
	ch := make(chan int)
	go func() {
		ch <- 42
	}()
	value := <-ch
	fmt.Println("Received:", value)
}

// Example: Fan-in pattern
func exampleFanIn() {
	fmt.Println("\n--- Example: Fan-In Pattern ---")
	ch1 := make(chan int)
	ch2 := make(chan int)

	go func() {
		for i := 0; i < 3; i++ {
			ch1 <- i
		}
	}()

	go func() {
		for i := 10; i < 13; i++ {
			ch2 <- i
		}
	}()

	// Merge channels
	for i := 0; i < 6; i++ {
		select {
		case val := <-ch1:
			fmt.Println("From ch1:", val)
		case val := <-ch2:
			fmt.Println("From ch2:", val)
		}
	}
}

// Example: Fan-out pattern
func exampleFanOut() {
	fmt.Println("\n--- Example: Fan-Out Pattern ---")
	jobs := make(chan int, 5)
	results := make(chan int, 5)

	// Fan-out: distribute work
	for w := 0; w < 3; w++ {
		go worker(w, jobs, results)
	}

	// Send jobs
	for j := 1; j <= 5; j++ {
		jobs <- j
	}
	close(jobs)

	// Collect results
	for r := 0; r < 5; r++ {
		fmt.Println("Result:", <-results)
	}
}

func worker(id int, jobs <-chan int, results chan<- int) {
	for job := range jobs {
		fmt.Printf("Worker %d processing job %d\n", id, job)
		time.Sleep(100 * time.Millisecond)
		results <- job * 2
	}
}
