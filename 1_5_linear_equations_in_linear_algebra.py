import numpy as np
import matplotlib.pyplot as plt

# Define vectors u and v
u = np.array([1,2])
v = np.array([2,1])

# Generate a grid of coefficients c1 and c2
c1_values = np.linspace(-2, 2, 10)
c2_values = np.linspace(-2, 2, 10)

# Create a meshgrid for c1 and c2
c1, c2 = np.meshgrid(c1_values, c2_values)

# Calculate all possible linear combinations of u and v
span_vectors = c1[..., np.newaxis] * u + c2[..., np.newaxis] * v

# Set up the plot
plt.figure(figsize=(8,8))
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)

# Plot the span vectors
for i in range(span_vectors.shape[0]):
    for j in range(span_vectors.shape[1]):
        plt.quiver(0,0, span_vectors[i, j, 0], span_vectors[i, j, 1], angles='xy', scale_units='xy', scale=1, color='blue', alpha=0.5)

# Plot the original vectors u and v
plt.quiver(0, 0, u[0], u[1], angles='xy', scale_units='xy', scale=1, color='red', label='u')
plt.quiver(0, 0, v[0], v[1], angles='xy', scale_units='xy', scale=1, color='green', label='v')

# Set plot limits
plt.xlim(-5,5)
plt.ylim(-5,5)

# Add labels and title
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Span{u,v} in 2D Space')
plt.legend()
plt.grid(True)
plt.show()