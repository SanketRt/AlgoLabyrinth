# MazeRace: Maze Solver Visualization

**MazeRace** is a Python project that generates random perfect mazes and solves them using four classic graph-search algorithms (BFS, DFS, Dijkstra, and A*) side by side in a quadrant layout, with real-time animation and performance comparison.

---

## 🔍 Features

- **Maze Generation**: Randomized DFS "recursive backtracker" for perfect mazes
- **Solvers**:
  - Breadth-First Search (BFS)
  - Depth-First Search (DFS)
  - Dijkstra's Uniform-Cost Search
  - A* Search (Manhattan or Euclidean heuristic)
- **Visualization**:
  - Split screen into 4 quadrants—one per algorithm
  - Animated exploration (blue) and final path (yellow)
  - Optional GIF preview embedded in README
- **Benchmarking**: Script to collect timing, node-count, and path-length metrics

---

## ⚙️ Requirements

- Python 3.9+
- [NumPy](https://numpy.org/)
- [Pygame](https://www.pygame.org/)
- [Matplotlib](https://matplotlib.org/) (for benchmarking plots)

Install with:

```bash
pip install -r requirements.txt
```

---

## 🚀 Getting Started

1. **Clone the repo**:
   ```bash
   git clone https://github.com/SanketRt/AlgoLabyrinth.git
   cd Labyrinth
   ```

2. **Create & activate venv**:
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate    # Windows: .venv\Scripts\Activate.ps1
   pip install -r requirements.txt
   ```

3. **Run the visualizer**:
   ```bash
   python3 visualize.py
   ```

You should see a window with four evolving mazes.

---

## 🔄 Solver Comparison in Action

![Quadrant Animation](assets/quadrants.gif)

---

## 🎥 Creating the Animation GIF

1. **Record a short clip** of the running visualizer, either with a screen-recording tool (e.g. [LICEcap](https://www.cockos.com/licecap/), Peek, or OBS Studio) or via command-line:

   ```bash
   # Example using ffmpeg on Linux/Mac (adjust display, size, duration):
   ffmpeg -y -f x11grab -r 60 -s ${WIDTH}x${HEIGHT} -i :0.0+${X},${Y} \
     -t 10 -vf "fps=15,scale=600:-1:flags=lanczos" assets/quadrants.gif
   ```

2. **Place the GIF** under `assets/quadrants.gif` in the repo

3. **The GIF will render inline** on the project page when you push to GitHub

---

## 📊 Benchmarking

Run the benchmarking script to compare performance across maze sizes:

```bash
python benchmark.py
```

This will output timing/node counts and pop up Matplotlib plots.

---

## 🤝 Contributing

Contributions are welcome! Feel free to:

- Tweak algorithms or add new solvers (e.g. Bidirectional BFS)
- Improve the GUI: add speed controls, start/stop buttons
- Support weighted mazes or diagonal moves

Please open an issue or PR.

---

## 📄 License

MIT © Sanket Rout