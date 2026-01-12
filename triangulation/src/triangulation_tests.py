import matplotlib.pyplot as plt
import math
import numpy as np

def draw_diagram(observer_x, observer_y, x1, y1, x2, y2, x3, y3, valid_point, angle12, angle23, angle31, centers_with_radii=None, show_circles=False, 
                 plot_ranges={"x_min": -2., "y_min": -2, "x_max": 2, "y_max": 2}, debug=False):
    """
    Draw a diagram showing the valid point, original points, and optionally circles.

    Args:
        x1, y1, x2, y2, x3, y3: Coordinates of the three points
        valid_point: The validated triangulation point
        angle12, angle23, angle31: The angles for the triangulation
        observer_x, observer_y: Coordinates of the observer point
        centers_with_radii: Optional dictionary of circle centers and radii
        show_circles: Whether to show the circles used in triangulation
        plot_ranges: Optional dictionary with keys x_min, y_min, x_max, y_max for plot limits
        debug: Whether to print debug information
    """
    # Create a figure
    plt.figure(figsize=(12, 8))

    # Plot the given points
    plt.scatter([x1, x2, x3], [y1, y2, y3], color='red', s=80, label='Reference Points')
    plt.text(x1, y1, f'P1 ({x1}, {y1})', fontsize=10, ha='right')
    plt.text(x2, y2, f'P2 ({x2}, {y2})', fontsize=10, ha='right')
    plt.text(x3, y3, f'P3 ({x3}, {y3})', fontsize=10, ha='right')

    # Plot the observer point
    plt.scatter([observer_x], [observer_y], color='blue', s=200, facecolors='none', edgecolors='blue', linewidth=2, label='Observer')
    plt.text(observer_x, observer_y, f'Observer ({observer_x}, {observer_y})', fontsize=10, ha='left')

    # Add triangle outline connecting the reference points
    plt.plot([x1, x2, x3, x1], [y1, y2, y3, y1], 'k--', alpha=0.5)

    # Plot the valid point
    vx, vy = valid_point
    plt.scatter([vx], [vy], color='green', s=100, label='Triangulated Point')
    plt.text(vx, vy, f'({vx:.2f}, {vy:.2f})', fontsize=10, ha='right')

    # Draw lines from the valid point to each given point
    plt.plot([vx, x1], [vy, y1], 'g-', alpha=0.7)
    plt.plot([vx, x2], [vy, y2], 'g-', alpha=0.7)
    plt.plot([vx, x3], [vy, y3], 'g-', alpha=0.7)

    # Draw angle arcs
    def draw_angle_arc(cx, cy, p1x, p1y, p2x, p2y, angle_label, color='blue'):
        # Calculate vectors from center to points
        v1x, v1y = p1x - cx, p1y - cy
        v2x, v2y = p2x - cx, p2y - cy

        # Calculate angles from center to each point
        angle1 = math.atan2(v1y, v1x)
        angle2 = math.atan2(v2y, v2x)

        # Determine which way to draw the arc (clockwise or counterclockwise)
        # based on the specified angle
        cross_product = v1x * v2y - v1y * v2x
        if cross_product < 0:  # Clockwise motion
            if angle2 > angle1:
                angle2 -= 2 * math.pi
        else:  # Counterclockwise motion
            if angle2 < angle1:
                angle2 += 2 * math.pi

        # Calculate radius for the angle arc (proportional to distance)
        radius = min(
            math.sqrt(v1x**2 + v1y**2),
            math.sqrt(v2x**2 + v2y**2)
        ) * 0.25

        # Draw arc
        theta = np.linspace(angle1, angle2, 100)
        x_arc = cx + radius * np.cos(theta)
        y_arc = cy + radius * np.sin(theta)
        plt.plot(x_arc, y_arc, color=color, linewidth=2)

        # Add angle label at the midpoint of the arc
        mid_angle = (angle1 + angle2) / 2
        text_x = cx + radius * 1.3 * math.cos(mid_angle)
        text_y = cy + radius * 1.3 * math.sin(mid_angle)
        plt.text(text_x, text_y, f'{angle_label}°', fontsize=10, ha='center', color=color)

    # Draw angle arcs for the three inscribed angles
    draw_angle_arc(vx, vy, x1, y1, x2, y2, angle12, 'blue')
    draw_angle_arc(vx, vy, x2, y2, x3, y3, angle23, 'purple')
    draw_angle_arc(vx, vy, x3, y3, x1, y1, angle31, 'green')

    # Draw circles if requested
    if show_circles and centers_with_radii:
        colors = ['tab:blue', 'tab:orange', 'tab:green']
        for i, (key, value) in enumerate(centers_with_radii.items()):
            centers, radius = value['Centers'], value['Radius']

            # Only draw circles with reasonable radii (not too large)
            if radius < 100:  # Skip very large circles
                for j, (cx, cy) in enumerate(centers):
                    circle = plt.Circle((cx, cy), radius, fill=False, linestyle='--',
                                      color=colors[i], alpha=0.3, label=f'{key} Circle {j+1}' if j == 0 else "")
                    plt.gca().add_patch(circle)

    # Set axis limits - use plot_ranges if provided, otherwise calculate automatically
    if plot_ranges is not None:
        plt.xlim(plot_ranges['x_min'], plot_ranges['x_max'])
        plt.ylim(plot_ranges['y_min'], plot_ranges['y_max'])
    else:
        # Calculate automatic limits with margin
        all_x = [x1, x2, x3, vx, observer_x]
        all_y = [y1, y2, y3, vy, observer_y]

        # Add some margin
        x_min, x_max = min(all_x), max(all_x)
        y_min, y_max = min(all_y), max(all_y)
        width = x_max - x_min
        height = y_max - y_min
        margin = max(width, height) * 0.3  # 30% margin

        plt.xlim(x_min - margin, x_max + margin)
        plt.ylim(y_min - margin, y_max + margin)
    
    plt.gca().set_aspect('equal', adjustable='box')

    # Add legend and grid
    handles, labels = plt.gca().get_legend_handles_labels()
    by_label = dict(zip(labels, handles))
    plt.legend(by_label.values(), by_label.keys(), loc='best')

    plt.grid(True)
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.title(f'Point Triangulated with Angles: {angle12}°, {angle23}°, {angle31}°')
    plt.tight_layout()

    plt.show()

def draw_diagram_s(s):
    draw_diagram(
        # observer_x, observer_y, 
        s.observers[0][0], s.observers[0][1],
        # x1, y1, x2, y2, x3, y3, 
        *s.points, # use points since they have been reordered
        # valid point
        s.triangulated_point,
        # angle12, angle23, angle31,
        # *s.angles_between_points_ground_truth,
        *s.angles_between_points_with_simulated_error, -1*np.sum(s.angles_between_points_with_simulated_error), # need to add an element here
        # centers_with_radii
        s.centers_with_radii, 
        show_circles=True, 
        debug=False
    )