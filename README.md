# Spinning Wheel State Selector

## Description

The Spinning Wheel State Selector is a Python program that creates an interactive graphical user interface (GUI) using the Tkinter library. Users can spin a virtual wheel, each section representing a different state, and the wheel comes to stop on a random state. States are color-coded and once visited, won't be visited again until all states have been visited. An option is also available to spin to a completely random state.

The wheel is drawn using polygon shapes for each state and colors are assigned using a color palette generator. States can be added to or modified in a separate JSON file.

## Installation

1. Clone the repository: 
```
git clone https://github.com/wt-chat-gpt/spinning-wheel.git
```

2. Navigate into the cloned directory: 

```
cd spinning-wheel
```

3. Install the necessary Python packages: 

```
pip install -r requirements.txt
```


## Usage

1. Add or modify states in the `states.json` file. Each state object should have a `text` attribute. A `color` attribute can also be added, but it's optional.

2. Run the program:
```
python spinning_wheel.py states.json
```


## Features

1. Interactive spinning wheel GUI
2. Option to select from unvisited states or completely random
3. State colors generated dynamically for visualization
4. The wheel scales based on window size

## Contributing

Pull requests are welcome. Please make sure to update tests as appropriate.

## License

This project is licensed under the terms of the GNU license.
