# 
# Makefile for compiling example emoji programs and building documentation.
#
# Written by: Randy Dang, October 2024

CFLAGS = -Wall -Wextra -Werror

all: hello_world README add_two_numbers

refresh:
	make clean_all
	make all

# Build `hello_world` example program
hello_world: hello_world.o
	gcc hello_world.o -o hello_world $(CFLAGS)

hello_world.o: hello_world.emoc
	./emocc hello_world.emoc -c -o hello_world.o $(CFLAGS)

# Build `add_two_numbers` example program
add_two_numbers: add_two_numbers.o
	gcc add_two_numbers.o -o add_two_numbers $(CFLAGS)

add_two_numbers.o: add_two_numbers.emoc
	./emocc add_two_numbers.emoc -c -o add_two_numbers.o $(CFLAGS)

# Build `README.md` documentation
README: README.md

README.md: README.md.src
	python gen_documentation.py README.md.src > README.md

# Clean up executables, object files, etc.
clean:
	rm -f hello_world add_two_numbers *.o

clean_all:
	rm -f hello_world add_two_numbers *.o README.md

