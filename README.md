# Vein Structure Generator

A Python script that generates realistic vein-like structures using Bézier curves with recursive branching and variable width tapering.

## Overview

This program creates organic, natural-looking vein patterns by combining mathematical curve generation with recursive branching algorithms. The veins start with a thick main branch that gradually tapers to zero width, with sub-veins branching off at various points.

## Features

- **Bézier Curve Generation**: Creates smooth, organic curves using control points
- **Variable Width Tapering**: All veins gradually decrease in width, reaching zero at their endpoints
- **Recursive Branching**: Sub-veins spawn from main veins, and sub-sub-veins can spawn from those
- **Tangent-Based Branching**: Branch directions are calculated based on the parent vein's tangent for natural flow
- **Randomized Structure**: Each generation produces a unique vein pattern

## Requirements

```bash
numpy
matplotlib
```

## Installation

```bash
pip install numpy matplotlib
```

## Usage

Simply run the script:

```bash
python vein_gen.py
```

This will generate and display a vein-like structure in a matplotlib window.

## Customization

You can modify several parameters in the script:

### Main Vein Parameters
- `num_control_points`: Number of control points for the main curve (default: 4)
- `initial_width`: Starting width of the main vein (default: 7)

### Sub-Vein Parameters
- `num_sub_veins`: Number of branches from the main vein (default: 7)
- `sub_vein_length`: Length multiplier for sub-veins (default: 0.2)
- `depth`: Recursion depth for sub-branching (default: 2)

### Example Customization

```python
# Generate more complex branching
sub_veins = generate_curved_sub_veins(
    main_curve, 
    main_widths, 
    num_sub_veins=10,  # More branches
    depth=3             # Deeper recursion
)
```

## How It Works

1. **Main Vein Generation**: Creates a primary Bézier curve using random control points
2. **Width Calculation**: Assigns linearly decreasing widths from thick to zero
3. **Sub-Vein Branching**: 
   - Randomly selects points along the parent vein
   - Calculates tangent direction at branch points
   - Generates curved sub-veins with slight angular deviation
   - Inherits parent width at the branch point
4. **Recursive Branching**: Repeats the process for each sub-vein up to specified depth
5. **Visualization**: Renders all curves with variable line widths

## Technical Details

- **Bézier Curve Formula**: Uses the standard parametric Bézier formula with binomial coefficients
- **Tangent Calculation**: Computed as the normalized difference between adjacent curve points
- **Branch Angle**: Random deviation up to ±45 degrees from parent tangent
- **Width Inheritance**: Sub-veins start with the same width as the parent at the branch point

## Output

The script generates a matplotlib figure showing:
- Green lines representing the vein structure
- Variable line widths that taper to zero
- Natural-looking branching patterns
- Organic, leaf-vein-like appearance

## Potential Applications

- Procedural texture generation
- Biological simulation visualization
- Generative art
- Educational demonstrations of recursive algorithms
- Game asset generation

