import pygame
import sys
import math

# 1. Initialize Pygame Engine
pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("2D Relativistic Spacetime Warp")
clock = pygame.time.Clock()

# Colors (Hex Values)
BG_COLOR = (10, 10, 15)       # Deep Space Void
BH_COLOR = (0, 0, 0)          # Absolute Black
RAY_COLOR = (0, 255, 200)     # Photon Cyan Neon
TEXT_COLOR = (150, 150, 150)

# 2. Setup Black Hole Physics Parameters
BH_X, BH_Y = WIDTH // 2, HEIGHT // 2
EVENT_HORIZON = 40            # Radius of the point of no return
GRAVITY_STRENGTH = 1800       # How violent the spacetime curvature is

# 3. Setup Light Ray (Photon) Initial State
ray_x = 50.0                  # Starts on the left edge
ray_y = 225.0                 # Slightly above the center line to pass the black hole
vx = 7.0                      # Constant speed of light moving right
vy = 0.0                      # No initial vertical movement
trail = []                    # Stores past pixels to draw the curved path

print("[SYSTEM] Core initialized. Simulating gravitational bending...")

# 4. Main Simulation Loop
running = True
while running:
   # --- REPLACED PHYSICS CORE WITH GENERAL RELATIVITY APPROXIMATION ---
 if ray_x < WIDTH and ray_x > 0 and ray_y < HEIGHT and ray_y > 0:
    dx = BH_X - ray_x
    dy = BH_Y - ray_y
    distance = math.hypot(dx, dy)

    if distance > EVENT_HORIZON:
        # Relativistic trick: As light gets closer, the gravity scale warps aggressively
        # This simulates the "Photon Sphere" where light can orbit a black hole
        force = GRAVITY_STRENGTH / (distance ** 2.3)  # Slightly higher power mimics warped space
        
        ax = force * (dx / distance)
        ay = force * (dy / distance)
        
        vx += ax
        vy += ay
        
        # Lock the speed of light so it only changes direction, never its actual speed
        speed = math.hypot(vx, vy)
        vx = (vx / speed) * 8.0 
        vy = (vy / speed) * 8.0

        ray_x += vx
        ray_y += vy
        trail.append((int(ray_x), int(ray_y)))
    else:
        pass

    # --- GRAPHICS CORE: Draw the Sp
    # Draw the curved trail of light rays
    if len(trail) > 1:
        pygame.draw.lines(screen, RAY_COLOR, False, trail, 2)
        
    # Draw the Photon Particle Tip
    if distance > EVENT_HORIZON:
        pygame.draw.circle(screen, (255, 255, 255), (int(ray_x), int(ray_y)), 4)

    # Draw the Singularity / Black Hole Core
    pygame.draw.circle(screen, BH_COLOR, (BH_X, BH_Y), EVENT_HORIZON)
    # Visual glowing edge barrier
    pygame.draw.circle(screen, (255, 100, 0), (BH_X, BH_Y), EVENT_HORIZON, 1)

    # System Diagnostics text overlay
    font = pygame.font.SysFont("Courier", 14)
    dist_text = font.render(f"Photon Proximity: {int(distance)}m", True, TEXT_COLOR)
    status_text = font.render("Status: Trapped in Orbit" if distance <= EVENT_HORIZON else "Status: Simulating Geodesic", True, TEXT_COLOR)
    screen.blit(dist_text, (20, 20))
    screen.blit(status_text, (20, 40))

    # Update Monitor Screen at 60 Frames Per Second
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()