import numpy as np
import matplotlib.pyplot as plt

# Function to calculate the Bézier curve
def bezier_curve(t, points):
    n = len(points) - 1
    curve = np.zeros((len(t), 2))
    for i in range(n + 1):
        binomial_coeff = np.math.comb(n, i)
        curve += np.outer((binomial_coeff * (1 - t)**(n - i) * t**i), points[i])
    return curve

# Function to generate a random Bézier curve for the main vein
def generate_random_curve(num_control_points=4, num_curve_points=100):
    control_points = np.random.rand(num_control_points, 2)
    t_values = np.linspace(0, 1, num_curve_points)
    curve_points = bezier_curve(t_values, control_points)
    return curve_points, control_points

# Function to calculate the tangent direction at a point on the curve
def tangent_at_point(curve, index):
    if index < len(curve) - 1:
        tangent = curve[index + 1] - curve[index]
    else:
        tangent = curve[index] - curve[index - 1]
    return tangent / np.linalg.norm(tangent)

# Function to plot a Bézier curve with gradually decreasing width, down to zero at the end
def plot_curve_with_variable_width(curve, initial_width):
    num_points = len(curve)
    widths = np.linspace(initial_width, 0, num_points)  # Gradually decrease width to 0
    for i in range(num_points - 1):
        plt.plot(curve[i:i+2, 0], curve[i:i+2, 1], 'g-', linewidth=widths[i])

# Recursive function to generate sub-veins and their sub-branches
def generate_curved_sub_veins(main_curve, main_widths, num_sub_veins=5, sub_vein_length=0.2, depth=2):
    sub_veins = []
    for _ in range(num_sub_veins):
        # Randomly pick a point along the main vein to start the sub-vein
        start_idx = np.random.randint(0, len(main_curve) - 1)
        start_point = main_curve[start_idx]
        
        # Get the tangent at the selected point for forward branching
        tangent = tangent_at_point(main_curve, start_idx)
        
        # The starting width of the sub-vein is the same as the parent vein's width at that point
        start_width = main_widths[start_idx]
        
        # Generate control points for curved sub-veins
        num_sub_control_points = 4  # Using 4 control points for sub-veins for curvature
        sub_control_points = [start_point]
        
        for i in range(1, num_sub_control_points):
            deviation_angle = (np.random.rand() - 0.5) * np.pi / 4  # Max 45-degree deviation
            rotation_matrix = np.array([[np.cos(deviation_angle), -np.sin(deviation_angle)],
                                        [np.sin(deviation_angle), np.cos(deviation_angle)]])
            
            direction = rotation_matrix @ tangent
            offset = direction * (sub_vein_length / num_sub_control_points) * i  # Progressively farther points
            sub_control_points.append(start_point + offset)
        
        # Generate the sub-vein Bézier curve
        sub_curve = bezier_curve(np.linspace(0, 1, 100), np.array(sub_control_points))
        sub_veins.append((sub_curve, start_width))
        
        # If depth allows, recursively generate sub-sub-veins with decreasing width
        if depth > 0:
            sub_sub_veins = generate_curved_sub_veins(sub_curve, np.linspace(start_width, 0, len(sub_curve)),
                                                      num_sub_veins=3, sub_vein_length=sub_vein_length / 2, depth=depth - 1)
            sub_veins.extend(sub_sub_veins)
    
    return sub_veins

# Generate the main vein (primary curve)
main_curve, main_control_points = generate_random_curve()

# Define the width profile for the main vein (broad at the start, tapering to 0)
main_widths = np.linspace(7, 0, len(main_curve))

# Generate curved sub-veins with recursive sub-branching and decreasing width
sub_veins = generate_curved_sub_veins(main_curve, main_widths, num_sub_veins=7, depth=2)

# Plot the main vein and its curved sub-veins with recursive branching
plt.figure(figsize=(8, 8))

# Plot the main vein with variable width (tapering to 0)
plot_curve_with_variable_width(main_curve, initial_width=7)

# Plot each curved sub-vein and its sub-branches with width tapering to 0
for sub_curve, initial_width in sub_veins:
    plot_curve_with_variable_width(sub_curve, initial_width)

plt.title("Vein-like Structure with Width Tapering to Zero")
plt.show()
