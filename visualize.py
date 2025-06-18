import pygame
import random
import math
import imageio
import numpy as np
from algorithms.geometry.jarvis import jarvis_march
from algorithms.geometry.graham import graham_scan

# ---- Visualization for Convex Hull ----
def main():
    pygame.init()
    WIDTH, HEIGHT = 800, 600
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Convex Hull: Jarvis vs Graham")
    clock = pygame.time.Clock()
    font = pygame.font.SysFont(None, 24)
    FPS = 30

    def generate_frames():
        # random point cloud
        pts = [(random.randint(50, WIDTH//2 - 50), random.randint(50, HEIGHT - 50)) for _ in range(30)]
        return list(jarvis_march(pts)), list(graham_scan(pts))

    jarvis_frames, graham_frames = generate_frames()
    max_steps = max(len(jarvis_frames), len(graham_frames))
    step = 0
    running = True

    frames_list = []
    start_ticks = pygame.time.get_ticks()

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    jarvis_frames, graham_frames = generate_frames()
                    max_steps = max(len(jarvis_frames), len(graham_frames))
                    step = 0
                    frames_list.clear()
                    start_ticks = pygame.time.get_ticks()
                elif event.key == pygame.K_RIGHT:
                    step = min(step + 1, max_steps - 1)
                elif event.key == pygame.K_LEFT:
                    step = max(step - 1, 0)

        screen.fill((30, 30, 30))

        # Draw labels
        label_j = font.render("Jarvis", True, (255, 255, 255))
        label_g = font.render("Graham", True, (255, 255, 255))
        screen.blit(label_j, (10, 10))
        screen.blit(label_g, (WIDTH//2 + 10, 10))

        # Draw Jarvis pane
        frame_j = jarvis_frames[min(step, len(jarvis_frames) - 1)]
        for x, y in frame_j["points"]:
            pygame.draw.circle(screen, (200, 200, 200), (x, y), 5)
        if len(frame_j["hull"]) > 1:
            pygame.draw.lines(screen, (0, 255, 0), False, frame_j["hull"], 2)
        if "current" in frame_j:
            cx, cy = frame_j["current"]
            pygame.draw.circle(screen, (255, 0, 0), (cx, cy), 6)
        if "candidate" in frame_j:
            qx, qy = frame_j["candidate"]
            pygame.draw.circle(screen, (0, 0, 255), (qx, qy), 6)

        # Draw Graham pane (offset right)
        offset = WIDTH // 2
        frame_g = graham_frames[min(step, len(graham_frames) - 1)]
        for x, y in frame_g["points"]:
            pygame.draw.circle(screen, (200, 200, 200), (x + offset, y), 5)
        if len(frame_g["hull"]) > 1:
            pygame.draw.lines(screen, (0, 255, 0), False,
                              [(x + offset, y) for x, y in frame_g["hull"]], 2)
        if "current" in frame_g:
            cx, cy = frame_g["current"]
            pygame.draw.circle(screen, (255, 0, 0), (cx + offset, cy), 6)
        if "candidate" in frame_g:
            qx, qy = frame_g["candidate"]
            pygame.draw.circle(screen, (0, 0, 255), (qx + offset, qy), 6)

        # Draw elapsed time at bottom-center, clear of labels
        elapsed_s = (pygame.time.get_ticks() - start_ticks) // 1000
        time_text = f"Time: {elapsed_s}s"
        time_lbl = font.render(time_text, True, (255, 255, 255))
        tx = WIDTH//2 - time_lbl.get_width()//2
        ty = HEIGHT - font.get_height() - 10
        screen.blit(time_lbl, (tx, ty))

        pygame.display.flip()

        # Record frame for GIF
        arr = pygame.surfarray.array3d(screen)
        frames_list.append(np.transpose(arr, (1, 0, 2)))

        clock.tick(FPS)
        step += 1
        if step >= max_steps:
            running = False

    # Save GIF
    gif_path = 'convex_hull_animation.gif'
    imageio.mimsave(gif_path, frames_list, fps=FPS)
    print(f"GIF saved to {gif_path}")

    pygame.quit()

if __name__ == "__main__":
    main()
