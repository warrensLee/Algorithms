.PHONY: help bfs dfs rdfs all clean

help:
	@echo "Targets:"
	@echo "  make bfs   - run BFS"
	@echo "  make dfs   - run DFS"
	@echo "  make rdfs  - run recursive DFS"
	@echo "  make all   - run all three"
	@echo "  make clean - remove generated outputs in bin/ (png files)"


bfs:
	@mkdir -p bin
	python3 src/main.py bfs 

# "HW2_SHOW_GUI=1 python3 src/main.py bfs" if you want to see the GUI

dfs:
	@mkdir -p bin
	python3 src/main.py dfs

rdfs:
	@mkdir -p bin
	python3 src/main.py rdfs

all: bfs dfs rdfs

clean:
	@rm -f bin/*.png
